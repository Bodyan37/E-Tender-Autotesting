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
        pass
        config.browser.quit()

    request.addfinalizer(teardown)


@pytest.fixture(scope="session", autouse=True)
def create_tender():
    config.tender = Tender(**config.tender_params)

@pytest.fixture
def tender():
    return config.tender