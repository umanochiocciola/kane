import modules_check
print('loading components...')
import subprocess
import socket
import sys
import pathlib
import webbrowser
import os, shutil
import glob
import pickle as pk
import traceback
import urllib.request
from urllib.request import urlopen
import urllib
from datetime import date
import Encription as enc
import threading as thr
import colorama
from termcolor import colored

today = date.today()
DATE = today.strftime("%d/%m/%Y")
LAST_CHECKED = DATE

version = '2.0.9.8'

sys_host = 'unknown'
if os.name == 'posix':
    monnezza = ';'
    cs = 'clear'
    sys_host = 'unix'
else:
    monnezza = '&'
    cs = 'cls'
    sys_host = 'win/DOS'

subprocess.call(cs, shell=True)

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

if __name__ == '__main__':
    username = input('$ Username: ')
    if os.path.exists(f'{directory}/usrs/{username}'):
        with open(f'{directory}/usrs/{username}/UserData.dat', 'rb') as f:
            passw, LAST_CHECKED = pk.load(f)
            passw = enc.decript(passw, 12)
        if passw != '':
    # NAISSSS
            while input(f'{username}\'s password: ') != passw:
                print('wrong password.\n')
            print('Welcome')
    else:
        print('creating user...')
        os.makedirs(f'{directory}/usrs/{username}')
        with open(f'{directory}/usrs/{username}/UserData.dat', 'wb') as f:
            pk.dump([enc.encript(passw, 12), LAST_CHECKED], f, protocol=2)



    if LAST_CHECKED != DATE:
        print('+==================+')
        print('|Daily update check|')
        print('+==================+\n')
        
        fp = urllib.request.urlopen("https://raw.githubusercontent.com/umanochiocciola/kane/main/version.txt")
        mybytes = fp.read()
        fp.close()
        latest = mybytes.decode("utf8").replace('\n', '')
        print(f'Your version: {version}')
        print(f'Latest version avaiable: {latest}\n')
        
        if version != latest: print('If you want to update, use the   upgrade   command')
        else: print('Congrats! You have the latest version')
        LAST_CHECKED = DATE

    with open(f'{str(pathlib.Path().absolute())}/usrs/{username}/UserData.dat', 'wb') as f:
            pk.dump([enc.encript(passw, 12), LAST_CHECKED], f, protocol=2)

else: username='external'

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
def dirlist(folder):
    webopen('file:///'+folder)

def priv_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return(ip)

def pub_ip():
    import re
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return(re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1))

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

################################################################
'''                 Config                      '''

attributes = {}


try:
    with open('sysconfig.conf', 'r') as f:
        for i in f.readlines():
            try: exec(f'attributes.update({i})')
            except:
                try: exec(i)
                except:
                    try: pull(i, ARGS)
                    except: 0

except:
    print('error while opening sysconfig.conf')
    with open('sysconfig.conf', 'x') as f:
        f.write("# edit this to configurate your kane os{'show_stderr': 1}{'do_input_log': 1}{'max_threads': 10}{'deamon_stdout': 1}{'deamon_stderr': 0}")
    attributes.update({'show_stderr': 0, 'do_input_log': 0, 'max_threads': 10, 'deamon_stdout': 1, 'deamon_stderr': 0})
    
################################################################

class NiceLittleOutput:
    def __init__(self, stdout, stderr, stdcolor):
        self.stdout = stdout
        self.stderr = stderr
        self.stcolor = stdcolor

deamons = []
playground = {}

