import wordset
import graphics
import random
import os

def choose_word(listofwords):
    return random.choice(listofwords).lower()


def display_UI(picture, word):
    os.system('cls')
    print(picture)
    print('\n')
    for i in word:
        print(i, end=' ')
    
    
def changing_pc_choice(pc_choice):
    word = ''
    for i in pc_choice:
        if i == ' ':
            word += ' '
        else:
            word += '_'
    return word
    
    
def get_letter(word, letters, used_letters, pc_choice):
    tmp = ''
    while True:
        found = False
        player_letter = input('\nWhat letter do you want to try?\n').lower()
        if player_letter in letters:
            if player_letter not in used_letters:    
                for i in range(len(pc_choice)):
                    if pc_choice[i] == player_letter:
                        tmp += player_letter
                        found = True
                    else:
                        tmp += word[i]
                used_letters += [player_letter]
                return tmp, found
            else:
                print('You already used this letter')

        else:
            print('Is not possible this thing')
def game():
    used_letters = []
    live = 0
    pc_choice = choose_word(wordset.WORDSET)
    wordinprogress = changing_pc_choice(pc_choice)
    while True:
        display_UI(graphics.HANGMANPICS[live], wordinprogress)
        print()
        wordinprogress, found = get_letter(wordinprogress, wordset.LETTERS, used_letters, pc_choice)
        if wordinprogress == pc_choice:
            lorw = True
            break
        elif not found:
            live += 1
            if live == len(graphics.HANGMANPICS):
                lorw = False
                break
    if lorw:
        display_UI(graphics.HANGMANPICS[live], wordinprogress)
        print()
        input(' - You Win - \n')
    else:
        input(' - You Lose - \n - The Word is {0} - \n'.format(pc_choice))
        
        
game()