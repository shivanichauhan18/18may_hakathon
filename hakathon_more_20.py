number=[50,40,23,70,56,12,5,10,7]
i=0
count=0
sum=0
while i<len(number):
	if number[i]>20 and number[i]<40:
		sum=sum+1
		count=count+number[i]
	i=i+1
print sum
print count