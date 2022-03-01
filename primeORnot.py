'''the number is called a prime number when the number is divible by only one and itself'''
number=int(input('enter the number: '))
def isprime(num):
    for i in range(2,num//2+1): #here the loop is taken from 2 to given number half becouse 0 and 1 are not taken becuase any number in number system is divisible by 0 and 1 the divisioblity is taken as when a nu,ber is divided by another if it leaves reminder zero then the number is taken as divisbile number by divisor
        if num%i==0:
            return False
    return True

print(isprime(number))