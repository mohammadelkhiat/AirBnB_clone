#!/usr/bin/python3
"""here is the console that user should interact with"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class defintion"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
