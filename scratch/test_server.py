import http.server
import socketserver
import os

PORT = 8001

class SecurityHeadersHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent MIME type sniffing
        self.send_header('X-Content-Type-Options', 'nosniff')
        # Referrer Policy
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        # X-Frame-Options
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        # Content-Security-Policy
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com https://cdn.jsdelivr.net; "
            "font-src 'self' data: https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
            "img-src 'self' data: https://www.google-analytics.com; "
            "connect-src 'self' https://www.google-analytics.com; "
            "frame-src 'self' https://www.google.com https://maps.google.com; "
            "frame-ancestors 'self';"
        )
        self.send_header('Content-Security-Policy', csp)
        
        super().end_headers()

# Change to the directory we want to serve
os.chdir('c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours')

with socketserver.TCPServer(("", PORT), SecurityHeadersHandler) as httpd:
    print(f"Serving at port {PORT} with security headers enabled.")
    httpd.serve_forever()
