#create a function to perform factorial
num=int(input("enter number"))
def fact(num):
    if num<0:
        print("not exist")

    elif num==0:
        print(1)
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print(fact)
fact(num)