from selenium import webdriver
from tests.base_test import *

class TestOwnerSuite(BaseOwnerTest):
    tender_type = negotiation_quick


class TestViewerSuite(BaseViewerLimitedTest):
    pass

# TODO: add provider claim logic?
if __name__ == '__main__':
    pass