def pull(command, ARGS, isdeamon=0):
    global directory, playground
    STDOUT = []
    STDERR = []
    stdout_color = ['white', 'on_grey']
    
    backup, username, user, deamons, collegamenti, attributes, InternalCommands, passw, LAST_CHECKED, elp, root, sys_host, cs, monnezza = ARGS
    
    for deam in deamons:
        if not deam.is_alive():
            deamons.remove(deam)
        
    for matteobandiera in [0]:
        if backup != username:
            STDOUT.append(f'User discrepancy detected: restoring last authorized user ({username})')
            backup = username
        if username != user:
            STDOUT.append(f'User discrepancy detected: restoring last authorized user ({backup})')
            user = username = backup

        directory = directory.replace('\\', '/')
        if 'usrs/' in directory and not user in directory:
            STDOUT.append(f"Access denied: property of {directory.replace(f'{root}/usrs', '')}")
            directory = f'{root}/usrs'

        if command == '': continue
        amand = command.split()
        for i in amand: i = i.replace('_', ' ')
        prom = amand[0]
        
        
        if attributes.get('do_input_log', 0):
            with open('input_log', 'a') as f:
                f.write(f'{command}\n')
        
        if command == 'wiki':
            webopen('https://github.com/umanochiocciola/kane/wiki')
        
        elif command == 'quit' or command == '!quit':
            sys.exit()
        
        elif command in collegamenti:
            subprocess.call(collegamenti.get(command, 'echo fac?'), shell=True)
        
        elif prom == 'rename':
            if len(amand) < 3:
                STDERR.append('error: rename:\nUsage: rename OLD NEW')
            else:
                os.rename(amand[1], amand[2])
        
        
        elif prom == 'pg':
            if len(amand) == 1: print(playground)
            elif amand[1] == 'clear': playground = {}
            elif amand[1] == 'new':
                if amand[3] == 'list': obj = []
                elif amand[3] == 'dict': obj = {}
                elif amand[3] == 'py': obj = exec(amand[4])
                else: obj = amand[3]
                playground.update({amand[2]: obj})
            elif amand[1] == 'play':
                print(pull(playground.get(amand[2], 'py print("It doesn\'t exist")'), (backup, username, user, deamons, collegamenti, attributes, InternalCommands, passw, LAST_CHECKED, elp, root, sys_host, cs, monnezza), isdeamon=0).stdout)
            elif amand[1] == 'exec':
                for i in playground[amand[2]]: print(pull(i, (backup, username, user, deamons, collegamenti, attributes, InternalCommands, passw, LAST_CHECKED, elp, root, sys_host, cs, monnezza), isdeamon=0).stdout)
            elif amand[1] == 'read':
                print(playground.get(amand[2], 'no.'))
            elif amand[1] == 'app':
                playground[amand[2]].append(amand[3])
            elif amand[1] == 'rm':
                playground.update({amand[2]: None})
        
        elif prom == 'rm':
            if amand[1] == '-d':
                shutil.rmtree(f'{directory}/{amand[2]}')
            else:
                poe = f'{directory}/{amand[1]}'
                if os.path.exists(poe):
                    os.remove(poe)
                else:
                    print(f"{amand[2]} doesn't exist")
        
        elif prom == 'deamon':
            if len(deamons) <= attributes.get('max_threads', 10):
                deamons.append(thr.Thread(target = pull, args=(command.replace('demon ', ''), backup, username, user, deamons, collegamenti, attributes, InternalCommands, passw, LAST_CHECKED, elp, root, directory, sys_host, cs, monnezza, 1)))
                deamons[len(deamons)-1].start()
            else:
                print('Max thread count reached. To cahnge this edit max_threads in sysconfig.conf')
        
        elif command == 'dirlist': dirlist(directory)
        
        elif command == 'ip':
            STDOUT.append(f'basic ip informations:\nlocalhost:\t127.0.0.1\nprivate ip:\t{priv_ip()}\npublic ip:\t{pub_ip()}')
        
        elif prom == 'short':
            faccherini = command.replace('short ', '').replace(amand[1]+' ', '').split(',')
            collegamenti.update({amand[1]: f'cd {faccherini[0]}{monnezza}{faccherini[1]}'})
            with open(f'shortcuts.dat', 'wb') as f:
                pk.dump([collegamenti, ''], f, protocol=2)
        
        elif prom == 'stream':
            try:
                if amand[1] == 'connect':
                    indi = amand[2].split(':')
                    indi.append(1000)
                    conn_sub_server((indi[0], int(indi[1])), amand[3].replace('_', ' '))
                elif amand[1] == 'serve':
                    amand.append(1000)
                    subprocess.call(f'python {amand[2]} {amand[3]}')
            except:
                STDERR.append('correct usage: stream connect ip:port request\n') 
            
        
        elif prom == 'pkg':
            if ' -g ' in command:
                requ = amand[len(amand)-1]
                subprocess.call(f"cd {root}/Packages{monnezza}git clone https://github.com/{requ}.git", shell = True)
            elif ' -p ' in command:
                requ = amand[len(amand)-1]
                subprocess.call(f"cd {root}/Packages{monnezza}pip install {requ}", shell = True)
            else:
                requ = command.replace('pkg ', '')
                subprocess.call(f'cd {root}/Packages{monnezza}curl {requ} -o {requ.split("/")[len(requ.split("/"))-1]}', shell=True)                

################################################################################# ci devi fà qualco'
        elif prom == 'lemmesee':
            STDOUT.append('lemmesee command is actually being revisited and it\'s not fully avaiable/functioning for this version of kane.')
            for i in dir():
                try:
                    if not ('elp' in i or i == 'backup'):
                        if 'all' in command:
                            STDOUT.append(f'{i}: {globals()[i]}')
                        elif not '__' in i and not 'function' in str(globals()[i]) and not 'module' in str(globals()[i]) and not 'InternalCommands' in i:
                            STDOUT.append(f'{i}: {globals()[i]}')
                except: 0
