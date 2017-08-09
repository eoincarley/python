import pdb
import numpy as np

def safe_pawns(pawns):

	pawns = list(pawns)
	safe_pawns = 0
	ranks = range(1,9)
	ranks = [str(arg) for arg in ranks]
	files = ['a', 'b', 'c' , 'd', 'e', 'f', 'g', 'h']

	for i in ranks:
		if i=='1':
			pos = [x+i for x in files]
		else:
			pos = pos + [x+i for x in files] 	
	pos = np.array(pos)

	for i in pawns:
		index = np.where(pos==i)[0][0]

		if i[1] != '1':
			if i[0]=='a': 
				safe_index = [index-7]
			elif i[0]=='h': 
				safe_index = [index-9]
			else: 
				safe_index = [index-7, index-9]


			if len(safe_index) == 1: 
				if pos[safe_index] in pawns: safe_pawns += 1
			else:	
				if pos[ safe_index[0] ] in pawns or pos[ safe_index[1] ] in pawns: safe_pawns += 1
			print i	
			print safe_pawns	

	return safe_pawns


result = safe_pawns({"a2","b4","c6","d8","e1","f3","g5","h8"})

print result


#if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
 #   assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
  #  assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
