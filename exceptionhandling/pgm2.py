no1=int(input("enter value for no1"))
no2=int(input("enter input for no2"))
try:
    res=no1/no2
    print(res)
except:
    no2 = int(input("enter input for no2"))
    try:
        res = no1 / no2
        print(res)
    except:
        no2 = int(input("enter input for no2"))
        res = no1 / no2
        print(res)
finally:
    print("hello anjana")
    print("bonjour anjana")