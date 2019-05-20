def menu(day):
	if day == "monday":
		food="dal bati"
	elif day == "tuesday":
		food="sabzi puri"
	else:
		food="chhole bhature"
	print "kya mai print ho jaungi?:"
	return food
	print "lekin mai to pakka print nhi ho paungi"

print menu("monday")
print menu("tuesday")
print menu("wednesday")
	