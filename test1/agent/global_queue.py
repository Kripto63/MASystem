"""Содержит класс описание структуры глобальной очереди"""

class global_queue:
    def __init__(self, queue = []):
        self.global_queue = queue
        # self.global_iter = None

    def add_item(self, item):
        self.global_queue = sorted(self.global_queue + item, key=lambda x: x['Т входа'])

