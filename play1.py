from random import randint
f = file('/Users/mumutongxue/grade.txt','r')
s = f.read()
f.close()
grade = s.split()
time = int(grade[0])
minT = int(grade[1])
sumT = int(grade[2])
time += 1
minT += 1
print 'the %d time'%(time)
guess = randint(1,100)
print 'guess the number:'
you = input()

while you != guess:
	if you - guess < 0:
		print 'your number is smaller,please guess again'
		you = input()
		minT += 1
	else:
		print 'your number is bigger,please guess again'
		you = input()
		minT += 1
print 'guess %d times'%(minT)
print 'Congratulation!'
sumT += minT
if int(grade[1]) != 0 :
	if minT < grade[1]:
		grade[1] = '%d'%(minT)
		print 'min time is %s'%(grade[1])
print 'the sum of playing is %d'%(sumT)
grade[0] = '%d'%(time)
grade[2] = '%d'%(sumT)
s = " ".join(grade)
f = file('/Users/mumutongxue/grade.txt','w')
f.write(s)
f.close()

