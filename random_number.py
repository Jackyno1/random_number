#猜數字遊戲
#產生一個隨機整數1~100
#使用者重複輸入數字
#猜對印出"終於猜對了!"
#猜錯要告訴他 比答案大/小

import random
while True:
	num = random.randint(1,100)
	while True:
		keyin = input('請輸入數字1~100:')
		keyin = int(keyin)
		if keyin > num:
			print('比答案大')
		elif keyin < num:
			print('比答案小')
		else:
			print('終於猜對了!')
			break
