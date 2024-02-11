#!/usr/bin/python3
"""here is the console that user should interact with"""

import cmd
import models.engine


class HBNBCommand(cmd.Cmd):
    """class defintion"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
