"""
Project name: Architecture Simulator
Author: Tom DIZDAREVIC & Thibaut MENIN
Desc: This file is the main project file. It contains the main menu and the main functions.
"""
from utils.Color import Color
from ISA import execute

def welcome():
    """
    Welcome message of our program
    """

    print(Color.GRAY.value)
    print("##################################################################################################")
    print("# ░█████╗░██████╗░░█████╗░██╗░░██╗██╗████████╗███████╗░█████╗░████████╗██╗░░░██╗██████╗░███████╗ #")
    print("# ██╔══██╗██╔══██╗██╔══██╗██║░░██║██║╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔════╝ #")
    print("# ███████║██████╔╝██║░░╚═╝███████║██║░░░██║░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝█████╗░░ #")
    print("# ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░░░██║░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░ #")
    print("# ██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░░██║░░░███████╗╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗ #")
    print("# ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝ #")
    print("#                                                                                                #")
    print("#            ░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░            #")
    print("#            ██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗            #")
    print("#            ╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝            #")
    print("#            ░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗            #")
    print("#            ██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║            #")
    print("#            ╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝            #")
    print("##################################################################################################\n")

def command_center(command:int=0) -> bool:
    """
    +-------------------+
    |---- Main Menu ----|
    +-------------------+

    This is the main menu.
    Choices available
    1. See the operations step by step
    2. See all the operations in one time
    3. Exit program
    """
    def print_menu():
        commandes = {1: f"{Color.WHITE.value}See the operations step by step", 2: f"{Color.WHITE.value}See all the operations in one time", 3: f"{Color.WHITE.value}Exit Program"}
        print(f"{Color.BLUE.value}1 - {commandes[1]}\n{Color.BLUE.value}2 - {commandes[2]}\n{Color.BLUE.value}3 - {commandes[3]}")
    
    print_menu()

    while command != 3:
        try:
            command = int(input(f"\n{Color.GREEN.value}Your choice: {Color.WHITE.value}"))
        except ValueError:
            command = 0
        
        print(f"{Color.RESET.value}", end="")

        if command == 1:
            if display_step_by_step():
                command = 0

        elif command == 2:
            if display_all_in_one():
                command = 0
        
        

        elif command == 3:
            for _ in range(0, 50):
                print("\n")
            print(Color.GREEN.value + "Exiting. Thank you for using our program! :)" + Color.RESET.value)
            return True

        print_menu()

    return True


def display_step_by_step(command: int = 1) -> bool:
    """
    A specific menu who display step by step in the terminal
    Display the next instruction and ask the user to press enter or space to continue
    """

    for _ in range(0, 50):
        print("\n")

    print("###       You choose to display the operations step by step.  ###\n"
          "###        Press enter to continue to the next instruction.   ###\n")

    execute(step=True)

    return True


def display_all_in_one(command:int=0):
    """
    A specific menu who display all action in one step in the terminal
    """

    print("###      You choose to display all the operations in one time.      ###\n")
    
    execute(step=False)
    
    return True


if __name__ == '__main__':
    welcome()
    command_center()
