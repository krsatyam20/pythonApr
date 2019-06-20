
#create a function

class a:
    
 def hello(s):
     print("hello")
        

class b(a):
    def add(x):
        print("add")

class c(b):
    def sub(x):
        print("sub")


#call a function

#a.hello()

#obj=a()
obj2=c()

obj2.hello()


obj2.add()


class addition:
    @staticmethod
    def add(a,b):
        c=a+b
        print(c)



a=addition()

a.add(10,20)













    
