import logging

from thespian.actors import *


class SimplestActor(Actor):
    def __init__(self):
        super().__init__()
        logging.info('Создан новый актор')

    def receiveMessage(self, msg, sender):
        logging.info(f'Актор с адресом {self.myAddress} получил сообщение {msg} от {sender}')
