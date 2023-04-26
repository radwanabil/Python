#1-​ Write a Python program which accepts the user's first and last name and print them inreverse order with a space between them.

# first_name = input('Enter your first name:')
# last_name = input('Enter your last name:')
# print(last_name +' '+first_name)

###########################################################
#2- Write a Python program that accepts an integer (n) and computes the value ofn+nn+nnn.

# n = int(input("Enter an integer: "))
# nn = int(str(n) + str(n))
# nnn = int(str(n) + str(n) + str(n))
# result = n + nn + nnn
# print(result)

###########################################################
#3- Write a Python program to print the following here document.

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")


###########################################################
#4- Write a Python program to get the volume of a sphere with radius 6.

# volume = 4/3 * 3.14 * 6.0**3
# print("the volume of the sphere is: ",volume)

###########################################################
#5- Write a Python program that will accept the base and height of a triangle and compute the area.

# base = float(input('Enter the base of triangle:'))
# height = float(input('Enter the height of triangle:'))
# area = 1/2 * base * height
# print("The area of the triangle is: ",area)

###########################################################
#6- Write a Python program to construct the following pattern, using a nested for loop.

# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(rows):
#     for j in range(rows-i):
#         print("*", end=" ")
#     print()

###########################################################
#7- Write a Python program that accepts a word from the user and reverse it.

# word = input('Enter the word you want to reverse:')
# reversed_word = ''.join(reversed(word))
# print(reversed_word)

###########################################################
#8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6

# for i in range(6):
#     if(i not in [3,6]):
#         print(i)

###########################################################
# 9-Write a Python program to get the Fibonacci series between 0 to 50

# a, b = 0, 1
# while b < 50:
#     print(b, end=" ")
#     a, b = b, a+b

###########################################################
# 10-Write a Python program that accepts a string and print how many digits an dnumbers

string = input("Enter a string to count the number of digits and numbers:")
digits = 0
letters = 0
for i in string:
    if i.isdigit():
        digits+=1
    if i.isalpha():
        letters+=1

print("Number of digits is: " , digits)
print("Number of letters is: " , letters)