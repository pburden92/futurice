import re

regex = re.compile('[^0-9+\-*/()]')


def compute(calculation):
	try:
		if clean(calculation):
			raise Exception
		answer = eval(calculation)
		return answer
	except:
		raise Exception


def clean(calculation):
	return bool(regex.match(calculation))
