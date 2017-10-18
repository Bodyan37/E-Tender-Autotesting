import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


from core import config


@pytest.mark.usefixtures("setup")
class BaseTest(object):
    pass
