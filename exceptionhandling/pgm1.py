no1=int(input("enter value for no1"))
no2=int(input("enter value for no2"))
lst=[1,2,3]
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)
try:
    print(lst[5])
except Exception as e:
    print(e.args)

#try:
#doubtful code
#except

