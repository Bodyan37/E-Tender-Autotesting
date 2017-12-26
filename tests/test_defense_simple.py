from tests.base_test import *


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'defense'


class TestViewerSuite(BaseViewerTest):
    def test_items_description_en(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.description_en in f('#item_descriptionEn_{}{}'.format(i, j)).text


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
