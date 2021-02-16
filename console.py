#!/usr/bin/python3
""" contains the entry point of the command interpreter"""


import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """  command interpreter """
    prompt = "(hbnb)"

    def do_create(self, args):
        """Creates a new instance of the clase name given
        as an argument"""
        if args:
            args = shlex.split(args)
            try:
                new_instance = globals()[args[0]]()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """  Prints the string representation of an instance
        based on the class name and id
        """
        if args:
            args = shlex.split(args)
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args)<2:
                print("** instance id missing **")
            else:
                dict_show = storage.all()
                key = args[0]+"."+args[1]
                if key in dict_show:
                    print(dict_show[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if args:
            args = shlex.split(args)
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args)<2:
                print("** instance id missing **")
            else:
                key = args[0]+"."+args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def emptyline(self):
        """No realiza ninguna accion
        """
        pass

    def do_EOF(self, line):
        """ Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True

"""inicio del programa"""
if __name__ == '__main__':
    import sys
    interprete = HBNBCommand()
    if len(sys.argv) > 1: # activa el modo no interactivo
        interprete.onecmd(' '.join(sys.argv[1:]))
    else:
        interprete.cmdloop() # modo interactivo