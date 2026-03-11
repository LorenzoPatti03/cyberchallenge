import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

PORT = 9010

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Analisi dell'URL ricevuto
        parsed_url = urlparse(self.path)
        path_solamente = parsed_url.path
        parametri = parse_qs(parsed_url.query)

        # Inizio della logica di risposta
        if path_solamente == "/S":
            # Caso 1: Percorso /S
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("ciao".encode())

        elif path_solamente == "/get_flag":
            # Caso 2: Percorso /get_flag
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            print('aaa')
            if 'flag' in parametri:
                valore_flag = parametri['flag'][0]
                risposta = f"Flag ricevuta: {valore_flag}"
            else:
                risposta = "Errore: parametro flag mancante"
            
            self.wfile.write(risposta.encode())

        else:
            # Caso 3: Qualsiasi altro percorso (404 Not Found)
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Percorso non trovato")

# Avvio del server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server pronto sulla porta {PORT}")
    print("Prova: http://localhost:9010/S")
    httpd.serve_forever()