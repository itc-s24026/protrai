#import datetime
#print(datetime.datetime.now()) 用导入模块的方式查看当前系统时间

#now = datetime.datetime.now()
#print(now) 用赋值方式查看当前系统时间

#print(now.strftime("%Y年%m月%d日 %H:%M:%S")) 用展开变数名查看当前系统时间

#print(calendar.month(2024,7)) 查看想要的年月日记时间，中间用逗号分布


import datetime
import calendar

# 現在の時刻を表示
current_time = datetime.datetime.now()
print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# 2024年6月のカレンダーを表示
print("\nCalendar for June 2024:")
print(calendar.month(2024, 6))

