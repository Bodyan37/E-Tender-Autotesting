from tests.base_test import *

class TestOwnerSuite(BaseOwnerTest):
    tender_type = negotiation


class TestViewerSuite(BaseViewerLimitedTest):
    pass

# class TestProviderSuite(BaseProviderTest):
#     pass


if __name__ == '__main__':
    pass