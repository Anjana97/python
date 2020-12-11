# def add(num1,num2):
#     res=num1+num2
#     print(res)
# add(10,20)


#variable lenght argument methods
#
# def add(*nums):
#     print(nums)
# add(10,20)
# add(10,20,30,40)
# add(10,11,12,13,14)

#to find the sum of all numbers
# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     print(total)
# add(10,20)
# add(10,20,30,40)
# add(10,11,12,13,14)


def printemp(**args):
    print(args)
printemp(home="kakkanad",name="anjana",workplace="rajagiri")