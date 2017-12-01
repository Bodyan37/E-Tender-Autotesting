from datetime import datetime
from tests.base_test import *
from core.conditions import *
from core.config import max_import_time

procedure = 'belowThreshold'


class TestTenderOwner(BaseTest):

    @pytest.mark.dependency(name="create")
    def test_create_tender(self, tender):
        login('owner')
        go_to_create(procedure)
        fill_tender(tender, procedure)
        f('#createTender').assure(clickable).click()
        tender.url = get_url()
        assert wait_for_export(tender), "Tender did not export in 5 minutes"

    @pytest.mark.dependency(depends=["create"])
    def test_tender_search(self, tender):
        assert search_tender(tender)


@pytest.mark.dependency(depends=["create"])
class TestViewerSuite(BaseViewerTest):

    def test_enquiry_period_end(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#enquiryEnd').text

    def test_tender_period_start(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#tenderStart').text


@pytest.mark.dependency(depends=["create"])
class TestProviderSuite(BaseTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        time.sleep((tender.tender_period.start.datetime - datetime.now()).seconds + max_import_time)
        refresh()
        add_bids(tender, procedure)


@pytest.mark.dependency(depends=["create"])
@pytest.allure.testcase("Provider2")
class TestProviderSuite2(BaseTest):
    def test_tender_search(self, tender):
        login('provider2')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender, procedure)

if __name__ == '__main__':
    pass
