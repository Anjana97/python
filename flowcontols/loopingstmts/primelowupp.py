#read low limit and upp limit prime numbers

low=int(input("enter the num1"))
upp=int(input("enter the num2"))
for num in range (low,upp+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num)