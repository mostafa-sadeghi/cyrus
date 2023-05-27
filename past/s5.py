# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# pygame   # unity
# print("our first slice of the list:", numbers[0:3])
# print("our second slice of the list:", numbers[4:7])
# web development       data science        hack and pentest       game      desktop applications

# [7,8,9]
# print(numbers[6:])
# [2,3,4,5]
# print(numbers[1:5])
# [3,4]
# print(numbers[2:4])
# [6,7,8,9]
# print(numbers[5:])


# tuple

# names = []
# names.append("cyrus")
# names.append("artin")
# names.append("reza")
# print(names)

# numbers = []
# numbers.append(1)
# numbers.append(2)
# numbers.append(5)
# print(numbers)

# number1 = int(input('enter a number: '))
# number2 = int(input('enter a number: '))
# number3 = int(input('enter a number: '))
# numbers.append(number1)
# numbers.append(number2)
# numbers.append(number3)
# print(numbers)


'''
write a program that takes 4 numbers from input and
put all 4 numbers in a list called `numbers` 
we want to sum all numbers from this list and print the result.

'''
# numbers = []
# number1 = float(input('enter a number: '))
# number2 = float(input('enter a number: '))
# number3 = float(input('enter a number: '))
# number4 = float(input('enter a number: '))
# numbers.append(number1)
# numbers.append(number2)
# numbers.append(number3)
# numbers.append(number4)
# print("all my numbers:", numbers)


names = []

name1 = input('enter a name: ')
name2 = input('enter a name: ')
name3 = input('enter a name: ')
name4 = input('enter a name: ')
name5 = input('enter a name: ')
names.append(name1)
names.append(name2)
names.append(name3)
names.append(name4)
names.append(name5)
print("all names :", names)

print("we want to manupolate the list...")
a_name_to_delete = input('enter a name to remove from our list: ')
names.remove(a_name_to_delete)

print("all names :", names)





# numbers = (1, 2, 3, 4, 5, 6)

# numbers.append()  # error
