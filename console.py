'''
Author: Shobi Ola-Adisa
File:  console.py
Date: 2024-01-12
Description: console for AirBnB clone
'''
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    '''HBNBCommand class

    commands:
    quit - exit the program
    EOF - exit the program
    '''

    prompt = '(hbnb) '

    class_names = ('BaseModel')

    def do_help(self, arg: str) -> bool | None:
        '''Method to handle help command
        '''
        return super().do_help(arg)

    def emptyline(self) -> bool:
        '''Method to handle empty line
        '''
        pass

    def help_quit(self) -> None:
        '''Method to print help for quit command
        '''
        print("Quit command to exit the program")

    def do_quit(self, arg: str) -> bool:
        '''Method to handle quit command
        '''
        return True
    
    def do_EOF(self, arg: str) -> bool:
        '''Method to handle EOF
        '''
        return True
    
    # def precmd(self, line):
    #     '''Called on input lines before they are processed by onecmd
    #     '''
    #     line = line.strip()
    #     return(line)
    
    def do_show(self, line):
        '''Prints the string representation of an instance with the exact id

Example: (hbnb) show BaseModel 1234-1234-1234
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                    search_id = args[1].strip()
                    search_key = "{}.{}".format(class_name, search_id)
                    storage.reload()
                    obj_dict = storage.all()
                    if search_key in obj_dict.keys():
                        obj = obj_dict[search_key]
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id

Example: (hbnb) destroy BaseModel 1234-1234-1234
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                    search_id = args[1].strip()
                    search_key = "{}.{}".format(class_name, search_id)
                    storage.reload()
                    obj_dict = storage.all()
                    if search_key in obj_dict.keys():
                        storage.delete(search_key)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        '''Prints the string form of all instances of the specified class name

Example: (hbnb) all BaseModel
        '''
        class_name = line.strip()
        if class_name in HBNBCommand.class_names or line == "":
            obj_dict = storage.all()
            if line:
                obj_list = [str(item) for item in obj_dict.values()
                            if item.__class__.__name__ == class_name]
            else:
                obj_list = [str(item) for item in obj_dict.values()]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on a class name and id.
Usage: (hbnb) update <class name> <id> <attribute name> "<attribute value>"
        '''
        print(line)
        if ('{' in line and '}' in line):
            a_index = line.find('{')
            z_index = line.find('}')
            arg_dict = eval(line[a_index:z_index + 1])
            line = line[:a_index - 1]
            for key in arg_dict:
                self.do_update(f"{line} {key} {arg_dict[key]}")
            return
        args = line.split()
        if len(args) >= 1:
            class_name = args[0]
            if class_name in HBNBCommand.class_names:
                if len(args) >= 2:
                    instance_id = args[1]
                    obj_dict = storage.all()
                    key = f"{class_name}.{instance_id}"
                    if key in obj_dict.keys():
                        obj = obj_dict[key]
                        if len(args) >= 3:
                            attribute_name = args[2]
                            if len(args) >= 4:
                                value = args[3].replace('"', '').replace("'", "")                                
                                setattr(obj, attribute_name, value)
                                storage.new(obj)
                                obj.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_create(self, line: str) -> None:
        '''Creates a new instance of Object, saves it (to the JSON file) and prints the id

        Example: (hbnb) create BaseModel
        '''
        args = line.split()
        if len(args) != 1:
            print("** class name missing **")
        else:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                obj = eval(class_name)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
