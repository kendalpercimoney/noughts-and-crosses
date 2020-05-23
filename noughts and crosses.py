import time
import random
from random import randint
import sys #for exit

#variables
print_sleep = (.00) #change to 0.3 for 'vibe'
end = False
playerWin = False
computerWin = False
repeats = 1
computer_piece = "O"
endCounter = 0

#play variables
one = ("1")
two = ("2")
three = ("3")
four = ("4")
five = ("5")
six = ("6")
seven = ("7")
eight = ("8")
nine = ("9")
valueset = False

def reset_board():
  global one 
  global two
  global three
  global four
  global five
  global six
  global seven
  global eight
  global nine
  global playerWin
  global computerWin
  one = ("1")
  two = ("2")
  three = ("3")
  four = ("4")
  five = ("5")
  six = ("6")
  seven = ("7")
  eight = ("8")
  nine = ("9")
  playerWin = False
  computerWin = False

def intro_scrn(): #print intro screen
    print ()
    print ("  n o u g h t s  &  c r o s s e s  ")
    print ()



def change_num(a): #assign the piece to its respective place
    global one 
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global valueset
    
    if (a == str(1)):
      
      one = x_o
    elif (a == str(2)):
      two = x_o
      valueset = True
    elif (a == str(3)):
      three = x_o
      valueset = True
    elif (a == str(4)):
      four = x_o
      valueset = True
    elif (a == str(5)):
      five = x_o
      valueset = True
    elif (a == str(6)):
      six = x_o
      valueset = True
    elif (a == str(7)):
      seven = x_o
      valueset = True
    elif (a == str(8)):
      eight = x_o
      valueset = True
    elif (a == str(9)):
      nine = x_o
      valueset = True
    elif (valueset == False): #run this code again if the wrong value has been input
      print("You must have pressed the wrong button! Try again.")
      b = input()
      change_num(b)

def comp_play(a): #assign the piece to its respective place
    global one 
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global valueset
    global x_o
    global computer_piece
    global endCounter
    global repeats
    global end
    
    if (endCounter == 50): #given that there is a lot of recursion, print this and call it a tie (computer can't find a place to place piece)
      print_scrn()
      print("You have a tie! Would you like to play again?")
    
      while repeats == 1:
        answer = input()
        if (answer == "Y" or answer == "y"):
          print ('Okay!')
          main_game()
        if(answer == "N" or answer == "n"):
          end = True
          return
        else:
          print("Sorry! I don't understand that answer. Try again.")
    endCounter += 1

    if (a == str(1)):
      if (one != x_o and one != computer_piece):
        one = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(2)):
      if (two != x_o and two != computer_piece):
        two = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(3)):
      if (three != x_o and three != computer_piece):
        three = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(4)):
      if (four != x_o and four != computer_piece):
        four = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(5)):
      if (five != x_o and five != computer_piece):
        five = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(6)):
      if (six != x_o and six != computer_piece):
        six = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(7)):
      if (seven != x_o and seven != computer_piece):
        seven = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(8)):
      if (eight != x_o and eight != computer_piece):
        eight = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
    elif (a == str(9)):
      if (nine != x_o and nine != computer_piece):
        nine = (computer_piece)
      else:
        comp_play(str(randint (1, 9)))
        
    
   

def user_place_check(a): #assign the piece to its respective place
    global one 
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global valueset
    global x_o
    global computer_piece
    global inputNum
    
    if (a == str(1)):
      if (one == x_o or one == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(2)):
      if (two == x_o or two == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(3)):
      if (three == x_o or three == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(4)):
      if (four == x_o or four == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(5)):
      if (five == x_o or five == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(6)):
      if (six == x_o or six == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(7)):
      if (seven == x_o or seven == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(8)):
      if (eight == x_o or eight == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)
    if (a == str(9)):
      if (nine == x_o or nine == computer_piece):
        print("You can't place your piece there! Please try again.")
        inputNum = input()
        user_place_check(inputNum)

def print_scrn():
    #print game screen

    time.sleep (.5)
    print (" ----------------------------- ")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    "+one+"    |    "+two+"    |    "+three+"    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|-----------------------------|")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    "+four+"    |    "+five+"    |    "+six+"    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|-----------------------------|")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    "+seven+"    |    "+eight+"    |    "+nine+"    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print (" ----------------------------- ")



def chk_win():
  global playerWin
  global computerWin
  if ((one == x_o and five == x_o and nine == x_o) or (three == x_o and five == x_o and seven == x_o)):
    playerWin = True
  if ((one == x_o and four == x_o and seven == x_o) or (two == x_o and five == x_o and eight == x_o) or (three == x_o and six == x_o and nine == x_o)):
    playerWin = True
  if ((one == x_o and two == x_o and three == x_o) or (four == x_o and five == x_o and six == x_o) or (seven == x_o and eight == x_o and nine == x_o)):
    playerWin = True
  if ((one == computer_piece and five == computer_piece and nine == computer_piece) or (three == computer_piece and five == computer_piece and seven == computer_piece)):
    computerWin = True
  if ((one == computer_piece and four == computer_piece and seven == computer_piece) or (two == computer_piece and five == computer_piece and eight == computer_piece) or (three == computer_piece and six == computer_piece and nine == computer_piece)):
    computerWin = True
  if ((one == computer_piece and two == computer_piece and three == computer_piece) or (four == computer_piece and five == computer_piece and six == computer_piece) or (seven == computer_piece and eight == computer_piece and nine == computer_piece)):
    computerWin = True

def input_check(): 
  global computer_piece
  global x_o
  if x_o == "O":
    computer_piece = "X"


#main game:
def main_game():
  global end
  global x_o
  global repeats
  global inputNum

  reset_board() #resets values in case this is a 2nd game
  

  intro_scrn()
  print("Would you like to play as X or O? (please enter one)")
  x_o = input()
  input_check()
  print("You have chosen " + x_o + " as the piece you would like to play with.")
  print_scrn()
  

  while end == False:
    print("Please select the number of the block in which you would like to place your piece:")

    #process
    inputNum = input() #get the place that the user would like to place their piece
    user_place_check(inputNum) #check if a piece is already there
    change_num(inputNum) #switch the number of the piece with its variable and place the piece
    

    chk_win() #check to see if player has won
    
    if (playerWin == True): #given that the player has won, print this and ask if they would like to play again.
      print_scrn()
      print("You won! Would you like to play again? Y or N")
  
      while repeats == 1:
        answer = input()
        if (answer == "Y" or answer == "y"):
          print ('Okay!')
          main_game()
        if(answer == "N" or answer == "n"):
          end = True
          return
        else:
          print("Sorry! I don't understand that answer. Try again.")


    comp_play(str(randint(1,9)))
    chk_win() #check to see if computer has won
    print_scrn()


    if (computerWin == True): #given that the computer has won, print this and ask if they would like to play again.
      print("Sorry, you lost. Would you like to play again? Y or N") 

      while repeats == 1:
        answer = input()
        if (answer == "Y" or answer == "y"):
          print ('Okay!')
          main_game()
        if(answer == "N" or answer == "n"):
          end = True
          return
        else:
          print("Sorry! I don't understand that answer. Try again.")

    #code for tie is in comp_run as it relies on recursion to determine a tie

#main:
 

main_game()
print("Thanks for playing!")
sys.exit()