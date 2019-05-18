mixed_list=["rahul","kaavay",12,5.0,34,9.4]
print type(mixed_list)
print mixed_list

mixed_list[1]="shivani"
print mixed_list

mixed_list[5]="shivi"
print mixed_list

num2=len(mixed_list)
print num2

mixed_list.append("jatin")
print mixed_list
print len(mixed_list)


mixed_list.pop(3)
print mixed_list

print len(mixed_list)


print "length of the list is",len(mixed_list),mixed_list.pop(2)

print "length of the list is",len(mixed_list),mixed_list.pop(2)

if "shivani" in mixed_list:
	print True
else:
	print False
	
