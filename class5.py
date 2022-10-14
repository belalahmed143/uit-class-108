
# class FirstClass:
#     p_d = 5
#     b = 8
# belal = FirstClass()
# student2 = FirstClass()

# print(belal.p_d)


# class FirstClass:
#     a=5
#     b=10
# student =  FirstClass()
# student2 = FirstClass()
# print(student.a, student.b)
# print(student2.a, student2.b)


# class EmpName:
#     f_name='Md.'
#     l_name='Hasanuzzaman'

# emp=EmpName()

# print(EmpName.f_name,EmpName.l_name)


# class Students:
#     name = "Ripon Mia"
#     age = 20
#     city = "Dhaka"

# student = Students()
# print(student.name,student.age,student.city)

# class class5:
#     a=4
#     b=9
# bahar = class5()
# bahar1=class5()

# print (bahar.a,bahar.b)
# print(bahar1.a)

# class Firstclass:
#     a=5
#     b=80
# stu1=Firstclass()
# stu2=Firstclass()

# print(stu1.a,stu1.b)
# print(stu2.a,stu2.b)



# class Cal:
#     def add(self,num1,num2):
#         return num1 + num1



# class cal:
#     def add(self, a, b):
#         return a+b
# cal1 = cal()
# print(cal1.add(4,6))


# class cal:
#     def add(self, a, b):
#         return a+b
#     def sub(self, a, b):
#         return a-b
#     def mul(self, a, b):
#         return a*b
#     def div(self, a, b):
#         return a/b

# cal1 = cal()
# print(cal1.add(5,6),cal1.sub(5,6),cal1.mul(5,6),cal1.div(5,6))

# class MyCal:
#     def add(self,a,b):
#         return a+b

#     def sub(self,a,b):
#         return a-b

#     def multiplication(self,a,b):
#         return a*b

#     def division(self,a,b):
#         return a/b


# x=int(input("Enter a value for x : "))
# y=int(input("Enter a value for y : "))

# Calc1=MyCal()

# print (Calc1.add(x,y))
# print (Calc1.sub(x,y))
# print (Calc1.multiplication(x,y))
# print (Calc1.division(x,y))


# class cal:
#     def add(self,num1,num2):
#         return num1+num2
#     def sub(self,num1,num2):
#         return num1-num2
#     def mult(self, num1,num2):
#         return num1*num2
#     def div(self,num1,num2):
#         return num1/num2            
# bahar = cal()
# print(bahar.add(5,5),bahar.sub(10,5),bahar.mult(3,4),bahar.div(10,2))class Cal:


# class cal:
#     def add(n,what,x,y):      
#         if what == '+':
#             return x+y
#         elif what == '-':
#             return x-y
#         elif what == 'x':
#             return x*y
#         elif what == '/':
#             return x/y
#         else:
#             return 'Wrong input'
# abc = cal()

# print (abc.add('+',10,2))


# item_name = input('item_name :')
# item_price = int(input('item_unit_price :'))
# item_quantity = int(input('item_quantity :'))

# # --------output---------
# print() # print For gape
# print('Takrim Grocery')
# print('You have purchased')
# print('Item Name :', item_name)
# print('Item Unit Price:', item_price)
# print('Item Quantity :', item_quantity)
# print('Net Total :', item_price * item_quantity)

# #-------Vat of price------
# def getVat(amount):
#     return amount*5/100
# sale = int(input('Sale Amoumt:'))
# vat_amount = getVat(sale)
# net = sale + vat_amount #---
# print('Sale:',sale)
# print(f'5% vat from the Government = {vat_amount}')
# print(f'Net Sale={net}')
# r=round(net)
# print(r)
# x = float(input('Paid:'))
# y = float(input('Net Sale:'))
# sub = float(x - y)
# print(f'balance={sub}')
# print('ধন্যবাদ,আবার আসবেন ')


# class MyCal:
#     def add(self,a,b):
#         return a+b

#     def sub(self,a,b):
#         return a-b

#     def multiplication(self,a,b):
#         return a*b

#     def division(self,a,b):
#         return a/b

# x=int(input("Enter a value for x : "))
# y=int(input("Enter a value for y : "))
# z=input("+,-,*,/or x for exit:")

# Calc1=MyCal()
# if z=='+':
#  print (Calc1.add(x,y))
# elif z=='-':
#  print (Calc1.sub(x,y))
# elif z=='*':
#  print (Calc1.multiplication(x,y))
# elif z=='/':
#  print (Calc1.division(x,y))
# elif z=='x':
#  exit()

# class cal:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mult(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b
# shohan = cal()
# print(shohan.add(8,5),shohan.sub(8,5),shohan.mult(8,5),shohan.div(8,5))

# class XTY:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b

#     def sub(self):
#         return self.a - self.b

# obj1 = XTY(10, 11)

# print(obj1.add())
# print(obj1.sub())

# class XTV:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def add(self):
#         return self.a+ self.b
#     def sub(self):
#         return self.a- self.b
#     def mul(self):
#         return self.a* self.b
#     def div(self):
#         if self.b !=0:
#          return self.a/ self.b

# cal12 =XTV(5,6)
# # print(type(cal12.a))

# print(cal12.add(),cal12.sub(),cal12.mul(),cal12.div())



class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def multiplication(self):
        return self.a*self.b

    def division(self):
        return self.a/self.b

 
x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

Calc1=MyClass(x,y)

print (Calc1.add())
print (Calc1.sub())
print (Calc1.multiplication())
print (Calc1.division())



















