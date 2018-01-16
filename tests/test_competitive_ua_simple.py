from tests.base_test import *
from core.et_data import competitive_dialogue_ua


class TestOwnerSuite(BaseOwnerTest):
    tender_type = competitive_dialogue_ua


class TestViewerSuite(BaseViewerOpenTest):
    pass


if __name__ == '__main__':
    pass