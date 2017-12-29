from tests.base_test import *


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'aboveThresholdEu'


class TestViewerSuite(BaseViewerTest):
    def test_items_description_en(self, tender):
        for i, lot in enumerate(tender.lots):
            for j, item in enumerate(lot.items):
                assert item.description_en in f('#item_descriptionEn_{}{}'.format(i, j)).text


class TestProviderSuite(BaseProviderTest):
    pass


class TestProviderSuite2(BaseProviderTest):
    user = 'provider2'

if __name__ == '__main__':
    pass
