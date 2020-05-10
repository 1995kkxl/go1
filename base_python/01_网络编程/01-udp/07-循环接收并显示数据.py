import socket
def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定一个本地信息
    localaddr = ("",5566) #ip 和 指定端口
    udp_socket.bind(localaddr)
    print(localaddr)
    while True:
        # 3. 接收数据
        recv_data = udp_socket.recvfrom(1024) #1024表示接收的最大字节
        #recv_data这个变量中存储的是一个元组（接收到的数据，（发送方的ip，port
        recv_msg = recv_data[0] #存储接收的数据
        send_addr = recv_data[1] #存储发送方的地址信息
        # 4. 打印接收到的数据
        print("%s:%s" %(str(send_addr),recv_msg.decode("gbk")))
    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
	main()