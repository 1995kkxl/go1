import re


def main():
	email = input("请输入一个邮箱地址:")
	#如果在正则表达式中需要用到了某些普通的字符,比如? .等 需要用到反斜杠进行转义
	#4位数@163.com
	ret = re.match(r"[a-zA-Z_0-9]{4,20}@163\.com",email)
	if ret:
		print("%s符合要求..." % email)
	else:
		print("%s不符合要求..." % email)

if __name__ == '__main__':
	main()