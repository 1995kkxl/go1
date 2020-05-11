import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(("",7890))

    #监听
    tcp_server_socket.listen(128)
    print("waiting....")
    #accept等待连接
    new_client_socket,client_Addr = tcp_server_socket.accept()
    print("处理ing...")
    print(client_Addr)

    #接收客户端发送过来的数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    #回送一部分数据给客户端
    new_client_socket.send("hhhhhhh".encode("utf-8"))

    #关闭套接字
    tcp_server_socket.close()
    new_client_socket.close()
if __name__ == '__main__':
    main()