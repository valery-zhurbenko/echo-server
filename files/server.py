import socket
import json

def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 5432))
    connection.listen(10)
    while True:
        print ('ready for a connection')
        try:
            current_connection, address = connection.accept()
            client_address = address[0]
            print ('From ', client_address)
            while True:
                data = current_connection.recv(2048)

                if data == b'quit\r\n':
                    current_connection.close()
                    break
        
                elif data == b'stop\r\n':
                    current_connection.shutdown(1)
                    current_connection.close()
                    exit()
        
                elif data:
                    print('sending data back to the client')
                    current_connection.sendall('Response: '.encode('utf-8'))
                    current_connection.sendall(data)
                    current_connection.send(client_address.encode('utf-8'))
                    current_connection.sendall('\n'.encode('utf-8'))
                    print(data, 'from:', client_address, '\n')
        finally:
            connection.close

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass