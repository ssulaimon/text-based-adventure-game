import random
import time
print("Title: The Quest for the Enchanted Amulet")
print(
    """
    The Fate of the Kingdom is in your hand our hero.
    Enter N to read the backstory of the event or S to skip the backstory
    """)
user_answer = input("Continue or Skip: ")
while not user_answer.upper() == "N" and not user_answer.upper() == "S":
    user_answer = user_answer = input("Continue or Skip: ")

if user_answer.upper() == "N":
    print("""
    Once upon a time, in the mystical land of Eldoria, a legendary artifact known as the Enchanted Amulet 
    was said to grant its possessor unimaginable powers. Many adventurers had sought it, but none had returned. You 
    are a brave and determined soul who has taken up the challenge to find the amulet and harness its incredible 
    power.""")
else:
    print("Welcome to the game")

user_weapon = ""
print("""
      The village Herbalist offers you a powerful charm to fight the battle ahead and also the village blacksmith 
      offers you his finest hand made weapon. You can only choose one. Please enter 1 for the charm and 2 for the 
      weapon""")


while not user_weapon == "charm" and not user_weapon == "weapon":
    weapon_of_choice = input("Your Weapon of Choice: ")
    if int(weapon_of_choice) == 1:
        user_weapon = "charm"
        print("You have been equipped with charm")
    elif int(weapon_of_choice) == 2:
        user_weapon = "weapon"
        print("You have been equipped with weapon")
    else:
        print("Invalid choice user")

print(
    """
    You begin your journey in the quaint village of Arborwood.
    The village elder tells you that the amulet is hidden deep within the Forbidden Forest, 
    a dark and treacherous place filled with magical creatures and deadly traps.
    Your first task is to reach the forest's entrance.
    """)
print(
    """
    As you approach the forest's entrance, you encounter a group of bandits blocking the path.
    """)
print(""" 
    Engage in combat with the bandits or Try to negotiate and convince them to let you pass peacefully.
    Enter E to engage in battle or N to negotiate with them
""")
user_answer = input("Your choice: ")
user_live = 100
if user_answer.upper() == "E":
    print(f"You have choose to engage with the bandit. You have {user_live} live")
    print("Battle started....")
    print("🎲Throw the dice")
    time.sleep(3)
    dice_throw_result = random.randint(1, 6)
    print("""
    Roll a six-sided dice (1-6):
    1, 2, 3: You defeat the bandits with your swordplay and quick reflexes, but you sustain minor injuries.
    4, 5: The battle is fierce, but you manage to fend them off without significant harm.
    6: You overpower the bandits effortlessly and emerge unscathed.""")
    print(f"You rolled number {dice_throw_result} on the dice")
    if dice_throw_result < 4:
        user_live = user_live - 30
        print(f"Your current live is {user_live}%")
    elif dice_throw_result < 6:
        user_live = user_live - 10
        print(f"Your current live is {user_live}%")
    else:
        print(f"Your current live is {user_live}%")
elif user_answer.upper() == "N":
    print("You have choose to negotiate with the bandit")
    print(
        """
        You attempt to reason with the bandits, explaining your quest for the 
        Enchanted Amulet and the potential rewards it could bring to Eldoria. 
        Surprisingly, some of them seem moved by your words. One of the bandits, who appears to be the leader, steps forward
        """)
    print(f"Leader: Alright, we'll let you pass, but only if you give us your {user_weapon}. We need it more than you do.")
    print(f"To release your {user_weapon} enter G or N to either battle")
    user_answer = input("Your answer: ")
    if user_answer.upper() == "G":
        print(f"you gave up your {user_weapon}")
        user_weapon = ""
    elif user_answer.upper() == "N":
        print("You chose to engage in battle ")
        print("Battle started....")
        print("🎲Throw the dice")
        dice_throw_result = random.randint(1, 6)
        print("""
           Roll a six-sided dice (1-6):
           1, 2, 3: You defeat the bandits with your swordplay and quick reflexes, but you sustain minor injuries.
           4, 5: The battle is fierce, but you manage to fend them off without significant harm.
           6: You overpower the bandits effortlessly and emerge unscathed.""")
        print(f"You rolled number {dice_throw_result} on the dice")
        if dice_throw_result < 4:
            user_live = user_live - 30
            print(f"Your current live is {user_live}%")
        elif dice_throw_result < 6:
            user_live = user_live - 10
            print(f"Your current live is {user_live}")
        else:
            print(f"Your current live is {user_live}")
    else:
        print("Invalid user input")
