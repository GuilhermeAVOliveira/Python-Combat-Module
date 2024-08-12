import random
import os

def Begin():
    os.system('cls')
    print("--------------------------------------------------")
    print("Welcome to the game!")
    print("--------------------------------------------------")
    print("Start Game?\n1 - Yes\n2 - No")
    resposta = int(input(""))
    if resposta == 2:
        os.system('cls')
        exit()
    else:
        create_player()
        create_npc()
        FightOrRun()

def combatLoop():
    os.system('cls')
    while npc["Health"] > 0:
        Combate()
        npc_attack(npc, player)
        if player["Health"] <= 0:
            print("Oh no, you died!")
            PlayerDeath()
    levelUp()
    delete_npc()
    create_npc()
    FightOrRun()

def FightOrRun():
    statsShow()
    print("Will you fight or run?\n1 - Fight\n2 - Run")
    resposta = int(input(" "))
    if resposta == 2:
        Begin()
    else:
        combatLoop()

def PlayerDeath():
    print("You died! Will you try again?\n1 - Try Again\n2 - Exit")
    resposta = int(input(" "))
    if resposta == 1:
        Begin()
    else:
        os.system('cls')
        exit()

def Combate():
    statsShow()
    print("Choos your action:\n1 - Attack\n2 - Shield\n3 - Run")
    print(player_shield)
    resposta = int(input(" "))
    os.system('cls')
    if resposta == 3:
        Begin()
    elif resposta == 2:
        player_shield()
    elif resposta == 1:
        player_attack()

def levelUp():
    global plevel
    player["Exp"] += int(npc["Level"]*10)
    print(f"You got {int(npc['Level']*10)} EXP!")
    while player["Exp"] >= player["MaxExp"]:
        player["Exp"] -= player["MaxExp"]
        plevel += 1
        playerReset()

def playerReset():
    player["Level"] = plevel
    player["MinDamage"] = (2 + int(plevel/2), 5 + plevel)
    player["MaxDamage"] = (5 + plevel, 6*plevel)
    player["MaxHealth"] = int(5 + player["MaxDamage"] + plevel)
    player["MaxExp"] = 10 * (plevel*2)

    player["Health"] = player["MaxHealth"]

def create_player():
    os.system('cls')
    global player
    global player_defense
    global plevel
    player_defense = False
    plevel = 1
    Name = input("Type your name: ")
    os.system('cls')
    pMinDamage = random.randint(2 + int(plevel/2), 5 + plevel)
    pMaxDamage = random.randint(5 + plevel, 6*plevel)
    pMaxHealth = int(5 + pMaxDamage + plevel)
    pHealth = pMaxHealth
    exp = 0
    maxExp = 10 * (plevel*2)

    player = {
        "Name": f"{Name}",
        "Level": plevel,
        "MinDamage": pMinDamage,
        "MaxDamage": pMaxDamage,
        "MaxHealth": pMaxHealth,
        "Health": pHealth,
        "Exp": exp,
        "MaxExp": maxExp,
    }

def create_npc():
    global npc 
    level = random.randint(0, 20)
    damage = int(5 + level/2)
    maxHealth = int(5 + damage + level)
    health = maxHealth

    npc = {
        "Name": f"Monster ({level})",
        "Level": level,
        "Damage": damage,
        "MaxHealth": maxHealth,
        "Health": health,
    }

def delete_npc():
    npc.clear

def statsShow():
        print("--------------------<><>---Você---<><>--------------------")
        print(f"Name/Lvl: {player['Name']} #{player['Level']} \nDmg: {player['MinDamage']} - {player['MaxDamage']}\nHP: {player['MaxHealth']}/{player['Health']}\nExp: {player['Exp']}/{player['MaxExp']}")
        print("--------------------<><>----------<><>--------------------")
        print(f"Name/Lvl: {npc['Name']} // Dmg: {npc['Damage']} - HP: {npc['MaxHealth']}/{npc['Health']}")
        print("--------------------<><>----------<><>--------------------")

def player_attack():
    global player_defense
    if player_defense == True:
        player_defense = False
    dano = random.randint(player["MinDamage"], player["MaxDamage"])
    npc["Health"] -= dano
    print(f"You attack, dealing {dano} damage!")

def player_shield():
    global player_defense
    player_defense = True
    print("You put your shield up, nothing will damage you!")

unique_numbers = set()
all_possible_numbers = {1, 2, 3}

def attack_chance():
    global unique_numbers
    global result

    if len(unique_numbers) == len(all_possible_numbers):
        unique_numbers.clear()

    available_numbers = list(all_possible_numbers - unique_numbers)
    if available_numbers:
        result = random.choice(available_numbers)
    else:
        result = random.choice(list(all_possible_numbers))

    unique_numbers.add(result)
    
    return result

def npc_attack(npc, player):
    print("The enemy prepares to hit you...")
    attack_chance()
    if result < 2 and player_defense == False:
        player["Health"] -= npc["Damage"]
        print(f"It hits! You lost {npc['Damage']} HP!")
    elif result < 2 and player_defense == True:
        print("It hits your shield! You receive no damage!")
    else:
        print("It miss! You receive no damage!")
         
Begin()