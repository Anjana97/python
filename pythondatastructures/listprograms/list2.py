#store odd and even numbers in list

limit=int(input("enter limit"))
lst=list()
lsteve=list()
lstodd=list()

for i in range (1,(limit+1)):
    lst.append(i)
    if((i%2)==0):
        lsteve.append(i)
    else:
        lstodd.append(i)

print(lsteve)
print(lstodd)
# print(sum(lst))