else:
    print("Invalid user input")

print("After a hot encounter with the bandit, you manage to defeat the bandits. Wounded but victorious, you proceed through the forest's entrance.")
print("""
As you delve deeper into the Forbidden Forest, you encounter a series of perplexing riddles carved on ancient stones.
Each riddle guards a different path, and solving them is essential to navigate through the forest safely.""")

riddles = [{"riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "options": ["An echo", "A river", "A tree"], "answer": "An echo"}, {"riddle": " I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I??", "options": ["Pencil lead", "Biro", "A tree"], "answer":"Pencil lead"}]

selected_riddle_index = random.randint(0, 1)
selected_riddle = riddles[selected_riddle_index]
print(selected_riddle["riddle"])
option = selected_riddle['options']
print(f"Options: {option}")
print("Think.... 🤔")
user_answer = input("Your riddle answer: ")
while not user_answer.lower() == selected_riddle["answer"].lower() and user_live > 0:
    user_live = user_live - 10
    print(f"Your current live is {user_live}%")
    print("Your answer is wrong try again")
    user_answer = input("Your riddle answer: ")
if user_live == 0:
    print("Game Over. You did not save the Kingdom ):, Quest failed try again later")
else:
    print("Correct! The stone glows briefly and reveals a hidden path to your left.")
    print(
        """
        You continue deeper into the forest, facing more challenges and riddles along the way. Your skills and wit are put to the test as you encounter magical creatures and overcome various obstacles. Eventually, you reach the heart of the Forbidden Forest, where the Enchanted Amulet awaits.
        """)
    print(
        """
        However, the amulet is guarded by an ancient and powerful guardian—a fearsome dragon! To claim the amulet, you must defeat the dragon in a battle of strength and will.
        """)
    print("The 🐉Dragon current live is 100%")
    print("ready for great battle")
    dragon_live = 100
    while not dragon_live == 0 and not user_live == 0:
        print("Player move")

        if not(user_weapon == ""):
            print(f"Do you have to use your {user_weapon}. Enter Y for Yes and N for N")
            user_answer = input("Your choice: ")
            if user_answer.upper() == "Y":
                print(f"💊{user_weapon} is engaged....")
                time.sleep(3)
                dragon_live -= 30
                user_weapon = ""
                print(f"Current 🐉dragon live is {dragon_live}%")

            elif user_answer.upper() == "N":
                print('You attacked the 🐉dragon.....')
                dice_throw_result = random.randint(1, 6)
                if dice_throw_result < 4:
                    print("🐉Dragon suffered a minor attack from the dragon")
                    time.sleep(3)
                    dragon_live -= 10
                    print(f"Current dragon live is {dragon_live}%")
                else:
                    print("🐉Dragon suffered a bad attack from the dragon")
                    time.sleep(3)
                    dragon_live -= 20
                    print(f"Current dragon live is {dragon_live}%")

            else:
                print('🎖️You attacked the dragon.....')
                dice_throw_result = random.randint(1, 6)
                if dice_throw_result < 4:
                    print("🐉Dragon suffered a minor attack from the dragon")
                    time.sleep(3)
                    dragon_live -= 10
                    print(f"Current 🐉dragon live is {dragon_live}%")
                else:
                    print("🐉Dragon suffered a bad attack from the dragon")
                    time.sleep(3)
                    dragon_live -= 20
                    print(f"Current dragon live is {dragon_live}%")
        else:
            print('🎖️You attacked the dragon.....')
            time.sleep(3)
            dragon_live -= 10
            print(f"Current 🐉dragon live is {dragon_live}%")

        if not(dragon_live == 0):
            print("🐉 Dragon move...")
            dice_throw_result = random.randint(1, 6)
            if dice_throw_result < 4:
                print("🔥You suffered a minor attack from the dragon.")
                time.sleep(3)
                user_live -= 10
                print(f"🎖️Your current live is {user_live}%")
            else:
                print("🔥You suffered a bad attack from the dragon")
                time.sleep(3)
                user_live -= 20
                print(f"🎖️Your current live is {user_live}%")
        else:
            break

    if user_live == 0:
        print("You lost the battle with the dragon. You cold not retrieve the Enchanted Amulet.😢")
    else:
        print("You won the battle our hero. You brought back the Enchanted Amulet to the village.😃")






