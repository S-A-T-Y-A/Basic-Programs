'''we have many approaches for swapping two numbers'''

#using third variable
num1,num2=map(int,input('enter the two numbers: ').split(',')) #hint:in input giving in terminal after ruuning the code give the input format as num1,num2
def swapthirdvarhelp(num1,num2):
    temp=num1 #store any one number in a third varible for reference becase in next line we are giving num2 value to num1 so then num1 value is lost so for that case the num1 value is stored in third value to provide that value to num2
    num1=num2
    num2=temp
    return num1,num2
print(f'before swapping num1,num2: {num1,num2}')
num1,num2=swapthirdvarhelp(num1,num2)
print(f'after swapping num1,num2: {num1,num2}')


#with out using third variable classic approach
print('without third variable')
num1,num2=map(int,input('enter the two numbers: ').split(','))
def classicapproach(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2
print(f'before swapping num1,num2: {num1,num2}')
num1,num2=classicapproach(num1,num2)
print(f'after swapping num1,num2: {num1,num2}')

#python trick approach
print('trick approach')
num1,num2=map(int,input('enter the two numbers: ').split(','))
num1,num2=num2,num1
print(num1,num2)