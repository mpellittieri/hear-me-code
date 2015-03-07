NumberOfBottles = range(100,0,-1)

for number in NumberOfBottles:
		print "{0} bottles of beer on the wall, {0} bottles of beer! \n If one of those bottles should happen to fall, {1} bottles of beer on the wall. \n".format(str(number), str(number-1))
	
