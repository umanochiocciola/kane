import KaneTerminal as kt

terminal = []
user = backup = username = 'noob'
passw = ''

version = kt.version
collegamenti = kt.collegamenti
InternalCommands = kt.InternalCommands
attributes = kt.attributes
deamons = []
playground = {}
elp = kt.elp
root = directory = kt.root
sys_host = kt.sys_host
monnezza = kt.monnezza

def pull(tin):
    return kt.pull(tin, (user, backup, username, [], collegamenti, attributes, InternalCommands, passw, '', elp, root, sys_host, 'NONE',monnezza))



mx = my = screen = None
def INIT(Mx, My, scri):
    global mx, my, screen
    mx, my, screen = Mx, My, scri



class prog_win:
    def __init__(self, scri='win', text='My Window'):
        self.scri = scri
        self.strs = [(0, 0, text)]
    
    def main(self, KEY):  
        if int(KEY) == 3: return 'DESTROY'





class term:
    def __init__(self, scri='term'):
        self.scri = scri
        self.strs = [(0, int(mx/2)-14, 'Kane Terminal\ntype quit to close'), (2, 0, '$ ')]
        self.BACCU = ''
    
        self.inputing = ''
    
    def main(self, KEY):  
        if KEY == 3: return 'DESTROY'
        if KEY == 0: 0
        
        elif KEY == 8: self.inputing = self.inputing[:-1] #backspace
        elif KEY == 10:
            pog = pull(self.inputing)
            self.inputing = ''
            foo, dummy, spr = self.strs[1]
            if pog.stderr != '':
                self.BACCU = spr +'\n'+ pog.stderr 
            else:
                self.BACCU = spr + '\n' + pog.stdout
            
            if pog.stdout == 'CS\n': self.BACCU = ''
            
        else: self.inputing += chr(KEY)
        
        self.strs[1] = (2, 0, self.BACCU+'\n$'+self.inputing)





class notepad:
    def __init__(self, scri='pad'):
        self.scri = scri
        self.strs = [(0, int(mx/2)-14, 'Kane Notepad'), (1, 3, 'UNSAVED - save: ^S  the first line will be the filename'), (2, 0, '')]
    
        self.inputing = ''
    
    def main(self, KEY):  
        if KEY == 3: return 'DESTROY'
        if KEY == 0: 0
        
        elif KEY == 8: self.inputing = self.inputing[:-1] #backspace
        elif KEY == 19:
            try:
                with open(self.inputing.split('\n')[0], 'w') as f: f.write(self.inputing.replace(self.inputing.split('\n')[0], ''))
                self.strs[1] = (1, 3, 'SAVED  - save: ^S  the first line will be the filename')
            except: self.strs[1] = (1, 3, 'UNABLE TO SAVE  - save: ^S  the first line will be the filename')
        else: self.inputing += chr(KEY)
        
        self.strs[2] = (2, 0, self.inputing)