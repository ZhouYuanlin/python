from random import choice
sum = 0
dircation = ['left', 'center', 'right']
for i in range(0,5):
	print "Choice one side to shoot:"
	print "left, center, right"
	sho = raw_input()
	com = choice(dircation)
	if sho == com:
		print "Oops..."
	else:
		print "Goal!"
		sum += 1

print "total is %d"%sum

