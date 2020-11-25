#amstrongnumber

num=int(input("enter a number"))
rev=0
while(num!=0):#123!=0 12!=0 1!=0
    digit=num%10#123%10=3 12%10=2 1
    rev=rev+(digit**3)#0+27 27+(2**3)=35 35+1=36
    num=num//10#12 12//10=1
print(rev)

