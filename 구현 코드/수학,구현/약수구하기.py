import math

def get_divisor(num):
	d = []
	length = int(math.sqrt(num))+1
	for i in range(1,length):
		if num % i == 0:
			d.append(i)
			d.append(num//i)
	d.sort()
	return d
