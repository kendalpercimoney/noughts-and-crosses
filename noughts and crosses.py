import time
import random
from random import randint

#variables
print_sleep = (.03)
end = False

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

def place_num(a): #assign the piece to its respective place
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
    
    if (a == str(1)):
      if (one != x_o and one != "O"):
        one = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(2)):
      if (two != x_o and two != "O"):
        two = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(3)):
      if (three != x_o and three != "O"):
        three = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(4)):
      if (four != x_o and four != "O"):
        four = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(5)):
      if (five != x_o and five != "O"):
        five = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(6)):
      if (six != x_o and six != "O"):
        six = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(7)):
      if (seven != x_o and seven != "O"):
        seven = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(8)):
      if (eight != x_o and eight != "O"):
        eight = ("O")
      else:
        place_num(str(randint (1, 9)))
    elif (a == str(9)):
      if (nine != x_o and nine != "O"):
        nine = ("O")
      else:
        place_num(str(randint (1, 9)))



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



#def comp_play():
  #if (two or four or six or eight == x_o):
  

    

#main game:
intro_scrn()
print("Would you like to play as X or O? (please enter one)")
x_o = input()
print("You have chosen " + x_o + " as the piece you would like to play with.")
print_scrn()
counter = 0

while end == False:
  print("Please select the number of the block in which you would like to place your piece:")

  #process
  input_num = input() #!add a check here
  change_num(input_num)

  place_num(str(randint(1,9)))
  #chk_win(input_num)
  print_scrn()

  
  counter = counter + 1
  if (counter == 5):
    end = True


