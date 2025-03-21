print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Will you make the right choices? Good luck, and stay alive!")

choice_1 = input("You start your mission at a crossroad. "
                 "Do you wish to go left or do you wish to go right?\n "). lower()
if choice_1 == "left":
   choice_2 = input("There is an empty dock, and a storm brewing. "
                    "Do you want to wait "
                    "or do you want to swim for the other side?\n ").lower()
   if choice_2 == "wait":
      choice_3 = input("You get a ride from a man with a boat. "
                       "There is a cave entrance with different "
                       "colored vines lining paths: "
                       "yellow, and black. "
                       "Which path do you take?\n ").lower()
      if choice_3 == "black":
         choice_4 = input("You make your way down the cave and find an altar. "
                         "On the altar are two symbols: an owl and a flower. "
                          "Which do you push?\n ")




         if choice_4 == "flower":
                     print("You press down on the flower, and from the ground rises a large chest! You have found it! "
                           "The treasure now belongs to you, brave traveler!")
         else:
            print("You pressed the owl symbol and a large pit opened beneath your feet. "
                  "You fell in and broke multiple bones, and you succumb to your wounds. "
                  "Game over. ")

      else:
        print("I am sorry, traveler. This is where your story ends. "
              "The cave collapsed on you and you died. "
              "Game over. ")


   else: print("You misjudged the strength of the coming storm "
                   "and as you try with all of your might "
                   "to fight the current, you drown. "
                   "Game over.")


else:
     print("You have chosen to go right. You make your way down the path and the sky turns to an eerie black, "
          "and you are eaten by a dragon! Game over.")
