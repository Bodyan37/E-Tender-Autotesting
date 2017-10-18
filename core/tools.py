from core import config
from core.elements import SmartElement, SmartElementsCollection
from core.conditions import present, clickable


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


