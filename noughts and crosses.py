import time


#variables
print_sleep = (.03)

#play variables
one = ("1")


def intro_scrn(): #print intro screen
    print ()
    print ("  n o u g h t s  &  c r o s s e s  ")
    print ()

def print_scrn():
    #print game screen

    time.sleep (.5)
    print (" ----------------------------- ")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    1    |    2    |    3    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|-----------------------------|")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    4    |    5    |    6    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|-----------------------------|")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print ("|    7    |    8    |    9    |")
    time.sleep (print_sleep)
    print ("|         |         |         |")
    time.sleep (print_sleep)
    print (" ----------------------------- ")

#def chk_win(a):
  #  if a == 1


#def comp_play():

#main game:
intro_scrn()
print("Would you like to play as X or O? (please enter one)")
x_o = input()
print("You have chosen " + x_o + " as the piece you would like to play with. Please select the number you would like to play:")
print_scrn()

#process
#input_num = input() #!add a check here
#chk_win(input_num)


