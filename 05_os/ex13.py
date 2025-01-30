import os
import calendar

def create_folders():
    months = list(calendar.month_name)[1:]

    for year in range(2018, 2026):
        for month in months:
            month_number = months.index(month)+1
            for day in range(1, (calendar._monthlen(year, month_number))+1):
                os.makedirs(f'sales_{year}/{month}_{year%100}/{day:02d}_{month[:3]}_{str(year)[2:]}')




create_folders()