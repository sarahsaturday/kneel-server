import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (get_all_metals,
                get_single_metal,
                create_metal,
                delete_metal,
                update_metal)
from views import (get_all_orders,
                get_single_order,
                create_order,
                delete_order,
                update_order)
from views import (get_all_sizes,
                get_single_size,
                create_size,
                delete_size,
                update_size)
from views import (get_all_styles,
                get_single_style,
                create_style,
                delete_style,
                update_style)

class HandleRequests(BaseHTTPRequestHandler):
    """
    Controls the functionality of any GET, PUT, POST, DELETE 
    requests to the server

    """

    def parse_url(self, path):
        """
        Parse the URL path.

        """
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def do_GET(self):
        """
        Handle HTTP GET requests.

        """
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
            else:
                response = get_all_metals()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response = get_all_sizes()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response = get_all_styles()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """
        Handle HTTP POST requests.

        """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new metal
        new_metal = None

        # Initialize new order
        new_order = None

        # Initialize new size
        new_size = None

        # Initialize new style
        new_style = None

        # Add a new metal, order, or size to the list
        if resource == "metals":
            new_metal = create_metal(post_body)
        elif resource == "orders":
            new_order = create_order(post_body)
        elif resource == "sizes":
            new_size = create_size(post_body)
        elif resource == "styles":
            new_style = create_style(post_body)

        # Encode the new object and send in response
        if new_order is not None:
            self.wfile.write(json.dumps(new_order).encode())
        elif new_size is not None:
            self.wfile.write(json.dumps(new_size).encode())
        elif new_style is not None:
            self.wfile.write(json.dumps(new_style).encode())
        else:
            self.wfile.write(json.dumps(new_metal).encode())

    def do_PUT(self):
        """
        Handle HTTP PUT requests.

        """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "metals":
            update_metal(id, post_body)
        if resource == "orders":
            update_order(id, post_body)
        if resource == "sizes":
            update_size(id, post_body)
        if resource == "styles":
            update_style(id, post_body)

        self.wfile.write("".encode())

    def _set_headers(self, status, new_order=None, new_size=None, new_style=None):
        """
        Set response headers.

        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        if new_order is not None:
            self.send_header('Order', f"/orders/{new_order['id']}")
        elif new_size is not None:
            self.send_header('Order', f"/sizes/{new_size['id']}")
        elif new_style is not None:
            self.send_header('Order', f"/styles/{new_style['id']}")
        self.end_headers()

    def do_OPTIONS(self):
        """
        Sets the options headers

        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        """
        Handle HTTP DELETE requests.

        """
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "metals":
            delete_metal(id)
        if resource == "orders":
            delete_order(id)
        if resource == "sizes":
            delete_size(id)
        if resource == "styles":
            delete_style(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

# point of this application.
def main():
    """
    Starts the server on port 8088 
    using the HandleRequests class

    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
