def add_numbers(add_value1,add_value2):
	sum=add_value1+add_value2
	print sum
add_numbers(56,12)



def add_number_list(first_list,second_list):
	i=0
	while i<len(first_list):
		sum=first_list[i]+second_list[i]
		print sum
		i=i+1
add_number_list([50,60,10],[10,20,13])