# print('hello')
# print("1+2*3")
# print(1+2*3)
# print((1+2)*3)
# score = 0
# print('my score is:', score)

# score = score + 1
# print('my score is:', score)

# score +=1
# print('my score is:', score)

# score = score -1
# print('my score is:', score)

# score -=1
# print('my score is:', score)


# print("hi every body.\nwelcome to our python class.")
# print("""hi every body.
# welcome to our python class.""")

# print("hi every body.
#       welcome to our python class.")
# print("He said, \"Aren't can't shouldn't wouldn't.\"")
# print('He said, "Aren\'t can\'t shouldn\'t wouldn\'t."')
# print('''He said, "Aren't can't shouldn't wouldn't."''')

# print('id\tname')
# print('01\tcyrus')

# print('hi.\rhello')
# print('hello\rhi')
# print('hi.\rwelcome to our python class.\rwelcome to our pygame')


# name = input('enter your name:> ')
# family = input('enter your family:> ')

# message = "hello" + " " + name + " " + family
# print(message)
# message = "hello %s %s" % (name, family)
# print(message)

# message = f"hello {name} {family}"
# print(message)
# if name == 'no':
#     print('sorry!!')

# elif name == 'yes':
#     print("Ok, let's go")


# we can use float for floating point numbers instead
# first_number = int(input('enter number 1: '))
# print(type(first_number))

# second_number = int(input('enter number 2: '))
# print(type(second_number))

# output = first_number + second_number

# print(f'{first_number} + {second_number} = {output}')


# n1 = float(input('enter a number :'))
# n2 = float(input('enter a number :'))

# print(f'{n1+n2}')

# exercise 1: write a program that gets student's name and three scores and then calculate student's average
# print message like this which shows student's name and average as :
# cyrus's average is : 90
# NOTE : average is sum of three score / 3

name = input("enter student's name:> ")
score1 = float(input('enter first score:> '))
score2 = float(input('enter second score:> '))
score3 = float(input('enter third score:> '))

average = (score1 + score2 + score3) / 3

print(f"{name}'s average is : {average:.2f}")
