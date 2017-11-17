from tests.base_test import *
from core.conditions import *

procedure = 'aboveThreshold'


class TestTenderOwner(BaseTest):

    def test_create_tender(self, tender):
        login('owner')
        go_to_create(procedure)
        fill_tender(tender, procedure)
        f('#createTender').assure(clickable).click()
        tender.url = get_url()
        assert wait_for_export(tender), "Tender did not export in 5 minutes"

    def test_tender_search(self, tender):
        assert search_tender(tender)


class TestViewerSuite(BaseViewerTest):
    pass


class TestProviderSuite(BaseTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)

if __name__ == '__main__':
    pass
