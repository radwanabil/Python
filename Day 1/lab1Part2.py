#1- Given a list of numbers, create a function that returns a list where all similar adjacent

# def remove_duplicates(list_with_duplicates):
#     new_list = []
#     for i in list_with_duplicates:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# list_with_duplicates = input("Enter list of numbers separated by commas: ")
# list_with_duplicates = list_with_duplicates.split(",")

# new_list = remove_duplicates(list_with_duplicates)
# print("List without duplicates: ", new_list)

###############################################################
# 2-​​Consider dividing a string into two halves

# def front_back_combine(a, b):
#     a_len = len(a)
#     b_len = len(b)
#     a_front = a[:a_len // 2 + a_len % 2]
#     a_back = a[a_len // 2 + a_len % 2:]
#     b_front = b[:b_len // 2 + b_len % 2]
#     b_back = b[b_len // 2 + b_len % 2:]
#     return a_front + b_front + a_back + b_back
# a = "abcde"
# b = "12345"
# result = front_back_combine(a, b)
# print(result)

###############################################################
# 3- Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# def is_unique(list_with_duplicates):
#     new_list = list(set(list_with_duplicates))
#     if len(new_list) == len(list_with_duplicates):
#         return True
#     return False


# list_with_duplicates = input("Enter list of numbers separated by commas to see if unique: ")
# list_with_duplicates = list_with_duplicates.split(",")

# output = is_unique(list_with_duplicates)
# print("is list unique?: ", output)


###############################################################
# 4- Given unordered list, sort it using algorithm bubble sort
# def bubbleSort( theSeq ):
#     n = len( theSeq )

#     for i in range( n - 1 ) :
#         flag = 0

#         for j in range(n - 1) :
            
#             if theSeq[j] > theSeq[j + 1] : 
#                 tmp = theSeq[j]
#                 theSeq[j] = theSeq[j + 1]
#                 theSeq[j + 1] = tmp
#                 flag = 1

#         if flag == 0:
#             break

#     return theSeq

# el = input("Enter list of numbers to be sorted seperated by commas: ")
# elements = el.split(",")
# result = bubbleSort(elements)

# print (result)

###############################################################
# 5-Guesses game
import random
def guesses_game():
    answer = random.randint(1,100)
    tries = 10
    guessed_nums = set()

    while tries > 0:
        guess = input("guess a number between 0 and 100: ")
        if int(guess) > 100 or int(guess) < 0:
            print("Not allowed. Please enter a number between 1 and 100.")
            continue
        if int(guess) in guessed_nums:
            print("You've already guessed that number. Try a different one.")
            continue

        guessed_nums.add(int(guess))
                
        if int(guess) == answer:
            print("Congratulations! You guessed the number in", 10 - tries + 1, "tries.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                guesses_game()
            else:
                print("Thanks for playing!")
            return

        if int(guess) < answer:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

        tries -= 1


    print("You used up all your tries. The answer was", answer)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        guesses_game()
    else:
        print("Thanks for playing!")

guesses_game()

