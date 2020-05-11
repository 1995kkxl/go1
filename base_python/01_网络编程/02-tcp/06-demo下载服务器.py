import socket
def send_file_2_client(new_client_socket,client_Addr):
    #1.接收客户端需要下载的文件名
    # 接收客户端发送过来的数据
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端（%s)需要下载的文件是：%s" % (str(client_Addr), file_name))

    file_content = None
    #2.打开这个文件，读取数据
    try:
        f = open(file_name,"rb") #rb是直接二进制
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有下载的文件（%s）" % file_name)
    # 3. 发送文件的数据给客户端
    # new_client_socket.send("hhhhhhh".encode("utf-8"))
    if file_content:
        new_client_socket.send(file_content)



def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server_socket.bind(("",7890))

    #监听
    tcp_server_socket.listen(128)
    while True:
        new_client_socket,client_Addr = tcp_server_socket.accept()

        #调用发送文件函数，返程为客户端服务
        send_file_2_client(new_client_socket,client_Addr)


        #关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()
if __name__ == '__main__':
    main()