#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import random
import pandas as pd
from pandas import Series, DataFrame

q1 = "Would you like to continue? "

def rename_file(file_name):
    if not ".csv" in file_name: 
        file_rename = file_name + ".csv" 
    return file_rename

def check_file(file_name):
    try:
        if os.path.isfile(file_rename) == True:
            print(f"\nVocabulary word list uploaded: {file_name}")
        else:
            print("\nI'm sorry. The file name you provided is not in the same directory.\n")
    except:
        print("\nError. Please try again.\n")
        
def yes_or_no(question):
        while True:
            user_input = input(question + " Y or N? ").lower().strip()
            if user_input == 'y':
                print("User Input = y")
                return True
            elif user_input == 'n':
                print("User Input = n")
                return False
                break
            else:
                print("I'm sorry. That is an invalid input. Y or N?")
                continue
                
def choose_card_range():
    q2= '''
        Would you like to choose the list of words to study?
        Press Y to indicate the range of cards you want to study.
        Press N to study all of the cards.'''
    while True:
        user_input = yes_or_no(q2)
        if user_input == True:
            start_index = input("Please type in the starting index number: ")
            stop_index = input("Please type in the ending index number: ")
            print(f"Your starting value is: {start_index}")
            print(f"Your ending value is: {stop_index}")
            if (start_index.isdigit() and stop_index.isdigit() and int(start_index) < int(stop_index)):
                print("Your word set has been selected.")
                range_input = [start_index, stop_index]
                return card_range.extend(range_input)
                break
        elif user_input == False:
            return card_range.extend([0, len(vocab_list)])
            break
        else:
            print("""I'm sorry. That is an invalid input. Please provide two integer values
                  where the second integer is larger than the first integer.""")
            continue
            
def choose_shuffle():
    q3 = "Would you like to randomize the cards?"
    while True:
        user_input = yes_or_no(q3)
        if user_input == True:
            return game.shuffle()
        elif user_input == False:
            break
        else:
            print("I'm sorry. That is an invalid input. Y or N?")
            continue
            
def quit_game():
    print("Keep studying the following saved words:\n")
    unknown_display = ""
    for i,j in game.saved:
        unknown_display = f"\n{i.strip()}: {j}"
        print(unknown_display)
    print("\nGoodbye!")


# In[ ]:


class VocabCardSet():

    def __init__(self):
        self.index = 0
        self.vocab_cardset = vocab_active
        self.saved = []
        
    def __str__(self):
        image_deck = " "
        for i in self.vocab_cardset:
            image_deck += f"\n{i[0].strip()}: {i[1]}\n"
        return image_deck
    
    def __iter__(self):
        return self
    
    def __len__(self):
        return len(self.vocab_cardset)
            
    def __next__(self): # Special method to cycle through the list when reaching the end of the index.
        flashcard = " "
        try:
            if self.index == len(self.vocab_cardset) - 1:
                self.index = 0
                result = self.vocab_cardset[self.index]
                return f"\n{result[0].strip()}: {result[1]}\n"
            
            elif 0 <= self.index < len(self.vocab_cardset):
                self.index += 1
                result = self.vocab_cardset[self.index]
                return f"\n{result[0].strip()}: {result[1]}\n"
        except:
            print("There are no more vocabulary words!")
            print("Please restart the app study your vocabulary words again.")
            print("error in next")
            return quit_game()
    
    def previous(self): # A function that returns the previous word in the list. 
        try:
            if self.index == 0: 
                self.index = len(self.vocab_cardset) - 1
                result = self.vocab_cardset[self.index]
                return f"\n{result[0].strip()}: {result[1]}\n"
            
            elif self.index > 0:
                self.index -= 1
                result = self.vocab_cardset[self.index]
                return f"\n{result[0].strip()}: {result[1]}\n"
        except:
            print("There are no more vocabulary words!")
            print("Please restart the app to study your vocabulary words again.")
            print("Error in previous")
            return quit_game()
    
    def shuffle(self):
        random.shuffle(self.vocab_cardset)
            
    def save_unknown(self): # A function that saves an unknown vocab word to another list.
        try:
            if self.index == len(self.vocab_cardset):
                self.index = 0
                unknown = self.vocab_cardset.pop(self.index)
                self.saved.append(unknown)
                print(f"""\nThe following word was saved:\n
                      {unknown[0].strip()}: {unknown[1].strip()}\n""")
            elif self.index < len(self.vocab_cardset):
                unknown = self.vocab_cardset.pop(self.index)
                self.saved.append(unknown)
                print(f"""\nThe following word was saved:\n
                      {unknown[0].strip()}: {unknown[1].strip()}\n""")
        except:
            print("There are no more vocabulary words!")
            print("Please restart the app to study your vocabulary words again.")
            print("Error in save unknown")
            return quit_game()
            
    def print_unknown(self): 
        saved_deck = ""
        for i in self.saved:
            saved_deck += f"{i[0]}: {i[1]}"
            return saved_deck


# In[ ]:


# Game play: Ask user to input vocab list file name and to continue
print("""Welcome to the Vocabulary Flash Card Study App!\n
    This app was intended to be used for studying vocabulary words.
    It does not keep score of correct or wrong answers.
    Instead, it allows users to cycle through the vocabulary flash card set 
    quickly for studying and personally assessing one's
    own performance.\n\n""")

print("""How the Vocabulary Flash Card App Works:
    The user will be prompted to input the file name of the .csv file
    he or she would like to study. Please have a .csv file saved in the
    same directory as this program. The user will get to choose certain
    user settings before starting the app, like choosing a subset of words
    from the entire vocabulary list or randomizing the words in the list. 
    The user will also be given a menu to allow the user to navigate through 
    the vocabulary list. The menu will allow the user to skip the word (S) 
    or to go back to the previous word (P). The user can also save 
    words in an unknown word pile for the user to review at the end (U).
    The user can also quit the App (Q) at any point during the game.""")

file_name = str(input("What is the name of the vocabulary list file you wish to study?"))
file_rename = rename_file(file_name)
check_file(file_rename)
data = pd.read_csv(file_rename, encoding = 'latin-1')
col_headers = list(data)
words_list = data[col_headers[0]].values.tolist()
definitions_list = data[col_headers[1]].values.tolist()
vocab_dict = dict(zip(words_list, definitions_list))
vocab_list = list(vocab_dict.items())

# Game play: Ask user to choose to study a specified set of cards or all cards in vocab list
card_range = []
choose_card_range()
vocab_active = vocab_list[int(card_range[0]): int(card_range[1])]
vocab_active_dc = dict(vocab_active)

game = VocabCardSet() 

# Game play: asks user if he or she wants to randomize cards
choose_shuffle()

# Game play: Start studying!
while True:
    if len(game.vocab_cardset) > 0:
        selection = input("""\nWhat would you like to do?
                      Skip to the next word? Press S.
                      Go back to previous word? Press P.
                      Mark word as unknown? Press U.
                      To quit flash card generator. Press Q.\n""").lower() 
        if selection == 's':
                #print("Skip")
            print(next(game))
        elif selection == 'p':
                #print("Previous")
            print(game.previous())
        elif selection == 'u': 
            print("Unknown")
            game.save_unknown()
        elif selection == 'q': 
            quit_game()
            break
        else: 
            print("I'm sorry. That's an invalid input.")
            continue  
    else:
        print("There are no more vocabulary words!")
        print("Please restart the app to study your vocabulary words again.")
        print("error at end of game")
        quit_game()
        break

