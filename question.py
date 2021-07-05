from answer import *
question_block = ['what','where','how','when','who']
names_recognised = ['dbg','ss','brj','kj','ss','bkb','dt','pmp','rj','db','am','drm','bp']
program_recognised = ['doese','cm','dons','sos','dob','docse','dome','docage','doce','doeaee']
#print("Nebula: ") 	
def question(*args):
	k = 0
	question_word = str(args[0])
	print(args[0])
	print(args[1])
	print(args[2])
	if (args[2]=="your" or args[2]=="nebula" or args[2]=="you"):
		result= str(about_me(question_word))
		return result
	name_word = str(args[1])
	for i in question_block:
		if (question_word==i):
			for j in names_recognised:
				if(name_word==j):
					k=1
					break
				else:
					k = 2
		if(k==1):
			return answer(args[0],args[1])	
			break
		else:
			continue

def questions(*args):
	k=0
	question = args[0]
	initial =  args[1]
	position = args[2]
	for i in question_block :
		if (question == i):
			for j in program_recognised:
				if (program == j):
					k=1
					break
				else:
					k=2
		if(k==1):
			answer(question,initial,position)
			break
		else:
			continue


def about_me(question):
	if (question=='what'):
		return("I am a chatbot. I help to provide some information on some topic on KU.")
	elif(question == "who"):
		return("I am a chatbot.")
	elif(question == "how"):
		return("I help by providing information which is stored in my database.")
	elif(question=="where"):
		return("I was born in Allen Maharjan's computer.")
	#print("You are asking {} question about Nebula".format(question))

