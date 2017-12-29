from faker import Factory
from core.et_data import *
from datetime import datetime, timedelta
import random


fake = Factory.create()


class Address:

    def __init__(self):
        self.region = list(regions.keys())[random.randint(0, len(regions)-1)]
        self.city = random.choice(regions[self.region])
        address = fake.address()
        self.street = address[:address.find('\n')]
        self.index = '{:0>5}'.format(random.randint(0, 99999))


class Datetime:

    def __init__(self, dttm):
        self.datetime = dttm.timestamp()
        self.date = dttm.strftime("%d-%m-%Y")
        self.time = dttm.strftime("%H:%M")


class Period:

    def __init__(self, start, end):
        self.start = Datetime(start)
        self.end = Datetime(end)


class Currency:

    def __init__(self, name='грн'):
        self.code = currencies[name]
        self.name = name


class Classification:

    def __init__(self):
        self.id = random.choice(list(cpvs.keys()))
        self.description = cpvs[self.id]


class Option:

    def __init__(self, value):
        self.title = fake.word()
        self.value = value


class Feature:

    def __init__(self):
        self.title = '{}-{}: {}'.format('f', fake.uuid4()[:8], fake.word() + fake.word())
        self.description = fake.sentence()
        self.options = [Option(1), Option(4)]


class Item:

    def __init__(self):
        self.description = '{}-{}: {}'.format('i', fake.uuid4()[:8], fake.sentence())
        self.description_en = fake.sentence()
        self.quantity = random.randint(0, 2147483647)
        self.unit = units[random.randint(0, len(units)-1)]
        self.features = [Feature()]
        #self.classification = Classification() -> tender
        start_date = datetime.now() + timedelta(days=10)
        end_date = start_date + timedelta(days=10)
        self.delivery_date = Period(start_date, end_date)
        self.delivery_address = Address()


class Lot:

    def __init__(self, items=1):
        self.title = '{}-{}: {}'.format('l', fake.uuid4()[:8], fake.sentence())
        self.description = fake.sentence()
        self.lot_value = round(random.uniform(3000, 4999999999.99), 2)
        self.minimal_step = round(random.uniform(0.005, 0.03) * self.lot_value, 2)
        self.items = [Item() for _ in range(0, items)]
        self.features = [Feature()]
        self.guarantee = round(random.uniform(3000, 4999999.99), 2)


class Tender:

    def __init__(self, is_multilot=True, vat=True, lots=1, items=2, hours=1, minutes=0):

        self.is_multilot = is_multilot
        self.title = fake.sentence()
        self.title_en = fake.sentence()
        self.description = fake.sentence()
        self.currency = Currency(random.choice(list(currencies.keys())))
        self.vat = vat
        self.lots = [Lot(items) for _ in range(0, lots)]
        self.budget = sum([lot.lot_value for lot in self.lots])
        start_date = datetime.now() + timedelta(minutes=10)
        end_date = start_date + timedelta(hours=hours, minutes=minutes)
        self.tender_period = Period(start_date, end_date)
        # enquiryPeriod.end_date = tenderPeriod.start_date
        self.features = [Feature()]
        self.classification = Classification()  # TODO different for items
        self.tender_id = ''
        self.type = None


if __name__ == '__main__':
    tender = Tender()
    print([i.lot_value for i in tender.lots])
    tp = tender.tender_period
    date = [int(i) for i in tp.start.date.split('-')[::-1]]
    time = [int(i) for i in tp.start.time.split(':')]
    print()
    a = (datetime(*(date+time)) - datetime.now()).total_seconds()
    print(a)
