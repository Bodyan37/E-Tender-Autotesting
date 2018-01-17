from tests.base_test import *

class TestOwnerSuite(BaseOwnerTest):
    tender_type = negotiation


class TestViewerSuite(BaseViewerLimitedTest):
    pass

# TODO: add provider claim logic?
if __name__ == '__main__':
    pass