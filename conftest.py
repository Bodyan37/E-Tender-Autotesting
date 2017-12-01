import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from core.tender import Tender
from core import config


@pytest.fixture(scope='class')
def setup(request):
    config.browser = webdriver.Chrome()
    config.browser.implicitly_wait(5)
    config.wait = WebDriverWait(config.browser, config.timeout)

    def teardown():
        config.browser.quit()

    request.addfinalizer(teardown)


@pytest.fixture(scope="module", autouse=True)
def create_tender():
    config.tender = Tender(**config.tender_params)

@pytest.fixture
def tender():
    return config.tender


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)
