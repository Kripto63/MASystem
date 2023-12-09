import logging
import datetime
import pandas as pd

from thespian.actors import *
from funcs.convertor_date import convertor_date


class actorKA(Actor):
    """
    Класс описывает актора КА
    """

    def __init__(self):
        super().__init__()
        self.name = 'name'
        self.number_of_sessions = 'sessions'
        self.completed_sessions = 'completed_sessions'
        self.priority = 'priority'
        self.date_start = 'date_start'
        self.entrance_lag = 'entrance_lag'
        self.session_body = 'session_body'
        self.output_lag = 'output_lag'
        self.schedule = 'schedule'

        self.queue = [[], [], []]
        self.addresses_PPI = {}

    def receiveMessage(self, msg, sender):
        if msg.get('message') == 'Передача данных':
            self.name = msg.get('name')
            self.number_of_sessions = msg.get('sessions')
            self.completed_sessions = msg.get('completed_sessions')
            self.priority = msg.get('priority')
            self.entrance_lag = msg.get('entrance_lag')
            self.session_body = msg.get('session_body')
            self.output_lag = msg.get('output_lag')
            self.date_start = datetime.datetime.strptime(msg.get('date_start'), '%d.%m.%Y %H:%M:%S')
            self.schedule = convertor_date(pd.read_excel(msg.get('schedule')).to_dict('index'), self.date_start,
                                           self.entrance_lag, self.session_body, self.output_lag, self.name)

        if msg.get('message') == 'Данные ППИ':
            self.addresses_PPI[msg.get('ППИ')] = msg.get('Адрес')
            # logging.info(self.addresses_PPI)

        if msg.get('initialization') == 2:
            logging.info('Начинаем перебор')
            self.createRequest(self.schedule)

        if msg.get('Запрос данных') == 'KA':
            print('*+' * 5 + self.name + '+*' * 5 + 'Количество сеансов с ППИ - ' + str(len(self.queue[2])))
            print(*zip(*self.queue), sep='\n')
            print('-' * 20)

        if msg.get('Ответ от ППИ'):
            logging.info(
                f'Актор ППИ с адресом {self.myAddress} и названием {self.name} получил сообщение {msg} от {sender}')
            if msg.get('Виток') not in self.queue[0]:
                if msg.get('Ответ от ППИ'):
                    self.queue[0].append(msg.get('Виток'))
                    self.queue[1].append(msg.get('Время'))
                    self.queue[2].append(msg.get('ППИ'))
                    self.send(sender, {'Ответ от КА': True, 'Время': msg.get('Время'), 'КА': self.name})
                    if self.completed_sessions < self.number_of_sessions:
                        self.completed_sessions += 1
        else:
            logging.info(
                f'Актор ППИ с адресом {self.myAddress} и названием {self.name} получил сообщение {msg} от {sender}')

        # logging.info(
        #     f'Актор ППИ с адресом {self.myAddress} и названием {self.name} получил сообщение {msg} от {sender}')

    def createRequest(self, msg):
        for i in range(1, 150):
            temp_info = list(filter(lambda x: x['Виток'] == i, msg))
            # print(temp_info)
            # print('-'*20)
            for j in temp_info:
                self.send(self.addresses_PPI[j['ППИ']], j)
