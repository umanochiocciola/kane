import subprocess
import socket
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
LAST_CHECKED = DATE

version = '2.0.9.7.5'

sys_host = 'unknown'
if os.name == 'posix':
    monnezza = ';'
    cs = 'clear'
    sys_host = 'unix'
else:
    monnezza = '&'
    cs = 'cls'
    sys_host = 'win/DOS'

try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(f"Kane terminal {version}")
except:
    print(f"Kane terminal {version}")
print('\nPress fn+f11 to toggle fullscreen')

def webopen(tin):
    webbrowser.open(tin)
    
def cd_punto(tin):
    build = ''
    for boi in tin:
        if boi == '/':
            build = ''
        else:
            build += boi
    return(tin.replace('/' + build, ''))

root = directory = str(pathlib.Path().absolute()).replace('\\', '/')
passw = ''
elp = "Kane 2.0 terminal manual: \n list of internal commands\n   type wiki to get more information. \n\n start:  open a program \n quit: quit terminal \n web open a URL in browser\n !helpKane OR help:  get this list ;)\n cd: jump to a directoryectory\n directory OR ls: list files in the folder\nupgrade: Upgrade kane version\n man <command>: read further informations about a command\n While giving a path, you can use * to referr to the current directoryectory\n makedirectory <directory>: create a directoryectory at the specified path.\n py <python command>: execute python line\n home: jump to home user folder"

username = input('$ Username: ')
if os.path.exists(f'{directory}/usrs/{username}'):
    with open(f'{directory}/usrs/{username}/UserData.dat', 'rb') as f:
        passw, LAST_CHECKED = pk.load(f)
    if passw != '':
        while input(f'{username}\'s password: ') != passw:
            print('wrong password.\n')
        print('Welcome')
else:
    print('creating user...')
    os.makedirs(f'{directory}/usrs/{username}')
    with open(f'{directory}/usrs/{username}/UserData.dat', 'wb') as f:
        pk.dump([passw, LAST_CHECKED], f, protocol=2)

if LAST_CHECKED != DATE:
    print('+==================+')
    print('|Daily update check|')
    print('+==================+\n')
    
    fp = urllib.request.urlopen("https://raw.githubusercontent.com/umanochiocciola/kane/main/version.txt")
    mybytes = fp.read()
    fp.close()
    latest = str(mybytes.decode("utf8"))
    print(f'Your version: {version}')
    print(f'Latest version avaiable: {latest}\n')
    
    if version != latest: print('If you want to update, use the   upgrade   command')
    else: print('Congrats! You have the latest version')
    LAST_CHECKED = DATE

with open(f'{str(pathlib.Path().absolute())}/usrs/{username}/UserData.dat', 'wb') as f:
        pk.dump([passw, LAST_CHECKED], f, protocol=2)

InternalCommands = {
    'test': "print('it works!')",
    '!helpKane': "print(elp)",
    'help': "print(elp)",
    'scream': "scream()",
    'gimmeh comics': "import antigravity",
    'cake': "print('You really need me to tell you that EVERY cake is a lie?')",
    "spin!": "print('weeeeee')"
}

'''geeky stuff'''
def scream():
    try:
        print('\aWhoo')
    except:
        print("sorry, apparently this doesn't work on your main OS")

def invia_comandi(s, comando):
    s.send(comando.encode())
    data = s.recv(4096)
    print(data.decode())
    print("Killing connection...")
    s.close()

def conn_sub_server(indirizzo_server, richie):
    try:
        s = socket.socket()
        s.connect(indirizzo_server)
        print(f"Succesfully connected to { indirizzo_server }")
        invia_comandi(s, richie)
    except socket.error as errore:
        print(f"Connection error \n{errore}")
        
'''bicos ies'''

collegamenti = {}
dummy = ''
try:
    with open(f'shortcuts.dat', 'rb') as f:
        collegamenti, dummy = pk.load(f)
except: 0

user = backup = username

