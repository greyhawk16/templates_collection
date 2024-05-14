import socket

def receive_file(file_name, host, port):
    BUFFER_SIZE = 4096  # Buffer size for receiving

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f'Waiting for connection at {host}:{port}')
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            with open(file_name, 'wb') as f:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    f.write(data)
            print('File received successfully!')

# Using the function to receive the file
saved_file_name = 'received_file-1.exe'  # Name of the file to be saved
HOST = '127.0.0.1'  
PORT = 65432
receive_file(saved_file_name, HOST, PORT)