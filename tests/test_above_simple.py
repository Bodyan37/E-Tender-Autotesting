from tests.base_test import *
from core.conditions import *

procedure = 'aboveThreshold'


@pytest.allure.testcase("TenderOwner")
class TestTenderOwner(BaseTest):

    @pytest.mark.dependency(name="create")
    def test_create_tender(self, tender):
        login('owner')
        go_to_create(procedure)
        fill_tender(tender, procedure)
        f('#createTender').assure(clickable).click()
        tender.url = get_url()
        assert wait_for_export(tender), "Tender did not export in 5 minutes"

    @pytest.mark.dependency(depends=["create"])
    def test_tender_search(self, tender):
        assert search_tender(tender)


@pytest.mark.dependency(depends=["create"])
@pytest.allure.testcase("Viewer")
class TestViewerSuite(BaseViewerTest):
    pass

@pytest.mark.dependency(depends=["create"])
@pytest.allure.testcase("Provider1")
class TestProviderSuite(BaseTest):
    def test_tender_search(self, tender):
        login('provider')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender, procedure)

@pytest.mark.dependency(depends=["create"])
@pytest.allure.testcase("Provider2")
class TestProviderSuite2(BaseTest):
    def test_tender_search(self, tender):
        login('provider2')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender, procedure)


if __name__ == '__main__':
    pass
