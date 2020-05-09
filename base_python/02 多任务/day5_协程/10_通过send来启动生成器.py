def create_num(all_num):
	a,b = 0, 1
	current_num = 0
	while current_num < all_num:
		#print(a)
		ret = yield a #如果一个函数中有yield语句, 那么这个就不在是函数,而是一个生成器的模板
		print(">>>>ret>>>>",ret)
		a,b = b, a+b 
		current_num += 1

obj = create_num(50)


ret = next(obj)
print(ret)

ret = obj.send("hhhhhhhhh")
print(ret)