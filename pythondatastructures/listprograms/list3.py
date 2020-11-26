# output 2*1=2,3**2=9,4**3=64,6**4=1296
lst=[2,3,4,6]
lst=list()
out=[]
i=1
for i in lst:
    num=i**(i-1)
    out.append(num)
print(out)