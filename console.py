'''
Author: Shobi Ola-Adisa
File:  console.py
Date: 2024-01-12
Description: console for AirBnB clone
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    HBNBCommand class

    commands:
    quit - exit the program
    EOF - exit the program
    '''

    prompt = '(hbnb) '

    def do_help(self, arg: str) -> bool | None:
        '''
        Method to handle help command
        '''
        return super().do_help(arg)

    def emptyline(self) -> bool:
        '''
        Method to handle empty line
        '''
        pass

    def help_quit(self) -> None:
        '''
        Method to print help for quit command
        '''
        print("Quit command to exit the program")

    def do_quit(self, arg: str) -> bool:
        '''
        Method to handle quit command
        '''
        return True
    
    def do_EOF(self, arg: str) -> bool:
        '''
        Method to handle EOF
        '''
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
