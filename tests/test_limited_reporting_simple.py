from tests.base_test import  *


class TestOwnerSuite(BaseOwnerTest):
    tender_type = reporting


class TestViewerSuite(BaseViewerLimitedTest):

    @pytest.mark.skip(reason="Cause: field is absent")
    def test_tender_cause(self, tender):
        pass

    @pytest.mark.skip(reason="CauseDescription: field is absent")
    def test_tender_cause_description(self, tender):
        pass


if __name__ == '__main__':
    pass
