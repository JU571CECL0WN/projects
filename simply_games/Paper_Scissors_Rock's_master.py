import random

print('Hello!')

input('Choose :Paper,Scissors or Rock\n').lower()


win_possibility = random.random()  
if win_possibility < 0.85:
    input('Game Over, you lose , try to win me (⌐■_■)')
else:
    print('You win, you are the master of this game')