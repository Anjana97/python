#sum of odd numbers within a given limits
low=int(input("enter lower number"))
upp=int(input("enter upper number"))
sum=0
if(low>upp):
    print("lower should be greater")
while(low<=upp):
    if(low%2!=0):
        sum+=low
    low+=1
print(sum)