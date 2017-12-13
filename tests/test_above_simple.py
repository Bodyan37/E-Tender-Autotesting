from tests.base_test import *


@pytest.allure.testcase("TenderOwner")
class TestTenderOwner(BaseTest):

    @pytest.mark.dependency(name="create")
    def test_create_tender(self, tender):
        tender.type = 'aboveThreshold'
        login('owner')
        create_tender(tender)
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
        add_bids(tender)


@pytest.mark.dependency(depends=["create"])
@pytest.allure.testcase("Provider2")
class TestProviderSuite2(BaseTest):
    def test_tender_search(self, tender):
        login('provider2')
        assert search_tender(tender)

    def test_add_bid(self, tender):
        add_bids(tender)


if __name__ == '__main__':
    pass
