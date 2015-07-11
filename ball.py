from random import choice
print 'Choice one side to shoot:'
print 'left, center, right'
you = raw_input()
print 'you kicked '+you
direction = ['left', 'center', 'right']
com = choice(direction)
print 'Computer saved ' + com
if you != com:
	print 'Goal!'
else:
	print "Oops..."
