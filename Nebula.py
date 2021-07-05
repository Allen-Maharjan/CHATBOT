import spacy
from pathlib import Path
import random
from greetings import greetings
from question import *
from parse import *
#from train_spacy import soldiers

def chatbot(info):
	model=None
	output_dir=Path("/home//allen//Documents//fourth year//chatbot//chatbot")
	n_iter=100
	#print("Nebula: Please enter only one question or setence. ")
	real_data= ''
	nlp = spacy.load(output_dir)
	name,initials,initial,position = '','','',''
	real_data = str(info)
	#print(real_data)
	# if (real_data != ''):
	new_data=parse(real_data)
	#print(new_data)
	data = nlp(new_data)
	#print(data)
	#return data
	# print("NEBULA: ",end='')
	for token in data.ents:
		if(token.label_== "person" ):
			name = str(token.text)
			count = len(name)
			if (count>4):
				initials=name_parse(name)
			else:
				initials = name
		elif(token.label_ == 'position'):
			position = str(token.text)
			count = len(position)
			if (count<5):
				initial = name_parse(position)
			else:
				initial = position
		elif(token.label_== 'program'):
			program = str(token.text)
			count = len(program)
			if (count<8):
				initial = name_parse(program)
			else:
				initial = program
	for token in data.ents:
		print(token.text,token.label_)
		if (token.label_=="question" or token.text=='who'):
			if (position ==''):	
				result=question(token.text,initials,name)
				print (result)
				return result
			elif (name == ''):
				result=questions(token.text,initial,position)
				return result
		if(token.label_=="GREET"):
			result=greetings(name)
			print('resutl is ',result)
			return result
		if (token.label_=="QUIT"):
			exit()
