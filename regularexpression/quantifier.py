from re import *
# pattern="a+"      #check for a and more than one a
# pattern="a*"      #a+ plus zero occurance of a
# pattern="a?"      #a plus zero number of a
pattern="^a"      #check for strating with 'a'
# pattern="a$"      #ending with a
# pattern='a{2,3}'    #check for minimun 2 a and max of 3 a
# matcher=finditer(pattern,"aaaabaabaaaaaba")
# for match in matcher:
#     print(match.start())
#     print(match.group())

matcher=fullmatch(pattern,"aaaabaabaaaaaba")
if matcher!=None:
    print("given string strating with a")
else:
    print("given string is not strating with a")