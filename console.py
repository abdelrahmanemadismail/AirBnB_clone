#!/usr/bin/python3
"""
Module for the HBNB command interpreter.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """

    prompt = "(hbnb) "
    classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]

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
            print([
                str(obj)
                for key, obj in storage.all().items()
                if key.split('.')[0] == arg
                ])

    def do_update(self, arg):
        """
        Update an instance based on class name and id.

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

    def default(self, line):
        """
        Override the default method to handle unrecognized commands.
        """
        parts = line.split('.')
        if len(parts) == 2:
            class_name = parts[0]
            method = parts[1].split('(')
            if class_name in self.classes:
                instances = storage.all()
                class_instances = [
                        str(obj)
                        for obj in instances.values()
                        if type(obj).__name__ == class_name
                        ]
                if method[0] == 'all':
                    print(class_instances)
                elif method[0] == 'count':
                    print(len(class_instances))

                elif method[0] == 'show':
                    if len(method) == 2:
                        arg = method[1].strip(')').strip('"').strip("'")
                    else:
                        arg = None
                    self.do_show(f"{class_name} {arg}")

                elif method[0] == 'destroy':
                    if len(method) == 2:
                        arg = method[1].strip(')').strip('"').strip("'")
                    else:
                        arg = None
                    self.do_destroy(f"{class_name} {arg}")

                elif method[0] == 'update':
                    if len(method) == 2:
                        arg = method[1].strip(')').strip('"').strip("'")
                        args = arg.strip(" ").replace(',', ' ')
                    else:
                        arg = None
                        args = None
                    self.do_update(f"{class_name} {args}")
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
