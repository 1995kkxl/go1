import socket

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #获取对方的ip和端口
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入端口："))
    #从键盘获取数据
    send_data = input("请输入发送的内容：")
    #可以使用套接字接发数据
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
    #接收回送的数据
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    #关闭套接字
    udp_socket.close()

if __name__ == '__main__':
    main()