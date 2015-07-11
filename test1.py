from random import randint
print 'Please input :your name'
name = raw_input() 

f = open('/Users/mumutongxue/game.txt')
lines = f.readlines()
f.close()

scores = {} 

for l in lines:
	s = l.split()
	scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
	score = [0, 0, 0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
	avg_times = float(total_times) / game_times
else:
	avg_times = 0

print '%s , you played %d times, the smallest time is %d ,ave is %.2f '%(name, game_times, min_times, avg_times)
num = randint(1, 100)
times = 0
print 'guess the number:'
you = input()
while you != num:
	if you > num:
		times += 1
		print 'too big, guess again:'
		you = input()
	else:
		times += 1
		print 'too small, guess again:'
		you = input()
print 'Congatulation! you guess %d times'%(times)
if times < min_times or game_times == 0:
	min_times = times
total_times += times
game_times += 1
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
	line = n + ' ' + ' '.join(scores[n]) + '\n'
	result += line
f = open('/Users/mumutongxue/game.txt','w')
f.write(result)
f.close()
