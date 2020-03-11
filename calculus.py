import re

regex = re.compile('[^0-9+\-*/()]')


def compute(calculation):
	print('a')
	try:
		print('b')
		if clean(calculation):
			raise Exception
		print('d')
		answer = eval(calculation)
		print(answer)
		return answer
	except:
		raise Exception


def clean(calculation):
	print('c')
	print(regex.match(calculation))
	return bool(regex.match(calculation))