# print(type(3))
# print(type(3.0))
# print(type('3'))
# print(type(True))
# print(type([1,2,3,4,56]))

# numbers = [1,2]
# print(numbers[0])
# numbers[0] = 100
# print(numbers)

# x = (1, 2)
# print(type(x))
# x[0] = 100  # error

# my_list = [101, 20, 10, 50, 60]

# for num in my_list:
#     print(num)
# for num in my_list:
#     print(num, end=" ")
# print(len(my_list))
# for index in range(len(my_list)):
#     if index != len(my_list) - 1:
#         print(my_list[index], end="-")
#     else:
#         print(my_list[index])


# my_list = ["Spoon", "fork", "knife"]

# for item in my_list:
#     print(item)

# my_list = [[2, 3], [4, 3], [6, 7]]
# for item in my_list:
#     print(item)

# my_list = [2,4,5,6]
# print(my_list)
# my_list.append(100)
# print(my_list)


# my_list = []
# for i in range(5):
#     userInput = input('Enter an integer: ')
#     userInput = int(userInput)
#     my_list.append(userInput)
#     print(my_list)
# print(f'sum of all numbers: {sum(my_list)}')


# x = '0123456789'
# print(x[0])
# print(x[1])
# print(x[-1])
# print(x[:6])
# print(x[6:])
# print(x[6:9])

# a = "Hi"
# b = "There"
# c = "!"
# print(a + b)
# print(a + b + c)
# print(3 * a)
# print((a + b)* 3)
# print((a*2)+ (b*2))
# a = "Hi There"
# print(len(a))

# b = [2,3,4,5,6,7,8,8]
# print(len(b))

# for character in "this is a test":
#     print(character.upper(), end='')
# print()
# print("this is a test".upper())

MONTHS = "JanFebMarAprMayJunJulAugSepOctNovDec"
all_months = []
for i in range(len(MONTHS)//3):
    all_months.append(MONTHS[3 * i: 3*i+3])
print(all_months)
number_of_month = int(input('Enter month`s number: '))
print(all_months[number_of_month-1])