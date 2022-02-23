#######################################################

# Date : 01/27/2022
# Title: Indiana Jones and Pazuzu's Diamond
# Matteo Meroni - MBAN 1
# Reference : "https://en.wikipedia.org/wiki/Indiana_Jones_and_the_Last_Crusade"

"""
Henry Walton Jones, Jr., better known as Indiana Jones, is a fictional archaeologist 
and protagonist of the franchise of the same name, created by George Lucas in homage 
to the action heroes of the film series of the 1930s. The character appears in four 
films directed by Steven Spielberg and a television series in novels, comic books, 
video games, and other media.

My game is not based on one of the Indiana Jones movies, but there are 
references to the movie: "Indiana Jones and the Last Crusade".

Stages:
1) Plane
2) Ground
3) Outside of the Temple
4) Inside of the Temple
"""

#importing necessary packages
import sys, time, random

#########################################################
# Constructing instruction and calling it to start the game
#########################################################

def instruction():
    
    # creating a While loop
    while True:
        instruction = input(prompt = "Do you want to read the instruction of the game?(Yes/No)").lower()
        
        # creating an if statement
        if instruction == "yes" or instruction == "y":
            print_slow("""\nYour main objective is to recover the diamond.
To do so, you'll have to face many dangers and solve puzzles that will 
put your cunning to the test. 

I will be your alter ego, so you must tell me what to do. 
I'm not very smart, so use words like WALK or LOOK followed by the name of an object 
(e.g., "ENTER IN THE TEMPLE"). 
Don't use complicated sentences with adverbs like LOOK CAREFULLY UNDER THE SEAT,
because they are beyond my comprehension.

Good Luck! (you'll need it)\n""")
            input(prompt = "< press enter to start the game >\n")
            # access to the start of the game
            start()
            break
        
        # adding an elif clause 
        elif instruction == "no" or instruction == "n":
            # access to the start of the game
            start()
            break
        
        # adding an else clause 
        else:
            print("\nPlease type Yes or No.")
            continue
    
        break
        
def start(): 
# printing introduction of the adventure game
    print_slow("""\n\nDuring World War II, Hitler was in search of artifacts 
of supernatural origin that could lead him to victory.  
At the time, the story was told of the precious Pazuzu's diamond, 
a jewel coming from another world and located in South America 
able to offer to anyone who possessed it the power of a God.
Fortunately, none of the Nazi researchers were ever able to find it 
and no one ever tried to find the diamond again.

Today you, the famous archaeologist and adventurer Indiana Jones, 
decide to venture out in search of the famous artifact.""")
    
    input(prompt = "< press enter to continue >\n")
    
    # access to the first scene
    plane()

#########################################################
# Constructing plane where the game starts
#########################################################

