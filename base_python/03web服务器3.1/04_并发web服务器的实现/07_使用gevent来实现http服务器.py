from gevent import monkey
import gevent
import socket
import re


#协程来
monkey.patch_all()


def serve_client(new_client_socket):
    """为这个客户端返回数据"""
    # 6.接收浏览器发送过来的http请求
    request = new_client_socket.recv(1024).decode("utf-8")

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
        f = open("./Charisma" + file_name, "rb")
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
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"

        # 将response header发送给浏览器--先以utf-8格式编码
        new_client_socket.send(response.encode("utf-8"))
        # 将response body发送给浏览器--直接是以字节形式发送
        new_client_socket.send(html_content)

    # 10. 关闭此次服务的套接字
    new_client_socket.close()


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

    while True:
        # 4.等待新客户端连接
        new_client_socket, client_addr = tcp_server_socket.accept()

        # 5.为连接上的客户端服务
        # 创建一个greenlet并不会导致其立即得到切换执行，
        # 还需要在其父greenlet（在哪个程序控制流中创建该greenlet，
        # 则这个程序控制流就是父greenlet）中遇到正确的阻塞延时类操作或调用greenlet对象的join()方法
        # （此处不需要使用join()函数，因为主程序由于死循环的缘故不会在greenlet执行结束前退出）
        greenlet = gevent.spawn(serve_client, new_client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()