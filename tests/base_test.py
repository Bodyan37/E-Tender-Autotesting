from core.tools import *
import allure
import json


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass


class BaseOwnerTest(BaseTest):
    user = 'owner'

    def test_login(self):
        login(self.user)

    @pytest.mark.dependency(name="create")
    def test_create_tender(self, tender):
        tender.type = self.tender_type
        create_tender(tender)
        tender.url = get_url()
        assert wait_for_export(tender), "Tender did not export in 5 minutes"
        allure.attach('tender', json.dumps(tender, default=lambda o: o.__dict__))

    @pytest.mark.dependency(depends=["create"])
    def test_tender_search(self, tender):
        assert search_tender(tender)


@pytest.mark.dependency(depends=["create"])
class BaseViewerTest(BaseTest):
    user = 'viewer'

    def test_login(self):
        login(self.user)

    def test_tender_search(self, tender):
        assert search_tender(tender)
        assert get_url() == tender.url

    def test_tender_title(self, tender):
        assert tender.title in f('#tenderTitle').text

    def test_tender_description(self, tender):
        assert tender.description in f('#tenderDescription').text

    def test_tender_budget(self, tender):
        assert spacify(tender.budget) in f('#tenderBudget').text

    def test_tender_currency(self, tender):
        assert tender.currency.code in f('#tenderCurrency').text

    def test_vat(self, tender):
        assert get_url() == tender.url
        if tender.vat:
            assert f('#includeVat')
        else:
            assert f('#excludeVat')

    def test_tender_id(self, tender):
        assert tender.tender_id in f('#tenderidua > b').text

    def test_tender_owner(self):
        assert 'TenderOwner#' in f('#tenderOwner').text

    def test_tender_period_end(self, tender):
        t = tender.tender_period.end
        assert t.date+', '+t.time in f('#tenderEnd').text

    def test_lots_title(self, tender):
        if tender.is_multilot:
            open_all_lots()
            for i, lot in enumerate(tender.lots):
                assert lot.title in f('#lotTitle_{}'.format(i)).get_attribute("title")

    def test_lots_description(self, tender):
        if tender.is_multilot:
            for i, lot in enumerate(tender.lots):
                assert lot.description in f('#lotDescription_{}'.format(i)).text

    def test_lots_value(self, tender):
        for i, lot in enumerate(tender.lots):
            assert spacify(lot.lot_value) in f('#lotValue_{}'.format(i)).text

    def test_lots_currency(self, tender):
        for i, lot in enumerate(tender.lots):
            assert tender.currency.code in f('#lotCurrency_{}'.format(i)).text

    def test_lots_vat(self, tender):
        assert get_url() == tender.url
        for i, lot in enumerate(tender.lots):
            if tender.vat:
                assert f('#lotVatInc_{}'.format(i))
            else:
                assert f('#lotVatExc_{}'.format(i))

    def test_lots_minimal_step(self, tender):
        for i, lot in enumerate(tender.lots):
            assert spacify(lot.minimal_step) in f('#lotMinimalStep_{}'.format(i)).text

    def test_lots_guarantee(self, tender):
        if tender.is_multilot:
            for i, lot in enumerate(tender.lots):
                assert spacify(lot.guarantee) in f('#lotGuarantee_{}'.format(i)).text

    def test_tender_guarantee(self, tender):
        assert spacify(sum([i.guarantee for i in tender.lots])) in f('#tenderGuarantee').text

    def test_items_description(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.description in f('#item_description_{}{}'.format(i, j)).text

    def test_items_delivery_date_start(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_date.start.date in f('#delivery_start_{}{}'.format(i, j)).text

    def test_items_delivery_date_end(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_date.end.date in f('#delivery_end_{}{}'.format(i, j)).text

    def test_items_delivery_address_region(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_address.region in f('#delivery_region_{}{}'.format(i, j)).text

    def test_items_delivery_address_city(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_address.city in f('#delivery_city_{}{}'.format(i, j)).text

    def test_items_delivery_address_street(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_address.street in f('#delivery_addressStr_{}{}'.format(i, j)).text

    def test_items_delivery_address_index(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.delivery_address.index in f('#delivery_postIndex_{}{}'.format(i, j)).text

    def test_items_classification_code(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert tender.classification.id in f('#classification_code_{}{}'.format(i, j)).text

    def test_items_classification_description(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert tender.classification.description in f('#classification_name_{}{}'.format(i, j)).text

    def test_items_units(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.unit in f('#item_unit_{}{}'.format(i, j)).text

    def test_items_quantity(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert str(item.quantity) in f('#item_quantity_{}{}'.format(i, j)).text


@pytest.mark.dependency(depends=["create"])
class BaseProviderTest(BaseTest):
    user = 'provider'

    def test_login(self):
        login(self.user)

    def test_tender_search(self, tender):
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)
