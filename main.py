from tools.keys import Keys
import time
from num2words import num2words
import colorama
from colorama import Fore, Back, Style
import inspect
from subprocess import call
import os
import platform
import keyboard
import json
import requests

colorama.init(convert=True, autoreset=True)

NUMBER_COLOR = Fore.MAGENTA
TEXT_COLOR = Fore.WHITE
ASCII_COLOR = Fore.MAGENTA

ERROR_COLOR = Fore.RED
INPUT_SUGGESTION_COLOR = Fore.CYAN
SUCCESS_COLOR = Fore.GREEN
INFORMATION_COLOR = Fore.YELLOW
keys = Keys()


def startup():
    """
    Prints all utility functions to the console
    """

    print(f"""
{ASCII_COLOR}     _                        _             _    _  _  _  _    _          
{ASCII_COLOR}  __| | __ _  _ _  ___  __ _ | | ___  _  _ | |_ (_)| |(_)| |_ (_) ___  ___
{ASCII_COLOR} / _` |/ _` || '_|/ -_)/ _` || |(_-< | || ||  _|| || || ||  _|| |/ -_)(_-<
{ASCII_COLOR} \__,_|\__,_||_|  \___|\__,_||_|/__/  \_,_| \__||_||_||_| \__||_|\___|/__/                                     
    """)

    string = ''''''
    functions = inspect.getmembers(Utilities, predicate=inspect.isfunction)
    system = platform.system()

    index = 1
    for function in functions:
        string += f' {NUMBER_COLOR}[{index}] {TEXT_COLOR}{function[0].replace("_", " ").title()}  '
        index += 1

    print(string)
    print()
    
    if ERROR:
        print(ERROR)
    
    print(f'{INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} Select a tool')
    tool = input(' >>> ')
    try:
        tool = int(tool)
    except:
        os.system('cls') if system.lower() == 'windows' else os.system('clear')
        return f'{ERROR_COLOR} [!] You must enter a number'

    # try:
    global SUB_ERROR
    SUB_ERROR = None
    while True:
        SUB_ERROR = getattr(Utilities, functions[tool-1][0])()
        if not SUB_ERROR:
            time.sleep(1)
            break
        
    # except:
    #     os.system('cls') if system.lower() == 'windows' else os.system('clear')
    #     return f'{ERROR_COLOR} [!] An error occured'

    os.system('cls') if system.lower() == 'windows' else os.system('clear')


def get_help(function_name):
    getattr(Utilities, function_name).__doc__.strip()