# defining the first scene
def plane():
        
    # printing the initial sentence of the room plane
    print_slow("""\nYou are piloting your single-seater plane over the dense 
Amazonian forest. Suddenly the engine loses power.
The controls are not responding! Do something to save yourself!

(Hint: maybe in the plane, there's something that can help you to survive!)\n""")

    # creating a while loop
    while True:
        choise_1 = input(prompt = 'What do you want to do?\n').lower()
        
        # writing a conditional statement
        if "don't" in choise_1 or "do not" in choise_1 or "not" in choise_1:
            print_slow("\nTell me what to do and not what not to do!\n")
            continue
        
        # adding an elif clause
        elif "jump" in choise_1 and "parachute" in choise_1:
            print_slow("\nYou are not wearing a parachute, yet!\n")
            continue
        
        # adding an elif clause  
        elif "eject" in choise_1 and "parachute" in choise_1:
            print_slow("\nYou are not wearing a parachute, yet!\n")
            continue
        
        # adding an elif clause 
        elif "use" in choise_1 and "parachute" in choise_1:
            print_slow("\nBefore to use it you have to find it!\n")
            continue
            
        # adding an elif clause 
        elif "take" in choise_1 and "parachute" in choise_1:
            print_slow("\nBefore to take it you have to find it!\n")
            continue
        
        # adding an elif clause 
        elif "wear" in choise_1 and "parachute" in choise_1 or "put" in choise_1 and "parachute" in choise_1:
            print_slow("\nBefore to wear it you have to find it!\n")
            continue
        
        # adding an elif clause
        elif "crash" in choise_1:
            fail()
            break
        
        # adding an elif clause
        elif "survive"in choise_1:
            print_slow("If you want to survive, tell me what to do!")
            continue
        
        # adding an elif clause
        elif "cry" in choise_1:
            print_slow("\nYou're crying like a baby, that won't help you not to die!\n")
            continue
        
        # adding an elif clause 
        elif "fly" in choise_1:
            print_slow("\nUnfortunatly you don't know how to fly!\n")
            continue
        
        # adding an elif clause 
        elif "jump" in choise_1 or "eject" in choise_1:
            print_slow("""\nAre you sure you haven't forgotten 
somethiiiinnggg
              ing
                ng
                  g
                  g
                  g
                  g
                  g
                  :
                  :
                  :
              \ splash /""")
            fail()
            break
        
        # adding an elif clause 
        elif "help" in choise_1 or "call" in choise_1:
            print_slow("\nCommunication systems are down and you're alone on the plane!")
            continue
            
        # adding an elif clause 
        elif "use" in choise_1 and "radio" in choise_1:
            print_slow("\nCommunication systems are down and you're alone on the plane!")
            continue
        
        # adding an elif clause    
        elif "search" in choise_1 or "look for" in choise_1 or "find" in choise_1:
            
            print_slow("""\nYou quickly searched in the airplane and you found a parachute 
and a delicious sandwich with ham and tomatoes.\n""")

            # creating a while loop
            while True:
                
                choise_2 = input(prompt = 'What do you want to do?\n').lower()
                
                # writing a conditional statement
                if "don't" in choise_2 or "do not" in choise_2 or "not" in choise_2:
                    print_slow("\nTell me what to do and not what not to do!\n")
                    continue
                
                # adding an elif clause
                elif "sandwich" in choise_2 and "parachute" in choise_2:
                    print_slow("\nYou can select one item at the time!\n")
                    continue
                
                # adding an elif clause 
                elif "eat" in choise_2 and "sandwich" in choise_2:
                    print_slow("\nThe sandwich was delicious but you lost time and the plane crashed!\n")
                    fail()
                    break
                    
                # adding an elif clause 
                elif "jump without parachute" in choise_2 or "jump without the parachute" in choise_2 or "eject without parachute" in choise_2 or "eject without the parachute" in choise_2:
                    print_slow("""\nAre you sure you haven't forgotten 
somethiiiinnggg
              ing
                ng
                  g
                  g
                  g
                  g
                  g
                  :
                  :
                  :
              \ splash /""")
                    fail() 
                    break
                
                # adding an elif clause 
                elif "jump with" in choise_2 and "parachute" in choise_2 or "eject with" in choise_2 and "parachute" in choise_2:
                    print_slow("""\nJust in time! The plane crashes to the ground as the parachute opens.
You gently descend to the mainland and, with any luck, 
manage to land in the middle of the dense Amazon rainforest.  
You abandon your parachute and start walking....\n""")
                    # access to the next room
                    ground()
                    break   
                
                # adding an elif clause 
                elif "use" in choise_2 and "parachute" in choise_2 or "take" in choise_2 and "parachute" in choise_2 or "wear" in choise_2 and "parachute" in choise_2 or "put the parachute on" in choise_2 or "put parachute on" in choise_2:
                    print_slow("""\nYou are now wearing the parachute. 
The aircraft is losing altitude, and you are running out of seconds!\n""")
                    
                    # creating a while loop
                    while True:
                        
                        choise_3 = input(prompt = "What do you want to do?\n").lower()
                        
                        # writing a conditional statement
                        if "don't" in choise_3 or "do not" in choise_3 or "not" in choise_3:
                            print_slow("\nTell me what to do and not what not to do!\n")
                            continue
                        
                        # adding an elif clause
                        elif "jump" in choise_3 or "eject" in choise_3:
                            print_slow("""\nJust in time! The plane crashes to the ground as the parachute opens.
You gently descend to the mainland and, with any luck, 
manage to land in the middle of the dense Amazon rainforest.  
You abandon your parachute and start walking....\n""")
                            
                            # accessing to the next room
                            ground()
                            break  
                        
                        # adding an elif clause 
                        elif "fly" in choise_3:
                            print_slow("\nUnfortunatly you don't know how to fly!")
                            continue
                        
                        # adding an elif clause 
                        elif choise_3 == "die" or choise_3 == "kill myself":
                            print_slow("You committed a suicide by shooting yourself in the head!")
                            fail()
                            break
                       
                        # adding an else clause 
                        else:
                            print(f"\nSorry, I don't know what you mean with: {choise_3}")
                            continue
                        
                        break
                
                # adding an elif clause 
                elif "fly" in choise_2:
                    print_slow("\nUnfortunatly you don't know how to fly!")
                    continue
                
                # adding an elif clause 
                elif "jump" in choise_2 or "eject" in choise_2:
                    print_slow("""\nAre you sure you haven't forgotten 
somethiiiinnggg
              ing
                ng
                  g
                  g
                  g
                  g
                  g
                  :
                  :
                  :
              \ splash /""")
                    fail() 
                    break
                
                # adding an elif clause 
                elif choise_2 == "die" or choise_2 == "kill myself":
                    print_slow("You committed a suicide by shooting yourself in the head!")
                    fail()
                    break
                
                # adding an else clause 
                else:
                    print(f"\nSorry, I don't know what you mean with: {choise_2}")
                    continue
                
                break
        
        # adding an elif clause 
        elif choise_1 == "die" or choise_1 == "kill myself":
            print_slow("\nYou committed a suicide by shooting yourself in the head!")
            fail()
            break
        
        # adding an elif clause 
        elif choise_1 == "parachute":
            print_slow("\nYou are not wearing a parachute, yet!")
            continue
        
        # adding an else clause 
        else:
            print(f"\nSorry, I don't know what you mean with: {choise_1}")
            continue
        
        break

