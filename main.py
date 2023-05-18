#assignment 1
#name: hooriya kazmi
#student id: 501031422
#For assignment 1, I decided to make my "problem" a game of hangman (which is essentially a guessing game) that I solve through the program I created. 
#The code includes every instance of the 5 learning objectives to tackle and find the mystery word.
#The way the program works is that I created a function to randomly choose a word from a list, and then the player has to guess that word by inputting a letter or a word. The player can make a maximum of 7 mistakes before it is game over.

import random
#here, i import random worldwide so it is accessible outside all the functions

def hangman_intro(): #just an introduction to the game to explain the rules and welcome the player
  print("=============================\nHello, and welcome to Hangman!\n=============================\n\nThe rules of the game are simple, the program randomly picks a word for the player to guess. The player can enter either letters or words into the input. The player has 7 hearts, meaning, they can only make 7 mistakes.")
  
  name = input("\nPlease enter your name here to begin the game: ") #the player enters their name here to begin the game
  
  print("\nTHE GAME HAS BEGUN! Best of luck " + name + "!")
  


def random_word(): #this function picks a random word that the player will guess from a list of words
  words_list = ["computer", "coding" , "halloween", "monkey" , "banana" , "chainsaw", "spooky" , "apple" , "laptop" , "red" , "blue"] #the list of words
  global word #making sure the variable word is accessible globally and in other functions
  word = (random.choice(words_list)) #random.choice randomly picks a word from the list, and then i set that selected word equal to word to use later on
  

def play_game():
  
  random_word() #running the random word picker function here so that if the player chooses to replay the game, a new word will be generated when running play_game() again
  
  word_length = len(word) #just assigning the length of the word to guess to a variable
  alphabet = "abcdefghijklmnopqrstuvwxyz" #making a string of alphabets that i use later to make sure the player enters a valid letter
  guessed_letters = "" #empty string to put the letters that the player guesses later on in
  attempts = 7 #originally starting off with 7 lives
  letters_left = word_length #this variable initially equals the length of the word. once it hits 0, it means the player has guessed all the letters.
  
  print("\nThe word has " + str(word_length) + " letters")

  
  while attempts > 0 and letters_left > 0: #a loop that exits the while loop when the player reaches 0 lives or "dies". Also exists if the words left to guess is 0, meaning the player wins
    print("\n\nYou have " + str(attempts) + " heart(s) left")
    print("The letter(s) you have guessed so far: " + guessed_letters)
    guess = input("\nEnter your guess here: ").lower() #making sure that the inputed word or letter is lowercase to match the rest of the function

    
    if len(guess) == 1: #condition if user guesses a letter, length of one

      if str(guess) not in alphabet: #had to convert guess into string to compare them. if string is not in the alphabet defined earlier, it means it does not have letters in it, thus being an invalid input
        print("\nSorry! That is not a valid input. Try again.")
  
      elif guess in word: #if the letter the player guessed is in the word
        if guess not in guessed_letters: #making sure the player didn't guess an already guessed letter
          print("\nBingo! Your guess was right!")
          guessed_letters = guessed_letters + " " + guess #adding the letter that just got guessed to the string of guessed letters
          letters_left = letters_left - 1*(word.count(guess)) #this is the letters left to guess, and as we guess more of the letters, we subtract it from letters left to guess (once i guess e in red, i would subtract e out of red, leaving just rd). In case a letter appears more than once in a word, i multiply 1 by how many times that letter might appear in the word since in that case, there would be less letter to guess.
  
        else: #if correct letter is guessed again
          print("\nYou have already guessed that! Try again!") #if the letter is in guessed_letters, the player will be asked to guess again
          
      else: #if the letter is not in the word
        if guess not in guessed_letters: #if the letter hasn't been guessed already
          print("\nSorry! That letter is not in the word")
          attempts = attempts - 1 #the player loses a heart for guessing incorrectly
          guessed_letters = guessed_letters + " " + guess #adding the guess to the string of guessed words
          
        else: #if an incorrect letter is guessed again
          print("\nYou have already guessed that! Try again!")

          

    elif len(guess) == word_length: #condition if user guesses a word
      if guess == word: #if the guess is the word, the player won
        print("\nWow! You got the right word!")
        letters_left = 0 #making letters_left equal 0 by default so that it shows the winning message
        break #stops it from playing the rest of the loop

      else:
        print("\nSorry! That was not the right word.")
        attempts = attempts - 1 #player loses a heart for guessing the wrong word

    else:
      print("\nThat is not a valid input. Try again!") #if player enters an invalid input (too long or short)
    correct_letters = [letter if letter in guessed_letters else '_ ' for letter in word] #a list made out of the letters that were guessed, otherwise replace _ for any guessed letters that are no in word (letters yet to be guessed still)
    #this makes it visually easier for the player to see what letters they have and haven't guessed, and their positions
    print("".join(correct_letters))  #combines the list into a string
    
  if letters_left == 0: #no more letters left to guess, which mean player wins 
    print("\nCongrats! You beat hangman and get to live another day.")

  elif attempts == 0: #if player runs out of hearts, they lose
    print("\nYou have ran out of hearts.\nGame over :(. The word was " + word)
    
  play_again = input("Would you like to play Again? Y or N: ").upper() #input for player to select if they want to play again





  
  if play_again == "Y": #if player selects Y
    play_game() #this runs the play_game function again while skipping introduction
    
  elif play_again == "N": #if player selects N
    print("See ya later!") #goodbye message
    
  else:#if player does not select Y or N, shows invalid input
    print("Sorry! that was not a valid input. Try again")
  
      
  
hangman_intro() #running introduction
play_game() #running the game
