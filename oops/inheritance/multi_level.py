class parent:
    def m1(self):
        print("print inside parent")

class child(parent):
    def m2(self):
        print("print inside child")

class subchild(child):   #multiple inheritance  u can give as  class subchild(child, parent)
    #this case is used when class child does'nt need parent, that's you can print child class as   class child()
    def m3(self):
        print("print  child")

sb=subchild()
sb.m3()
sb.m2()
sb.m1()

ch=child()
ch.m2()
ch.m1()

pa=parent()
pa.m1()
