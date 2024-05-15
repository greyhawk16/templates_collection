# <참고 사이트>
# https://foxtrotin.tistory.com/278
# https://techexpert.tips/python/python-file-transfer-using-sockets/


from socket import *
import os
import sys


HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((HOST, PORT))

print('연결에 성공했습니다.')
filename = input('전송할 파일 이름을 입력하세요: ')
clientSock.sendall(filename.encode('utf-8'))
data_transferred = 0

print("파일 %s 전송 시작" %filename)

with open(filename, 'rb') as f:
    try:
        # 2안
        data = f.read(BUFFER_SIZE)
        while data:
            data_transferred += len(data)
            clientSock.send(data)
            data = f.read(BUFFER_SIZE)

        print("전송완료 %s, 전송량 %d" %(filename, data_transferred))

    except Exception as ex:
        print(ex)
