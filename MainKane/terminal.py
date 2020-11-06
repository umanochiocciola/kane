import subprocess
import sys
import pathlib
import webbrowser
import os
import glob
import pickle as pk
import traceback
import urllib.request
from datetime import date

today = date.today()
DATE = today.strftime("%d/%m/%Y")
LAST_CHACKED = DATE

version = '2.0.9.3'

try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"Kane terminal {version}")
except:
    print(f"Kane terminal {version}")
print('\nPress fn+f11 to toggle fullscreen')

def webopen(tin):
    webbrowser.open(tin, new=1)
    
def cd_punto(tin):
    build = ''
    for boi in tin:
        if boi == '/':
            build = ''
        else:
            build += boi
    return(tin.replace('/' + build, ''))

directory = str(pathlib.Path().absolute())
passw = ''
elp = "Kane 2.0 terminal manual: \n list of internal commands\n   type wiki to get more information. \n\n start:  open a program \n quit: quit terminal \n web open a URL in browser\n !helpKane OR help:  get this list ;)\n cd: jump to a directoryectory\n directory OR ls: list files in the folder\nupgrade: Upgrade kane version\n man <command>: read further informations about a command\n While giving a path, you can use * to referr to the current directoryectory\n makedirectory <directory>: create a directoryectory at the specified path.\n py <python command>: execute python line\n home: jump to home user folder"

username = input('$ Username: ')
if os.path.exists(f'{directory}/users/{username}'):
    with open(f'{directory}/users/{username}/UserData.dat', 'rb') as f:
        passw, LAST_CHACKED = pk.load(f)
    if passw != '':
        while input(f'{username}\'s password: ') != passw:
            print('wrong password.\n')
        print('Welcome')
else:
    print('creating user...')
    os.makedirs(f'{directory}/users/{username}')
    with open(f'{directory}/users/{username}/UserData.dat', 'wb') as f:
        pk.dump([passw, LAST_CHACKED], f, protocol=2)

if LAST_CHACKED != DATE:
    print('+==================+')
    print('|Daily update check|')
    print('+==================+\n')
    
    fp = urllib.request.urlopen("https://raw.githubusercontent.com/umanochiocciola/kane/main/version.txt")
    mybytes = fp.read()
    fp.close()
    latest = str(mybytes.decode("utf8"))
    print(f'Your version: {version}')
    print(f'Latest version avaiable: {latest}\n')
    
    print('If you want to update, use the   upgrade   command')

InternalCommands = {
    'test': "print('it works!')",
    '!helpKane': "print(elp)",
    'help': "print(elp)",
    'scream': "scream()",
    'gimmeh comics': "import antigravity",
    'cake': "print('You really need me to tell you that EVERY cake is a lie?')",
    "lemme see": "dir()",
    "spin!": "spin()"
}

'''geeky stuff'''
def scream():
    try:
        print('\aWhoo')
    except:
        print("sorry, apparently this doesn't work on your main OS")

def spin():
    print('weeeeee')
'''bicos ies'''

user = username

