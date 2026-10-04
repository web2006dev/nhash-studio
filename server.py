import http.server
import socketserver
import sys

PORT = 8087

class NhashStudioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

NhashStudioHTTPRequestHandler.extensions_map.update({
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.html': 'text/html',
})

if __name__ == '__main__':
    print(f"Starting Nhash Studio web server on port {PORT}...")
    try:
        with socketserver.TCPServer(("", PORT), NhashStudioHTTPRequestHandler) as httpd:
            print(f"Nhash Studio Website Live at: http://localhost:{PORT}")
            print("Press Ctrl+C to terminate.")
            httpd.serve_forever()
    except Exception as e:
        print(f"Error launching server: {e}", file=sys.stderr)
        sys.exit(1)
