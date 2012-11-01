import numpy as np

b = np.zeros(10000)
line_num = 0

def judgeGender1():
	F = open('input.data', 'r')
	f = open('output.data', 'a')
	for line in F.readlines():
		a = line.split()
		if a[0] > a[1]:
			f.write(str(1)+"\n")
		else:
			f.write(str(2)+"\n")
		line_num+=1
	F.close()
	f.close()

def judgeGender2():
	F = open('input.data', 'r')
	for line in F.readlines():
		a = line.split()
		if a[0] > a[1]:
			b[line_num] = 1
		else:
			b[line_num] = 2
		line_num+=1
	F.close()
	f = open('output.data', 'w')
	for i in range(line_num):
		f.write(str(int(b[i]))+"\n")
	f.close()

#judgeGender1()
judgeGender2()	# supposed to be faster since less IO