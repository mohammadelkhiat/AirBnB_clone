#!/usr/bin/python3
"""here is the console that user should interact with"""

import cmd
import models.engine
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class defintion"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg, id):
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        elif id not in self.classes[arg]().id:
            print("** no instance found **")
        else:
            rtrn = models.storage.all()
            print(rtrn)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
