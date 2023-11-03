from colorama import Fore
import sys
import game
import os


def clear():
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system('clear')


if __name__ == '__main__':
    clear()
    print(f"""{Fore.RED}
██       ██████  ███    ██ ███████ ██   ██    ██              
██      ██    ██ ████   ██ ██      ██    ██  ██               
██      ██    ██ ██ ██  ██ █████   ██     ████                
██      ██    ██ ██  ██ ██ ██      ██      ██                 
███████  ██████  ██   ████ ███████ ███████ ██                 
                                                              
{Fore.CYAN}                                                            
███████ ██    ██ ██████  ██    ██ ██ ██    ██  █████  ██      
██      ██    ██ ██   ██ ██    ██ ██ ██    ██ ██   ██ ██      
███████ ██    ██ ██████  ██    ██ ██ ██    ██ ███████ ██      
     ██ ██    ██ ██   ██  ██  ██  ██  ██  ██  ██   ██ ██      
███████  ██████  ██   ██   ████   ██   ████   ██   ██ ███████ 
                                                              
                                                              """)
    
    print(f"{Fore.YELLOW}LonelySurvival  Copyright (C) 2023  MF366\n")
    input(f"{Fore.MAGENTA}Hit ENTER to start...{Fore.RESET}")
    game.start_point()
    