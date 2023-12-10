from thespian.actors import *
import logging
from Actors.actorPPI import actorPPi
from Actors.actorKA import actorKA

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

if __name__ == '__main__':
    actorSystem = ActorSystem()

    # создаем акторы ППИ
    anadyr = actorSystem.createActor(actorPPi)
    dudinka = actorSystem.createActor(actorPPi)
    krasnoyarsk = actorSystem.createActor(actorPPi)
    murmansk = actorSystem.createActor(actorPPi)
    khabarovsk = actorSystem.createActor(actorPPi)

    list_PPI = [anadyr, dudinka, krasnoyarsk, murmansk, khabarovsk]
    list_name_PPI = ['Анадырь', 'Дудинка', 'Красноярск', 'Мурманск', 'Хабаровск']

    # передаем названия ППИ
    actorSystem.tell(anadyr, {'message': 'Передача данных', 'name': 'Анадырь'})
    actorSystem.tell(dudinka, {'message': 'Передача данных', 'name': 'Дудинка'})
    actorSystem.tell(krasnoyarsk, {'message': 'Передача данных', 'name': 'Красноярск'})
    actorSystem.tell(murmansk, {'message': 'Передача данных', 'name': 'Мурманск'})
    actorSystem.tell(khabarovsk, {'message': 'Передача данных', 'name': 'Хабаровск'})

    # создаем КА
    KA1 = actorSystem.createActor(actorKA)
    KA2 = actorSystem.createActor(actorKA)
    KA3 = actorSystem.createActor(actorKA)

    # передаем данные для КА
    actorSystem.tell(KA1, {
        'message': 'Передача данных',
        'name': 'KA1',
        'priority': 0.7,
        'sessions': 14,
        'completed_sessions': 0,
        'date_start': '26.11.2023 12:15:00',
        'entrance_lag': 15,
        'session_body': 100,
        'output_lag': 15,
        'schedule': 'KA_1_500.xlsx'
    })

    actorSystem.tell(KA2, {
        'message': 'Передача данных',
        'name': 'KA2',
        'priority': 0.5,
        'sessions': 8,
        'completed_sessions': 0,
        'date_start': '26.11.2023 14:15:00',
        'entrance_lag': 25,
        'session_body': 120,
        'output_lag': 25,
        'schedule': 'KA_2_500.xlsx'
    })

    actorSystem.tell(KA3, {
        'message': 'Передача данных',
        'name': 'KA3',
        'priority': 0.3,
        'sessions': 4,
        'completed_sessions': 0,
        'date_start': '26.11.2023 17:15:00',
        'entrance_lag': 50,
        'session_body': 150,
        'output_lag': 50,
        'schedule': 'KA_3_500.xlsx'
    })

    # Передаем адреса ППИ в КА
    for PPI, name_PPI in zip(list_PPI, list_name_PPI):
        actorSystem.tell(KA1, {
            'message': 'Данные ППИ',
            'ППИ': name_PPI,
            'Адрес': PPI
        })

    for PPI, name_PPI in zip(list_PPI, list_name_PPI):
        actorSystem.tell(KA2, {
            'message': 'Данные ППИ',
            'ППИ': name_PPI,
            'Адрес': PPI
        })

    for PPI, name_PPI in zip(list_PPI, list_name_PPI):
        actorSystem.tell(KA3, {
            'message': 'Данные ППИ',
            'ППИ': name_PPI,
            'Адрес': PPI
        })

    actorSystem.tell(KA1, {'initialization': 2})
    actorSystem.tell(KA2, {'initialization': 2})
    actorSystem.tell(KA3, {'initialization': 2})

    actorSystem.tell(KA1, {'Запрос данных': 'KA'})
    actorSystem.tell(KA2, {'Запрос данных': 'KA'})
    actorSystem.tell(KA3, {'Запрос данных': 'KA'})

    for i in list_PPI:
        actorSystem.tell(i, {'Запрос данных': 'PPI'})
