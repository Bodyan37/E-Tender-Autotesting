from tests.base_test import *
from core.config import max_import_time


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'belowThreshold'


class TestViewerSuite(BaseViewerOpenTest):

    def test_enquiry_period_end(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#enquiryEnd').text

    def test_tender_period_start(self, tender):
        t = tender.tender_period.start
        assert t.date+', '+t.time in f('#tenderStart').text


class TestProviderSuite(BaseProviderTest):

    def test_add_bid(self, tender):
        if time.time() < tender.tender_period.start.datetime:
            time.sleep(tender.tender_period.start.datetime - time.time() + max_import_time)
            refresh()
        add_bids(tender)


class TestProviderSuite2(BaseProviderTest):
    user = 'provider2'


if __name__ == '__main__':
    pass