#########################################################
# Constructing ground and calling it to start the game
#########################################################

# defining the ground scene
def ground():
    
    # print the initial sentence of the room ground
    print_slow("""\nAfter hours of walking, you meet a local indigenous.
He looks very friendly.\n""")
    
    # creating the list of possible questions
    question_list = ["""'Are you here to steal the Pazuzu's Diamond?'""",
                     """'Are you here to burn down the forest?'""",
                     """'Are you here to enslave our tribe?'""",
                     """'Are you a murderer?'""",
                     """'Have you seen my wife?'"""]
    
    # creating a while loop
    while True:
        
        choise_4 = input(prompt = 'What do you want to do?\n').lower()
        
        # writing a conditional statement
        if "don't" in choise_4 or "do not" in choise_4 or "not" in choise_4:
            print_slow("\nTell me what to do and not what not to do!\n")
            continue
            
        # adding an elif clause
        elif choise_4 == "die" or choise_4 == "kill myself":
            print_slow("\nYou committed a suicide by shooting yourself in the head!\n")
            fail()
            break
        
        # adding an elif clause
        elif "kill" in choise_4 or "shoot" in choise_4:
            print_slow("""\nYou pulled out your nine caliber pistol and fired a shot 
right between the poor native's eyes. 
You are a horrible person, but you can continue on your way.
You start to walk again.\n""")
            outside_temple()
            break
        
        # adding an elif clause 
        elif "fly" in choise_4:
            print_slow("\nUnfortunatly you don't know how to fly yet!")
            continue
        
        # adding an elif clause 
        elif "play" in choise_4:
            print_slow("""\nIndigenous: 'I don't want to play with you!'""")
            continue
         
        # adding an easter egg to the game
        elif "love" in choise_4 or "hug" in choise_4:
            print("""────────█████─────────────█████
────████████████───────████████████
──████▓▓▓▓▓▓▓▓▓▓██───███▓▓▓▓▓▓▓▓▓████
─███▓▓▓▓▓▓▓▓▓▓▓▓▓██─██▓▓▓▓▓▓▓▓▓▓▓▓▓███
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓▓▓──────────────────▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓─██───████─█──█─█████─▓▓▓▓▓▓██
██▓▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██
███▓▓▓▓▓▓─██───█──█─█──█─█████─▓▓▓▓▓▓██
███▓▓▓▓▓▓─██───█──█─█──█─██────▓▓▓▓▓▓██
─███▓▓▓▓▓─████─████─████─█████─▓▓▓▓███
───███▓▓▓▓▓──────────────────▓▓▓▓▓▓███
────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
─────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
───────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
──────────████▓▓▓▓▓▓▓▓▓▓▓▓████
─────────────███▓▓▓▓▓▓▓████
───────────────███▓▓▓███
─────────────────██▓██
──────────────────███
────────█████─────────────█████
────████████████───────████████████
──████▓▓▓▓▓▓▓▓▓▓██───███▓▓▓▓▓▓▓▓▓████
─███▓▓▓▓▓▓▓▓▓▓▓▓▓██─██▓▓▓▓▓▓▓▓▓▓▓▓▓███
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓───────────────────────────▓▓▓▓██
██▓▓─███──█─████─█───█─████─█████──▓▓██
██▓▓─██─█─█─█────█───█─█────█──██──▓▓██
██▓▓─██─█─█─████─██─██─████─████───▓▓██
██▓▓─██─█─█─█─────███──█────█──██──▓▓██
██▓▓─██──██─████───█───████─█──███─▓▓██
─██▓▓▓───────────────────────────▓▓▓███
───███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
─────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
───────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
──────────████▓▓▓▓▓▓▓▓▓▓▓▓████
─────────────███▓▓▓▓▓▓▓████
───────────────███▓▓▓███
─────────────────██▓██
──────────────────███
────────█████─────────────█████
────████████████───────████████████
──████▓▓▓▓▓▓▓▓▓▓██───███▓▓▓▓▓▓▓▓▓████
─███▓▓▓▓▓▓▓▓▓▓▓▓▓██─██▓▓▓▓▓▓▓▓▓▓▓▓▓███
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
██▓▓▓▓▓▓▓────────────────────▓▓▓▓▓▓▓▓██
██▓▓▓▓▓───████▄─███─████─█████──▓▓▓▓▓██
███▓▓▓▓───██──█──█──█────█──────▓▓▓▓███
███▓▓▓▓───██──█──█──████─█████──▓▓▓▓███
─███▓▓▓───██──█──█──█────────█──▓▓▓▓██
──████▓───████▀─███─████─█████──▓████
───███▓▓───────────────────── ▓▓▓███
────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
─────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
───────████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
──────────████▓▓▓▓▓▓▓▓▓▓▓████
─────────────███▓▓▓▓▓▓▓███
───────────────███▓▓▓███
─────────────────██▓██
──────────────────███


You start to walk again.""")
            # access to the next room
            outside_temple()
            break
            
        # adding an elif clause    
        elif "talk" in choise_4 or "ask" in choise_4 or "speak" in choise_4:
            
            # creating a while loop
            while True:
                question = random.choice(question_list)
                answer_1 = input(prompt = f'Indigenous: {question} (Yes/No)\n').lower()
                
                # writing a nested conditional statement
                if question == "'Are you here to steal the Pazuzu's Diamond?'" and answer_1 == "yes" or question == "'Are you here to steal the Pazuzu's Diamond?'" and answer_1 == "y":
                    print_slow("""\nThe indigenous man stabs you with his blade, you are dead!
Telling the truth is not always a good idea.\n""")
                    fail()
                    break
                
                # adding an elif clause
                elif question == "'Are you here to burn down the forest?'" and answer_1 == "yes" or question == "'Are you here to burn down the forest?'" and answer_1 == "y":
                    print_slow("""\nThe indigenous man stabs you with his blade, you are dead!
Indigenous: 'We don't want arsonists around here.'\n""")
                    fail()
                    break
                
                # adding an elif clause
                elif question == "'Are you here to enslave our tribe?'" and answer_1 == "yes" or question == "'Are you here to enslave our tribe?'" and answer_1 == "y":
                    print_slow("""\nThe indigenous man stabs you with his blade, you are dead!
Indigenous: 'We want to be free'.\n""")
                    fail()
                    break
                
                # adding an elif clause
                elif question == "'Are you a murderer?'" and answer_1 == "yes" or question == "'Are you a murderer?'" and answer_1 == "y":
                    print_slow("""\nThe indigenous man stabs you with his blade, you are dead!
Indigenous: 'You are not that good'.\n""")
                    fail()
                    break
                
                # adding an elif clause
                elif question == "'Have you seen my wife?'" and answer_1 == "yes" or question == "Have you seen my wife?" and answer_1 == "y":
                    print_slow("""\nThe indigenous man stabs you with his blade, you are dead!
Indigenous: "How do you know my wife?".\n""")
                    fail()
                    break
                    
                # adding an elif clause 
                elif answer_1 == "no" or answer_1 == "n":
                    
                    # creating a while loop
                    while True:
                        answer_2 = input(prompt = """\nIndigenous: 'Are you sure?'(Yes/No)\n""").lower()
                
                        if answer_2 == "no" or answer_2 == "n":
                            print_slow("\nThe indigenous man stabs you with his blade, you are dead\n")
                            fail()
                            break
                        
                        # adding an elif clause 
                        elif answer_2 == "yes" or answer_2 == "y":
                            
                            # creating a while loop
                            while True:
                                answer_3 = input(prompt = """\nIndigenous: 'Are you sure that you are sure?'(Yes/No)\n""").lower()
                                
                                # writing a nested conditional statement
                                if answer_3 == "no" or answer_3 == "n":
                                    print_slow("\nThe indigenous man stabs you with his blade, you are dead\n")
                                    fail()
                                    break
                                
                                # adding an elif clause 
                                elif answer_3 == "yes" or answer_3 == "y":
                                    print_slow("""\nIndigenous: 'The only thing that I can do is wish you good luck,
I hope you will not die in the forest.'

You start to walk again.\n""")
                                    outside_temple()
                                    break
                                
                                # adding an else clause 
                                else:
                                    print("\nPlease type Yes or No")
                                    continue
                                
                                break
                        
                        # adding an else clause 
                        else:
                            print("\nPlease type Yes or No")
                            continue
                        
                        break
                
                # adding an else clause 
                else:
                    print("\nPlease type Yes or No")
                    continue
                
                break
        
        # adding an else clause 
        else:
            print(f"\nSorry, I don't know what you mean with: {choise_4}")
            continue
            
        break

