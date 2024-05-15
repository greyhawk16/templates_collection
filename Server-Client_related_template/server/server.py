# <참고 사이트>
# https://foxtrotin.tistory.com/278
# https://techexpert.tips/python/python-file-transfer-using-sockets/


from socket import *
from os.path import exists
import sys


HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024
STORAGE_FOLDER = './uploads/'

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((HOST, PORT))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()
print(str(addr),'에서 접속했습니다')

file_name = connectionSock.recv(BUFFER_SIZE) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
file_name = file_name.decode('utf-8')
print('받을 파일 이름 : ', file_name) #파일 이름을 일반 문자열로 변환한다

with open(STORAGE_FOLDER + file_name, 'wb') as f:
    data = connectionSock.recv(BUFFER_SIZE)
    while data:
        f.write(data)
        data = connectionSock.recv(BUFFER_SIZE)

    print(f'Received {file_name}')