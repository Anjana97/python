#2
#2+22=24
#3
#3+33+333=369

# num=int(input("Enter number"))
# sum=i=p=0
# while(i<num):
#   p=p+((10**i)*num)
#   sum+=p
#   i+=1
#  print(sum)


#or

num=int(input("Enter number"))
sum=i=0
while(i<num):
    sum+=sum+((10**i)*num)
    i += 1
print(sum)