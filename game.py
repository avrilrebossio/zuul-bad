from room import Room
from command_parser import Parser


class Game:

    def __init__(self):
        self.createRooms()
        self.parser = Parser()

    def createRooms(self):
        outside = Room("outside the main entrance of the university")
        theater = Room("in a lecture theater")
        pub = Room("in the campus pub")
        lab = Room("in a computing lab")
        office = Room("in the computing admin office")

        outside.setExits(None, theater, lab, pub)
        theater.setExits(None, None, None, outside)
        pub.setExits(None, outside, None, None)
        lab.setExits(outside, office, None, None)
        office.setExits(None, None, None, lab)

        self.currentRoom = outside

        return

    def play(self):
        self.printWelcome()

        finished = False
        while(not finished):
            command = self.parser.getCommand()
            finished = self.processCommand(command)
        print("Thank you for playing.  Good bye.")

    def printWelcome(self):
        print()
        print("Welcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.")
        print("")
        print("You are " + self.currentRoom.getDescription())
        print("Exits: ")
        if(self.currentRoom.northExit is not None):
            print("north ")
        if(self.currentRoom.eastExit is not None):
            print("east ")
        if(self.currentRoom.southExit is not None):
            print("south ")
        if(self.currentRoom.westExit is not None):
            print("west ")
        print()

    def processCommand(self, command):
        want_to_quit = False

        if(command.isUnknown()):
            print("I don't know what you mean...")
            return False

        command_word = command.getCommandWord()
        if(command_word == "help"):
            self.printHelp()
        elif(command_word == "go"):
            self.goRoom(command)
        elif(command_word == "quit"):
            want_to_quit = self.quit(command)

        return want_to_quit

    def printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.")
        print()
        print("Your command words are:")
        print("   go quit help")

    def goRoom(self, command):
        if(not command.hasSecondWord()):
            print("Go where?")
            return

        direction = command.getSecondWord()
        next_room = None
        if direction == "north":
            next_room = self.currentRoom.northExit
        if direction == "east":
            next_room = self.currentRoom.eastExit
        if direction == "south":
            next_room = self.currentRoom.southExit
        if direction == "west":
            next_room = self.currentRoom.westExit

        if next_room is None:
            print("There is no door!")
        else:
            self.currentRoom = next_room
            print("You are " + self.currentRoom.getDescription())
            print("Exits: ")
            if(self.currentRoom.northExit is not None):
                print("north ")
            if(self.currentRoom.eastExit is not None):
                print("east ")
            if(self.currentRoom.southExit is not None):
                print("south ")
            if(self.currentRoom.westExit is not None):
                print("west ")
            print()

    def quit(self, command):
        if(command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True


game = Game()
game.play()
