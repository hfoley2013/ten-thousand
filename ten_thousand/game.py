from ten_thousand.game_logic import GameLogic

playing = True


def default_roller(num):
    return GameLogic.roll_dice(num)


def welcome():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    if choice == "y":
        start()
    if choice =="n":
        print("OK. Maybe another time")


def start():
    total_points = 0
    round_number = 1
    while playing:
        round_score = play_round(round_number)
        if round_score == -1:
            break

        total_points += round_score
        print(f"You banked {round_score} points in round {round_number}")
        print(f"Total score is {total_points} points")
        round_number += 1

    print(f"Thanks for playing. You earned {total_points} points")


def play_round(round_number, roller=GameLogic.roll_dice):
    # unbanked_points = 0
    dice_not_kept = 6
    # kept_score = []
    round_score = 0
    print(f"Starting round {round_number}")
    while True:
        roll_string = ""
        roll = roller(dice_not_kept)
        #roll = (1, 1, 1, 1, 1, 1)
        for x in roll:
            roll_string += str(x) + " "
        print(f"Rolling {dice_not_kept} dice...")
        print(f"*** {roll_string} ***")
        if GameLogic.calculate_score(roll) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            round_score = 0
            return round_score



        # handles cheating uses validation function from GameLogic class

        keepers = confirm_keepers(roll, roll_string)
        if keepers == -1:
            return -1
        dice_not_kept -= len(keepers)
        if dice_not_kept == 0:  # hot dice
            dice_not_kept = 6  # reset to six
        round_score += GameLogic.calculate_score(tuple(keepers))

        print(f"You have {round_score} unbanked points and {dice_not_kept} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        choice_to_reroll = input("> ")
        if choice_to_reroll == "b":
            return round_score
        if choice_to_reroll == "q":
            return -1
        #handle quitting by returning 0 / -1

        # have the bank option in here somewhere


def confirm_keepers(roll, roll_string):

    while True:
        #values = [int(value) for value in keeper_string if value.isdigit()]

        #old solution
        # for x in keepers:
        #     all_kept_dice.append(int(x))
        #     kept_score.append(int(x))

        print("Enter dice to keep, or (q)uit:")
        user_input_dice_to_keep = input("> ")

        if user_input_dice_to_keep == "q":
            return -1


        formatted_user_input_dice_to_keep = [int(value) for value in user_input_dice_to_keep if value.isdigit()]

        if GameLogic.validate_keepers(roll, formatted_user_input_dice_to_keep):
            return formatted_user_input_dice_to_keep
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {roll_string} ***")


if __name__ == '__main__':

    rolls = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]

    def mock_roller(rolls):
        return (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)
        #return rolls

    welcome()
