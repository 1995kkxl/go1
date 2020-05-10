import socket
def main():
	#创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定本地信息
	udp_socket.bind(("", 5566))

	while  True:

		#从键盘发送数据
		send_data = input("请输入你要发送的数据")

		# 可以使用套接字首发数据
		#udp_socket.sendto(b"发送哈哈哈哈哈哈测试",  ("XXX.XXX.XXX.XXX",8142)) #ip和端口 b字符串
		udp_socket.sendto(send_data.encode("utf-8"), ("192.168.2.103",8080)) #发送任意字符到目标机器
	# 关闭套接字
	udp_socket.close()

if __name__ == '__main__':
	main()