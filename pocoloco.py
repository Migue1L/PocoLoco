"""Based off a dice-rolling game found in Port Coquitlam; python project"""
# NEXT STEPS:
# - Finish clening up interface
# - Put game on a website
# - Clean up website/ visually appealing

import random
import time

#players
p1 = {'name': 'edgar', 'score': 0, 'case': 0, 'chips': 0, 'order': 0}
p2 = {'name': 'emz','score': 0, 'case': 0, 'chips': 0, 'order': 0}
p3 = {'name': 'spike','score': 0, 'case': 0, 'chips': 0, 'order': 0}
human = {'name': 'human','score': 0, 'case': 0, 'chips': 0, 'order': 0}

order = [p1, p2, p3, human]

dice = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def rules():
    """This method handles outputting the instructions of the game"""
    print("\nRules:")
    print("This is Poco Loco! A dice-rolling game where the objective is \
to lose all your chips as quickly as possible! Heres how it works:")
    print("1. Each player rolls up to the amount of times that the first \
player rolls to get best possible score")
    print("2. There are different rolls, ranked from best to worst:")
    print("  - PoCo!: 4, 5, 6")
    print("  - 3 of a kind (ex. 3, 3, 3)")
    print("  - Loco!: 1, 2, 3")
    print("  - For other rolls, add up the score using:")
    print("     • 1 = 100 points")
    print("     • 2 = 2 points")
    print("     • 3 = 3 points")
    print("     • 4 = 4 points")
    print("     • 5 = 5 points")
    print("     • 6 = 60 points")
    print("3. Lowest scoring player will be given chips by other participants following this:")
    print("  - 1 chip if the winners score is a points total")
    print("  - 2 chips if the winners score is LoCo")
    print("  - 3 chips if the winners score is 3 of a kind")
    print("  - 4 chips if the winners score is PoCo")
    print("4. Tie-breaks will result in a random winner")
    print("5. Rounds keep being played until there is a winner")

def dice_roll():
    """This method handles the rolling of the 6-sided dice and its display"""
    result = ''

    roll1 = random.randint(1,6)
    result+=str(roll1)
    dice1 = dice[roll1]
    roll2 = random.randint(1,6)
    result+=str(roll2)
    dice2 = dice[roll2]
    roll3 = random.randint(1,6)
    result+=str(roll3)
    dice3 = dice[roll3]

    for i in range (5):
        print(dice1[i], end=' ')
        print(dice2[i], end=' ')
        print(dice3[i])

    return result

def set_up():
    """ This method handles the setup, including printing the title and rules."""

    print(" ____    ___      __   ___       _       ___      __   ___  ")
    print("|    \\  /   \\    /  ] /   \\     | |     /   \\    /  ] /   \\ ")
    print("|  o  )|     |  /  / |     |    | |    |     |  /  / |     |")
    print("|   _/ |  O  | /  /  |  O  |    | |___ |  O  | /  /  |  O  |")
    print("|  |   |     |/   \\_ |     |    |     ||     |/   \\_ |     |")
    print("|  |   |     |\\     ||     |    |     ||     |\\     ||     |")
    print("|__|    \\___/  \\____| \\___/     |_____| \\___/  \\____| \\___/ ")

    rules()
    name = input("\nTo begin, please enter your name: ")
    human["name"] = name

    chip = int(input(f"Welcome, {name}! Please enter the amount of starting chips: "))
    p1["chips"] = chip
    p2["chips"] = chip
    p3["chips"] = chip
    human["chips"] = chip

    random.shuffle(order)
    print("PLAY ORDER:\n")
    print(f"1-{order[0]['name']}")
    print(f"2-{order[1]['name']}")
    print(f"3-{order[2]['name']}")
    print(f"4-{order[3]['name']}\n")

def case(result):
    """This method handles the different cases when rolling the dice"""
    #case 0 - no special rules
    #case 1 - Loco!
    #case 2 - 3 of a kind
    #case 3 = PoCo!

    if set(result) == {'4', '5', '6'}:
        return 3
    elif set(result) == {'1', '2', '3'}:
        return 1
    elif result[0] == result[1] == result[2]:
        return 2
    else:
        return 0

