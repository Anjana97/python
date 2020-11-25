flag=0
num=int(input("enter number"))
#num=int(input("enter number"))
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
if(flag==0):
    print("prime number")
else:
    print("not prime number")
