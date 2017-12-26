from tests.base_test import *


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'aboveThreshold'


class TestViewerSuite(BaseViewerTest):
    pass


class TestProviderSuite(BaseProviderTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)


class TestProviderSuite2(BaseProviderTest):
    def test_tender_search(self, tender):
        login('provider2')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)


if __name__ == '__main__':
    pass
