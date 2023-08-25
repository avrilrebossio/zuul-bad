from commandwords import CommandWords
from command import Command


class Parser:
    def __init__(self):
        self.commands = CommandWords()

    def getCommand(self):
        word1 = None
        word2 = None

        input_line = input("> ")
        text = input_line.split(' ')
        if len(text) > 0:
            word1 = text[0]
            if len(text) > 1:
                word2 = text[1]

        if(self.commands.isCommand(word1)):
            return Command(word1, word2)
        else:
            return Command(None, word2)
