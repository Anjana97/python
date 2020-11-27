#descending order
lst=[2,1,5,3,9,8,6,7]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[j]>lst[i]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
print(lst)
