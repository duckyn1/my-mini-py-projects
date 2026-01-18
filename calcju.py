import time
import math

principle = 0
time1 = 0
rate = 0

while principle <= 0:
    principle = float(input("Enter ur principle amount: "))
    if principle <= 0:
        print("principle can't be equal or smaller than zero")

while rate <= 0:
    rate = float(input("Enter ur rate: "))
    if rate <= 0:
        print("rate can't be equal or smaller than zero")

while time1 <= 0:
    time1 = float(input("Enter ur time: "))
    if time1 <= 0:
        print("time principle can't be equal or smaller than zero")

totalpr = principle * (1 + rate / 100) ** time1

print("Calculating balance..")
time.sleep(0.5)
print(f"{principle} * (1 + {rate} / 100) ** {time1}")
time.sleep(0.5)
print(f"{principle} * (1 + {rate} / 100) ** {time1} = {round(totalpr)}")
time.sleep(0.5)
print(f"Balance after {round(time1)} year/s: {round(totalpr):.2f}$")