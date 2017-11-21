import time
# time.localtime(time.time())

def GetNowTime():   #获取当前系统时间
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

Age = int(input('What is yoiur curretn age?'))
RetireAge = int(input('At what age would you like to retire?'))
print('You have %s years left until you can retire.'%(RetireAge-Age) #打印离退休的时间
      
# print(GetNowTime()) #打印当前系统时间
