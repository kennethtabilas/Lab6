'''
    File name: python_Lab1.py
    Author: Kenneth Tabilas 
    Date created: 08/26/2024
    Python Version: 3.6.9 
'''
message = "Go Gators !!"
print(message)

import random  # imports the library named random  # the random funtion help the python to pick the random number or items that is given.

def rps():  #the rps funtion allows python to group the codes together and run it to the task we want
    
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    user = input("Choose your weapon: "). lower() #the input will be what the user chooses and the lower will input a lowercase letter so it will treat Rock as rock. 
    comp = random.choice(['rock', 'paper', 'scissors']) # the random.choice will list of choice foe the computer to pick picks.  while the comp will store the information will be the computer   
    print()

    print('Player Chose', user) # this will display what thw user and the computer has pick 
    print('Computer Chose', comp)
    print()

    
    if user == comp:
        print("tie")
    elif user == 'rock' and comp == 'scissors':
        print('winner')
    elif user == 'scissors' and comp == 'paper':
        print('winner')
    elif user == 'paper' and comp == 'rock':
        print('winner')
    elif user == 'rock' and comp == 'paper':
        print('lost')
        print("Better luck next time...")
    elif user == 'scissors' and comp == 'rock':
        print('lost')
        print("Better luck next time...")
    elif user == 'paper' and comp == 'scissors':
        print('lost')
        print("Better luck next time...")
    else: 
        print("invalid choice")
    

rps()