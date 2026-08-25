import random


# ================= ATTRIBUTES =================

health = 100
max_health = 100

stamina = 100
max_stamina = 100

money = 0

level = 1

experience = 0
experience_required = 100

hand_damage = 12
defence = 0


# ================= INVENTORY =================

swords = ["Basic-sword"]

potions = ["instant health"]

armours = ["Leather-armour"]


# ================= EQUIPPED STATUS =================

equipped_sword = None
equipped_armour = None


# ================= ENEMIES =================

enemies = [

    {
        "name": "Goblin",
        "health": 50,
        "damage": 15,
        "reward": 10,
        "xp": 25
    },

    {
        "name": "Wolf",
        "health": 40,
        "damage": 30,
        "reward": 25,
        "xp": 50
    },

    {
        "name": "Dragon",
        "health": 100,
        "damage": 45,
        "reward": 50,
        "xp": 100
    }

]


# ================= ROLE SELECTOR =================

def role_selector():

    print("Select a Role to Play:")
    print("-----------------------------")

    print("1. Hunter")
    print("Stronger physical damage but weaker magic damage.")

    print("-----------------------------")

    print("2. Mage")
    print("Weaker physical damage but stronger magic damage.")

    role_choice = int(input("Enter a role to choose (1, 2): "))

    match role_choice:

        case 1:

            print("You have chosen the Hunter role!")

            hunter_id = random.randint(1, 99)
            role_card = f"HR-{hunter_id}"

            print(f"ID: {role_card}")

            return "Hunter", role_card


        case 2:

            print("You have chosen the Mage role!")

            mage_id = random.randint(1, 99)
            role_card = f"Mage-{mage_id}"

            print(f"ID: {role_card}")

            return "Mage", role_card


        case _:

            print("Invalid role selected.")

            return role_selector()


# ================= PLAYER INDEX =================

def show_index():

    print("============== PLAYER INDEX ==============")

    print(f"""

Name : {name}

Role : {role}

ID : {role_card}

Health : {health}/{max_health}

Stamina : {stamina}/{max_stamina}

Level : {level}

XP : {experience}/{experience_required}

Money : {money}

Hand Damage : {hand_damage}

Sword Bonus : {get_sword_bonus()}

Total Damage : {get_total_damage()}

Defence : {defence}

Armour Bonus : {get_armour_bonus()}

Total Defence : {get_total_defence()}

""")


# ================= INVENTORY =================

def show_inventory():

    print("=============== INVENTORY ===============")

    option = None

    while option != 4:

        print("""
1. Swords
2. Potions
3. Armours
4. Back
""")

        option = int(input("Enter (1 - 4) to view the items: "))

        match option:

            case 1:

                print("You have:")

                for sword in swords:
                    print(sword)


            case 2:

                print("You have:")

                for potion in potions:
                    print(potion)


            case 3:

                print("You have:")

                for armour in armours:
                    print(armour)


            case 4:

                print("Going back...")


            case _:

                print("Invalid choice, try again.")


# ================= EQUIPMENT =================

def show_equipment():

    global equipped_sword
    global equipped_armour

    option = None

    while option != 3:

        print(f"""
=============== EQUIPMENT ===============

Equipped Sword: {equipped_sword}

Equipped Armour: {equipped_armour}

1. Equip Sword
2. Equip Armour
3. Back
""")

        option = int(input("Enter a choice (1-3): "))

        match option:

            case 1:

                print("Currently you have:")

                for sword in swords:
                    print(sword)

                choice = input("Enter a sword to equip: ")

                if choice in swords:

                    equipped_sword = choice

                    print(f"{choice} equipped!")

                else:

                    print("You don't own that sword.")


            case 2:

                print("Currently you have:")

                for armour in armours:
                    print(armour)

                choice = input("Enter an armour to equip: ")

                if choice in armours:

                    equipped_armour = choice

                    print(f"{choice} equipped!")

                else:

                    print("You don't own that armour set.")


            case 3:

                print("Going back...")


            case _:

                print("Invalid choice.")


# ================= SWORD STATS =================

def get_sword_bonus():

    if equipped_sword == "Basic-sword":
        return 3

    elif equipped_sword == "Iron-sword":
        return 5

    elif equipped_sword == "Diamond-sword":
        return 8

    else:
        return 0


# ================= ARMOUR STATS =================

def get_armour_bonus():

    if equipped_armour == "Leather-armour":
        return 3

    elif equipped_armour == "Iron-armour":
        return 5

    elif equipped_armour == "Diamond-armour":
        return 8

    else:
        return 0


