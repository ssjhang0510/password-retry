#密碼重試程式
password = 'a123456'
x = 1
while x <= 3:
	key = input('請輸入使用者密碼: ')
	if key != password:
		x = x + 1
		print('密碼錯誤，還有',4-x,'次機會')
	else:
		print('登入成功')
		break