#########################################################
# Constructing outside_temple
#########################################################

# defining the outside_temple scene
def outside_temple():
    
    # print the initial sentence of the room outside_temple
    print_slow("""\nYou are now in front of a majestic temple!
You advance slowly and read the following numbers on the gate:

1
11
21 
1211
111221

It looks like a sequence of numbers.
Next to the handle, there is a panel where to insert a code.\n""")
    
    # creating a password
    password = "312211"
    password = int(password)
    attempt = 2
    # creating a while condition
    while True:
        pwd_attempt = input(prompt = """Which of the following combinations do you want to type in?

- 312211
- 112351
- 112212
\n> """)
        
        # insert the try function
        try:
            pwd_attempt = int(pwd_attempt)
            # writing a conditional statement
            if pwd_attempt == int(password) and attempt >= 1:
                print_slow("""\nThat is correct. You may enter.
The gate of the temple is now open.\n""")
                temple()
                break
            
            # adding an elif clause 
            elif pwd_attempt == int("112351") and attempt == 1 or pwd_attempt == int("112212") and attempt == 1:
                print_slow(f"""\nThat is not the correct password.
A big rock falls on your head!\n""")
                fail()
                break
            
            # adding an elif clause 
            elif pwd_attempt == int("112351") and attempt > 1 or pwd_attempt == int("112212") and attempt > 1:
                print_slow(f"""\nThat is not the correct password.
You have 1 attempt left.\n""")
                attempt -= 1
                continue
        
            # adding an else clause 
            else:
                print("\nThat's not a possible combination.")
                continue
        
        # insert the except function for non numerical input   
        except ValueError:
            print("\nSelect only numbers. Please try again.")
            continue

        break

