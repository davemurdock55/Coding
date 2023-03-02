# 
# # mini choose your own adventure game
# def adventure():
#      print("You are in a dark room.")
#      print("There is a door to your right and left.")
#      print("Which one do you take?")
#      choice = input("> ")
#      if choice == "left":
#           bear_room()
#      elif choice == "right":
#           cthulhu_room()
#      else:
#           dead("You stumble around the room until you starve.")
#           
#           
# def bear_room():
#      print("There is a bear here.")
#      print("The bear has a bunch of honey.")
#      print("The fat bear is in front of another door.")
#      print("How are you going to move the bear?")
#      bear_moved = False
#      while True:
#           choice = input("> ")
#           if choice == "take honey":
#                dead("The bear looks at you then slaps your face off.")
#           elif choice == "taunt bear" and not bear_moved:
#                print("The bear has moved from the door.")
#                print("You can go through it now.")
#                bear_moved = True
#           elif choice == "taunt bear" and bear_moved:
#                dead("The bear gets pissed off and chews your leg off.")
#           elif choice == "open door" and bear_moved:
#                gold_room()
#           else:
#                print("I got no idea what that means.")
#                
# def cthulhu_room():
#      print("Here you see the great evil Cthulhu.")
#      print("He, it, whatever stares at you and you go insane.")
#      print("Do you flee for your life or eat your head?")
#      choice = input("> ")
#      if "flee" in choice:
#           start()
#      elif "head" in choice:
#           dead("Well that was tasty!")
#      else:
#           cthulhu_room()
#           
#           
# adventure()


# mini choose your own adventure game

# starting off the story
print("You are in Hyrule. Gaurdian shooting you")

# Getting their response and putting in the variable called "RunOrFightGuardian" (and making it lowercase so we don't have to worry about that)
RunOrFightGuardian = input("Do you want to fight or run?").lower()

if RunOrFightGuardian == "run":
     print("You didn't die. You ran away from the Guardian.")
else :
     print("You died. You fought the Guardian and lost.")
     Whatdoyoudo = input("hi your name is luke and you have three hearts in a place ca lled hyrule, you are in a forest and you see a guardian shooting at you. you have to run or fight. what do you do?")
     
     