"""
Hangman game for the console shell
"""

import random


class Hangman:
    """
    Prints and controls everything showed to the player.
    """

    def __init__(self):
        self.word = str()
        self.player_guess = list()  # A list of characters with all player
        # guesses
        self.correct_guess = list()  # Player current correct guesses
        # self.solved = False  # is the word solved
        self.chances = 5

    def pick_word(self):
        # Picks the word from a list, returns it
        wordlist = open('wordlist', mode='rt')
        self.word = random.choice(wordlist.readlines())
        wordlist.close()
        self.word = self.word.strip('\n')

    def start(self):
        print('Welcome to Hangman.\n'
              'We have chosen a random word. Your goal is to guess it '
              'before you are hanged.')
        # self.display_word()
        # self.display_chances()
        self.player_guess.clear()
        self.correct_guess.clear()
        self.chances = 5
        self.pick_word()  # The target word
        self.choose()

    def choose(self):
        self.display_word()
        self.display_chances()
        choice = input('Do you want to choose a letter or guess? (l/g)\n')
        if choice == 'l':
            self.hint_letter()
            pass
        elif choice == 'g':
            self.guess()
        else:
            print('Pick one of the options.')
            # self.display_word()
            self.choose()

    def hint_letter(self):
        choice = input('Type your letter: ')
        if len(choice) > 1:
            print('You can only guess one letter at the time.\n')
            self.hint_letter()
        else:
            if choice in self.player_guess:
                print('You already guessed \'{}\'.\n'.format(choice))
                self.hint_letter()
            else:
                if choice in self.word:
                    print('Correct! the word has {} letter(s) \'{}\'.\n'.format(
                        self.word.count(choice), choice))
                    self.correct_guess.append(choice)
                    self.player_guess.append(choice)
                    self.solved()

                else:
                    print('Sorry, that letter is not in the word.\n')
                    self.player_guess.append(choice)
                    self.chances -= 1
                    # self.display_word()
                    # self.display_chances()
                    self.fail()

    def solved(self):
        counter = 0
        while counter < len(self.word):
            for c in self.word:
                if c not in self.correct_guess:
                    self.choose()
                else:
                    counter += 1
        else:
            self.win()

    def display_word(self):
        if len(self.correct_guess) == 0:
            print('_ ' * len(self.word))
        else:
            for c in self.word:
                if c in self.correct_guess:
                    print('{} '.format(c), end='')
                else:
                    print('_ ', end='')

    def display_chances(self):
        print('You have {} chances left.\n'.format(self.chances))

    def guess(self):
        guess = input('What is your guess: ')
        if guess == self.word:
            self.win()
        else:
            self.chances -= 1
            print('Sorry, but that\'s not it.\n')
            # self.display_chances()
            # self.display_word()
            self.fail()

    def fail(self):
        if self.chances <= 0:
            print('You\'ve been hanged. The word was: {} \n Better luck next '
                  'time\n'.format(self.word))
            self.again()
        else:
            self.choose()

    def again(self):
        choice = input('Want to go again? (y/n)\n')
        if choice == 'y':
            # self.__init__()
            self.start()
        else:
            exit()

    def win(self):
        print('Congratulations. You have guessed correctly the word \'{'
              '}\'.\n'.format(self.word))
        self.again()


if __name__ == '__main__':
    game = Hangman()
    game.start()
