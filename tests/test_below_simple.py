from tests.base_test import *
from core.config import max_import_time


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'belowThreshold'


class TestViewerSuite(BaseViewerTest):

    def test_enquiry_period_end(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#enquiryEnd').text

    def test_tender_period_start(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#tenderStart').text


class TestProviderSuite(BaseProviderTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        time.sleep(tender.tender_period.start.datetime - time.time() + max_import_time)
        refresh()
        add_bids(tender)


class TestProviderSuite2(BaseProviderTest):
    def test_tender_search(self, tender):
        login('provider2')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)

if __name__ == '__main__':
    pass
