import logging
from agent.Device import Device
from agent.global_queue import global_queue

if __name__ == "__main__":
    KA1 = Device(
        name='KA1',
        priority=0.7,
        sessions=14,
        completed_sessions=0,
        date_start='26.11.2023 12:15:00',
        entrance_lag=15,
        session_body=100,
        output_lag=15,
        schedule='KA_1_500.xlsx'
    )
    KA2 = Device(
        name='KA2',
        priority=0.5,
        sessions=8,
        completed_sessions=0,
        date_start='26.11.2023 16:25:00',
        entrance_lag=20,
        session_body=75,
        output_lag=15,
        schedule='KA_2_500.xlsx'
    )
    KA3 = Device(
        name='KA3',
        priority=0.3,
        sessions=4,
        completed_sessions=0,
        date_start='26.11.2023 22:27:00',
        entrance_lag=20,
        session_body=120,
        output_lag=20,
        schedule='KA_3_500.xlsx'
    )

    queue = global_queue()
    queue.add_item(KA1.schedule)
    queue.add_item(KA2.schedule)
    for i in queue.global_queue:
        print(i)
