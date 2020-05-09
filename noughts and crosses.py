import time


#variables
print_sleep = (.03)

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

#main game:
intro_scrn()
print("Would you like to play as X or O? (please enter one)")
x_o = input()
print("You have chosen " + x_o + " as the piece you would like to play with.")
print_scrn()
print("Please select the number of the block in which you would like to place your piece:")


#process
input_num = input() #!add a check here
change_num(input_num)
#chk_win(input_num)
print_scrn()


