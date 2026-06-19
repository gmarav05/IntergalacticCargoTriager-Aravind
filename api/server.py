import http.server
import json
import os

PORT = 8000

class CargoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Check HTTP header X-System-Override: true (case-insensitive check)
        override_header = self.headers.get('X-System-Override', '').lower()
        if override_header == 'true':
            self.send_response(418, "I'm a teapot")
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b"System override denied.")
            return

        # 2. Check endpoint: GET /api/cargo
        path = self.path.split('?')[0]
        if path == '/api/cargo':
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            project_root = os.path.dirname(script_dir)

            json_path = os.path.join(project_root, "parser", 'Task 1 - Aravind - Parser.json')

            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json; charset=utf-8')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8'))
                except Exception as e:
                    self.send_response(500)
                    self.send_header('Content-Type', 'text/plain; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(f"Internal server error: {str(e)}".encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.end_headers()
                self.wfile.write(b"JSON data file not found.")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Not Found")

def run_server():
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, CargoHandler)
    print(f"Starting server on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