class Utilities:
    
    @staticmethod
    def jumping_jacks():
        """
         Automatically does jumping jacks on roblox based on certain set peramiters
        """
        if SUB_ERROR:
            print()
            print(SUB_ERROR)

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} How many JJ's?")
        num_of_jjs = input('  |  >>> ')

        try:
            num_of_jjs = int(num_of_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if num_of_jjs == 0 or str(num_of_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} Starting number?")
        starting_jjs = input('  |  >>> ')
        try:
            starting_jjs = int(starting_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if starting_jjs == 0 or str(starting_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print()

        s = 3
        while True:
            print(f'{INFORMATION_COLOR}  | Starting in {s} seconds - Ensure you make the game window the primary window\r', end='')
            time.sleep(1)
            s -= 1

            if s == 0:
                print()
                print(f'{INFORMATION_COLOR}  | Started...')
                break
        
        print()
        print()
        while True:
            count = num2words(starting_jjs).upper()

            with open('config.json', 'r') as file:
                data = json.load(file)["interval_by_seconds"]

            keyboard.write('/')
            for letter in count:
                if starting_jjs <= 10:
                    wait = data["less_than_or_equal_to_10"]
                elif starting_jjs > 10 and starting_jjs <= 20:
                    wait = data["less_than_or_equal_to_20"]
                elif starting_jjs > 20:
                    wait = data["more_than_20_less_than_100"]
                if starting_jjs > 100:
                    wait = data["more_than_100"]

                time.sleep(wait)
                keyboard.write(letter)
                time.sleep(wait) 

            keyboard.write('\n')

            keys.directKey('SPACE')
            time.sleep(0.05)
            keys.directKey("SPACE", keys.key_release) 

            print(f'{SUCCESS_COLOR}  |  {starting_jjs}/{num_of_jjs}\r', end='')
            starting_jjs += 1
            if starting_jjs == num_of_jjs + 1:
                print(f'{SUCCESS_COLOR}  |  [+] {starting_jjs-1}/{num_of_jjs}')
                break
        return

    @staticmethod
    def hell_jacks():
        if SUB_ERROR:
            print()
            print(SUB_ERROR)

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} How many HJ's?")
        num_of_jjs = input('  |  >>> ')

        try:
            num_of_jjs = int(num_of_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if num_of_jjs == 0 or str(num_of_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} Starting number?")
        starting_jjs = input('  |  >>> ')
        try:
            starting_jjs = int(starting_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if starting_jjs == 0 or str(starting_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print()

        s = 3
        while True:
            print(f'{INFORMATION_COLOR}  | Starting in {s} seconds - Ensure you make the game window the primary window\r', end='')
            time.sleep(1)
            s -= 1

            if s == 0:
                print()
                print(f'{INFORMATION_COLOR}  | Started...')
                break
        
        print()
        print()
        while True:
            count = num2words(starting_jjs).upper()

            with open('config.json', 'r') as file:
                data = json.load(file)

            for letter in count:
                keyboard.write('/')
                time.sleep(0.05)
                keyboard.write(letter)
                time.sleep(0.1)
                keyboard.write('\n')
                time.sleep(data["interval_after_sending_single_helljack_letter"])
                keys.directKey('SPACE')
                time.sleep(0.05)
                keys.directKey("SPACE", keys.key_release) 

            interval_by_seconds = data["interval_by_seconds"]

            keyboard.write('/')
            for letter in count:
                if starting_jjs <= 10:
                    wait = interval_by_seconds["less_than_or_equal_to_10"]
                elif starting_jjs > 10 and starting_jjs <= 20:
                    wait = interval_by_seconds["less_than_or_equal_to_20"]
                elif starting_jjs > 20:
                    wait = interval_by_seconds["more_than_20_less_than_100"]
                if starting_jjs > 100:
                    wait = interval_by_seconds["more_than_100"]

                time.sleep(wait)
                keyboard.write(letter)
                time.sleep(wait) 

            keyboard.write('\n')

            keys.directKey('SPACE')
            time.sleep(0.05)
            keys.directKey("SPACE", keys.key_release) 

            print(f'{SUCCESS_COLOR}  |  {starting_jjs}/{num_of_jjs}\r', end='')
            starting_jjs += 1
            if starting_jjs == num_of_jjs + 1:
                print(f'{SUCCESS_COLOR}  |  [+] {starting_jjs-1}/{num_of_jjs}')
                break
        return

    @staticmethod
    def grammar_jacks():
        if SUB_ERROR:
            print()
            print(SUB_ERROR)

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} How many GJ's?")
        num_of_jjs = input('  |  >>> ')

        try:
            num_of_jjs = int(num_of_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if num_of_jjs == 0 or str(num_of_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} Starting number?")
        starting_jjs = input('  |  >>> ')
        try:
            starting_jjs = int(starting_jjs)
        except:
            return f'{ERROR_COLOR}  |  [!] You must enter a number'

        if starting_jjs == 0 or str(starting_jjs)[0] == '-':
            return f'{ERROR_COLOR}  |  [!] You must enter a valid number'

        print()

        s = 3
        while True:
            print(f'{INFORMATION_COLOR}  | Starting in {s} seconds - Ensure you make the game window the primary window\r', end='')
            time.sleep(1)
            s -= 1

            if s == 0:
                print()
                print(f'{INFORMATION_COLOR}  | Started...')
                break
        
        print()
        print()
        while True:
            count = num2words(starting_jjs).title() + '.'

            with open('config.json', 'r') as file:
                data = json.load(file)["interval_by_seconds"]

            keyboard.write('/')
            for letter in count:
                if starting_jjs <= 10:
                    wait = data["less_than_or_equal_to_10"]
                elif starting_jjs > 10 and starting_jjs <= 20:
                    wait = data["less_than_or_equal_to_20"]
                elif starting_jjs > 20:
                    wait = data["more_than_20_less_than_100"]
                if starting_jjs > 100:
                    wait = data["more_than_100"]

                time.sleep(wait)
                keyboard.write(letter)
                time.sleep(wait) 

            keyboard.write('\n')

            keys.directKey('SPACE')
            time.sleep(0.05)
            keys.directKey("SPACE", keys.key_release) 

            print(f'{SUCCESS_COLOR}  |  {starting_jjs}/{num_of_jjs}\r', end='')
            starting_jjs += 1
            if starting_jjs == num_of_jjs + 1:
                print(f'{SUCCESS_COLOR}  |  [+] {starting_jjs-1}/{num_of_jjs}')
                break
        return

    # @staticmethod
    # def rank_checker():
    #     print(f"  | {INPUT_SUGGESTION_COLOR} [NUM] {Fore.RESET} Please enter the username")
    #     username = input('  |  >>> ')

    #     data = {
    #     "usernames": [
    #         f"{username}"
    #     ],
    #     "excludeBannedUsers": True
    #     }

    #     response = requests.post(f'https://users.roblox.com/v1/usernames/users', data=data)
    #     json = response.json()

    #     if not json['data']:
    #         return f'{ERROR_COLOR}  |  [!] You must enter a valid username'

    #     userid = json['Id']
    
    #     response = requests.get(url=f'https://groups.roblox.com/v2/users/{userid}/groups/roles')

    #     print(response)



global ERROR
ERROR = None
while True:
    ERROR = startup()