def scoring(result, player_case, player_name, player):
    """This method handles calculating the score based off the player's roll"""
    if player_case == 3:  # PoCo!
        player['score'] = 5000
        return f"{player_name} got PoCo!\n"
    elif player_case == 1:  # Loco!
        player['score'] = 300
        return f"{player_name} got LoCo!\n"
    elif player_case == 2:  # 3 of a Kind
        player['score'] = 400 + int(result[0])
        return f"{player_name} got 3 of a Kind!\n"
    else:
    #Other rolls
        score = 0
        for c in result:
            if c == '1':
                score += 100
            elif c == '2':
                score +=2
            elif c == '3':
                score += 3
            elif c == '4':
                score += 4
            elif c == '5':
                score += 5
            elif c == '6':
                score += 60
        player['score'] = score
        return f"{player_name} scored {score} points\n"

def turn(round_number):
    """This method handles the logic for a single round of PoCo Loco"""
    print('-'*11 + '-' * len(str(round_number)))
    print('|', "round ", round_number, '|')
    print('-'*11 + '-' * len(str(round_number)))

    for player in order:
        print(f"{player['name']} currently has {player['chips']} chips")
    print("\n")
    # Initialize max_rolls to the limit - 3.
    max_rolls = 3

    for _, player in enumerate(order):
        print(f"{player['name']}'s turn:")
        roll = 1
        for j in range(1, max_rolls+1):
            print(f"Roll {j}/{max_rolls}")
            rolls = dice_roll()
            player['case'] = case(rolls)
            message = scoring(rolls, player['case'], player['name'], player)
            print(message)

            # Only want to prompt when another roll is available
            if player == human and j < max_rolls:
                choose = input("Roll again? (y/n): ").lower()
                if choose != "y":
                    break
            elif player['score'] > 15:
                break

            roll+=1
        max_rolls = min(max_rolls, roll)

        # Pause for 1 sec to allow human to view each round
        time.sleep(1)

    # Low/High Score & Tie-Breaker
    low_score = min(player['score'] for player in order)
    high_score = max(player['score'] for player in order)

    low_scorers = [player for player in order if player['score'] == low_score]
    high_scorers = [player for player in order if player['score'] == high_score]

    if len(low_scorers) > 1:
        print("There is a tie for the lowest score! A random player is chosen.")
        low_scorer = random.choice(low_scorers)
    else:
        low_scorer = low_scorers[0]

    if len(high_scorers) > 1:
        print("There is a tie for the highest score!")
        high_scorer = random.choice(high_scorers)
    else:
        high_scorer = high_scorers[0]

    print(f"{high_scorer["name"]} won this round")
    print(f"{low_scorer["name"]} lost this round\n")

    # Calculate chip distribution
    winner_case = high_scorer['case']
    give_chips = 0
    if winner_case == 0:  # Points total
        give_chips = 1
    elif winner_case == 1:  # LoCo
        give_chips = 2
    elif winner_case == 2:  # 3 of a Kind
        give_chips = 3
    elif winner_case == 3:  # PoCo
        give_chips = 4

    # Remove correct amount of chips
    for player in order:
        if player != low_scorer:
            # ensure the player doesn't give more chips than they have
            player['chips'] -= min(give_chips, player["chips"])
            low_scorer['chips'] += give_chips
            print(f"{player['name']} gave {give_chips} chips to {low_scorer['name']}")

    # Find who won and allow player to control when to proceed
    num_winners = sum(player["chips"] <= 0 for player in order)
    if num_winners > 0:
        if num_winners == 1:
            winner = [player["name"] for player in order if player["chips"] == 0][0]
            print(f"{winner} has won the game!")
        else:
            winners = [player["name"] for player in order if player["chips"] == 0]
            print(f"\n{', '.join(winners)} have 0 chips!\nChoosing winner randomly.\n")
            winner = random.choice(winners)
            print(f"{winner} has won the game!")

        # Print out final chip count
        print("\nFinal chip count:")
        for p in order:
            print(f"{p['name']}: {p['chips']} chips")
        return False

    input("\n(enter) to continue to the next round")
    return True

def main():
    """This handles and sets up the environment to play the game"""
    set_up()
    round_num = 1
    while True:
        if not turn(round_num):
            break
        round_num += 1

if __name__ == "__main__":
    main()