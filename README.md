# LAB - Class 06

## Project: Ten Thousand

## Author: Harper Foley

## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/ten-thousand)
* [Rules of the Game](https://en.wikipedia.org/wiki/Dice_10000)

## Collaborators/Contributors

* `game.py` code created in collaboration with Ian Shirley, Oliver Speir, Dylan Cabral, and Aubrey Corsetti

### Setup

* To set up this repo create a local repository on your machine
* Create a virtual environment for Python
  * `python3.11 -m venv .venv`
* Activate the venv file
  * `source .venv/bin/activate`
* Install `pytest` and `pytest-watch`
  * `pip install pytest pytest-watch`
* Use `git clone` to clone the repo to your local machine
  * `git clone https://github.com/hfoley2013/ten-thousand.git`
* Your repo is now ready to run the Ten Thousand dice game simulator program

### How to initialize/run

* To run the test scripts:
  * Run `pytest` in the CLI
* To run the program:
  * Run `python3.11 -m ten_thousand.game`
  * Answer the prompts in order to see a print out of a the output of your dice rolls and scoring
  * For additional information on the rules of the game, you can consult the rules of the game [here](https://en.wikipedia.org/wiki/Dice_10000)

### Tests

* How do you run tests?
  * Tests are conducted via `pytest`
