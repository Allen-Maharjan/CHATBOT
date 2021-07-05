def answer(*args):
	question = args[0]
	name = args[1]
	program = ''
	answers = open('Answers.txt','r')
	line = answers.readlines() 
	if (name == 'ss' or (name == 'co' or program == 'cm')  ):
		if(question=='who'):
			return(line[4])
		elif(question == 'where'):
			return(line[5])
		elif(question == 'how'):
			return(line[6])
	if (name == 'dbg' or (name == 'hod' or program =='dons')):
		if(question=='who'):
			return(line[8])
		elif(question == 'where'):
			return(line[9])
		elif(question == 'how'):
			return(line[10])
	if (name == 'brj' or (name == 'hod' or program =='doese')):
		if(question=='who'):
			return(line[0])
		elif(question == 'where'):
			return(line[1])
		elif(question == 'how'):
			return(line[2])
	if (name == 'kj' or (name == 'dean' or program == 'sos')):
		if(question=='who'):
			return(line[12])
		elif(question == 'where'):
			return(line[13])
		elif(question == 'how'):
			return(line[14])
	if (name == 'bkb' or (name == 'hod' or program == 'docse')):
		if(question=='who'):
			return(line[20])
		elif(question == 'where'):
			return(line[21])
		elif(question == 'how'):
			return(line[22])
	if (name == 'dt' or (name == 'hod' or program == 'dome')):
		if(question=='who'):
			return(line[24])
		elif(question == 'where'):
			return(line[25])
		elif(question == 'how'):
			return(line[26])
	if (name == 'pmp' or (name == 'hod' or program == 'docage')):
		if(question=='who'):
			return(line[28])
		elif(question == 'where'):
			return(line[29])
		elif(question == 'how'):
			return(line[30])
	if (name == 'rj' or (name == 'hod' or program == 'doce')):
		if(question=='who'):
			return(line[32])
		elif(question == 'where'):
			return(line[33])
		elif(question == 'how'):
			return(line[34])
    #if (name == 'db' or (name == 'hod' or program == 'doeaee')):
    # if (name == 'rj' or (name == 'hod' or program == 'doce')):
    # 	if(question=='who'):
    # 		return(line[36])
    # 	elif(question=='where'):
    # 	    return(line[37])
    # 	elif(question=='how'):
    # 	    return(line[38])    	