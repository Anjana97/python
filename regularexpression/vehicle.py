#KL08BS1375 => VALID
#GJ08BN2211 => INVALID

from re import *
rule="KL\d{2}[A-Z]{2}\d{1-4}"

vehiclenum=input("enter vehicle number")
matcher=fullmatch(rule,vehiclenum)
if matcher!=None:
    print("valid")
else:
    print("invalid")