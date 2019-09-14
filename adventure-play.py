import time

import random

gun = ["sks", "akm", "vss"]

mapes = ["vickanda","meramar"

areas = ["shelter", "airport"]
        
gun = random.choice(gun)
        
mapes= random.choice(mapes) 
        
areas = random.choice(areas)
        
        
def mary(message):
         
    print(messaage)
        
    time.sleep(5) 
         
def mystery():
       mystery = input("do you want play again ?\n"
                       
           "Please anwser with yes or no.\n") 
         
      if mystery == "yes":
         
          dieroll()
         
      elif mystery == "no":
         
          return(mary("OK, goodbye."))
      else:
          mary("Please anwser with yes or no")
          mystery()
          
          
def dieroll():
         
    choice = input("Enter 1 to go to the areas.\n"
                   
                   "Enter 2 to go into the cave.\n"
                   
                   "Please enter 1 or 20.\n")
         
    if choice == "1":
         
        areas() 
         
    elif choice == "2": 
          cave()
             
def cave():
    mary("you are in a game .click on the button and do'nt be afriad!")
         
    gun.append(anygun)
         
    mary("it's very bad . do you need to lentern.what will you do now?")
         
 
    mary(" start far all things in the ground there is a gift here ")
         
    mary("now take a gift")
         
    mary("wow you are excellent")
         
    mary("dont leave,look under the ground there is a tunnel.it takes you to areas.")
         
    mary(" you are an Awesome player")
         
    dieroll()
    
    
    
    
def areas():
    mary("you ae under ground now ,are you ready? or not.if you are not ready stop")
         
    mary("I thinkj you are ready now ! start")
         
    mary("dont escape fom any gang .they are not perfect go ahead")
         
    mary(mapes + "what is  the mapes ,it's big. lets start.let is destroy them")
         
    turtle = input("your turtle 1 or 20have not third !\n"
                   
                   "1 start the match\hi" 
                   
                   "2 end the match\hi")
         
         
         
    if turtle == "1":
                  
        mary("you are  the hero")
         
        mary("choose your gift  now"+gun)
         
        dieroll()
         
         
    if turtle == "2":
         
        mary("good luck . play again")
         
        turnchoice = input("your choice 1 to complete or 2\n" "1.yes\n" "2.no\n")
         
    if turnchoice == "1":
         
        mary("the end")
         
    else:
         
        turnchoice == "2":
        mary("see you next time\n")
         
        mystery()
               
def start():
    mary("your achievment many thing . go ahead" + areas)
    mary("are you good hero?! go!")    
    dieroll()
beginning()
