# 2016 4 20  14 | 2016 2 20  9 | 2015 12 31  1
import datetime
#
Year, Month, Day = map(int, input().split())
# print(Year, Month, Day)
Step = int(input())
# print(Step)
Start_Date = datetime.date(Year, Month, Day)
# print(Start_Date)
End_Date = Start_Date + datetime.timedelta(Step)
# print(End_Date)
timestampStr = End_Date.strftime("%Y %m %d").replace(' 0', ' ')
# print('Future Date : ', timestampStr)
print(timestampStr)