import time
import math
k1 = 0
s1 = 0
while s1 < 100:
	s1 = s1 +2**k1
	print("S是%d" % s1)
	time.sleep(0.01)
	k1 = k1 + 1
	print("K是%d" % k1)
	print("--------循环ing-----------")