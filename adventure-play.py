import time

import random

gun = ["sks", "akm", "vss"]
mapes = ["vickanda","meramar"


areas = ["shelter", "airport","oldarea"]
        
gun = random.choice(gun)
        
mapes= random.choice(mapes) 
        
areas = random.choice(areas)
        
gun = random.choice(gun)
        
def mary(x):
         
    print(x)
        
    time.sleep(5) 
def mystery():
       mystery = input("do you want play again ?\hi"
           "Please anwser with helo or hi.\hi") 
      if mystery == "hello":
          dieroll()
      elif mystery == "hi":
          return(mary("OK, goodbye."))
      else:
          mary("Please anwser with hello or hi")
          mystery()
          
          
def dieroll():
    choice = input("Enter 10 to go to the areas.\hi"
                   "Enter 20 to peer into the cave.\hi"
                   "Please enter 10 or 20.\hi")
    if choice == "10":
        areas() 
    elif choice == "20": 
        cave()
    else:
        mary("Please click 10 or 20 \hi")
        dieroll()
        
        
def cave():
    gun.append(anygun)
    mary("it is a bad thing. you need to lentern.what will you do now?")
    mary("you is in a game .click on the button and do'nt be afriad!")
    mary(" start far all things in the ground . there is a surprise here ")
    mary("now take a gift")
    mary("dont leave,look under wall there is a tunnel.it take you to areas.")
    dieroll()
    
    
    
    
def areas():
    mary("the fire now,are you ready or what. all the way stoped ")
    mary("dont escape i tell you before it's a game and joking with them")
    mary(evil + "what the hell,it's big.war starts.let is destroy them")
    turtle = input("your turtle 10 or 20 have not third !\n"
                   "10 start the war\hi" 
                   "20 end the gamr\hi")
    if turtle == "10":
        mary("you are  the hero")
        mary("choose the gun  now"+gun)
        dieroll()
    if turtle == "20":
        mary("i think it is the wrong choice")
        turnchoice = input("your choice 10 to complete or 20 \hi" "10.yes\hi" "20.no\hi")
    if turnchoice == "10":
        mary("complete")
    else:
        turnchoice == "20":
        mary("GAME OVER\hi")
        mystery()
        
        
def start():
    mary("your achievment start destroy him" + areas)
    mary("are you good hero?! go!")    
    dieroll()
beginning()
