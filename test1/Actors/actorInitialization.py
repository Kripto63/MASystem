import logging

from thespian.actors import *


class actorInitialization(Actor):
    """Класа описывает агента, который будет запускать обработку данных"""

    def __init__(self):
        super().__init__()

    def receiveMessage(self, msg, sender):
        print(f'Актор инициализации {self.myAddress} получил сообщение {msg} от {sender}')
        self.send(sender, msg)
