'''
the factorial is taken as muliple of all numbers form the given number to the 1
that is if we have to find the factorial of 5 the we have to calucalte 5*4*3*2*1=120 120 is factorial of 5
we can have this approach by reverse loop or while loop we will see both
'''
number=int(input('enter the number: '))
# factorial=1 initaate a variable with 1 becuese we should muliply if we give zero we doesn't get it because multiplied with zero we get zero only
#with for loop
def usingfor(number):
    factorial=1
    for i in range(number,0,-1):
        factorial*=i
    return factorial
print(f'using for : {usingfor(number)}')

#with while lopp

def usingwhile(number):
    num=number #stroing the given in a varible to perform operation
    factorial=1
    while num>=1:
        factorial*=num
        num-=1
    return factorial
print(f'using while : {usingwhile(number)}')