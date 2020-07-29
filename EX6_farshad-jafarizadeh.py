#045
total = 0
while total <= 50:
    n = int(input('enter a number: '))
    total += n
    print('the total is',total)

#046
n = 0
while not(n > 5):
    n = int(input('enter a number: '))
else:
    print('The last number you entered was',n)

#047
total = int(input('enter first number: '))
n = int(input('enter second number: '))
total += n
ans = input('type "y" if you want to add another number: ')
while ans == 'y':
    n = int(input('enter a number: '))
    total += n
    ans = input('type "y" if you want to add another number: ')
else:
    print(total)

#048
name = input('enter the name of person you want to invite to the party: ')
guest = [name]
print(name,'has now been invited')
count = 1
ans = input('Do you want to invite sb else? type "y" if yes: ')
while ans == 'y':
    name = input('enter the name of person you want to invite to the party: ')
    print(name,'has now been invited')
    count += 1
    ans = input('Do you want to invite sb else? type "y" if yes: ')
else:
    print(count)

#049
compnum = 50
count = 0
n = int(input('enter your guess: '))
while n != compnum:
    if n > compnum:
        print('too high')
        count += 1
        n = int(input('enter your guess: '))
    elif n < compnum:
        print('too low')
        count += 1
        n = int(input('enter your guess: '))
else:
    count += 1
    print('Well done. you took',count,'attempts')

 #050
n = int(input('enter a number between 10 and 20: '))
while not(10 <= n <= 20):
    if n < 10:
        print('too low ')
        n = int(input('enter a number between 10 and 20: '))
    elif n > 20:
        print('too high')
        n = int(input('enter a number between 10 and 20: '))
else: 
    print('Thank you')

 #051
num = 10
print('There are',num,'green bottles hanging on the wall,',num,'green bottles hanging on the wall'\
      ' and if 1 green bottle should accidentally fall')
n = int(input('how many green bottles will be hanging on the wall? :'))
while num != 0:
    while n != num - 1:
        n = int(input('No, try again: '))
    else:
        num -= 1
        print('There are',num,'green bottles hanging on the wall,',num,'green bottles hanging on the wall'\
        ' and if 1 green bottle should accidentally fall')
    if num == 0:
        break
    n = int(input('how many green bottles will be hanging on the wall? :'))