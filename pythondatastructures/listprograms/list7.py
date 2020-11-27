#find least positive integer
lst=[-2,-1,0,1,2,5]
cnt=1
for i in range(0,len(lst)):
    if cnt in lst:
        cnt+=1
        pass
    else:
        print(cnt)
        break