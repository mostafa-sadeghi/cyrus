# for i in range(5):
#     print("I want to learn pygame...")
#     print("OK")

# print("outside...")


# for i in range(10):
#     print(i, end=' ')

# for i in range(1,11):
#     print(i, end=' ')

# for i in range(1,11,2):
#     print(i, end=' ')
# print()

# for i in range(2,11,2):
#     print(i, end=' ')


# for i in range(10,0,-1):
#     print(i, end=' ')


# for i in [2,3,4,6,7,8,0,9,-1]:
#     print(i * 2, end=' ')

# for s in 'cyrus':
#     print(s, end=' ')

# for a in (1,2,3,6,8,9):
#     print(a**2, end=' ')

# for x in {1, 2, 3, 4, 8, 9, 0}:
#     print(x, end=' ')

# Nesting loops

# for i in range(3):
#     print("a")

# for j in range(3):
#     print("b")


# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

# total = 0
# for i in range(1001):
#     total += i # total = total + i
# print("total is:",total)


# total = 0

# for i in range(5):
#     number = int(input('enter a number:> '))
#     total = total + number  # total += number

# print("total is:", total)


# number_of_zeros = 0

# for i in range(5):
#     new_number = int(input('enter a number:> '))
#     if new_number == 0:
#         number_of_zeros += 1


# print("number of zeros :", number_of_zeros)




# user_name = input('enter a name: ')
# if user_name == 'cyrus':
#     exit()
#     print("something")

# print("blalalallalla")


# for i in range(10):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# quit = 'n'
# while quit == "n":
#     quit = input("Do you want to quit? ")

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit == "y":
#         done = True


import random

# for i in range(10):
#     my_random = random.randrange(50)
#     print(f'random number is: {my_random}')

ACTIONS = ["rock","paper","scissors"]
player_score = 0
computer_score = 0

while True:
    print("Game started")
    computer_hand = random.choice(ACTIONS)
    user_selection = ''
    while (not user_selection.isdecimal()) or (user_selection not in('1','2','3')):
        print("Enter '1' for rock, '2' for paper, '3' for scissors...")
        user_selection = input('> ')
    player_hand = ACTIONS[int(user_selection)-1]
    print("player's hand:",player_hand)
    print("computer's hand:",computer_hand)

    if player_hand == 'rock' and computer_hand == 'scissors':
        player_score += 1
        print("player wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")
    
    elif player_hand == 'paper' and computer_hand == 'rock':
        player_score += 1
        print("player wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")
    
    elif player_hand == 'scissors' and computer_hand == 'paper':
        player_score += 1
        print("player wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")



    elif player_hand == 'scissors' and computer_hand == 'rock':
        computer_score += 1
        print("computer wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")
    
    elif player_hand == 'rock' and computer_hand == 'paper':
        computer_score += 1
        print("computer wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")
    
    elif player_hand == 'paper' and computer_hand == 'scissors':
        computer_score += 1
        print("computer wins...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}")

    else:
        print("Equal...")
        print(f"{'player':<9}{'score:':>7}")
        print(f"{'me':<9}{player_score:>7}")
        print(f"{'computer':<9}{computer_score:>7}") 

    print("Do you want to continue?(Yes or No) ")
    if input('> ').lower().startswith('n'):
        print("Thank you for joining us...")
        break