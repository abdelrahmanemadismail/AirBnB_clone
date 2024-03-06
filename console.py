#!/usr/bin/python3
"""
Module for the HBNB command interpreter.
"""


import cmd



class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
