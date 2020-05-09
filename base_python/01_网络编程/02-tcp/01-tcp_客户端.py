import socket


def main():
	#1. 创建tcp的套接字
	tcp_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#2. 链接服务器
	#tcp_scoket.connet(("XXX.XXX.XX.X" 1254))
	server_ip = input("请输入要链接的ip:")
	server_port = int(input("请输入端口:"))
	server_addr = (server_ip, server_port)
	tcp_scoket.connect(server_addr)

	#3. 发送数据/接收数据
	send_data = input("请输入你要发送的内容:")
	tcp_scoket.send(send_data.encode("utf-8"))
	#4. 关闭套接字
	tcp_scoket.close()


if __name__ == '__main__':
	main()