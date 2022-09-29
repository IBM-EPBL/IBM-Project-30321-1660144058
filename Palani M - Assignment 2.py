import random
import time
while True:
    temp=random.randint(1,50)
    humudity=random.randint(1,80)
    print("Temperature: ",temp)
    print("Humudity: ",humudity)
    if((temp>15 and temp<50) and (humudity>30 and humudity<60)):
        print("Room's Temperature and Humudity is Normal")
        print("Alarm OFF")
    else:
        print("Room's Temperature and Humudity is Abnormal")
        print("Alarm ON")
    time.sleep(1)
