from random import randint
def compare(a,b):
	if a<b:
		if b - a < 5:
			print "%d is big,but close\n"%b
		else:
			print "%d is big, but too far\n"%b
	if a>b:
		if a - b <5:
			print "%d is small,but close\n"%b
		else:
			print "%d is small,but too far\n"%b
a = randint(0, 1000)
print "guess the number\n"
b = input();
print
while a != b:
	compare(a,b)
	print "guess again\n"
	b = input()
	print 
print "Bingo,%d is right!\n"%a


