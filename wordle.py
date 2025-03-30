# -*- coding: utf-8 -*-
"""
Student: Matan Ashkenazi
ID:209756188
Assignment no. 3
Program: hide_text.py
"""
#matan 17/2/2024
import random

def get_words():
    word_database_file = open("words.txt", "r")
    word_database = word_database_file.read().split()
    word_database_file.close()
    return word_database

def compare_words(cpu,user, unused_letters):
    result = ''
    for i in range(len(cpu)):
        if user[i] in unused_letters:
            unused_letters = unused_letters.replace(user[i], '')
        if user[i] == cpu[i]:
            result += 'O'
            if user[i] in unused_letters:
                unused_letters = unused_letters.replace(user[i], '')
        elif user[i] in cpu:
            result += 'X'
            if user[i] in unused_letters:
                unused_letters = unused_letters.replace(user[i], '')
        else:
            result += '_'
            
    return result, unused_letters
                
def play_wordle(cpu,database):
    print("Welcome to Wordle. Guess a word:")
    tries = 0
    unused_letters = "abcdefghijklmnopqrstuvwxyz" 
    while tries < 6:
        user_guess = input("")
        if user_guess not in database:
            print("Word not in the list")
            continue
        tries += 1
        result, unused_letters = compare_words(cpu, user_guess, unused_letters)
        if result == 'OOOOO':
            print(result, "\nYou won!!!")
            break
        if tries == 6 and result != "OOOOO":
            print(f"You lost!! The word was '{cpu}'")
            break
        print(result)
        print(f"Unused letters: {unused_letters}")
         
def main():
    
    word_database = get_words()
    cpu_choice = random.choice(word_database)
    play_wordle(cpu_choice , word_database)
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    