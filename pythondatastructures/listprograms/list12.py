#searching element with its pairs

lst=[2,1,3,4,6,7]
lst.sort()
low=0
upp=len(lst)-1
ele=int(input("enter number"))
flag=0
while(low<=upp):
    total=lst[low]+lst[upp]
    # case1
    if(ele<total):
        upp-=1


    # case2
    if(ele>total):
        low+=1
    # case3
    if(ele==total):
       print("pairs are",lst[low],"",lst[upp])
       break