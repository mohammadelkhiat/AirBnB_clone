#!/usr/bin/python3
"""here is the console that user should interact with"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class defintion"""
    PROMPT = "(hbnb)"

    def do_EOF(self, line):
        exit()

    def do_quit(self, line):
        exit()

    def emptyline(self):
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
