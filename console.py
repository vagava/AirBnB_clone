#!/usr/bin/python3
""" contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """  command interpreter """
    prompt = "(hbnb)"


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
    interprete.cmdloop() 