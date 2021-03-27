import socket
import threading
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime



def handle_client(client_connection):

    request = client_connection.recv(1024).decode()
    if not request == "":
        req_split = request.split(" ")
        method = req_split[0]
        url = req_split[1]
        content = req_split[2].replace("\n", "")
        print(request.replace("\n", ""))
        now = datetime.now()
        date = str(format_date_time(mktime(now.timetuple())))
                
        if method == 'GET':
            # if url == '/':
            #     response = f"{content} 200 OK\n\n"
            
            if url == '/':
                html = """<html>
                                                            <head>
                                                                <title>Hello World</title>
                                                            </head>
                                                            <body>
                                                                <h1>Hello World!</h1>
                                                                <p>Welcome to the index.html web page..</p>
                                                            </body>
                                                            </html>\n\n\n\n"""
                response = f"{content} 200 OK\r\nContent-Type: text/html\r\nDate: "+date+"\r\nContent-Length: " + str(
                    len(html)) + "\r\n\r\n" + html
            elif url == "/img":
                f = open("img.jpg", "rb")
                html = f.read()
                response = f"{content} 200 OK\r\nContent-Type: image/jpeg\r\nDate: "+date+"\r\nContent-Length: " + str(
                    len(html)) + "\r\n\r\n" 
                response = (response).encode() + html
                
            else:
                response = f"{content} 404 NOT FOUND\n\n" + \
                    """<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>"""

        elif method == 'HEAD':
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nDate: " + date + "\r\n\r\n"
        elif method == 'PUT':
            response = f"{content} 500 SERVER ERROR\n\n"
        elif method == 'POST':
            response = f"{content} 304 NOT MODIFIED\n\n"
        else:
            response = f"{content} 400 Bad Request\n\n"
        if type(response) == str:
            response = response.encode()
        client_connection.sendall(response)
        client_connection.close()


def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 80

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print('Listening on port %s ...' % SERVER_PORT)
    while True:
        client_connection, client_address = server_socket.accept()
        threading.Thread(target=handle_client,
                         args=(client_connection,)).start()

    server_socket.close()


if __name__ == "__main__":
    main()
