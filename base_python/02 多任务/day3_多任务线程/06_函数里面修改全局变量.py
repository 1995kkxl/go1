

num = 100 
nums = [11,11]
def test1():
	global num

	num += 100

def test12():
	nums.append(33)

print(num)
print(nums)

test1()
test12()

print(num)
print(nums)