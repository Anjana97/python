from re import *
# pattern='[a-z]'        #all lower case letters
# pattern='[0-9]'        #all numbers
# pattern='[A-Z]'
# pattern='[^0-9]'       #except numbers wil print
# pattern='[^a-z]'       #except lowercase letters
# pattern='[^a-zA-Z0-9 ]' #special characters
# pattern='[a-zA-Z0-9]'    #print except special characters amd extra space
#pattern ="\s"              #spaces
#pattern="\S"                  #expect space
# pattern="\d"              #digits
# pattern="\D"                #excep digits
#pattern="\w"                   #[a-zA-Z0-9]
pattern="\W"                    #special character
matcher=finditer(pattern,"abc Z@#!&.7k")
for match in matcher:
    # print(match.start())
    print(match.group())