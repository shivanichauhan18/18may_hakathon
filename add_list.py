def add_numbers(number1,number2):
	sum=number1+number2
	print sum
add_numbers(56,12)



def add_number_list(first_list,second_list):
	i=0
	while i<len(first_list):
		sumOfListIndex=first_list[i]+second_list[i]
		print sumOfListIndex
		i=i+1
add_number_list([50,60,10],[10,20,13])