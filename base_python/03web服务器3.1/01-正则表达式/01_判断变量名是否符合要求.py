import re

#re.match(正则表达式，需要处理的字符串)

def main():
	names = ["age", "_age", "1age" , "ange1", "a_age", "age_1_", "age!", "a#123"]
	for name in names:
		# ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
		ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name) #^符号开头,$符号结尾 匹配从头到尾
		if ret:
			print("变量名:%s 符合要求...通过正则匹配出来的数据是:%s" % (name, ret.group()))
		else:
			print("变量名:%s 不符合要求..." % name)

if __name__ == '__main__':
	main()