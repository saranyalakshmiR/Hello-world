def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,5]))

list=[10, 11, 12, 13, 14, 11]
l=[]
for i in list:
  l.insert(0,i)
print(l)

Ans:[11, 14, 13, 12, 11, 10]

3. Take 20 integer inputs from user and print the following:
number of positive numbers
print("Enter 10 integers:")
mylist = list(map(int, input().split()))
print("Positive numbers are:-")
for i in mylist:
    if i > 0:
        print(i, end=" ")
print()