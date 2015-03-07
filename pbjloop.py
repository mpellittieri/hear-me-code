bread = input("How many slices of bread do you have?")
peanutbutter = input("How much peanut butter do you have?")
jelly = input ("How much jelly do you have?")
sandwich = 1

while bread >= 2 and peanutbutter >=1 and jelly >=1:
	print "I'm making sandwich #{0}".format(sandwich)

	bread = bread - 2

	peanutbutter = peanutbutter - 1
	jelly = jelly - 1 
	sandwich = sandwich + 1

print "All done; only had enough bread for {0} sandwiches.".format(sandwich - 1)
