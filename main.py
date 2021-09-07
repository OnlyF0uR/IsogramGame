# Imports
import tkinter as tk
from enum import Enum

# Little config section
TRIES_AMOUNT = 15
LETTER_AMOUNT = 5


# Enum for outcomes of the word validation process
class StatusType(Enum):
    NO_TRIES_LEFT = 1
    INCORRECT_LETTER_AMOUNT = 2
    NOT_AN_ISOGRAM = 3
    VALID_ISOGRAM = 4


class GameHandler:
    # Constructor
    def __init__(self):
        self.triesLeft = TRIES_AMOUNT
        # IDEA: Add spellchecking from pyEnchant or something

    # Check if a word is valid and returns
    def validate_word(self, wrd):
        """
        :param wrd: The word that needs to be checked
        :type wrd: str
        :return: a StatusType enum corresponding to the outcome of the checks
        """
        # Check if there are zero tries left
        if self.triesLeft == 1:
            self.triesLeft = TRIES_AMOUNT
            return StatusType.NO_TRIES_LEFT

        # Subtract a try
        self.triesLeft = self.triesLeft - 1

        if len(wrd) == LETTER_AMOUNT:
            # Loop through the characters
            for char in wrd:
                # Check if there is a digit and if the letter occurs more then once
                if char.isdigit() or wrd.count(char) > 1:
                    return StatusType.NOT_AN_ISOGRAM

            self.triesLeft = TRIES_AMOUNT
            return StatusType.VALID_ISOGRAM
        else:
            return StatusType.INCORRECT_LETTER_AMOUNT


# Should be instantiated once
class WindowHandler:
    def __init__(self):
        # Instantiate classes
        self.game_handler = GameHandler()
        window = tk.Tk()

        window.title('Isogram Game')
        window.geometry('500x300')

        info_frame = tk.LabelFrame(window, text='Information')
        info_frame.pack(expand=True, fill=tk.BOTH)

        # Label with some text that will show up in the information frame
        tk.Label(info_frame, text='\nAn isogram is a word in which each letter appears only once.\n'
                                  'You have a number of chances to enter a word that complies with the rules.\n\nRules:'
                                  '\n- Amount of tries: ' + str(TRIES_AMOUNT) + '\n- Amount of letters: ' + str(LETTER_AMOUNT) + '').pack()

        input_frame = tk.LabelFrame(window, text='Input')
        input_frame.pack(expand=True, fill=tk.BOTH)

        self.status_text = tk.StringVar()
        self.status_text.set('Enter a word... (' + str(TRIES_AMOUNT) + ' tries left)')
        tk.Label(input_frame, textvariable=self.status_text).pack()

        word = tk.StringVar()
        word_enter = tk.Entry(input_frame, textvariable=word)
        word_enter.pack()

        button = tk.Button(input_frame, text='Controleren', command=lambda: self.__handleclick__(word.get()))
        button.pack()

        window.mainloop()

    def __handleclick__(self, word):
        res = self.game_handler.validate_word(word)
        if res == StatusType.NO_TRIES_LEFT:
            self.status_text.set('No tries left :(')
        elif res == StatusType.INCORRECT_LETTER_AMOUNT:
            self.status_text.set('Amount of letters does not match, ' + str(self.game_handler.triesLeft) + ' tries left.')
        elif res == StatusType.NOT_AN_ISOGRAM:
            self.status_text.set('That is not an isogram, ' + str(self.game_handler.triesLeft) + ' tries left.')
        elif res == StatusType.VALID_ISOGRAM:
            self.status_text.set('Well done, that is an isogram!')


if __name__ == "__main__":
    WindowHandler()
