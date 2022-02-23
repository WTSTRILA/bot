import math

class Result:
	def __init__(message, square, room):
		message.square = square
		message.room = room
		
	def ofice(message):
		if message.square <= 20:
			print (f'Вам будет достаточно 1 огнетушителей ВВК-2')
		elif message.square > 20 and message.square < 100:
			if message.room == 0:
				a = math.ceil(message.square/20)
				return(f'Вам будет достаточно {a} огнетушителей ВВК-3.5')
			elif message.room > 0: 
				div = message.square - (message.room * 20)
				b = math.ceil(div/20)
				if div < 20:
					return(f'Вам будет достаточно {message.room} огнетушителей ВВК-2')
				else:
					return(f'Вам будет достаточно {b + message.room} огнетушителей ВВК-3.5')
		elif message.square > 100:
			c = math.ceil(message.square/10)
			q = math.ceil(c/3.5)
			return(f'Вам будет достаточно {q} огнетушителей ВВК-3.5 и 1 огнетушитель ВП-5')
		
	def proizvodstvo(message):
		if message.square <= 25:
			return ('Вам будет достаточно 2 огнетушителя ВП-5')
		elif message.square > 25 and message.square < 50:
			return('Вам будет достаточно 3 огнетушителя ВП-5')
		elif message.square > 50 and message.square < 150:
			return('Вам будет достаточно 4 огнетушителя ВП-5')
		elif message.square > 150 and message.square < 250:
			return('Вам будет достаточно 6 огнетушителя ВП-5')
		elif message.square > 250 and message.square < 500:
			return('Вам будет достаточно 8 огнетушителя ВП-5')
		elif message.square > 500 and message.square < 1000:
			return ('Вам будет достаточно 16 огнетушителя ВП-5')
		if message.square > 1000: 
			a = []
			while message.square >= 0:
				a.append((message.square // 1000) * 16)
				a.append(message.square % 1000)
				if a[1] <= 25:
					return (f'Вам будет достаточно {2 + int(a[0])} огнетушителя ВП-5')
				elif a[1] > 25 and a[1] < 50:
					return(f'Вам будет достаточно {3 + int(a[0])} огнетушителя ВП-5')
				elif a[1] > 50 and a[1] < 150:
					return(f'Вам будет достаточно {4 + int(a[0])} огнетушителя ВП-5')
				elif a[1] > 150 and a[1] < 250:
					return(f'Вам будет достаточно {6 + int(a[0])} огнетушителя ВП-5')
				elif a[1] > 250 and a[1] < 500:
					return(f'Вам будет достаточно {8 + int(a[0])} огнетушителя ВП-5')
				elif a[1] > 500 and a[1] < 1000:
					return (f'Вам будет достаточно {16 + int(a[0])} огнетушителя ВП-5')

