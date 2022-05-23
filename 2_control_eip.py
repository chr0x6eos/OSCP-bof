#!/usr/bin/env python3
import socket

ip = ""
port = 1337
timeout = 5

prefix = ""
# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l LEN
buffer = prefix + ""
# !mona findmsp -distance LEN

def send(buffer):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        s.send(bytes(buffer, "latin-1"))
        s.recv(1024) # Try to received afterwards
        s.close()

if __name__ == '__main__':
    try:
        send(buffer)
    except Exception as ex:
        print(f"Error:\n{ex}")
        quit