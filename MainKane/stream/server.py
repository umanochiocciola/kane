import socket
import sys

banca = {
    'test': 'it works!',
    'help': 'to get kane assistance, type help in your terminal\nto get stream client help type man stream\nto get stream serving help... well that\'s coming soon :P',
    'random_ascii_art': "    .\n /\\ /|\n((.Y(!\n \\ |/\n /  6~6,\n \\ _    +-.\n  \\`-=--^-'\n   \\ \\ "
}
def ricevi_comandi(conn):
    richiesta = conn.recv(4096)
    data = banca.get(richiesta.decode(), 'no item found')
    conn.sendall(data.encode())


def sub_server(indirizzo, backlog=1):
    print("Kane Stream server started")
    while 1:
        try:
            s = socket.socket()                    
            s.bind(indirizzo)                     
            s.listen(backlog)                     
            print('Ready to accept a new connection')
        except socket.error as errore:
            print(f"Something went wrong\n{errore}")
            print(f"Server reboot aptempt")
            sub_server(indirizzo, backlog=1)
        conn, indirizzo_client = s.accept()
        print(f"Connection: {indirizzo_client}")
        ricevi_comandi(conn)



sub_server(("", int(sys.argv[1])))
