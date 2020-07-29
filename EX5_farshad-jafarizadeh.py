#069
countries = ('Iran', 'USA', 'Canada', 'Germany', 'Italy')
print(countries)
country = input('Please enter the name of a country from tuple: ')
print(countries.index(country))
#070
countries = ('Iran', 'USA', 'Canada', 'Germany', 'Italy')
print(countries)
n = int(input('Please enter a number which 0 <= n <= 4 :'))
print(countries[n]) 
#071
L = ['football', 'basketball']
sport = input('Please enter your favorite sport: ')
L.append(sport)
L.sort()
print(L)
#072
subject = ['maths', 'algebra', 'literature', 'physics', 'chemistry',\
          'statistics']
print(subject)
dislike = input('Which one do you dislike(: : ')
subject.remove(dislike)
print(subject)
#073
food = {}
for i in range(1,5):
    F = input('Please enter 4 of your favourite foods: ')
    food[i] =  F
print(food)
#agar manzoor soal in ast ke shoamre ghaza ra vared konad:
n = int(input('Which one do you want to get rid of? (: : '))
del(food[n])
print(food)
#sorting
new = {}
for i in range(1,len(food)+1):
    new[i] = food[i+1]      #how to sort a dictionary respect to keys algorithm               
print(new)
#074
colours = []
for i in range(10):
    t = input('Please enter a list of 10 colours: ')
    colours.append(t)
a = int(input('Please modify start of the range your number should be 0 <= n <=4 : '))
b = int(input('Please modify end   of the range your number should be 5 <= n <=9 : '))
print(colours[a:(b+1)]) 
#075
numbers = [110, 821, 429]
print(numbers)
f = 0 #flag for finding
n = int(input('enter a 3 diigit number: '))
for i in numbers:
    if i == n:
        print(numbers.index(i))
        f = 1 #set f if find
else:
    if f == 0:
        print('That is not in the list')
#076
L =[]
for i in range(3):
    t = input('name 3 people you want to invite them to the party: ')
    L.append(t)
ans = input('Do you want to invite more? : ')
while ans != 'no':
    t = input('name the person you wanna invite: ')
    L.append(t)
    ans = input('Do you want to invite more? : ')
else:
    print(len(L))
#077
L =[]
for i in range(3):
    t = input('name 3 people you want to invite them to the party: ')
    L.append(t)
ans = input('Do you want to invite more? : ')
while ans != 'no':
    t = input('name the person you wanna invite: ')
    L.append(t)
    ans = input('Do you want to invite more? : ')
else:
    print(L)
name = input('type one name from the list: ')
pos = L.index(name)
print(pos)
ans = input('do you still want to invite this person? :')
if ans == 'no':
    L.remove(name)
print(L)
#078
L = ['Dorehami', 'Gvarzeshi', 'be khane bar migardim(:', 'paythakht']
for i in L:
    print(i)
programm = input('enter your TV programm: ')
pos = int(input('enter the position: '))
L.insert(pos,programm) 
for i in L:
    print(i)
#079
nums = []
i = 1
for i in range(3):
    n = int(input('enter the number: '))
    nums.append(n)
ans = input('Do you want to keep the last number you entered? :')
if ans == 'no':
    del(nums[-1])
print(nums)