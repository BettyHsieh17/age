driving = input('請問您是否有開過車')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit
age = input('請問您幾歲?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過測驗')
	else:
		print('怎麼可能 你在哪開的')
elif driving =='沒有':
	if age >= 18:
		print('該去考駕照囉')
	else:
		print('再等幾年就可以了')
