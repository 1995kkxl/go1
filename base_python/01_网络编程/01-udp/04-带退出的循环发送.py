import socket
def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        #从键盘发送数据
        send_data = input("请输入你要发送的数据")
        if send_data =="exit":
            break

        # 可以使用套接字首发数据
        #udp_socket.sendto(b"发送哈哈哈哈哈哈测试",  ("XXX.XXX.XXX.XXX",8142)) #ip和端口 b字符串
        udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1",1024)) #发送任意字符到目标机器
    # 关闭套接字
        udp_socket.close()

if __name__ == '__main__':
    main()