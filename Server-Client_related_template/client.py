# https://nikhilroxtomar.medium.com/file-transfer-using-tcp-socket-in-python3-idiot-developer-c5cf3899819c
# https://www.geeksforgeeks.org/file-transfer-using-tcp-socket-in-python/
# https://techexpert.tips/ko/python-ko/python-%EC%86%8C%EC%BC%93%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%8C%8C%EC%9D%BC-%EC%A0%84%EC%86%A1/

import socket


FORMAT = "utf-8"
SIZE = 1024


def send_filename(filename, host, port):
    BUFFER_SIZE = 4096  # Buffer size for sending

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(filename.encode(FORMAT))
        print(f"file sent: {filename}")
         

def send_file(filename, host, port):
    BUFFER_SIZE = 4096  # Buffer size for sending

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                s.sendall(data)
        print('File sent successfully!')

# Using the function to send the file
filename = 'xfoil.exe'  # Name of the file to be sent
HOST = '127.0.0.1'  
PORT = 65432
send_file(filename, HOST, PORT)