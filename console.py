#!/usr/bin/python3
""" contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """  command interpreter """
    prompt = "(hbnb)"

    def do_create(self, args):
        """Creates a new instance of the clase name given
        as an argument"""
        if args:
            try:
                new_instance = globals()[args]()
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")
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