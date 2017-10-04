for x in range (1,101):
	if x%3 and x&5:
		print "FizzBuzz"
	elif x%3:
		print "Fizz"
	elif x%5:
		print "Buzz"
	else:
		print x
