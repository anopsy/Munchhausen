# Python Program to Print Natural Numbers from 1 to N
 
number = int(input("How many Munchhausen numbers are there in a range from 0 to: "))

print("The List of Munchhausen Numbers {0} are".format(number)) 

    
    
for i in range(1, number + 1):
    sum=0
    list=[int(a) for a in str(i)]
    
    for x in list:
        sum = sum + (x**x)
    #print(list, sum)
    if sum == int(i):
        print(i)

