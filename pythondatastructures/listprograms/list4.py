#output [7,7,9,10,3,1,2]
lst=[6,6,8,9,4,2,3]
output=[]
for num in lst:
    if(num<5):
        output.append((num-1))
    else:
        output.append((num+1))
print(output)
