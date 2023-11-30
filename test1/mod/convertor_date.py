import datetime

def convertor_date(schedule, date_start, entrance_lag, session_body, output_lag, name):
    """Перевод локального времени в фактическое"""
    total = []
    min_session = entrance_lag + output_lag
    session = session_body + min_session
    for i in schedule.items():
        temp = i[1]
        if temp['Длительность'] >= session:
            i[1]['Т входа'] = date_start + datetime.timedelta(seconds=temp['Т входа'])
            i[1]['Т выхода'] = date_start + datetime.timedelta(seconds=temp['Т выхода'])
            i[1]['КА'] = name
            total.append(i[1])
    return total