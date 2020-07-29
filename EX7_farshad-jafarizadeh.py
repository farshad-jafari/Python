def fibo (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        print('error')
    else:
        return fibo(n-1)+fibo(n-2)

def EX7(n) :
    L = []
    for i in range(n+1):
        L.append(fibo(i))
    else:
        print(L)
EX7(5)