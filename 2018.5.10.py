#This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

for guessesTaken in range(1,7):
  print('Take a guess.')
  guess = int(input())
  if guess < secretNumber:
    print('Low.')
  elif guess > secretNumber:
    print('Hight.')
  else:
    break
if guess ==secretNumber:
  print('Good job!'+ str(guessesTaken)+ 'guesses!')
else
  print('Nope'+str(secretNumber))
