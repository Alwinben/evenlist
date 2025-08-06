l1=[]
l2=[]
a=int(input("enter the range of the list :"))
for i in range (a):
    x=int(input("enter the element :"))
    l1.append(x)
print("the given list is \n",l1)   
for i in l1:
    if i not in l2:
        l2.append(i)
print("the new list is \n ",l2)        
