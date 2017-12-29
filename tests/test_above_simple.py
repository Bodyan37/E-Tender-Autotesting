from tests.base_test import *


class TestOwnerSuite(BaseOwnerTest):
    tender_type = 'aboveThreshold'


class TestViewerSuite(BaseViewerTest):
    pass


class TestProviderSuite(BaseProviderTest):
    pass


class TestProviderSuite2(BaseProviderTest):
    user = 'provider2'


if __name__ == '__main__':
    pass
