#Python Intro Worksheet


#1 - User Favorite Programming Language

def fav_programming_languages():
    programming_languages = ["Java", "JavaScript", "C#", "Python"]
    userFav = input("Enter your favorite programming language: ")
    matching_language = check_for_matching(programming_languages, userFav)
    print(matching_language)


#checks to see if user input matches a value in the list
def check_for_matching(programming_languages, userFav):
     for language in programming_languages:
        if userFav == language:
            return language    

#fav_programming_languages()




#2 - Random number between min and max number

import random

def run_random_number():
    user_min = int(input("Enter a number for the minimum: "))
    user_max = int(input("Enter a number for the maximum: "))
    random_num = random_number(user_min, user_max)
    print(random_num)

#gets random number in range
def random_number(min, max):
    num = random.randint(min, max)
    return num


#run_random_number()


#3 Write the reversal of a word

def run_reverse_word():
    user_word = input("Enter a word to reverse it: ")
    reversed_word = reverse_word(user_word)
    print(reversed_word)

def reverse_word(word):
    reversed_word = word[::-1]
    return reversed_word

#run_reverse_word()



#4 Print every number frow 100 to 1 if divisible by 4 print banana, 7 print flamingo, 4 and 7 Flamingo-Banana

def run_flamingo_banana():
    start_num = 100
    flamingo_banana(start_num)

def flamingo_banana(num):
    while num > 0:
        if num % 4 == 0 and num % 7 == 0:
            print("Flamingo-Banana")
            num -= 1
        elif num % 4 == 0:
            print("Banana")
            num -= 1
        elif num % 7 == 0:
            print("Flamingo")
            num -= 1
        else:
            print(num)
            num -= 1

#run_flamingo_banana()




#5 Take a list of numbers and make a new list of numbers less than 5

def run_less_than_five():
    starting_nums = [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]
    nums_less_than_five = less_than_five(starting_nums)
    print(nums_less_than_five)

def less_than_five(nums):
    list_nums = []
    for num in nums:
        if num < 5 and not num in list_nums:
            list_nums.append(num)
    
    return list_nums

#run_less_than_five()




#6 Get user name and age and print year they turn 100
import datetime

def run_calculate_hundred():
    user_name = input("What is your name?")
    user_age = int(input("What is your age?"))
    year = calculate_hundred(user_age)
    print(user_name + ", you turn 100 in the year " + str(year))


def calculate_hundred(age):
    current_year = datetime.datetime.now().year
    hundred_year = 100 - age + current_year
    
    return hundred_year

run_calculate_hundred()