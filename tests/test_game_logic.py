import pytest
from game_logic import *

def test_roll_dice():
    game = GameLogic()

    # Test rolling 1 die
    dice_roll = game.roll_dice(1)
    assert len(dice_roll) == 1
    assert isinstance(dice_roll[0], int)
    assert 1 <= dice_roll[0] <= 6

    # Test rolling 2 dice
    dice_roll = game.roll_dice(2)
    assert len(dice_roll) == 2
    assert all(isinstance(die, int) for die in dice_roll)
    assert all(1 <= die <= 6 for die in dice_roll)

    # Test rolling 3 dice
    dice_roll = game.roll_dice(3)
    assert len(dice_roll) == 3
    assert all(isinstance(die, int) for die in dice_roll)
    assert all(1 <= die <= 6 for die in dice_roll)

    # Test rolling 4 dice
    dice_roll = game.roll_dice(4)
    assert len(dice_roll) == 4
    assert all(isinstance(die, int) for die in dice_roll)
    assert all(1 <= die <= 6 for die in dice_roll)

    # Test rolling 5 dice
    dice_roll = game.roll_dice(5)
    assert len(dice_roll) == 5
    assert all(isinstance(die, int) for die in dice_roll)
    assert all(1 <= die <= 6 for die in dice_roll)

    # Test rolling 6 dice
    dice_roll = game.roll_dice(6)
    assert len(dice_roll) == 6
    assert all(isinstance(die, int) for die in dice_roll)
    assert all(1 <= die <= 6 for die in dice_roll)
