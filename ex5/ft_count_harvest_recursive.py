def ft_count_harvest_recursive():
    harvest_day = int(input("Days until harvest: "))

    def count_days(day):
        if day <= harvest_day:
            print("Day ", day)
            count_days(day + 1)
    count_days(1)
    print("Harvest time!")
