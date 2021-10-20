import random
import random_number
import randint

def guess_number():
      random_number = random.randint(1,9)
      player_name = input("Enter Your Name:")
      confirm_play = input("Would you like to start the Game? (Enter yes/no):")
      attempts = 0

      while confirm_play.lower() == "yes":

            guess = int(input("Guess the number between 1 and 9:"))


            if guess < 0 or guess > 20:
                  print("Please guess number in ranges")

            elif guess ==  random_number:
                  print("Congratulations",player_name,"YOU WON THE GAME")
                  attempts += 1
                  print("It took you",attempts,"attempts to win the game")
                  break

            elif guess > random_number:
                  print("HINT:Try smaller number")
                  attempts += 1

            elif guess < random_number:
                  print("HINT:Try larger number")
                  attempts += 1

            else:
                  print("Thank You",player_name,"for being with us.")