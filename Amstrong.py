'''A number is called as amstrong when the sum of cube of individual digit in a given number is equal to the number the that is called as amstrong number'''

#classic approach
def classicAmstrong(number):
    #same as for palindrome we have to acess all the digits in the number 
    temp=number #store the number in temp variable to perform operations
    newnum=0
    while temp>0:
        digit=temp%10
        newnum=newnum+(digit**3) # here ** is called as power that is 2**3 we get 8 asusual 2**2=4
        temp=temp//10
    if newnum==number:
        print('Amstrong')
    else:
        print('Not Amstrong')
number=int(input('enter the number: '))    
classicAmstrong(number)
print('another approach')
#trick approach
def trickAmstrong(number):
    temp=str(number) # for this approach convert the given number into string data type
    # now for acces the each element in the string converted number b using for or while loop
    newnum=0
    for i in temp:
        digit=int(i)**3
        newnum+=digit
    if number==newnum:
        print('Armstrong')
    else:
        print('Not armstrong')
trickAmstrong(number)