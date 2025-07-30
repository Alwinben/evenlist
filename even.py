numbers=int(input("enter the no elements in the list"))
list=[]
even = []
for i in range(numbers):
    number=int(input("enter the numbers"))
    list.append(number)
    if number % 2 == 0:
        even.append(number)
print(list)
print("Even numbers:", even)
