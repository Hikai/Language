"""
Web server.

??
"""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    """Request handler class."""

    def do_get(self):
        """Get request process."""
        self.send_response(200)
        self.end_headers()
#         html = """<html>
#     <head><title>asdf</title></head>
#     <body><p>hello</p></body>
# </html>"""
#         self.wfile.write(html)
        message = "hello"
        self.wfile.write(bytes(message, "utf8"))
        return

server_adress = ('', 7578)
http_deamon = HTTPServer(server_adress, Handler)
http_deamon.serve_forever()
