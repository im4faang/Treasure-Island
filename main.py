import os
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 
print("Hit enter after making choices.")
choice1 = input("Are you ready to start this adventure? Type 'y' or 'n': ").lower()
if choice1 == "y":
  os.system("clear")
  choice2 = input("You land on an unknown island. After walking a while, you come across two roads. Where do you want to go? Type 'left' or 'right'.\n").lower()
  if choice2 == "left":
    print("You spot a cave. You decide to enter it. It's dark. You flinch a bit and hit a rock. When you open your eyes, you see someone chasing you. He's a bandit!")
    print("""
                '-.               .-'
_______________'-._________.-'______________
'-.           _    '-. .-'   _           .-'
   '-.       (_)  /      \  (_)       .-'
      '-.        /        \        .-'
         '-.____/          \____.-'
                \_ _ _ _ _ /
            //////////\\\\\\\\\
           ///////////\\\\\\\\\\
          |||| .-----------._||||
          |||| '-|___|___|-' ||||
          \\\\  '---------'  ////
            \\\|||||||||||||///
              \\\\\\\\///////
                \\\\\\///// 
    """)
    choice3 = input("What would you do? Hit 'y' to escape or 'n' to grovel down.\n").lower()
    if choice3 == "n":
      print("Oh blimey, you peasant! What are you doing? Are you scared...pftt?! I'll spare you if you answer three questions of mine.")
      choice4 = input("Are you ready? Type 'y' or 'n': ").lower()
      if choice4 == "y":
        q1 = input("I’m tall when I’m young, and I’m short when I’m old. What am I? ").lower()
        if q1 == "candle":
          q2 = input("The more of this there is, the less you see. What is it? ").lower()
          if q2 == "darkness":
            q3 = input("What is always in front of you but can’t be seen? ").lower()
            if q3 == "future":
              print("Damn you human, you are smart after all! You can proceed further.")
              print("That was hard. You nailed it. You wake up and move and somehow escape the cave.")
              choice5 = input("You come across three doors. 'Red', 'Yellow' and 'Blue'. Type 'r' or 'y' or 'b' respectively.\n").lower()
              if choice5 == "y":
                print("Congratulations, you find the treasure. You win!")
              elif choice5 == "r":
                print("Oh lad, it's a room full of fire. Game Over.")
              elif choice5 == "b":
                print("Hungry ogres are going to have a feast. Game Over.")
              else:
                print("Err, wrong choice. Game Over.")
            else:
              print("Err, the answer is future. Behold my wrath. Game Over.")
          else:
            print("Err, the answer is darkness. Behold my wrath. Game Over.")          
        else:
          print("Err, the answer is candle. Behold my wrath. Game Over.") 
      elif choice4 == "n":
        print("Are you questioning my intelligence of asking questions or you simply are a fool? Die, you puny human! Game Over.")
      else:
        print("Err, wrong choice. Game Over.")
    elif choice3 == "y":
      print("Oooo, bang bang! He cowboy'ed a gun and took a sling shot. Game Over!")
    else:
      print("Err, wrong choice. Game Over.")
  elif choice2 == "right":
    print("You fell in a hole. Game Over.")
  else:
    print("Err, wrong choice. Game Over.")
elif choice1 == "n":
  print("Goodbye!")
else:
  print("Err, wrong choice. Game Over.")
