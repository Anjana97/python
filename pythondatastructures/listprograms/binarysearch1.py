#asending order

lst=[2,5,1,8,7,6,3,11,10]
#sort the listusing sort function
# data=sorted(lst)
# print(data)

#sort without sorting function
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)-1):
        if (lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
