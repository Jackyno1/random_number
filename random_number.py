#猜數字遊戲
#產生一個隨機整數1~100
#使用者重複輸入數字
#猜對印出"終於猜對了!"
#猜錯要告訴他 比答案大/小

#印出猜了幾次

import random
while True:
	lowlimit = input('請輸入最小值:')
	lowlimit = int(lowlimit)
	uplimit = input('請輸入最大值:')
	uplimit = int(uplimit)
	num = random.randint(lowlimit, uplimit)
	content = print('請輸入數字',lowlimit, '~', uplimit)
	i = 0
	while True:
		keyin = input(content)
		keyin = int(keyin)
		if keyin > num:
			print('比答案大')
			i = i + 1
		elif keyin < num:
			print('比答案小')
			i = i + 1
		else:
			print('終於猜對了!')
			print('你猜了', i + 1, '次')
			break
