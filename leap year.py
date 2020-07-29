year = int(input('Please enter year: ')) #receives input
if year % 4 != 0 :
    print('not a leap year')
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
             print('not a leap year')
    else:
        print('leap year')
        
            
        
    
