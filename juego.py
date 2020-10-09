import random
import sys


actionlist = ["You fell into a trap and died",
"You got bit by a random snake, you lost 40 hp",
"There is a toxic gas around the area and you suffer the effects, you lose 40hp",
"The hunger is getting stronger, you lose 20 hp",

"You find an armed skeleton, seeking vengeance for his life. His stats: attack: 10, defence: 0 ",
"You find a clone of you but extremely aggresive. His stats: attack: 40, defence: 1",
"A giant rat with humanoid body stares at you with his red eyes. His stats: attack: 1, defence: 20",

"You find a full armor kit, +10 defence",
"You find an ancient weapon, looking sharp. +20 attack",
"You find a longer stick, +10 attack",

"You find the final treasure. Good job! You completed the quest and came back to your house"]

print("\n\t\tWelcome to Dungeons\n\n")
# Inicio 
name = input("What is your name?\n")

print("Welcome",name,",get ready to enter the magnificient dungeon. You will face horrible monsters. I hope youre ready for it, or you won't escape alive.")



#Variables del juego
health_bar = 100
defence = 0
attack = 5

# Funcion aleatoria del juego
def lose_health(hp):
  global health_bar
  health_bar-=hp
  if(health_bar<=0):
    print("Oops... you died\n")
    replay()

def replay():
  replay = input("Do you want to replay? (Y/N)")
  if(replay=="Y"):
    return
  sys.exit()

def attack_F(atk,defe):
  global health_bar
  choice = input("Do you want to fight him? (Y/N)\n")
  if(choice=="N"):
      print("You tried to escape but you still got hit and lost 20 hp")
      lose_health(20)
  elif(choice=="Y"):
      if(random.choice(range(0,10))<=3): #He attacks first
        if(defence>atk): 
            print("He attacked first but your defense is higher. You escape and lose 20 hp.")
            lose_health(20)
        else: 
            print("He attacked and hit you, you lost half of your hp")
            health_bar /= 2
      else: 
        if(attack<defe): 
            print("You tried to attack but his defence is higher. You escape and lose 20 hp.")
            lose_health(20)
        else:
            print("You attacked him and killed him.")
  else:
      print("Please, press Y or N")
    

def action_main () :
  global defence
  global attack
  choice = random.choice(range(0,len(actionlist)-1))
  print(actionlist[choice],".\n")

  if(choice==0):
    lose_health(100)
  elif(choice==1):
    lose_health(40)
  elif(choice==2):
    lose_health(40)
  elif(choice==3):
    lose_health(20)
  elif(choice==4):
    attack_F(10,0)
  elif(choice==5):
    attack_F(40,1)
  elif(choice==6):
    attack_F(1,20)
  elif(choice==7):
    defence+=10
  elif(choice==8):
    attack+=20
  elif(choice==9):
    attack+=10
  elif(choice==10):
    replay()




#Inicializador
while (1>0):
  print("---------------------------------------------------\n\t\t YOUR STATS")
  print("\nHealth:",health_bar)
  print("\nAttack:",attack)
  print("\nDefense:",defence)
  print("---------------------------------------------------\n\n")
  lol = input("What side do you want to take? (L/R)\n")
  action_main()
