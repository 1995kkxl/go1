import socket
import re
import multiprocessing

class WSGIServer(object):
    #首先执行init方法
    def __init__(self):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 通过设定套接字选项解决[Errno 98]错误
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_server_socket.bind(("", 7899))

        # 3.变为监听套接字
        self.tcp_server_socket.listen(128)

    def serve_client(self,new_client_socket):
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
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"

            # 将response header发送给浏览器--先以utf-8格式编码
            new_client_socket.send(response.encode("utf-8"))
            # 将response body发送给浏览器--直接是以字节形式发送
            new_client_socket.send(html_content)

        # 10. 关闭此次服务的套接字
        new_client_socket.close()


    def run_forever(self):
        """用来完成程序整体控制"""
        # 定义计数器，记录浏览器发起的请求次数
        request_counter = 0

        while True:
            # 4.等待新客户端连接
            new_client_socket, client_addr = self.tcp_server_socket.accept()

            # 5.为连接上的客户端服务
            process = multiprocessing.Process(target=self.serve_client, args=(new_client_socket,))
            process.start()

            new_client_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()

def main():
    '''控制整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行'''
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()