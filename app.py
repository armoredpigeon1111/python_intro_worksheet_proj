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


run_random_number()