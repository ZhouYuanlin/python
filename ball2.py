from random import choice
direction = ['left', 'center', 'right']
ysum = 0
csum = 0
for i in range(0,5):
	print "please input your direction"
	print "direction is %s"%direction
	you = raw_input()
	com = choice(direction)
	if you == com:
		print "Oops..."
		csum += 1
	elif you != com:
		print "Goals!"
		ysum += 1
while ysum == csum:
 	you = input
 	com = choice(direction)
 	ysum == csum 
	if you == com:
		print "Oops..."
		csum += 1
	elif you != com:
		print "Goals!"
		ysum += 1
print "the score is %d : %d"%(csum,ysum)
		
