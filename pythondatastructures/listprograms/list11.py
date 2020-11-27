#[1,2,3,5,6,7,8,9,10]
# 0 1 2 3 4 5 6 7 8
#low     mid      upp
lst=[1,2,3,5,6,7,8,9,10]
low=0
# lst.sort() or lst=sorted(lst)
lst=sorted(lst)
# print(lst)
upp=len(lst)-1
flag=0
# print(low,"and",upp, "and", mid)
search=int(input("enter element to search"))
while(low<upp):
    mid = (low + upp) // 2
    if(search>lst[mid]):
        low=mid+1
    elif(search<lst[mid]):
        upp=mid-1
    elif(search==lst[mid]):
       flag=1
       break


if (flag>0):
    print("found")
else:
    print("not found")
