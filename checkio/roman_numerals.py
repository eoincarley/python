import pdb

def checkio(n):
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman

        n %= arabic

    return result


#--------------------------------------------#
#
def roman_numerals(data):

	number = int(data)
	denoms = [1000, 500, 100, 50, 10, 5, 1]
	numerals = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
	numeral = ''

	for i in range(0, len(denoms), 2):
		result = number/denoms[i]
		if result > 0:
			if result<4:
				numeral += numerals[i]*int(result)
			elif result==4:
				numeral += numerals[i] + numerals[i-1]	
			elif result==5:
				numeral += numerals[i-1]	
			elif (result>5 and result<9):
				rem = result-5
				numeral += numerals[i-1] + numerals[i]*rem
			elif result==9:
				numeral += numerals[i] + numerals[i-2]

		number -= denoms[i]*result	

	return numeral


#--------------------------------------------#
#
result = roman_numerals(800)

#result1 = checkio(80)

print result
