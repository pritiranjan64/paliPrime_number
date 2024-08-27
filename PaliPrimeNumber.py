#print pali prime number in a given range using function.
def isPrime(n):
    dummy=n
    if dummy<=1:
        return False
    for i in range(2,dummy//2+1):
        if dummy%i==0:
            return False
    else:
        return True
def reverse_number(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
def isPaliPrime(n):
    rev=reverse_number(n)
    if isPrime(n) and n==rev:
        return True
    else:
        return False
def paliPrimeNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isPaliPrime(n):
            print(n)
        
paliPrimeNumbers(10,100)            



#print first N pali prime number using function.
def isPrime(n):
    dummy=n
    if dummy<=1:
        return False
    for i in range(2,dummy//2+1):
        if dummy%i==0:
            return False
    else:
        return True
def reverse_number(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
def isPaliPrime(n):
    rev=reverse_number(n)
    if isPrime(n) and n==rev:
        return True
    else:
        return False
def first_n_Paliprime(n):
    number=1
    c=0
    while True:
        if isPaliPrime(number):
            c+=1
            print(number)
        if c==n:
            break
        number+=1
first_n_Paliprime(10)     


#print first Nth pali prime number using function.
def isPrime(n):
    dummy=n
    if dummy<=1:
        return False
    for i in range(2,dummy//2+1):
        if dummy%i==0:
            return False
    else:
        return True
def reverse_number(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
def isPaliPrime(n):
    rev=reverse_number(n)
    if isPrime(n) and n==rev:
        return True
    else:
        return False
def first_n_Paliprime(n):
    number=1
    c=0
    while True:
        if isPaliPrime(number):
            c+=1
        if c==n:
            print(number)
            break
        number+=1
first_n_Paliprime(10)           