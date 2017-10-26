from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time
import re
import pytest
from tests.base_test import BaseTest
from core.tools import *
from core.conditions import *
from selenium.webdriver.support.ui import Select
from core.et_data import users

path = "http://40.69.95.23/#/"
#path = "http://192.168.103.42/#/"

max_import_time = 180


def search_tender(tender):
    visit(path)
    f('div.row-search.fr > input').set_value(tender.tender_id).press_enter()
    time.sleep(4)
    if tender.title in get_source():
        f('#container a.tender-table-title.ng-binding').click()
        return True
    return False


def login(user):
    visit(path)
    try:
        f('#login').click()
    except (ElementNotVisibleException, TimeoutException):
        visit(path + 'login')
    f('#inputUsername').set_value(users[user])
    f('#inputPassword').set_value('Qq123456')
    f('#btn_submit').click()
    until_not(f('.blockUI'), present)


class TestTenderOwner(BaseTest):

    def test_create_tender(self, tender):
        login('owner')
        f('a[data-target="#procedureType"]').assure(clickable).click()
        Select(f('#chooseProcedureType')).select_by_visible_text('Допорогові закупівлі')
        f('#goToCreate').click()
        #  fill tender fields
        if tender.is_multilot:
            f('#isMultilots').click()
        f('#title').set_value(tender.title)
        f('#description').set_value(tender.description)
        Select(f('#currency')).select_by_visible_text(tender.currency.name)
        if tender.vat:
            fs('#valueAddedTaxIncluded')[-1].click()
        # TODO Features
        # clear lots
        if tender.is_multilot:
            f('#lotRemove_0').click()
        else:
            f('#itemRemove_00').click()
        # fill lots
        for i, lot in enumerate(tender.lots):
            if tender.is_multilot:
                f('#addLot_').click()
                f('#lotTitle{}'.format(i)).set_value(lot.title)
                f('#lotDescription{}'.format(i)).set_value(lot.description)
            # TODO Guarantee
            f('#lotValue_{}'.format(i)).set_value(lot.lot_value)
            f('#minimalStep_{}'.format(i)).set_value(lot.minimal_step)
            # TODO Features
            for j, item in enumerate(lot.items):
                f('#addLotItem_{}'.format(i)).click()
                f('#itemsDescription{}{}'.format(i, j)).set_value(item.description)
                f('#itemsQuantity{}{}'.format(i, j)).set_value(item.quantity)
                fs('#itemsUnit{}{} div:nth-of-type(1) > input'.format(i, j))[0].set_value(item.unit).press_enter().press_enter()
                f('#openClassificationModal{}{}'.format(i, j)).click()
                f('#classificationCode').assure(clickable).set_value(tender.classification.id)
                time.sleep(2.5)
                f('#code').click()
                f('#classification_choose').click()
                until_not(f('.blockUI'), present)
                f('#delStartDate{}{}'.format(i, j)).set_value(item.delivery_date.start.date)
                f('#delEndDate{}{}'.format(i, j)).set_value(item.delivery_date.end.date)
                Select(f('#region_{}{}'.format(i, j))).select_by_visible_text(
                    item.delivery_address.region)
                Select(f('#city_{}{}'.format(i, j))).select_by_visible_text(
                    item.delivery_address.city)
                f('#street_{}{}'.format(i, j)).set_value(item.delivery_address.street)
                f('#postIndex_{}{}'.format(i, j)).set_value(item.delivery_address.index)

        period = tender.tender_period
        f('#enquiryPeriod_endDate_day').set_value(period.start.date)
        f('#enquiryPeriod_endDate_time').set_value(period.start.time)
        f('#tenderPeriod_startDate_day').set_value(period.start.date)
        f('#tenderPeriod_startDate_time').set_value(period.start.time)
        f('#tenderPeriod_endDate_day').set_value(period.end.date)
        f('#tenderPeriod_endDate_time').set_value(period.end.time)
        f('#createTender').click()
        for i in range(10):
            time.sleep(30)
            refresh()
            tender.tender_id = f('#tenderidua > b').text
            result = re.match(r'UA-\d{4}-.*', tender.tender_id)
            if result:
                break
        time.sleep(30) 
        tender.url = get_url()

        assert result is not None, "Tender did not export in 5 minutes"

    def test_tender_search(self, tender):
        assert search_tender(tender)


class TestViewerSuite(BaseTest):

    def test_tender_search(self, tender):
        login('viewer')
        assert search_tender(tender)

    def test_tender_title(self, tender):
        assert tender.title in f('#tenderTitle').text

    def test_tender_description(self, tender):
        assert tender.description in f('#tenderDescription').text

    def test_tender_budget(self, tender):
        assert spacify(tender.budget) in f('#tenderBudget').text

    def test_tender_currency(self, tender):
        assert tender.currency.code in f('#tenderCurrency').text

    def test_vat(self, tender):
        if tender.vat:
            assert f('#includeVat')
        else:
            assert f('#excludeVat')

    def test_tender_id(self, tender):
        assert tender.tender_id in f('#tenderidua > b').text

    def test_tender_owner(self):
        assert 'TenderOwner#' in f('#tenderOwner').text

    def test_enquiry_period_end(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#enquiryEnd').text

    def test_tender_period_start(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#tenderStart').text

    def test_tender_period_end(self, tender):
        t = tender.tender_period.end
        assert t.date+', '+t.time in f('#tenderEnd').text

    def test_lots_title(self, tender):
        if tender.is_multilot:
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
        for i, lot in enumerate(tender.lots):
            if tender.vat:
                assert f('#lotVatInc_{}'.format(i))
            else:
                assert f('#lotVatExc_{}'.format(i))

    def test_lots_minimal_step(self, tender):
        for i, lot in enumerate(tender.lots):
            assert spacify(lot.minimal_step) in f('#lotMinimalStep_{}'.format(i)).text

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


#@pytest.mark.skip
class TestProviderSuite(BaseTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        time.sleep((tender.tender_period.start.datetime - datetime.now()).seconds + max_import_time)
        refresh()
        f('#sendBid_0').click()
        for i, lot in enumerate(tender.lots):
            until_not(f('.blockUI'), present)
            f('#bidAmount_{}'.format(i)).set_value(lot.lot_value*0.95)
            f('#createBid_{}'.format(i)).click()

if __name__ == '__main__':
    pass
