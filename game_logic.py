import random

class GameLogic:
    def roll_dice(self, num_dice):
        dice_roll = []
        for i in range(num_dice):
            dice_roll.append(random.randint(1, 6))
        return tuple(dice_roll)

    def calculate_score(self, dice_roll):
        num_ones = dice_roll.count(1)
        num_twos = dice_roll.count(2)
        num_threes = dice_roll.count(3)
        num_fours = dice_roll.count(4)
        num_fives = dice_roll.count(5)
        num_sixes = dice_roll.count(6)

        score = 0

        # Calculate score for ones
        score += num_ones * 100

        # Calculate score for twos
        score += num_twos * 200

        # Calculate score for threes
        score += num_threes * 300

        # Calculate score for fours
        score += num_fours * 400

        # Calculate score for fives
        score += num_fives * 500

        # Calculate score for sixes
        score += num_sixes * 600

        # Calculate score for straight
        if num_ones == 1 and num_twos == 1 and num_threes == 1 and num_fours == 1 and num_fives == 1 and num_sixes == 1:
            score += 1500

        # Calculate score for three pairs
        if num_ones == 2 and num_twos == 2 and num_threes == 2 and num_fours == 2 and num_fives == 2 and num_sixes == 2:
            score += 750

        # Calculate score for two trios
        if ((num_ones == 3 and num_twos == 3) or (num_ones == 3 and num_threes == 3) or (num_ones == 3 and num_fours == 3) or (num_ones == 3 and num_fives == 3) or (num_ones == 3 and num_sixes == 3)) and ((num_twos == 3 and num_threes == 3) or (num_twos == 3 and num_fours == 3) or (num_twos == 3 and num_fives == 3) or (num_twos == 3 and num_sixes == 3)) and ((num_threes == 3 and num_fours == 3) or (num_threes == 3 and num_fives == 3) or (num_threes == 3 and num_sixes == 3)) and ((num_fours == 3 and num_fives == 3) or (num_fours == 3 and num_sixes == 3)) and ((num_fives == 3 and num_sixes == 3)):
            score += 1500

        # Calculate score for three of a kind
        if num_ones >= 3 or num_twos >= 3 or num_threes >= 3 or num_fours >= 3 or num_fives >= 3 or num_sixes >= 3:
            score += 1000
            score += sum(dice_roll)

        # Calculate score for leftover ones
        score += (num_ones % 3) * 100

        # Calculate score for leftover fives
        score += (num_fives % 3) * 50

        return score
