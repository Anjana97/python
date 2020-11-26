#output value=6 (4,2)
lst=[1,2,3,4,6,7]
sum=6
for i in lst:
    for j in lst:
        ctotal=i+j
        if(sum==ctotal):
            print((i,j))
            break