while True:
    directory = directory.replace('\\', '/')
    command = input(directory + ' ## ' + user +'$~ ')
    
    if command == '':
        continue
    
    elif command == 'wiki':
        webopen('https://github.com/umanochiocciola/kane/wiki')
    
    elif command == 'quit' or command == '!quit':
        sys.exit()
    
    elif 'pkg ' in command:
        if ' install ' in command:
            requ = command.replace('package install ', '')
            subprocess.call(f"cd Pakages&git clone https://github.com/{requ}.git", shell = True)
    
    elif 'file' in command:
        try:
            if command[0] + command[1] + command[2] + command[3] == 'file':
                tg = command.replace('file ', '')
                try:
                    open(f'{directory}/{tg}', 'x')
                    print(f'created {tg}')
                except:
                    print('[Kane Error 3] unable to create file')
                continue
        except:
            1+1
    
    if 'read ' in command:
        try:
            if command[0] + command[1] + command[2] + command[3] == 'read':
                with open(f"{directory}/{command.replace('read ')}") as f:
                    print(f.read())
        except:
            1+1
    
    elif 'start ' in command:
        try:
            os.startfile(directory + '/' + command.replace('start ', '').replace('*', directory))
        except:
            try:
                os.startfile(command.replace('start ', '').replace('*', directory))
            except:
                print('file not found')
    
    elif command == 'password' or command == 'pwd':
        print(f'Changing password for {user}')
        passw = input('$:>')
        with open(f'{directory}/users/{username}/UserData.dat', 'wb') as f:
            pk.dump([passw, LAST_CHACKED], f, protocol=2)
            print(f'saved succesfully!\n')
        
            
    elif 'makedir' in command:
        dar = command.replace('makedir ', '')
        if not '/' in dar:
            dar = f'{directory}/{dar}'
        if not os.path.exists(dar):
            os.makedirs(dar)
            print(f'{dar} succesfully created!')
    
    elif command == 'home':
        directory = f'{str(pathlib.Path().absolute())}/users/{user}'
    
    elif 'man ' in command:
        com = command.replace("man ","")
        try:
            man = open(f'Manual/{com}.txt', 'r')
            print(man.read())
            man.close()
        except:
            print(f'There\'s no manual for {com}')
        
    elif command == 'dir' or command == 'ls':
        for file in glob.glob(f'{directory}/*'):
            print(file.replace(f'{directory}', '').replace(directory.replace('/', '\\'), ''))
            
    elif 'dir ' in command:
        arg = command.replace('directory ', '')
        for file in glob.glob(f'{directory}*.{arg}'):
            print(file.replace(f'{directory}', ''))
            
    elif 'ls ' in command:
        arg = command.replace('ls ', '')
        for file in glob.glob(f'{directory}/*.{arg}'):
            print(file.replace(f'{directory}/', '').replace(directory.replace('/', '\\') + '/', ''))
            
    elif 'web ' in command:
        we = command.replace("web ", "")
        try:
            webopen(we)
            print(f'opening {we} ...')
        except:
            print('Unable to connect to the website, try to check internet connession')
            
    elif command == 'update':
        subprocess.call("pip install pygame", shell = True)
        
    elif command == 'username':
        print('KaneTerminal.setup: Insert username')
        user = input('$> ')
        if not os.path.exists(f'{str(pathlib.Path().absolute())}/users/{user}'):
            passw = '' 
            os.makedirs(f'{str(pathlib.Path().absolute())}/users/{user}')
            with open(f'{str(pathlib.Path().absolute())}/users/{user}/UserData.dat', 'wb') as f:
                pk.dump([passw, LAST_CHACKED], f, protocol=2)
                print(f'{user} folder created succesfully!!')
        else:
            with open(f'{str(pathlib.Path().absolute())}/users/{user}/UserData.dat', 'wb') as f:
                passw, LAST_CHACKED = pk.load(f)
        try:
            with open('UserData.dat', 'wb') as f:
                pk.dump([passw, LAST_CHACKED], f, protocol=2)
                print(f'saved succesfully!')
            if passw != '':
                if input(f'{user}\'s password: ') == passw:
                    print('Welcome!')
                else:
                    sys.exit()
        except:
            print('[Kane error 2]: Error while saving data. Please reboot Kane or install it again.')
        
    elif command == 'upgrade':
        print('installing new version on /kane')
        subprocess.call("git clone https://github.com/umanochiocciola/kane.git", shell = True)
        print('\nDone. Overwrite /kane/MainKane files on your MainKane folder.')
        
    elif 'cd' in command:
        if command.replace("cd","") == '..':
            directory = cd_punto(directory)
        elif '/' in command:
            directory = command.replace("cd ","").replace("*", directory)
        else:
            directory = f'{directory}/{command.replace("cd ","").replace("*", directory)}'
            
    elif len(command)>=2 and command[0] == 'p' and command[1] == 'y':
        try:
            exec(command.replace('py ', ''))
        except:
            print('\n\n+=====================================+\n')
            traceback.print_exc(limit=None, file=None, chain=True)
            print('\n+=====================================+\n')
    else:
        ab = InternalCommands.get(command, 'fuc')
        if ab == 'fuc':
            subprocess.call(f'cd {directory}&{command}', shell=True)
        else:
            exec(InternalCommands.get(command, "print('Uknown Internal, directoryect or external command.')"))
    print('   ')
