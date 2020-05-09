#coding=utf-8
from socket import *


def main():
    #1、创建socket套接字
    #socket(参数1，参数2)
    #参数1 = AF_INET固定的
    #参数2 = SOCK_DGRAM表示udp，上篇文章中说过SOCK_STREM表示tcp
    udpSocket = socket(AF_INET,SOCK_DGRAM)

    #2、准备接收方的地址
    sendAddress = ("192.168.56.1",8080)

    #3、从键盘输入需要发送的数据
    sendData = input("请输入要发送的数据：")

    #4、发送数据到指定电脑
    udpSocket.sendto(sendData.encode("utf-8"),sendAddress)

    #5、关闭socket套接字
    udpSocket.close()

if __name__ == '__main__':
    main()