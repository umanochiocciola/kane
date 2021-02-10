import curses
from progrs import *

screen = curses.initscr()
curses.start_color()
curses.curs_set(0)

# lines, columns, start line, start column
#my_window = curses.newwin(15, 20, 0, 0)

my, mx = screen.getmaxyx()  # dimensioni schermo
screen.clear()              #

INIT(mx, my, screen)

##  colors

COLORS = [
    (curses.COLOR_BLUE, curses.COLOR_WHITE), # deafult window
]

for i in range(len(COLORS)):
    f, b = COLORS[i]
    curses.init_pair(i+1, f, b)

##


menu = [
    prog_win,
    term,
    notepad
    
]

opened = []

while 1:
    
    

    ###            aggiornamenti grafici
    
    screen.addstr(0,0, '█'*mx) # barra applicazioni
    screen.addstr(1,0, '█'*mx) #
    screen.addstr(2,0, '█'*mx) #
    
    try:
        for i in opened[0].strs:
            y, x, sp = i
            screen.addstr(y+3, x, sp)
    except: 0
    
    for i in range(len(menu)):
        screen.addstr(1, 5*i, menu[i]().scri+' '*(4-len(menu[i]().scri)))
        
    
    bos = ''
    for i in range(len(opened)):
        if i == 0:
            bos += '[' + opened[i].scri + ']  '
        else:
            bos += opened[i].scri + '  '

    screen.addstr(my-1, 0, f'windows: {bos}')
    
    
    
    ## comandi
    KEY = int(screen.getch())
    
    if not( KEY in [27, 4, 9]):
        for i in range(len(opened)):
            try:
                g = opened[i].main(KEY)
                if g == 'DESTROY': opened.remove(opened[i])
                KEY = 0
            except:
                try: opened.remove(opened[i])
                except: 0
    
    if KEY == 27: break

    elif KEY == 4:
        KEY = int(screen.getch())
        new = menu[int(chr(KEY))-1]()
        opened.insert(0, new)

    elif KEY == 9:
        a = opened[0]
        opened.remove(opened[0])
        opened.append(a)

    ###

    screen.refresh()
    screen.clear()
    ###

curses.curs_set(1)
curses.endwin()