# s1 = 40 + 15
# print(s1)

# s2 = 60+18
# print(s2)

# def student(a,b):
#     # return print('result : ', a+b)
#     result = a + b
#     #  print(result)
#     return result


# s1 = student(55,17)
# print('s1 : ', s1)

# s2 = student(75,17)
# print('s2 : ', s2)

# s3 = student(73,17)
# print('s3 : ', s3)


# def teacher(name):
#     return name

# t1 = teacher('Belal')

# print('teacher name : ',t1)

# def person(name,s_id,dep):
#     return name, s_id, dep

# def student(std_name,std_id,std_dept='Computer'):
#     return std_name,std_id,std_dept

# print(student('Hasan','4353'))
# print(student('Hasan1','43533'))
# print(student('Hasan2','43534'))


# print(student('Ashraf',123,'EEE'))
# print(student('Omar Faruk ',435.3,'CIA'))
# print(student('Hasan Ali','4353','BBA'))
# print(student('Ranga','8788','CSE'))

# n =int(input('Enter Your number : '))

# sum = 0
# for i in range(1,n):
#     sum += i

# print('Result : ', sum)


# def shop_total_sale(*args):
#     print(type(args))
#     sum = 0
#     for amount in args:
#         sum = sum + amount
#     return sum

# total_amount = shop_total_sale(54,67,23,46,78,90,11,34,56,34)

# print('Total Sale Amount : ', total_amount)



# def add(**kwargs):
#     print(type(kwargs))
#     sum = 0
#     for key in kwargs:
#         sum = sum + kwargs[key]
#     return sum
# total = add(a=54,b=67,c=23,d=46)
# print(total)


# @add
# def add2():
#     pass


# def add(**kwargs):
#     sum=0
#     for key in kwargs:
#         sum=sum+kwargs[key]
#     return sum

# total=add(a=45,b=48)
# print(total)


x=input("Enter a value for x : ")
y=input("Enter a value for y : ")

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(int(x)+int(y))
  elif(z=='-'):
    print(int(x)-int(y))
  elif(z=='*'):
    print(int(x)*int(y))
  elif(z=='/'):
    print(int(x)/int(y))
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")




