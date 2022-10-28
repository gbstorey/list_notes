def temps():
    days = int(input("How many days would you like to input?: "))
    day_temps = {}
    while days > 0:
        day_temps[days] = float(input(f"Day {days}'s high temp: "))
        days -= 1

    total = 0
    for temp in day_temps.values():
        total += temp
    average = float(total/len(day_temps))

    days_above = 0
    for temp in day_temps.values():
        if temp > average:
            days_above += 1

    print(f"Average = {average} \n {days_above} day(s) above average")

temps()
