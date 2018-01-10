import socket
import time

SERVER_ADDRESS = (_HOST, _PORT) = '', 9999
REQUST_QUEUE_SIZE = 5

def handle_request(soc):
    data = soc.recv(1024)
    print(data.decode())

    http_response = b"""\
                        HTTP/1.1 200 OK

                        Hello, World!
                        """

    soc.sendall(data.encode('utf-8'))
    time.sleep(60)

def server_listener():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUST_QUEUE_SIZE)

    print('Serving HTTP on port {port} ...'.format(port=_PORT))

    while True:

        new_sock, addr = listen_socket.accept()
        handle_request(new_sock)
        new_sock.close()


if __name__ == '__main__':
    server_listener()