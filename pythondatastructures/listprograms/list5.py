#output [14,11,10,13]
lst=[2,5,6,3]
total=sum(lst) #16
out=[]
for num in lst:
    out.append((total-num)) #16-2=14,16-5=11....
print(out)
