'''A word is said to be anagram to another word when both the words have same lenght and have same charcters '''
w1=input('enter the word one: ')
w2=input('enter the word two: ')
if len(w1)==len(w2):
    w1,w2=list(w1),list(w2) #here the words are converted to list becuase the string data type does not have a sort function
    w1.sort()
    w2.sort()
    if w1==w2:
        print('anagram') #this condition is printed when the two words have same lenght and same charcters
    else:
        print('Not Anagram') #this condition is printed when the two words have same lenght but dont have same charcters
else:
    print('Not anagram') #this condition is printed when both the words are of different lenght
    

'''
 the sort is used becuase
 the angrams have same lenght and same charters
 for example (cat,act),(elbow,below)
 in cat and act the lenght are same and if sort them we have [a,c,t] and[a,c,t] now the two words have same chacters if we sort them we have the same words like act so if we compare them by sorting and if they are equal they are anagram
'''