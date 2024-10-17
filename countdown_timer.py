import time

hour = int(input("Enter the hours: "))
min = int(input("Enter the minutes: "))
sec = int(input("Enter the seconds: "))

seconds = min*60+hour*3600+sec

for x in range (seconds,0,-1):
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!!!")