import socket
def main():
#创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 可以使用套接字首发数据
	udp_socket.sendto(b"发送哈哈哈哈哈哈测试", ("XXX.XXX.XXX.XXX",8142)) #ip和端口 b字符串
	# 关闭套接字
	udp_socket.close()

	print("-----run-----")

if __name__ == '__main__':
	main()