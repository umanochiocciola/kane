
def encript(sbo, start):
    st = int(start)
    out = ''
    for i in sbo:
        if ord(i) + st >= 110000:
            ping = (ord(i) + st) - 110000
        else: ping = ord(i) + st
        out +=  chr(ping)
        
    return(out)

def decript(sbo,start):
    st = int(start)
    out = ''
    for i in sbo:
        if ord(i) - st <= 0:
            ping = (ord(i) - st) + 110000
        else: ping = ord(i) - st
        out += chr(ord(i) - st)

    return(out)