#########################################################
# Constructing temple
#########################################################

# defining temple scene
def temple():
    
    # printing the initial sentence of the room temple
    print_slow("""\nCongratulations, you are in the temple!
You see a long corridor and a stone of rare beauty at the end of it.  
Above the stone, there is an inscription:
"Only the penitent man will pass".\n""")
    
    # creating a while loop
    while True:
        
        choise_6 = input(prompt = """What do you want to do?
A) Walk to the diamond and grab it.
B) Kneel on the ground.
C) Shoot with your gun.
D) Exit from the temple.
\n""").lower()
        
        # writing a conditional statement
        if "don't" in choise_6 or "do not" in choise_6 or "not" in choise_6:
            print_slow("\nTell me what to do and not what not to do!\n")
            continue
        
        # adding an elif clause
        elif "walk" in choise_6 or "grab" in choise_6 or choise_6 == "a":
            print_slow("\nYou can take two steps but then out of nowhere a big blade cuts your head off!\n")
            fail()
            break
            
        # adding an elif clause
        elif "exit" in choise_6 or "go out" in choise_6 or choise_6 == "d":
            print_slow("""\nAs soon as you go out the gate close!\n""")
            outside_temple()
            break
            
        # adding an elif clause
        elif "shoot" in choise_6 or "gun" in choise_6 or choise_6 == "c":
            print_slow("""\nAs soon as you pull out the gun a long blade cuts your arm, 
you fall to the ground and bleed to death!\n""")
            fail()
            break
        
        # adding an elif clause 
        elif "kneel" in choise_6 or choise_6 == "b":
            print_slow("""\nA penitent man his humble, he kneels before God!
You are free to go ahead and take the Pazuzu's Diamond!\n""")
            win()
            break
        
        # adding an else clause 
        else:
            print("\nInvalid answer\n")
            continue
        
        break

