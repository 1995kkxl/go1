import time

def task_1():
	while True:
		print("----1-----")
		time.sleep(0.3)
		yield

def task_2():
	while True:
		print("----2-----")
		time.sleep(0.3)
		yield

def main():
	t1 = task_1()
	t2 = task_2()
	#先让t1运行一会,当t1中遇到yield的时候,再返回到while循环,然后
	#执行t2,当遇到yield的时候,再次切换到t1中
	#这样t1,t2交替运行,最终实现多任务..的协程
	while True:
		next(t1)
		next(t2)

if __name__ == '__main__':
	main()