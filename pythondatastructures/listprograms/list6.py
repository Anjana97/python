#seaching the elements in the list
lst=[120,11,12,13,14]
num=int(input("enter the element to search"))
flag=0
for i in lst:
    if i==num:
        flag+=1
        break
    else:
        flag=0

if flag>0:
    print("element found")
else:
    print("not found")

    #orrrr

# if (num in lst):
#     print("element found")
#
# else:
#     print("not found")

