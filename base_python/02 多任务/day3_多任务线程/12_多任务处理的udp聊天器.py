import socket
import threading

def recv_msg(udp_socket):
    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket,dest_ip,dest_port):
    # 发送数据
    while True:
        send_data = input("请输入发送的数据：")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    #1.创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2.绑定本地信息
    udp_socket.bind(("",7890))
    #3.获取对方ip和port
    dest_ip = input("请输入ip:")
    dest_port = int(input("端口："))

    #4.创建两个线程
    t_recv = threading.Thread(target=recv_msg,args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,dest_ip,dest_port))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()