import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(("",7890))

    #监听
    tcp_server_socket.listen(128)
    while True:
        print("waiting....")
        #accept等待连接
        new_client_socket,client_Addr = tcp_server_socket.accept()
        print("===%s===客户端连接成功..." % str(client_Addr))

        #接收客户端发送过来的数据
        recv_data = new_client_socket.recv(1024)
        print(recv_data)

        #回送一部分数据给客户端
        new_client_socket.send("service is ok...".encode("utf-8"))

        #关闭套接字
        #关闭accept返回的套接字 意味着 不会再为这个客户端服务
        new_client_socket.close()
    #如果将监听套接字 关闭了，那么会导致不能再次等待新客户端的到来，即XXX.accept就会失败
    tcp_server_socket.close()
if __name__ == '__main__':
    main()