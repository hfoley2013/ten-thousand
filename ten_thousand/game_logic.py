from random import randint
from collections import Counter

class GameLogic:

    @staticmethod
    def roll_dice(num_dice=6):
       return tuple([randint(1,6) for _ in range(num_dice)])

    @staticmethod
    def calculate_score(dice_roll):
        dice_count = Counter(dice_roll)

        score_dict = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

        score = 0

        # calculate straight
        if len(dice_count) == 6:
            return 1500

        # calculate triple doubles
        if len(dice_count) == 3 and all(value == 2 for value in dice_count.values()):
            return 1500

        # score based on face value
        for face_value, count in dice_count.items():
            if face_value == 5 and count <= 2:
                score += 50 * count
            elif face_value == 1 and count <= 2:
                score += 100 * count
            elif face_value == 1 and count == 3:
                score += 1000
            elif count == 3:
                score += score_dict[face_value]
            elif count == 4:
                score += score_dict[face_value] * 2
            elif count == 5:
                score += score_dict[face_value] * 3
            elif count == 6:
                score += score_dict[face_value] * 4

        return score
