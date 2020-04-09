#The_Nerves_of_steel_game by Adrian Bobrowski
#mysecondproject

import time
import random

print('Welcome to The Nerves Of Steel game!')
time.sleep(3)
print('Rules are: I will think random time between 5 and 20 seconds and start to count down')
time.sleep(5)
print('Meanwhile all the players can sit down, last player to sit before time is up wins!')
time.sleep(5)
print('Players still standing when the time ends are eliminated')
time.sleep(5)
print('Okay, get ready we are starting in 10 seconds')

i=10
while i >= 0:
    print(i)
    i -= 1
    time.sleep(1)

print('Players stand!')

time.sleep(random.randint(5,20))

print('Time is up! Last to sit down wins!')