# ================= FINAL STATS =================

def get_total_damage():

    return hand_damage + get_sword_bonus()


def get_total_defence():

    return defence + get_armour_bonus()


# ================= DUNGEON =================

def enter_dungeon():

    global health
    global money
    global experience

    # Select one random enemy
    enemy = random.choice(enemies)

    # Get values from that enemy dictionary
    enemy_name = enemy["name"]
    enemy_health = enemy["health"]
    enemy_damage = enemy["damage"]
    enemy_reward = enemy["reward"]
    enemy_xp = enemy["xp"]

    print(f"""
========== DUNGEON ==========

You encountered a {enemy_name}!

Enemy Health : {enemy_health}
Enemy Damage : {enemy_damage}
""")

    while health > 0 and enemy_health > 0:

        print("""
========== BATTLE ==========
""")

        print(f"Player Health : {health}")
        print(f"Enemy Health  : {enemy_health}")

        print("""
1. Attack
2. Escape
""")

        choice = int(input("Enter your choice: "))

        # ========== ATTACK ==========

        if choice == 1:

            damage = get_total_damage()

            enemy_health -= damage

            print(f"""
You attacked {enemy_name}!

Damage dealt: {damage}

{enemy_name} Health: {enemy_health}
""")

            # Enemy dies

            if enemy_health <= 0:

                print(f"You killed the {enemy_name}!")

                money += enemy_reward
                experience += enemy_xp

                print(f"""
========== REWARDS ==========

Money earned: {enemy_reward}

XP earned: {enemy_xp}

Total Money: {money}

Total XP: {experience}
""")

                break

            # Enemy attacks if still alive

            enemy_attack = enemy_damage - get_total_defence()

            if enemy_attack < 0:
                enemy_attack = 0

            health -= enemy_attack

            print(f"""
{enemy_name} attacked you!

Damage received: {enemy_attack}

Your Health: {health}
""")

        # ========== ESCAPE ==========

        elif choice == 2:

            escape_chance = random.choice([True, False])

            if escape_chance:

                print("You successfully escaped!")

                break

            else:

                print("Escape failed!")

                enemy_attack = enemy_damage - get_total_defence()

                if enemy_attack < 0:
                    enemy_attack = 0

                health -= enemy_attack

                print(f"""
{enemy_name} attacked you!

Damage received: {enemy_attack}

Your Health: {health}
""")

        else:

            print("Invalid choice!")

    # ========== PLAYER DEATH ==========

    if health <= 0:

        print("""
========== GAME OVER ==========

You died in the dungeon!
""")


# ================= GAME START =================

print(r"""
                                        ___====-_  _-====___
                                  _--^^^#####//      \\#####^^^--_
                               _-^##########// (    ) \\##########^-_
                              -############//  |\^^/|  \\############-
                            _/############//   (@::@)   \\############\_
                           /#############((     \\//     ))#############\
                          -###############\\    (oo)    //###############-
                         -#################\\  / VV \  //#################-
                        -###################\\/      \//###################-
                       _#/|##########/\######(   /\   )######/\##########|\#_
                       |/ |#/\#/\#/\/  \#/\##/  \/  \/  \##/\#/  \/\#/\#/\| \|
                       `  |/  V  V  `   V  \#\ \    / /#/  V   '  V  V  \|  '
                          `   `  `      `   / | \  / | \   '      '  '   '
                                           (  |  \/  |  )
                                          __\ |  |  | /__
                                         (vvv(VVV)(VVV)vvv)

                       ___________________________________________________
                      |                                                   |
                      |               DUNGEON OF DISTURBANCE              |
                      |___________________________________________________|
""")



name = input("Enter your username: ")

print(f"Username: {name}")


enter = input("Type (e) to enter and create a character: ")

if enter == "e":

    role, role_card = role_selector()


# ================= MAIN MENU =================

menu = input("Enter (m) to access menu: ")

while menu == "m":

    print("""
============== DUNGEON MASTER - MENU ==============

1. Player Index
2. Inventory
3. Equipment
4. Enter Dungeon
5. Exit
""")

    choice = int(input("Enter (1-5) to access the menu: "))

    match choice:

        case 1:

            show_index()


        case 2:

            show_inventory()


        case 3:

            show_equipment()


        case 4:

            enter_dungeon()


        case 5:

            print("Exiting game...")

            break


        case _:

            print("Invalid choice!")