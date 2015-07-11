f = file('/Users/mumutongxue/output.txt')
lines = f.readlines()
results = []
f.close()
for line in lines:
	 data = line.split()
	 sum = 0
	 for i in data[1:]:
	 	if int(i) < 60:
	 		print 'go in' 
	 		continue
	 	sum += int(i)
	 result = '%s\t : %d\n'%(data[0], sum)
	 results.append(result)
output = file('/Users/mumutongxue/2.txt', 'w')
output.writelines(results)
output.close()