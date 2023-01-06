# def plus_one(number):
#     return number + 1
# plus_one(5)
# print(plus_one(5))


# def plus_one(number):
#     return number + 1

# def function_call(f):
#     number_to_add = 5
#     return f(number_to_add)

# print(function_call(plus_one))

# def uppercase_decorator(f,k):
#     def change():
#         func = f()
#         func2 = k()
#         print('******')
#         make_uppercase = func.upper()
#         make_lower = func2.lower()      
#         return make_uppercase, make_lower
#         print('******')
#     return change

# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi,say_hi)
# print(decorate())


# @uppercase_decorator
# def say_hi():
#     return 'hello there'

# print(say_hi())


def d_fuc(fun):
    def wrapper():
        print('#######')
        fun()
        fun()
        fun()
        print('@@@')
    return wrapper

@d_fuc
def a_dec():
    print('Hello')

a_dec()
