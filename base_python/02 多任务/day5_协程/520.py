import time
a = 0
while a<3000:
	# print("爱你",a,"次!")
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"爱你",a,"次!")
	a += 1
	time.sleep(1)