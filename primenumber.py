# this is a program for primenumbers in python
def primenum(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if (n%i)==0:
                print(f'{n} is not a prime number')
                break
        else:
            print(f'{n} is  a prime number')
    else:
        print(f'{n} is Not a prime number')
