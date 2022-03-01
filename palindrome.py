'''for palindrome we have many approches the palindrome is taken when the number is reversed then it as the same sequence as original number like  "aha"=="aha" this word is an palindrome'''

#plaindrome word

from tkinter import N


word=input('enter the word: ')
word_reversed=word[::-1] #it was a trik to reverse the word or string
if word==word_reversed:
    print('palindrome')
else:
    print('not palindrome')
#THE NUMBER IS ALSO SAME BUT THE NUMBER SHUOLD BE STRING DATA TYPE

#classic approach for string reverse
word=input('enter the word for classic approach: ')
def classic_approach(word):
    word_rev='' #intialise a word with empty string
    #now ioterate the loop from reverse that is from len(stirng) to intial index that if len of string is 5 then we have loop like 4,3,2,1,0
    for i in range(len(word)-1,-1,-1):
        word_rev+=word[i]
    if word_rev==word:
        print('palindrome')
    else:
        print('not palindrome')
        
classic_approach(word)

#basic approach to check a number is palindorme or not
'''
for this we should no that we have number 123 then if say 123%10 then we get 3 and as well 123%100=23 and so on and as similar if we say 123//10=12 and 123//100=1

'''
number=int(input('enter the number: '))
def checknumber(number):
    temp=number #store the given number in a variable for future reference
    new_num=0                                             
    while number>0:
        digit=number%10                              
        new_num=new_num*10+digit
        number//=10
        
    if temp==new_num:
        print('Palindrome')
    else:
        print('not palindrome')

checknumber(number)     

'''
the process that is while is continued untill the number is greter than zero
lets us take number=123
now intially new_num=0
and number//=10 this n is used for removing the unit digit
now in step 1
new_num=0
number=123
enters the while loop checks condition number>0 i.e 123>0 so enters the loop
in loop we get digit by number%10 digit=3 that 123%10=3
now this is added to new _numbwer that new_num=new_num*10+digit i.e it is like 0*10+3=3 now new_num=3
and number=number//10 this will remove the unit digit that is like 123//10 we have 12 as number noe number=12
and again comes to top checks loop condition number>0 so agia process is cintinued unit number gets 0
that is like the process continues
in second loop
number=12
then number//10 we have 1
in next loop number=1
then number//10 we have 1
still number>0
in this loop the further again number//10 then 1//10=0
so again comes to top and checks the while condition it becomes falls and whille loop is terminated

'''