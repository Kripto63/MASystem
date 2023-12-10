import logging

import pandas as pd


if __name__ == "__main__":
     schedule = pd.read_excel('500.xlsx')
     #print(schedule)
     PPI = schedule.to_dict('index')
     print(PPI)
     list_PPI = sorted(set([PPI[i]['ППИ'] for i in PPI]))
     print(list_PPI)
