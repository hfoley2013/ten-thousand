from ten_thousand.game_logic import GameLogic

default_roller = GameLogic.roll_dice

# Welcome the user and ask them to play
def welcome_user():
    print("Welcome to Ten Thousand")
    print("(y) to play or (n) to decline")

    user_choice = input("> ")
    print(user_choice)
    return user_choice

# Starts the game if user selects (y)es, or exits the game if declined
def start_game():
    user_choice = welcome_user()
    if user_choice is "> y":
        play()
    elif user_choice is not "> y":
        print("Ok. Maybe another time.")

# Executes the game
def play(roller=default_roller):
    """
    Start the game using the default_roller
    """
    round_count = 1
    total_points = 0
    num_dice = len(roller(6))

    while total_points < 10000:
        do_round(round_count, num_dice, roller)

# Starts a round
def do_round(round_count, num_dice, roller):
    print(f"Starting round {round_count}")
    print(f"Rolling {num_dice} dice...")
    
    dice = roller(num_dice)
    dice_lst = [int(i) for i in dice]
    dice_str = ""
    
    for i in dice_lst:
        dice_str += str(i) + " "
    
    print(f"*** {dice_str} ***")
    
    print("Enter dice to keep, or (q)uit")

    keep_dice = input("> ")

    kept_dice = tuple([int(i) for i in keep_dice])
    
    unbanked_score = GameLogic.calculate_score(kept_dice)
    print(unbanked_score)
    
    print(f"You have {unbanked_score} unbanked points in round {round_count}")
    
    round_count += round_count + 1

# Prompt user choice

# Ends a round
    

if __name__ == '__main__':
    start_game()
