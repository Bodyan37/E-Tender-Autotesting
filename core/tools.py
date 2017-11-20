from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.support.ui import Select
from core import config
from core.config import path
from core.elements import SmartElement, SmartElementsCollection
from core.conditions import present, clickable
from core.et_data import users, tender_types
import pytest
import time
import re

def spacify(s):
    s = str(s)
    return (''.join([' ' + n if i % 3 == 2 else n
                     for i, n in enumerate(s[:s.index('.')][::-1])][::-1]) + s[s.index('.'):]).lstrip().replace('.',
                                                                                                                ',')


def visit(url):
    config.browser.get(url)


def refresh():
    config.browser.refresh()


def get_url():
    return config.browser.current_url


def get_source():
    return config.browser.page_source


def f(locator):
    return SmartElement(locator)


def fs(locator):
    return SmartElementsCollection(locator)


def until_not(locator, condition):
    config.wait.until_not(condition(locator))
    return locator


def until(locator, condition):
    config.wait.until(condition(locator))
    return locator


@pytest.allure.step
def fill_tender(tender, procedure):
    if tender.is_multilot:
        f('#isMultilots').click()
    f('#title').set_value(tender.title)
    if procedure in ('aboveThresholdEu',):
        f('#titleEN').set_value(tender.title_en)
    f('#description').set_value(tender.description)
    Select(f('#currency')).select_by_visible_text(tender.currency.name)
    if tender.vat:
        fs('#valueAddedTaxIncluded')[-1].click()
    # TODO Features
    fill_lots(tender, procedure)
    fill_tender_periods(tender.tender_period, procedure)


@pytest.allure.step
def search_tender(tender):
    visit(path)
    f('div.row-search input').set_value(tender.tender_id).press_enter()
    until_not(f('.blockUI'), present)
    if tender.title in get_source():
        f('#container a.tender-table-title.ng-binding').click()
        return True
    return False


@pytest.allure.step
def login(user):
    visit(path)
    try:
        f('#login').click()
    except (ElementNotVisibleException, TimeoutException):
        visit(path + 'login')
    f('#inputUsername').set_value(users[user])
    f('#inputPassword').set_value('Qq123456')
    f('#btn_submit').click()
    until_not(f('.blockUI'), present)
    try:
        f('#i_got_it').click()  # skip news
    except:
        pass


@pytest.allure.step
def fill_tender_periods(period, procedure):
    if procedure == 'belowThreshold':
        f('#enquiryPeriod_endDate_day').set_value(period.start.date)
        f('#enquiryPeriod_endDate_time').set_value(period.start.time)
        f('#tenderPeriod_startDate_day').set_value(period.start.date)
        f('#tenderPeriod_startDate_time').set_value(period.start.time)
    f('#tenderPeriod_endDate_day').set_value(period.end.date)
    f('#tenderPeriod_endDate_time').set_value(period.end.time)


@pytest.allure.step
def fill_lots(tender, procedure):
    if tender.is_multilot:
        f('#lotRemove_0').click()
    else:
        f('#itemRemove_00').click()
    for i, lot in enumerate(tender.lots):
        if tender.is_multilot:
            f('#addLot_').click()
            f('#lotTitle{}'.format(i)).set_value(lot.title)
            f('#lotDescription{}'.format(i)).set_value(lot.description)
        # TODO Guarantee
        f('#lotValue_{}'.format(i)).set_value(lot.lot_value)
        f('#minimalStep_{}'.format(i)).set_value(lot.minimal_step)
        # TODO Features
        for j, item in enumerate(lot.items):
            f('#addLotItem_{}'.format(i)).click()
            f('#itemsDescription{}{}'.format(i, j)).set_value(item.description)
            if procedure in ('aboveThresholdEu',):
                f('#itemsDescriptionEN{}{}'.format(i, j)).set_value(item.description_en)
            f('#itemsQuantity{}{}'.format(i, j)).set_value(item.quantity)
            fs('#itemsUnit{}{} div:nth-of-type(1) > input'.format(i, j))[0].set_value(
                item.unit).press_enter().press_enter()
            f('#openClassificationModal{}{}'.format(i, j)).click()
            f('#classificationCode').assure(clickable).set_value(tender.classification.id)
            time.sleep(2.5)
            f('#code').click()
            f('#classification_choose').click()
            until_not(f('.blockUI'), present)
            f('#delStartDate{}{}'.format(i, j)).set_value(item.delivery_date.start.date)
            f('#delEndDate{}{}'.format(i, j)).set_value(item.delivery_date.end.date)
            Select(f('#region_{}{}'.format(i, j))).select_by_visible_text(
                item.delivery_address.region)
            Select(f('#city_{}{}'.format(i, j))).select_by_visible_text(
                item.delivery_address.city)
            f('#street_{}{}'.format(i, j)).set_value(item.delivery_address.street)
            f('#postIndex_{}{}'.format(i, j)).set_value(item.delivery_address.index)


def go_to_create(procedure):
    f('a[data-target="#procedureType"]').assure(clickable).click()
    Select(f('#chooseProcedureType')).select_by_visible_text(tender_types[procedure])
    f('#goToCreate').click()

@pytest.allure.step
def wait_for_export(tender):
    for i in range(10):
        time.sleep(30)
        refresh()
        if re.match(r'UA-\d{4}-.*', f('#tenderidua > b').text):
            tender.tender_id = f('#tenderidua > b').text
            tender.url = get_url()
            return True
    return False


@pytest.allure.step
def add_bids(tender, procedure):
    until_not(f('.blockUI'), present)
    f('li:nth-child(2) > span').click()
    for i, lot in enumerate(tender.lots):
        until_not(f('.blockUI'), present)
        f('#bidAmount_{}'.format(i)).set_value(lot.lot_value * 0.95 // 1)
        if procedure != 'belowThreshold':
            f('#selfEligible').click() #_{}'.format(i)
            f('#selfQualified').click()
        f('#createBid_{}'.format(i)).click()
