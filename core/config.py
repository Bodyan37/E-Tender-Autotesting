from selenium import webdriver

browser = None
wait = None
tender = None
timeout = 15
tender_params = {'is_multilot': True,
                 'vat': True,
                 'lots': 1,
                 'items': 2,
                 'hours': 1,
                 'minutes': 0
}