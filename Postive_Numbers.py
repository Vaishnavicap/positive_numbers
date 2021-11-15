#n is variable for storing no. of elements
n = int(input("Enter the number of elements in list :"))
list1 = [] #storing all elements
list2 = [] #storing all postive elements
for i in range(n):
    x = int(input())
    list1.insert(i,x)
    if(x > 0):
        list2.append(x)
print("List of all Numbers inserted :")
print(list1)        
print("List of all Postive Numbers:")
print(list2)