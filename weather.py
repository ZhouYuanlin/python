# -*- coding:utf-8 -*-
from city import city
import urllib2
import json
cityname = raw_input('请输入你要查询天气的城市：\n')
citycode = city.get(cityname)
if citycode:
		url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%(citycode)
		content = urllib2.urlopen(url).read()
		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = '%s\n%s  %s'%(result['weather'], result['temp1'], result['temp2'])
		print str_temp
else:
	print '没有找到该城市'
