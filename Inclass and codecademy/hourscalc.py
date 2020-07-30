hour1 = float(input("Hour1 "))
min1 = float(input("mins1 "))
hour2 = float(input("Hour2 "))
min2 = float(input("mins2 "))
total_hours = hour2 - hour1
total_mins = min2 - min1
if total_mins >= 60:
    total_mins = total_mins - 60
    total_hours = total_hours + 1
elif total_mins <= 0:
    total_mins = total_mins + 60
    total_hours = total_hours - 1

print(int(total_hours),":",int(total_mins))