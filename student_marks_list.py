student_marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
list_length=len(student_marks)
index=0
more_than50=0
less_than50=0
less_than_marks_50=0
more_than_marks_50=0
while index<list_length:
	if student_marks[index]<50:
		less_than50=less_than50+student_marks[index]
		less_than_marks_50=less_than_marks_50+1
	else:
		more_than50=more_than50+student_marks[index]
		more_than_marks_50=more_than_marks_50+1
	index=index+1
print "marks more_than50 is:"+str(more_than50),"and our 50 se jyada student_marks ki no is"+str(more_than_marks_50)
print "marks of less then 50 is:"+str(less_than50) ,"and our 50 se kam student_marks ki no is "+str(less_than_marks_50)



total=more_than_marks_50+less_than_marks_50

print total