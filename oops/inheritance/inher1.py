#inheritance
#parent    base      super
#child    derived    subclass

class parent:
    def phone(self):
        print("have nokia 5310")
        self.__laptop()
    def __laptop(self): #private method
        print("i have lap")

class child (parent):
   def bike(self):
       print("i have duke")


ch=child()
ch.phone()
ch.bike()


#explanation
#here function phone is public and __laptop is private, __ indicate private method
#the child can inherit parent by calling ch.parent function
#ch is the objectof child. so whenever we need to cal some function we need to use ch.function
#to call a private function in child, first we need to set a calling function of private method in public class,
#that is call private function inside the publich function in parent class