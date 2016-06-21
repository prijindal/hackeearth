for i in xrange(input()):
	s = raw_input()
	suvojit = s.count("SUVOJIT")
	suvo = s.count("SUVO") - suvojit
	print("SUVO = "+ str(suvo) +", SUVOJIT = "+str(suvojit) +"")
