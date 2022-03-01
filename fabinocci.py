# fabinoci sequence is taken as 0,1,1,2,3,5,8,13,21 and so on
'''and the fabinocci is started with 0 and 1 and next number is obtained by adding previos two numbers'''
#fabinocci sequence usinmg loop
def fabinocci_sequence(num):
    fabi_list=[0,1]
    for i in range(1,num):
        next_number=fabi_list[-1]+fabi_list[-2]
        fabi_list.append(next_number)
    return fabi_list
num=int(input('enter the length of sequence: '))
# print(fabinocci_sequence(num))

#fabinoci using recursion
'''recursion is called as the function is called inside the same function'''

'''in recursive method form 0 to the requed lenght a loop is created a and each value is given to function and that function creates the fabinocii number at that range '''

'''
for example the for loop is going on and the i value is 4
i.e i==4
then i value 4 in given to function and the function as two conditions those are called base condition when should the recursion should stop
the condition are i==0 return 0 but our i=4 so this conditiojn is false
second elif condition i==1 return 1 but this also fails
then recursion conditon is what
return fabinocii(num-1)+fabinocii(num-2)
so first consider fabinocci(num-1) ie our num=4 so num-1 is 3 
three is passed to the function again the if and elif condition are checked those got failed again 
fabinocii(num-1)+fabinocii(num-2) but now num=3 so num-1=2 and num-2=1
now again same process is carried out untill the based condition is reached and this tree of recursion can be of like as
                       
                       num=4 --->final level
                        / \
                       3   2  -->level 2
                      /\   /\ 
                     2  1  1 0 -->level 1
                    /\                    
   base level-->   1  0  
 
 
 Now at base level we have condition return 1 if num==1 and return 0 if num==0
 based on that at base level in one child num==1 so that function returns 1 and in onother child num==0 so it returns 0 and these two get added up because we have been ading the return values
 fabinocci(num-1)+fabinocci(num-2)
 so at base level we have 1+0=1
 in next level this 1 is added up to to right child of 3 value so then we have 1+1=2
 and then 2 is passed to the level two for function who calls by passing the value 3
 
 now the same procees is continued  for the tree 
                        2
                       / \
                      1   0
                at down level we have 1+0=1
                and this given to the upper level at positon 2
now at level 2 we have the value
 2 and 1
 now final recursion level 2+1 is given as output that is 3
'''
def fabinoci_recursive(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
       return fabinoci_recursive(num-1)+fabinoci_recursive(num-2)
for i in range(num):
    print(fabinoci_recursive(i),end='->')