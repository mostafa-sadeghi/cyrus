# print('Hello')
# print("1+2")

# score = 0
# print("score value is:", score)

# score += 1
# print("score value is:", score)

# score = score + 1
# print("score value is:", score)

# score = score - 1
# print("score value is:", score)

# score -= 1
# print("score value is:", score)


# print("hello\nwelcome")
# print("c:\\new folder")
# print("c:\new folder")
# print('hello\twelcome')

# print('hi\rhello')
# print('hello\rhi')

# print('hello every body.\rwelcome to our python class.\rwelcome to our pygame')
# name = input('enter a name:> ')
# if name == "cyrus":
#     print("welcome cyrus")

# x = 1

# x + 1
# x = x + 1

# print(x)

# X = 4
# X = 5
# print(X)
# Y = 3
# print(X/Y)
# print(X//Y)

# a = 4

# b = 5

# if a > b:
#     print("1")

# if a < b:
#     print("2")

# a = 4

# b = 4
# if a >= b:
#     print("1")

# if a <= b:
#     print("2")


# a = 4
# b = 4

# if a > b or a == b:
#     print('a and b are equal')

# write a program that takes student's age and
# print kid if age < 8
# print junior if 8 <= age < 12
# print teenager if 12 <= age < 18
# print adult if age >= 18
# name = input('enter your name:> ')

# age = int(input('enter your age:> '))

# if age <= 8:
#     print(f"{name} you are kid")
# elif 8 < age <= 12:
#     print()


# a = 5
# b = 5

# if a == b:
#     print("a and b are equal")

# if a != b:
#     print("a and b are not equal")


# a = int(input('enter first number'))
# b = int(input('enter first number'))
# c = int(input('enter first number'))


# a = True
# if a:
#     print("ok")

# if not a:
#     print("not ok")


# a = True
# b = False

# if a and b:
#     print("ok")


# a = True
# b = False

# if a or b:
#     print("ok")
# a = 3
# b = 4
# c = a == b
# print(c)
# if 1:  # Truethy
#     print("one")
# every numbers excep zero are truethy which mean they evaluate to True
# if 0:
#     print("zero")
# if -1:
#     print("-1")
# if '':
#     print("balalalal")
# if ' ':
#     print("balalalal")
# user_name = input('enter user name:> ')
# password = input('enter password:> ')

# if user_name and password:
#     print("ok")
#     print("username and password is not empty.")

# else:
#     print("you must enter user name and password")

#
# a = "c"

# if a == "B" or "b":
#     print("a is equal to b. Maybe.")

# if a =="B" or a =="b":
#     print("a is equal to b.")


USERNAME = "admin"
PASSWORD = 'root'


user_name = input('enter the user name:> ')
password = input('enter the password:> ')

if not user_name or not password:
    print('user name or password is empty.')
else:
    if user_name == USERNAME and password == PASSWORD:
        print("welcome.")
        print("login success")
        print("you are a valid user.")
    else:
        print("username or password is not correct.")
