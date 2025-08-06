n = int (input("enter the range : "))
ls=[]
for i in range (n):
    x1=int(input("enter the element: "))
    x2=int(input("enter the element: "))
    ls.append((x1,x2))
for i in range (n):
    for j in range(0,n-i-1):
        if(ls[j][1]>ls[j+1][1]):
            temp=ls[j]
            ls[j]=ls[j+1]
            ls[j+1]=temp
print("the sorted list is : \n ",ls)
        