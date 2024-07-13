import os
import random
import colorama
from colorama import Fore, Style
import pyfiglet
colorama.init(autoreset=True)

if os.path.exists('4letter'):
    print(Fore.GREEN + '[/] Config Folder Exists')
    print(Fore.GREEN + '[+] Continuing...')
else:
    print(Fore.GREEN + '[/] Creating Config Folder')
    os.mkdir('4letter')
    print(Fore.GREEN + '[+] Config Folder Created')

banner = pyfiglet.figlet_format('4letter', font='graffiti')
print(Fore.RED + banner)

def generate4lettername():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    name = ''
    for i in range(4):
        name += letters[random.randint(0, 25)]
    return name

rhead = input('Threads: ')

with open(os.path.join('4letter', 'generated.txt'), 'w') as f:
    for i in range(int(rhead)):
        name = generate4lettername()
        f.write(name + '\n')
        print(Fore.RED + f'[{i+1}]' + Fore.WHITE + ' Generated: ' + Fore.LIGHTBLACK_EX + name)