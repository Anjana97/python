bdate=input("enter bdy dd-mm-yy")
cdate=input("enter bdy dd-mm-yy")

print(bdate)
print(cdate)

bdate,bmonth,byear=bdate.split("-")
cdate,cmonth,cyear=cdate.split("-")

age=int(cyear)-int(byear)

