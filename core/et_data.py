# -*- coding: utf-8 -*-
currencies = {
    'грн': 'UAH',
    'євро': 'EUR',
    'американський долар': 'USD',
    'англійський фунт стерлінгів': 'GBP',
    'російський рубль': 'RUB'
}
units = ['Бобіна', 'Людей', 'Людино-година', 'Рулон', 'блок', 'гектар', 'Гігакалорія',
         'Кіловар', 'Кіловат-година', 'кілограми', 'Кілокалорія', 'кілометри', 'комплект', 'літр', 'лот',
         'метри квадратні', 'метри кубічні', 'мегават-година в годину', 'місяць', 'набір', 'Одиниця', 'пара',
         'пачок', 'пачка', 'Погонний метр', 'послуга', 'рейс', 'роботи', 'Робочі дні', 'тони', 'тисяча кубічних метрів',
         'Тисяч штук', 'упаковка', 'Флакон', 'штуки', 'ящик']
cpvs = {
    '03111300-5': 'Насіння соняшника',
    '03114200-5': 'Фураж',
    '03117120-1': 'Рослини, що використовуються у фармацевтиці',
    '18213000-5': 'Вітрозахисні куртки',
    '35411100-9': 'Основні бойові танки',
    '35510000-2': 'Військові кораблі',
    '35513200-5': 'Допоміжні дослідницькі судна',
    '03450000-9': 'Розсадницька продукція',
    '09111100-1': 'Вугілля',
    '09121200-5': 'Магістральний газ',
    '09132300-6': 'Бензин з етанолом',
    '09200000-1': 'Нафта, вугілля і нафтопродукти',
    '09211650-2': 'Гальмівні рідини',
    '30237121-3': 'Послідовні інфрачервоні порти',
    '30237240-3': 'Веб-камери',
    '30237330-1': 'Картриджі цифрової аудіострічки (DAT-картриджі)',
    '43411000-7': 'Сортувальні та просіювальні машини',
    '43611200-1': 'Промислові бурові головки',
    '43612700-3': 'Обладнання свердловинних горловин',
    '51112200-2': 'Послуги зі встановлення електричного контрольного обладнання'
}
regions = {
    'Луганська область': ['Алмазна', 'Алчевськ', 'Антрацит', 'Боково-Хрустальне', 'Брянка', 'Вознесенівка', 'Гірське',
                          'Старобільськ', 'Суходільськ', 'Хрустальний', 'Щастя'],
    'Київська область': ['Березань', 'Біла Церква', 'Богуслав', 'Бориспіль', 'Боярка', 'Бровари', 'Васильків', 'Узин',
                         'Фастів', 'Чорнобиль', 'Яготин'],
    'Чернігівська область': ['Бахмач', 'Бобровиця', 'Борзна', 'Городня', 'Ічня', 'Корюківка', 'Мена', 'Ніжин',
                             'Новгород-Сіверський', 'Носівка', 'Остер', 'Прилуки', 'Семенівка', 'Сновськ', 'Чернігів'],
    'Херсонська область': ['Берислав', 'Генічеськ', 'Гола Пристань', 'Каховка', 'Нова Каховка', 'Олешки', 'Скадовськ',
                           'Таврійськ', 'Херсон'],
    'Одеська область': ['Ананьїв', 'Арциз', 'Балта', 'Березівка', 'Білгород-Дністровський', 'Біляївка', 'Болград',
                        'Чорноморськ', 'Татарбунари', 'Южне'],
    'Тернопільська область': ['Бережани', 'Борщів', 'Бучач', 'Заліщики', 'Збараж', 'Зборів', 'Копичинці', 'Кременець',
                              'Хоростків', 'Чортків', 'Шумськ'],
    'Запорізька область': ['Бердянськ', 'Василівка', 'Вільнянськ', 'Гуляйполе', 'Дніпрорудне', 'Енергодар', 'Запоріжжя',
                           'Токмак'],
    'Хмельницька область': ['Волочиськ', 'Городок', 'Деражня', 'Дунаївці','Старокостянтинів', "Кам'янець-Подільський",
                            'Красилів', 'Нетішин', 'Полонне', 'Славута', 'Ізяслав', 'Хмельницький', 'Шепетівка'],
    'Миколаївська область': ['Баштанка', 'Вознесенськ', 'Нова Одеса', 'Новий Буг', 'Очаків',
                             'Снігурівка', 'Южноукраїнськ'],
    'Рівненська область': ['Березне', 'Вараш', 'Дубно', 'Дубровиця', 'Здолбунів', 'Корець', 'Костопіль', 'Острог',
                           'Радивилів', 'Рівне', 'Сарни'],
    'Кіровоградська область': ['Благовіщенське', 'Бобринець', 'Гайворон', 'Долинська', "Знам'янка", 'Кропивницький',
                               'Мала Виска', 'Новомиргород', 'Новоукраїнка', 'Олександрія', 'Помічна', 'Світловодськ'],
    'Вінницька область': ['Бар', 'Бершадь', 'Вінниця', 'Гайсин', 'Гнівань', 'Жмеринка', 'Іллінці', 'Калинівка',
                          'Хмільник', 'Шаргород', 'Ямпіль'],
    'Житомирська область': ['Андрушівка', 'Баранівка', 'Бердичів', 'Житомир', 'Коростень', 'Коростишів', 'Малин',
                            'Новоград-Волинський', 'Овруч', 'Радомишль'],
    'Донецька область': ['Авдіївка', 'Амвросіївка', 'Бахмут', 'Білицьке', 'Білозерське', 'Бунге', 'Волноваха', 'Гірник',
                         "Слов'янськ", 'Сніжне', 'Соледар', 'Торецьк', 'Українськ', 'Харцизьк', 'Хрестівка', 'Донецьк'],
    'Дніпропетровська область': ['Апостолове', 'Верхівцеве', 'Верхньодніпровськ', 'Вільногірськ', 'Дніпро',
                                 'Підгородне', 'Покров', "П'ятихатки", 'Синельникове'],
    'Львівська область': ['Белз', 'Бібрка', 'Борислав', 'Броди', 'Буськ', 'Великі Мости', 'Глиняни',
                          'Судова Вишня', 'Трускавець', 'Турка', 'Угнів', 'Хирів', 'Ходорів', 'Червоноград'],
    'Полтавська область': ['Гадяч', 'Глобине', 'Горішні Плавні', 'Гребінка', 'Заводське', 'Зіньків', 'Карлівка',
                           'Кобеляки', 'Кременчук', 'Лохвиця', 'Лубни', 'Миргород', 'Пирятин', 'Полтава', 'Хорол'],
    'Закарпатська область': ['Берегове', 'Виноградів', 'Іршава', 'Мукачеве', 'Рахів', 'Свалява', 'Тячів', 'Ужгород',
                             'Хуст', 'Чоп'],
    'Івано-Франківська область': ['Болехів', 'Бурштин', 'Галич', 'Городенка', 'Долина', 'Івано-Франківськ', 'Калуш',
                                  'Коломия', 'Косів', 'Надвірна', 'Рогатин', 'Снятин', 'Тисмениця', 'Тлумач', 'Яремча'],
    'Чернівецька область': ['Вашківці', 'Вижниця', 'Герца', 'Заставна', 'Кіцмань', 'Новодністровськ', 'Новоселиця',
                            'Сокиряни', 'Сторожинець', 'Хотин', 'Чернівці'],
    'Волинська область': ['Берестечко', 'Володимир-Волинський', 'Горохів', 'Камінь-Каширський', 'Ківерці', 'Ковель',
                          'Луцьк', 'Любешів', 'Любомль', 'Нововолинськ', 'Рожище', 'Устилуг'],
    'АР Крим': ['Алупка', 'Алушта', 'Армянськ', 'Бахчисарай', 'Білогірськ', 'Джанкой', 'Євпаторія', 'Інкерман', 'Керч',
                'Ялта'],
    'Сумська область': ['Білопілля', 'Буринь', 'Ворожба', 'Глухів', 'Дружба', 'Конотоп', 'Кролевець', 'Лебедин',
                        'Охтирка', 'Путивль', 'Ромни', 'Середина-Буда', 'Суми', 'Тростянець', 'Шостка'],
    'Черкаська область': ['Ватутіне', 'Городище', 'Жашків', 'Звенигородка', 'Золотоноша', "Кам'янка", 'Канів',
                          'Чигирин', 'Шпола'],
    'Харківська область': ['Балаклія', 'Барвінкове', 'Богодухів', 'Валки', 'Вовчанськ', 'Дергачі', 'Зміїв', 'Ізюм',
                           'Харків', 'Чугуїв']
}
tender_types = {
    'belowThreshold': 'Допорогові закупівлі',
    'aboveThreshold': 'Відкриті торги',
    'aboveThresholdEu': 'Відкриті торги з публікацією англ.мовою',
    'defense': 'Переговорна процедура для потреб оборони',
    'competitiveDialogue': 'Конкурентний діалог',
    'competitiveDialogueEu': 'Конкурентний діалог з публікацією на англ. мовою',
    'reporting': 'Звіт про укладений договір'
}
users = {
    'owner': 'auto_owner',
    'viewer': 'auto_viewer',
    'provider': 'auto_provider1',
    'provider2': 'auto_provider2'
}

reporting = 'reporting'

if __name__ == '__main__':
    for i in regions:
        print("'{}':[],".format(i))
