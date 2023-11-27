"""Содержит класс описание структуры космического аппарата"""
import datetime
import pandas as pd

class Device:
    def __init__(self, name = 'KA',priority=0, sessions=14, completed_sessions=0, date_start='27.11.2023 17:08:00',
                 entrance_lag=15, session_body=100, output_lag=15, schedule='', ):
        self.name = name
        self.number_of_sessions = sessions
        self.completed_sessions = completed_sessions
        self.priority = priority
        self.date_start = datetime.datetime.strptime(date_start, '%d.%m.%Y %H:%M:%S')
        self.entrance_lag = entrance_lag
        self.session_body = session_body
        self.output_lag = output_lag
        self.schedule = pd.read_excel(schedule).to_dict('index')


