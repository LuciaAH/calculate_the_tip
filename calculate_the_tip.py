def tip(cost):
	t = round(int(cost) * 0.1) #round 四捨五入
	print('在費率10%的狀況下，小費為', t, '總金額為', int(cost) + t)

tip(input('今天帳單多少錢?'))