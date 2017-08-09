import pdb

def non_unique(data):
	
	data_new = data*1
	
	for elem in data:
		if data.count(elem) == 1: data_new.remove(elem)
	
	return data_new
	

check_list = [1,2,2,3,4,5,5,10,10]

check_list = non_unique(check_list)

print check_list			
