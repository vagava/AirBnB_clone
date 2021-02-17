#!/usr/bin/python3
""" contains the entry point of the command interpreter"""


import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import amenity
from models.city import city
from models.place import place
from models.review import review
from models.state import state


class HBNBCommand(cmd.Cmd):
    """  command interpreter """
    prompt = "(hbnb) "

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

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""
        list_all=[]
        if args:
            args = shlex.split(args)
            if args[0] in globals():
                for key, value in storage.all().items():
                    if value.__class__.__name__== args[0]:
                        list_all.append(value.__str__())
                print(list_all)
            else:
                print("** class doesn't exist **")
        else:
            for element in storage.all().values():
                list_all.append(element.__str__())
            print(list_all)

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute """
        if args:
            args = shlex.split(args)
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args)<2:
                print("** instance id missing **")
            elif args[0]+'.'+args[1] not in storage.all():
                print("** no instance found **")
            elif len(args)<3:
                print("** attribute name missing **")
            elif len(args)<4:
                print("** value missing **")
            else:
                key=args[0]+'.'+args[1]
                obj = storage.all()[key]
                obj.__dict__[args[2]] = args[3]
                obj.save()
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
    interprete = HBNBCommand()
    interprete.cmdloop() # modo interactivo
