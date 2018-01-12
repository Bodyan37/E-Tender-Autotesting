import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from core.tender import Tender
from core import config
import allure
import json


@pytest.fixture(scope='class')
def setup(request):
    config.browser = webdriver.Chrome()
    config.browser.implicitly_wait(5)
    config.wait = WebDriverWait(config.browser, config.timeout)

    def teardown():
        config.browser.quit()

    request.addfinalizer(teardown)


@pytest.fixture(scope="module", autouse=True)
def create_tender(request):
    config.tender = Tender(**config.tender_params)

    def teardown():
        allure.attach('tender', json.dumps(config.tender, default=lambda o: o.__dict__))

    request.addfinalizer(teardown)


@pytest.fixture
def tender():
    return config.tender
