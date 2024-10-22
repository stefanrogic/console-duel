import random

class Character:
    def __init__(self, name, health_bar, attack, defend, action):
        self.name = name
        self.health_bar = health_bar
        self.attack = attack
        self.defend = defend
        self.action = action

    def status(self):
        print(self.name, self.health_bar)

turn = 1
player = Character(input("What is your name?: "), 15, 0, 0, 0)
enemy = Character("Enemy", 15, 0, 0, 0)


def print_status():
    player.status()
    enemy.status()

def start_game():
    print("[START] --------------------------------------------\n")
    print_status()
start_game()

def generate(a = 0, b= 5):
    return random.randint(a, b)

def attack():
    if enemy.action == 0:
        enemy.health_bar -= player.attack
        player.health_bar -= enemy.attack
        print(f"{player.name} attacked for {str(player.attack)} damage.")
        print(f"{enemy.name} attacked for {str(enemy.attack)} damage.")

    else:
        enemy.health_bar += enemy.defend
        enemy.health_bar -= player.attack
        print(f"{player.name} attacked for {str(player.attack)} damage.")
        print(
            f"{enemy.name} deflected {str(enemy.defend) if player.attack >= enemy.defend else str(player.attack)} and took {str(abs(player.attack - enemy.defend)) if player.attack - enemy.defend > 0 else "no"} damage{f" ({enemy.defend - player.attack} added to the health)" if enemy.defend - player.attack > 0 else ""}.")

def defend():
    if enemy.action == 0:
        player.health_bar += player.defend
        player.health_bar -= enemy.attack
        print(f"{enemy.name} attacked for {str(enemy.attack)} damage.")
        print(
            f"{player.name} deflected {str(player.defend) if enemy.attack >= player.defend else str(enemy.attack)} and took {str(abs(enemy.attack - player.defend)) if player.attack - player.defend > 0 else "no"} damage{f" ({player.defend - enemy.attack} added to the health)" if player.defend - enemy.attack > 0 else ""}."
            )

    else:
        player.health_bar += player.defend
        enemy.health_bar += enemy.defend
        print(f"{player.name} added {str(player.defend)} health.")
        print(f"{enemy.name} added {str(enemy.defend)} health.")

while player.health_bar > 0 and enemy.health_bar > 0:
    enemy.attack = generate()
    enemy.defend = generate()
    enemy.action = generate(0, 1)

    player.attack = generate()
    player.defend = generate()

    print(f"\n[TURN {str(turn)}] -------------------------------------------")
    print("\nEnemy is attacking" if enemy.action == 0 else "\nEnemy is defending")

    player_action = input(f"Attack ({str(player.attack)} Damage) or Defend (Up to {str(player.defend)} damage)? (A/d): ").lower()

    if (
        player_action == "a"
        or player_action == "attack"
    ):
        attack()
        turn += 1
    elif (
        player_action == "d"
        or player_action == "defend"
    ):
        defend()
        turn += 1
    else:
        print("You entered wrong action!")

    print_status()

    if player.health_bar <= 0 < enemy.health_bar:
        print("\n[YOU LOSE] -----------------------------------------")

    if player.health_bar > 0 >= enemy.health_bar:
        print("\n[YOU WIN] ------------------------------------------")

    if player.health_bar <= 0 and enemy.health_bar <= 0:
        print("\n[DRAW] ---------------------------------------------")






