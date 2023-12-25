from mimesis import Person, Code, Generic
from mimesis.builtins import RussiaSpecProvider
from mimesis.locales import Locale
from mimesis.enums import Gender
from transliterate import translit, get_available_language_codes
from random import randint

generic = Generic(locale=Locale.EN)
person = Person(Locale.RU)
code = Code()
ru = RussiaSpecProvider()

def get_values():
    first_name = person.first_name(gender=Gender.FEMALE)
    last_name = person.last_name(gender=Gender.FEMALE)
    patronymic = ru.patronymic(gender=Gender.FEMALE)
    email = f"{translit(first_name+last_name, 'ru', reversed=True)}@mail.ru"
    email = email.replace("'", "")
    phone = code.imei()[0:11]
    birth_date = str(generic.datetime.date())
    password = generic.person.username()

    nations = ['Русский', 'Татарин', 'Украинец', 'Белорус', 'Серб', 'Курд', 'Армянин', 'Узбек']
    nation = nations[randint(0, len(nations)-1)]

    jobs = ['Программист', 'Крановщик', 'Сталевар', 'Полицейский', 'Пожарный']
    job = jobs[randint(0, len(jobs)-1)]

    return {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'patronymic': patronymic,
        'birth_date': birth_date,
        'job': job,
        'nation': nation,
        'phone': phone
    }