# creating a UDF to print slow the words
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

# defining the win scenario
def win():
    
    # printing the sentence in case the player win
    print("""\n _     _  ___   __    _  __    _  _______  ______   
| | _ | ||   | |  |  | ||  |  | ||       ||    _ |  
| || || ||   | |   |_| ||   |_| ||    ___||   | ||  
|       ||   | |       ||       ||   |___ |   |_||_ 
|       ||   | |  _    ||  _    ||    ___||    __  |
|   _   ||   | | | |   || | |   ||   |___ |   |  | |
|__| |__||___| |_|  |__||_|  |__||_______||___|  |_|
                                                    
    \n""")
    print_slow("""You have succeed in your quest for the Pazuzu's Diamond.\n""")
    print('<Game Over>')
    
    # giving the possibility to restart the game
    while True:
        end = input("""What do you want to do?
1. Restart the game
2. Stop to play\n""").lower()
        
        # writing a conditional statement
        if "restart" in end or "1" in end or "one" in end:
            start()
            break
    
        # adding an elif clause 
        elif "stop" in end or "2" in end or "two" in end:
            print("Thank you for playing, see you soon!")
            exit(0)
            break
        
        # adding an else clause
        else:
            print("""\nInvalid answer""")
            continue
        
        break
    
# defining the fail scenario
def fail():
    
    # printing the sentence in case the player die
    print_slow("""
           @     
           @     
        @@@@@@@  
           @     
           @     
           @     
       ____#____ 
      /        / 
     /  ~~~~  /  
    /  ~~~~  /   

I am very saddened by your untimely passing.... 
Besides, it's always the best who leaves (is not it?).

You have failed in your quest for the Pazuzu's Diamond.\n""")
    print('<Game Over>')
    
    # giving the possibility to restart the game
    while True:
        end = input("""What do you want to do?
1. Restart the game
2. Stop to play\n""").lower()
        
        # writing a conditional statement
        if "restart" in end or "1" in end or "one" in end:
            start()
            break
    
        # adding an elif clause 
        elif "stop" in end or "2" in end or "two" in end:
            print_slow("Thank you for playing, see you soon!")
            exit(0)
            break
        
        # adding an else clause
        else:
            print("""\nInvalid answer""")
            continue
        
        break
    
# to start the code from the beginning
instruction()
