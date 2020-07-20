"""
s=input("enter the String: ")
count=0
for i in s:
    if i!=2:
        #print("the character present at ",count,"letter is",i)
         print("the character present at ", count, "equal to character is", i)
    else:
        print("not same character",i)
    count+=1
print("count: ",count)
"""
num=int(input("Enter how many rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

num=int(input("Enter how many rows: "))
for i in range(1,num+1):
    print("*" * i)

for i in range(4):
    for j in range(4):
        print("i={} and j={}".format(i,j))


"""
i=0
while 1:
    print("Hello")
    i+=1
    if i==5:
        break
"""

i=1     #i is declared mandetory
while 1234:
    print("hello")
    i=i+1
    if i==5:
        break


for i in range(10):
    if i==7:
        break
    print(i)

cart=[10,20,400,600]
for item in cart:
    if item>=500:
        print("Sorry... does not order processing We can mandatory to pay insurance")
        break
    print("order processing",item)








