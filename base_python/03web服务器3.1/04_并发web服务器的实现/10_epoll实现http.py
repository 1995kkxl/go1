import socket
import re
import select

#只能在linux环境下运行 因为win没有epoll

def serve_client(new_client_socket,request):
    """为这个客户端返回数据"""
    # 6.接收浏览器发送过来的http请求
    #request = new_client_socket.recv(1024).decode("utf-8")

    # 7.将请求报文分割成字符串列表
    request_lines = request.splitlines()
    print(request_lines)

    # 8.通过正则表达式提取浏览器请求的文件名
    file_name = None
    ret = re.match(r"^[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("file_name:", file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 9.返回http格式的应答数据给浏览器
    try:
        f = open("./html" + file_name, "rb")
    except Exception:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "-----file not found-----"
        new_client_socket.send(response.encode("utf-8"))
    else:
        # 9.1 读取发送给浏览器的数据-->body
        html_content = f.read()
        f.close()
        # 9.2 准备发送给浏览器的数据-->header

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body) #相当于关闭套接字，让浏览器不一直转
        response_header += "\r\n"
        #response_header是文件rb打开的二进制，需要转换一下str
        response = response_header.encode("utf-8") + response_body
        # 将response header发送给浏览器--先以utf-8格式编码
        new_client_socket.send(response)
        # 将response body发送给浏览器--直接是以字节形式发送
        #new_client_socket.send(html_content)

    # 10. 关闭此次服务的套接字 Content-Length这里处理了
    #new_client_socket.close()


def main():
    """用来完成程序整体控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 通过设定套接字选项解决[Errno 98]错误
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定端口
    tcp_server_socket.bind(("", 7899))

    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False) #将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    #将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(),select.EPOLLIN) #select.EPOLLIN监测套接字是否有输入

    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll() #默认会堵塞，直到os监测到数据到来 通知事件通知方式 告诉这个程序 才开始解堵塞
        #[(fd, event),(套接字对应的文件描述符，这个文件描述符到底是什么事件，例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            # 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_client_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_client_socket.fileno(),select.EPOLLIN)
                fd_event_dict[new_client_socket.fileno()] = new_client_socket
            elif event == select.EPOLLIN:
                #判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024)
                if recv_data:
                    serve_client(fd_event_dict[fd],recv_data.decode("utf-8"))
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()