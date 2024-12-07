from datetime import datetime

date1 = datetime(year=2012, month=9, day=28, hour=12, minute=32,second=30)
date2 = datetime(year=2024, month=5, day=5, hour=8, minute=0, second=0)
td = date2 - date1
print(td.total_seconds())