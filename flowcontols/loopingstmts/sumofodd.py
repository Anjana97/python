low=int(input("enter number"))
upp=int(input("enter number"))
evensum=oddsum=0
for i in range (low,upp):
    if((i%2)==0):
        evensum+=i
    else:
        oddsum+=i
print(oddsum,",",evensum)