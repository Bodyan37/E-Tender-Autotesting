from faker.generator import random
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.support.ui import Select
from core import config
from core.config import path
from core.elements import SmartElement, SmartElementsCollection
from core.conditions import present, clickable
from core.et_data import users, tender_types, reporting, negotiation, negotiation_quick, tender_cause
import allure
import time
import re
from core.tender import Cause


def spacify(s):
    s = str(s / 1)
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


def wait_ui():
    # TODO: refactor
    until_not(f('.blockUI'), present)


def until(locator, condition):
    config.wait.until(condition(locator))
    return locator


def scroll_to_bottom():
    config.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def open_all_lots():
    f('#openAllLots').click()


@allure.step
def fill_tender(tender):
    check_multilots(tender)
    fill_tender_periods(tender.tender_period, tender.type)
    f('#title').set_value(tender.title)
    f('#description').set_value(tender.description)
    if tender.type in ('aboveThresholdEu',):
        f('#titleEN').set_value(tender.title_en)
    if tender.type in (negotiation, negotiation_quick):
        set_cause(tender)
    Select(f('#currency')).select_by_visible_text(tender.currency.name)
    if tender.vat:
        fs('#valueAddedTaxIncluded')[-1].click()
    # TODO Features
    fill_lots(tender)


@allure.step
def search_tender(tender):
    visit(path)
    wait_ui()
    if tender.type in (reporting, negotiation, negotiation_quick):
        f('#naviTitle1').assure(clickable).click()
    f('div.row-search input').set_value(tender.tender_id).press_enter()
    wait_ui()
    if tender.title in get_source():
        f('#container a.tender-table-title.ng-binding').click()
        return True
    return False


@allure.step
def login(user):
    visit(path)
    try:
        f('#login').click()
    except (ElementNotVisibleException, TimeoutException):
        visit(path + 'login')
    f('#inputUsername').set_value(users[user])
    f('#inputPassword').set_value('Qq123456')
    f('#btn_submit').click()
    # wait_ui()
    try:
        f('#i_got_it').click()  # skip news
    except:
        pass


@allure.step
def create_tender(tender):
    go_to_create(tender.type)
    fill_tender(tender)
    press_create()


@allure.step
def fill_tender_periods(period, procedure):
    if procedure in (reporting, negotiation, negotiation_quick):
        return None
    if procedure == 'belowThreshold':
        f('#enquiryPeriod').set_value(period.start.date)
        f('#enquiryPeriod_time').set_value(period.start.time)
        f('#startDate').set_value(period.start.date)
        f('#startDate_time').set_value(period.start.time)
    f('#endDate').set_value(period.end.date)
    f('#endDate_time').set_value(period.end.time)


@allure.step
def fill_lots(tender):
    if tender.is_multilot:
        f('#lotRemove_0').click()
    else:
        f('#itemRemove_00').click()
    for i, lot in enumerate(tender.lots):
        if tender.is_multilot:
            f('#addLot_').click()
            f('#lotTitle{}'.format(i)).set_value(lot.title)
            f('#lotDescription{}'.format(i)).set_value(lot.description)
        f('#lotValue_{}'.format(i)).set_value(lot.lot_value)
        if tender.type not in (reporting, negotiation, negotiation_quick):
            f('#minimalStep_{}'.format(i)).set_value(lot.minimal_step)
            Select(f('#guarantee_{}'.format(i))).select_by_index(1)
            f('#lotGuarantee_{}'.format(i)).set_value(lot.guarantee)
        # TODO Features
        for j, item in enumerate(lot.items):
            f('#addLotItem_{}'.format(i)).click()
            f('#itemsDescription{}{}'.format(i, j)).set_value(item.description)
            if tender.type in ('aboveThresholdEu', 'defense'):
                f('#itemsDescriptionEN{}{}'.format(i, j)).set_value(item.description_en)
            f('#itemsQuantity{}{}'.format(i, j)).set_value(item.quantity)
            fs('#itemsUnit{}{} div:nth-of-type(1) > input'.format(i, j))[0].set_value(
                item.unit).press_enter().press_enter()
            f('#openClassificationModal{}{}'.format(i, j)).click()
            f('#classificationCode').assure(clickable).set_value(tender.classification.id)
            time.sleep(2.5)
            f('#code').click()
            f('#classification_choose').click()
            wait_ui()
            f('#delStartDate{}{}'.format(i, j)).set_value(item.delivery_date.start.date)
            f('#delEndDate{}{}'.format(i, j)).set_value(item.delivery_date.end.date)
            Select(f('#region_{}{}'.format(i, j))).select_by_visible_text(
                item.delivery_address.region)
            Select(f('#city_{}{}'.format(i, j))).select_by_visible_text(
                item.delivery_address.city)
            f('#street_{}{}'.format(i, j)).set_value(item.delivery_address.street)
            f('#postIndex_{}{}'.format(i, j)).set_value(item.delivery_address.index)


def go_to_create(procedure):
    wait_ui()
    f('a[data-target="#procedureType"]').assure(clickable).click()
    Select(f('#chooseProcedureType')).select_by_visible_text(tender_types[procedure])
    f('#goToCreate').click()


def press_create():
    scroll_to_bottom()
    f('#createTender').assure(clickable).click()


def check_multilots(tender):
    if tender.type == reporting:
        return None
    if tender.is_multilot:
        f('#isMultilots').click()


def set_cause(tender):
    if tender.type == negotiation:
        del tender_cause['quick']
    tender.cause = Cause(random.choice(list(tender_cause.keys())))
    Select(f('#cause')).select_by_value(tender.cause.name)
    f('#causeDescription').set_value(tender.cause_description)


@allure.step
def wait_for_export(tender):
    for i in range(10):
        time.sleep(30)
        refresh()
        if re.match(r'UA-\d{4}-.*', f('#tenderidua > b').text):
            tender.tender_id = f('#tenderidua > b').text
            tender.url = get_url()
            return True
    return False


@allure.step
def add_bids(tender):
    wait_ui()
    f('li:nth-child(2) > span').click()
    wait_ui()
    open_all_lots()
    for i, lot in enumerate(tender.lots):
        wait_ui()
        f('#amount{}'.format(i)).set_value(lot.lot_value * 0.95 // 1)
        if tender.type != 'belowThreshold':
            f('#selfEligible').click()  # _{}'.format(i)
            f('#selfQualified').click()
        f('#createBid_{}'.format(i)).click()