##################################################################################
        elif prom == 'file':

            tg = amand[1]
            try:
                open(f'{directory}/{tg}', 'x')
                STDOUT.append(f'created {tg}')
            except:
                STDERR.append('[Kane Error 3] unable to create file')
            continue
        
        #elif prom == 'kanescript' or prom == 'ks':
        
        elif prom == 'read':
            try:
                with open(f"{directory}/{command.replace('read ', '')}") as f:
                    STDOUT.append(f.read())
            except:
                STDERR.append(f"Unable to open {command.replace('read ', '')}")

        elif prom == 'start':
            try:
                os.startfile(amand[1].replace('*', directory))
            except:
                try:
                    os.startfile(amand[1].replace('*', directory))
                except:
                    STDERR.append('file not found')
        elif command == 'cs':
            subprocess.call(cs, shell=True)
        
        elif command == 'password' or command == 'pwd':
            STDOUT.append(f'Changing password for {user}')
            passw = input('$:>')
            with open(f'{root}/usrs/{username}/UserData.dat', 'wb') as f:
                pk.dump([enc.encript(passw, 12), LAST_CHECKED], f, protocol=2)
                STDOUT.append(f'saved succesfully!\n')
            
                
        elif prom == 'makedir':
            dar = amand[1]
            if not '/' in dar:
                dar = f'{directory}/{dar}'
            if not os.path.exists(dar):
                os.makedirs(dar)
                STDOUT.append(f'{dar} succesfully created!')
        
        elif command == 'home':
            directory = f'{str(pathlib.Path().absolute())}/usrs/{user}'
        
        elif prom == 'man':
            com = amand[1]
            stdout_color = ['cyan', 'on_blue']
            try:
                man = open(f'Manual/{com}.txt', 'r')
                STDOUT.append(man.read())
                man.close()
            except:
                STDOUT.append(f'There\'s no manual for {com}')
            
        elif command == 'dir' or command == 'ls':
            for file in glob.glob(f'{directory}/*'):
                STDOUT.append(file.replace(f'{directory}', '').replace(directory.replace('/', '\\'), ''))
                
        elif prom == 'dir':
            arg = amand[1]
            for file in glob.glob(f'{directory}*.{arg}'):
                STDOUT.append(file.replace(f'{directory}', ''))
                
        elif prom == 'ls':
            arg = amand[1]
            for file in glob.glob(f'{directory}/*.{arg}'):
                STDOUT.append(file.replace(f'{directory}/', '').replace(directory.replace('/', '\\') + '/', ''))
                
        elif prom == 'web':
            we = amand[1]
            try:
                webopen(we)
                STDOUT.append(f'opening {we} ...')
            except:
                STDERR.append('Unable to connect to the website, try to check internet connession')
                
        elif command == 'update':
            subprocess.call("pip install pygame", shell = True)
            
        elif command == 'upgrade':
            STDOUT.append('installing new version on /kane')
            subprocess.call("git clone https://github.com/umanochiocciola/kane.git", shell = True)

            
            with open(f"{root}/kane/README.txt") as f:
                    STDOUT.append(f.read())
            
            STDOUT.append('\nDone. Overwrite /kane/MainKane files on your MainKane folder.\n')
            STDOUT.append('updated succesfully')
            
        elif 'cd' in command:
            if command.replace("cd","") == '..':
                directory = cd_punto(directory)
            elif '/' in command:
                ghen = command.replace("cd ","").replace("*", directory)
                if os.path.exists(ghen):
                    directory = ghen
                else:
                    STDERR.append(f'can\'t jump to {ghen} : directory doesn\'t exist')
            else:
                ghen = f'{directory}/{command.replace("cd ","").replace("*", directory)}'
                if os.path.exists(ghen):
                    directory = ghen
                else:
                    STDERR.append(f'can\'t jump to {ghen} : directory doesn\'t exist')
                
        elif prom == 'py':
            try:
                exec(command.replace('py ', ''))# ignore this first 3 lines if getting errors when using py command
            except:
                STDERR.append('\n\n+=====================================+\n')
                STDERR.append(traceback.format_exc())
                STDERR.append('\n+=======================================+\n')
        else:
            try:
                exec(f'from Packages.{prom} import main; main.{amand[1]}({amand})')
            except:
                ab = InternalCommands.get(command, 'fuc')
                if ab == 'fuc':
                    stdout_color[0] = 'yellow'
                    plot = subprocess.run(f'cd {directory}{monnezza}{command}', shell=True, stderr = subprocess.PIPE)
                    if plot.stderr == b'':
                        STDOUT.append('\nexternal command executed with no errors :{D')
                    else:
                        STDERR.append(plot.stderr)
                        STDERR.append(f'Kane shell error: {prom}: doesn\'t exist neither in kane nor in your host system\n or an error occured while executing external command')
                else:
                    exec(InternalCommands.get(command, "STDERR.append('Uknown Internal, direct or external command.')"))

    stdout = ''
    stderr = ''
    for ou in STDOUT: stdout += f'{ou}\n'
    for er in STDERR: stderr += f'{er}\n'
    if not attributes.get('show_stderr', 0): stderr = 'Kane shell error: {prom}: doesn\'t exist neither in kane nor in your host system\n or an error occured while executing external command'
    
    return(NiceLittleOutput(stdout, stderr, stdout_color,))

colorama.init()
if __name__ == '__main__':
    while True:
        try:
            foffi = pull(input(colored(f'{directory} ## {username} $~ ', 'green')), (backup, username, user, deamons, collegamenti, attributes, InternalCommands, passw, LAST_CHECKED, elp, root, sys_host, cs, monnezza))
            print(colored(foffi.stdout, foffi.stcolor[0], foffi.stcolor[1]) + '\n' + colored(foffi.stderr, 'red'))
        except SystemExit:
            sys.exit()
        except:
            print(colored(F'Error: your command caused this process to crash.\n', 'yellow', 'on_red'))
