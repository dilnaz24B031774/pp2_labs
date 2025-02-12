import random

def guess_the_number():
  """Plays the "Guess the number" game."""
  number = random.randint(1, 20)
  name = input("Hello! What is your name? ")

  print(f"Well, {name}, I am thinking of a number between 1 and 20.")
  guesses = 0
  while True:
    
    try:
      guess = int(input("Take a guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    guesses += 1

    if guess == number:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break
    elif guess < number:
        print("Your guess is too low. Take a guess.")
    else:
        print("Your guess is too high. Take a guess.")

guess_the_number() 
def myfunc(a,b = 5):
   return a+b
myfunc(5)

  

    
    