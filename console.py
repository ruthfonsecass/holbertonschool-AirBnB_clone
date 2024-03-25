#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import user
from models.place import place
from models.state import state
from models.city import city
from models.amenity import amenity
from models.review import review
import sys
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes = {"BaseModel": base_model, "Amenity": amenity,
                "City": city, "Place": place,
                "Review": review, "State": state, "User": user}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    
    def do_create(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instance = self.classes[args[0]]()
            instance.save()
            print(instance.id)


    def do_show(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])


    def do_destroy(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


    def do_all(self, line):
        args = line.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for key, obj in storage.all().items():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    
    def do_update(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instance = storage.all()[key]
            setattr(instance, args[2], args[3])
            instance.save()


    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        


    def show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
