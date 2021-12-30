import datetime
# Input a unix time to check what the brightness at that time will be
while True:
    now = datetime.datetime.fromtimestamp(int(input())) - datetime.timedelta(hours=6)
    timep = 1 - ((now.hour * 60 + now.minute) / 900)
    if timep < 0:
        timep = 0
    print(round(timep*255),timep, now.hour, now.minute)
    print(((round(timep*255),round(timep*255),round(timep*200))))