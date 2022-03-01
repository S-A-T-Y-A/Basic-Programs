'''for clasic approach we can use same technique that is %10 and again number//10 for getting unit digits'''

#for trick approach

def sumofdigits(number):
    #covert it to string
    numstr=str(number)
    sum_=0
    for i in numstr:
        sum_+=int(i) #here i is coverted to int because intially we have converted to str so again we have converting it to int for adding
    return sum_

number=int(input('enter the number: ')) #no need of the int here it was your wish beacuse we anyway converting the number into string in functuion
print(sumofdigits(number))