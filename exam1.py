"""
1. write a program thst takes student`s name, family and three course scores
and you must calculate student`s average
and print message like this
"""
# name = input("Enter your name: ")
# family = input("Enter your family: ")

# score_1 = float(input("Enter first score: "))
# score_2 = float(input("Enter second score: "))
# score_3 = float(input("Enter third score: "))

# average = (score_1 + score_2 + score_3)/3
# print(f"{name} {family}'s average is {average}")


"""
2. write a program that takes a name and prints its character reversely
with for loop

and the n with while loop 
"""
# name = input("enter a name: ")
# for i in range(len(name) - 1, -1, -1):
#     print(name[i], end=" ")
# name = input("enter a name: ")

# i = len(name) - 1

# while i >= 0:
#     print(name[i], end=" ")
#     i -= 1

"""
3. write a program that takes 5 student`s name and store them in a list called students_names
and you should print first and last item in the list
then append a new name in the list 
and last you must take a new student`s name and remove it from the list (if exists)

"""
students_names = []

for i in range(5):
    new_name = input("Enter a name: ")
    students_names.append(new_name)

name_to_delete = input("enter a name: ")
for name in students_names:
    if name == name_to_delete:
        students_names.remove(name)

print(students_names)