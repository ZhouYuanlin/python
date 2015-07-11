from random import randint
a = randint(1,100)
print "guess my number?\n"
b = input()
print
while b != a:
    if b > a:
        if (b-a)<5:
            print "%d is too big,but close\n"%b
        else:
            print"%d is too big,and too far\n"%b
    if b < a:
        if (a-b)<5:
            print "%d is too small,but close\n"%b
        else:
            print"%d is too small,and too far\n"%b
    print "guess again\n"
    b = input()
    print
print "Bingo, %d is right\n"%b

			