while True:
    if backup != username:
        print(f'User discrepancy detected: restoring last authorized user ({username})')
        backup = username
    if username != user:
        print(f'User discrepancy detected: restoring last authorized user ({backup})')
        user = username = backup

    directory = directory.replace('\\', '/')
    if 'usrs/' in directory and not user in directory:
        print(f"Access denied: property of {directory.replace(f'{root}/usrs', '')}")
        directory = f'{root}/usrs'
    
    command = input(directory + ' ## ' + user +'$~ ')
    if command == '': continue
    amand = command.split()
    prom = amand[0]
    
    if command == 'wiki':
        webopen('https://github.com/umanochiocciola/kane/wiki')
    
    elif command == 'quit' or command == '!quit':
        sys.exit()
    
    elif command in collegamenti:
        subprocess.call(collegamenti.get(command, 'echo fac?'), shell=True)
        
    elif prom == 'short':
        faccherini = amand[2].split(',')
        collegamenti.update({amand[1]: f'cd {faccherini[0]}{monnezza}{faccherini[1]}'})
        with open(f'shortcuts.dat', 'wb') as f:
            pk.dump([collegamenti, ''], f, protocol=2)
    
    elif prom == 'stream':
        try:
            if amand[1] == 'connect':
                indi = amand[2].split(':')
                indi.append(1000)
                conn_sub_server((indi[0], int(indi[1])), amand[3])
            elif amand[1] == 'serve':
                amand.append(1000)
                subprocess.call(f'python3 {amand[2]} {amand[3]}')
        except:
            print('correct usage: stream connect ip:port request\n') 
        
    
    elif prom == 'pkg':
        if ' install ' in command:
            requ = command.replace('pkg install ', '')
            subprocess.call(f"cd Pakages&git clone https://github.com/{requ}.git", shell = True)
    
    elif prom == 'lemmesee':
        for i in dir():
            if not 'elp' in i:
                if 'all' in command:
                    print(f'{i}: {globals()[i]}')
                elif not '__' in i and not 'function' in str(globals()[i]) and not 'module' in str(globals()[i]) and not 'InternalCommands' in i:
                    print(f'{i}: {globals()[i]}')
    
    elif prom == 'file':

        tg = amand[1]
        try:
            open(f'{directory}/{tg}', 'x')
            print(f'created {tg}')
        except:
            print('[Kane Error 3] unable to create file')
        continue
    
    elif prom == 'read':
        try:
            with open(f"{directory}/{command.replace('read ', '')}") as f:
                print(f.read())
        except:
            print(f"Unable to open {command.replace('read ', '')}")

    elif prom == 'start':
        try:
            os.startfile(directory + '/' + amand[1].replace('*', directory))
        except:
            try:
                os.startfile(amand[1].replace('*', directory))
            except:
                print('file not found')
    elif command == 'cs':
        subprocess.call(cs, shell=True)
    
    elif command == 'password' or command == 'pwd':
        print(f'Changing password for {user}')
        passw = input('$:>')
        with open(f'{directory}/usrs/{username}/UserData.dat', 'wb') as f:
            pk.dump([passw, LAST_CHECKED], f, protocol=2)
            print(f'saved succesfully!\n')
        
            
    elif prom == 'makedir':
        dar = amand[1]
        if not '/' in dar:
            dar = f'{directory}/{dar}'
        if not os.path.exists(dar):
            os.makedirs(dar)
            print(f'{dar} succesfully created!')
    
    elif command == 'home':
        directory = f'{str(pathlib.Path().absolute())}/usrs/{user}'
    
    elif prom == 'man':
        com = amand[1]
        try:
            man = open(f'Manual/{com}.txt', 'r')
            print(man.read())
            man.close()
        except:
            print(f'There\'s no manual for {com}')
        
    elif command == 'dir' or command == 'ls':
        for file in glob.glob(f'{directory}/*'):
            print(file.replace(f'{directory}', '').replace(directory.replace('/', '\\'), ''))
            
    elif prom == 'dir':
        arg = amand[1]
        for file in glob.glob(f'{directory}*.{arg}'):
            print(file.replace(f'{directory}', ''))
            
    elif prom == 'ls':
        arg = amand[1]
        for file in glob.glob(f'{directory}/*.{arg}'):
            print(file.replace(f'{directory}/', '').replace(directory.replace('/', '\\') + '/', ''))
            
    elif prom == 'web':
        we = amand[1]
        try:
            webopen(we)
            print(f'opening {we} ...')
        except:
            print('Unable to connect to the website, try to check internet connession')
            
    elif command == 'update':
        subprocess.call("pip install pygame", shell = True)
        
        try:
            with open('UserData.dat', 'wb') as f:
                pk.dump([passw, LAST_CHECKED], f, protocol=2)
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
            ghen = command.replace("cd ","").replace("*", directory)
            if os.path.exists(ghen):
                directory = ghen
            else:
                print(f'can\'t jump to {ghen} : directory doesn\'t exist')
        else:
            ghen = f'{directory}/{command.replace("cd ","").replace("*", directory)}'
            if os.path.exists(ghen):
                directory = ghen
            else:
                print(f'can\'t jump to {ghen} : directory doesn\'t exist')
            
    elif prom == 'py':
        try:
            exec(command.replace('py ', ''))
        except:
            print('\n\n+=====================================+\n')
            traceback.print_exc(limit=None, file=None, chain=True)
            print('\n+=====================================+\n')
    else:
        ab = InternalCommands.get(command, 'fuc')
        if ab == 'fuc':
            subprocess.call(f'cd {directory}{monnezza}{command}', shell=True)
        else:
            exec(InternalCommands.get(command, "print('Uknown Internal, directoryect or external command.')"))
    print('   ')

