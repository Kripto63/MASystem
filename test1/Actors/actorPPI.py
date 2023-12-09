import logging
from thespian.actors import *


class actorPPi(Actor):
    """
    Класс описывает актора ППИ
    """

    def __init__(self):
        super().__init__()
        self.queue = [[], [], []]
        self.name = None

    def receiveMessage(self, msg, sender):
        if msg.get('message') == 'Передача данных':
            self.name = msg.get('name')
        # logging.info(f'Актор ППИ с адресом {self.myAddress} и названием {self.name} получил сообщение {msg} от {sender}')
        if msg.get('Виток'):
            handler = self.check_time_range(self.queue[0], (msg['Т входа'], msg['Т выхода']))
            self.send(sender,
                      {'Ответ от ППИ': handler, 'Виток': msg['Виток'], 'Время': (msg['Т входа'], msg['Т выхода']),
                       'ППИ': self.name})

        if msg.get('Ответ от КА'):
            self.queue[0].append(msg.get('Время'))
            self.queue[1].append(msg.get('КА'))
            self.queue[2].append({msg.get('Время'): msg.get('КА')})
            self.queue[2] = sorted(self.queue[2], key=lambda d: next(iter(d.keys()))[0])

        if msg.get('Запрос данных') == 'PPI':
            print('*-' * 5 + self.name + '-*' * 5 + 'Количество сеансов с КА - ' + str(len(self.queue[2])))
            print(*self.queue[2], sep='\n')
            print('+' * 20)

        # print(self.queue)
        # logging.info(
        #     f'Актор ППИ с адресом {self.myAddress} и названием {self.name} получил сообщение {msg} от {sender}')

    def check_time_range(self, existing_ranges, new_range):
        if existing_ranges:
            for r in existing_ranges:
                if new_range[0] >= r[0] and new_range[1] <= r[1]:  # проверяем вложенность
                    return False
                if new_range[0] < r[1] and new_range[1] > r[0]:  # проверяем пересечение
                    return False
            return True
        else:
            existing_ranges.append(new_range)
            return True
