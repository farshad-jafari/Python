year  = int(input('Please enter year: ' )) #receives year
month = int(input('Please enter month: ')) #receives month
day   = int(input('Please enter day: '  )) #receives day
if year % 4 != 0 :
    print('not a leap year')
    y = 0
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
            y = 1
        else:
             print('not a leap year')
             y = 0
    else:
        print('leap year')
        y = 1
if y == 0:
    months = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
else:
    months = [31 ,29 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
day_of_year = day + sum(months[:(month - 1)])
if   day_of_year % 10 == 1:
    print('it is the',day_of_year,'st day of year')
elif day_of_year % 10 == 2:
    print('it is the',day_of_year,'nd day of year')
elif day_of_year % 10 == 3:
    print('it is the',day_of_year,'rd day of year')
else:
    print('it is the',day_of_year,'th day of year')
