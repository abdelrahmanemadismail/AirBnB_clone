#!/usr/bin/python3
"""
Module for the HBNB command interpreter.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User



class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.

        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance.

        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.

        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """
        Print all string representation of all instances.

        Usage: all [<class_name>]
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in storage.all().items() if key.split('.')[0] == arg])

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attribute.

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
