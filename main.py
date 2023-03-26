import random

# There are two possible outcomes
options = ["heads", "tails"]

# These variables are responsible for the guess history
correct_count = 0
total_count = 0

#This variable is responsible for the continuation of the game
continue_game = "yes"

# Game begins here:
while continue_game == "yes":
  guess = ""
  
  # Asking to guess the outcome
  while guess not in options:
    guess = input("Guess the outcome of a random coin flip: type 'heads' or 'tails' (without quotes):\n")
    if guess in options:
      break
    else:
      print("Your input is incorrect.")
  
  # Flipping the coin
  outcome = random.choice(options)
  print("I flipped a coin and this is what came out:\n" + outcome)
  if guess == outcome:
    print("Your guess was correct.")
    correct_count += 1
  else:
    print("You guessed it wrong. Try again.")
  total_count +=1
  
  # Printing the guess history
  print("\nTotal coin flips:", total_count)
  print("How many times you guessed:", correct_count)

  #This code may need to be improved to include cases where a person enters something other than yes or no.
  continue_game = input("\nDo you want to flip the coin again? Type 'yes' or 'no' (without quotes): ")
  if continue_game == "no":
    break
