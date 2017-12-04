from selenium import webdriver

browser = None
wait = None
tender = None
timeout = 10
tender_params = {'is_multilot': True,
                 'vat': True,
                 'lots': 1,
                 'items': 2,
                 'hours': 1,
                 'minutes': 0
}
max_import_time = 240
path = "http://40.69.95.23/#/"
#path = "http://192.168.103.42/#/"
#path = "http://localhost:6234/#/"
