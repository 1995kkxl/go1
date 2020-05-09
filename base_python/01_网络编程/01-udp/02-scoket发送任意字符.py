import socket
def main():
	#创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#从键盘发送数据
	send_data = input("请输入你要发送的数据")

	# 可以使用套接字首发数据
	#udp_socket.sendto(b"发送哈哈哈哈哈哈测试",  ("XXX.XXX.XXX.XXX",8142)) #ip和端口 b字符串
	udp_socket.sendto(send_data.encode("utf-8"), ("192.168.56.1",8080)) #发送任意字符到目标机器
	# 关闭套接字
	udp_socket.close()

	print("-----run-----")

if __name__ == '__main__':
	main()