#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter for the AirBnB clone.
"""

import cmd
from models import storage  # Import the storage instance
from models.base_model import BaseModel  # Import BaseModel class
from models.user import User  # Import the User model

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)."""
        print()  # To ensure the prompt exits cleanly
        return True

    def emptyline(self):
        """Override the emptyline method to do nothing on an empty input line."""
        pass

    def do_create(self, class_name):
        """Creates a new instance of a given class, saves it, and prints its id."""
        if not class_name:
            print("** class name missing **")
        elif class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            if class_name == "BaseModel":
                new_instance = BaseModel()
            elif class_name == "User":
                new_instance = User()  # Create a new User instance
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Shows the string representation of an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(instance_key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            if instance_key in storage.all():
                del storage.all()[instance_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, class_name=""):
        """Prints all string representations of instances of a given class or all classes."""
        if class_name and class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            instances = [
                str(instance) for key, instance in storage.all().items()
                if not class_name or key.startswith(class_name + ".")
            ]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f"{args[0]}.{args[1]}"
            instance = storage.all().get(instance_key)
            if instance is None:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(instance, attr_name, attr_value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
