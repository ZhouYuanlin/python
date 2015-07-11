from random import randint
a = randint(1,100)
print "guess what's the number I think"
b = input()
while a!=b :
	if a < b :
		print "too big!"
	if a > b :
		print "too small!"
	print "input again!"
	b = input()
print "Congratulation!"