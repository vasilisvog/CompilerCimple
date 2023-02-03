#Vasileios Vogiannou 3193 cs03193
#Dimitra Machairidou 4108 cs04108

#Globals

import sys
import os
keimeno=open(sys.argv[1],"r")
#Checks true if the file extention is correct
boolextention=(sys.argv[1]).endswith('.ci') 

state=0
lektikiMonada=""
line=0
type=""

etiketa=0
tetrades_me_etiketa=[]
metritis=0
temporary_variables=[]
variables=[]
program_name=""
#check if cimple program has function or procedure
flag=0

SymbolArray=[]
nestingLevel=0
typos = ""
#gia na fenete pantou
MIPS_file_name=((sys.argv[1][:len(sys.argv[1])-2])+"asm")
MIPS_file=open(MIPS_file_name,"w+")
MIPS_file.write("b LMain"+"\n")
#pointer gia tin ektiposi tou mips arxeiou
thesh_MIPS=0
#flag gia elegxo yparksis return
flagReturn=False

#We use one of the methods from  the presentation.
#We check out all the cases one at a time.

def lektikosAnalitis():

	#Use 'global' to change the global variables.
	
	global state,lektikiMonada,line,type,flag
	state=0
	lektikiMonada=""
	type=""
	
	notTelikes=[0,1,2,3,4,5,6,7]
	
	while state in notTelikes:
	
		input=keimeno.read(1)
		if(input == '\r'):
			input=keimeno.read(1)
		if state==0 and (input==" " or input=="\t"):       
			state=0
		elif state==0 and input.isalpha()==True:
			state=1
		elif state==0 and input.isdigit()==True:
			state=2
		elif state==0 and input=="+":
			state="+"
			type="addOperation"
		elif state==0 and input=="-":
			state="-"
			type="addOperation"
		elif state==0 and input=="*":
			state="*"
			type="mulOperation"
		elif state==0 and input=="/":
			state="/"
			type="mulOperation"
		elif state==0 and input=="=":
			state="="
			type="relOperation"
		elif state==0 and input=="<":
			state=3
		elif state==0 and input==">":
			state=4
		elif state==0 and input==":":
			state=5
		elif state==0 and input==";":
			state=";"
			type="delimiter"
		elif state==0 and input==",":
			state=","
			type="delimiter"
		elif state==0 and input=="[":
			state="["
			type="groupSymbol"
		elif state==0 and input=="]":
			state="]"
			type="groupSymbol"
		elif state==0 and input=="(":
			state="("
			type="groupSymbol"
		elif state==0 and input==")":
			state=")"
			type="groupSymbol"
		elif state==0 and input=="{":
			state="{"
			type="groupSymbol"
		elif state==0 and input=="}":
			state="}"
			type="groupSymbol"
		elif state==0 and input==".":
			state=7
		elif state==0 and input=="\n":
			state=0 
			line=line+1
		elif state==0 and input=="#":
			state=6
		elif state==0 and input=="":
			print("eof")
			exit(0)
		
		elif state==1 and (input==" " or input=="\t"):
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input.isalpha()==True:
			state=1
		elif state==1 and input.isdigit()==True:
			state=1
		elif state==1 and input=="+":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="-":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="*":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="/":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="=":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="<":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==">":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==":":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==";":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==",":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="[":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="]":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="(":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==")":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="{":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="}":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input==".":
			state="anagnoristiko"
			type="identifier"
		elif state==1 and input=="\n":
			state="anagnoristiko"
			type="identifier"
			line=line+1
			
		elif state==2 and (input==" " or input=="\t"):
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input.isalpha()==True:
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input.isdigit()==True:
			state=2
		elif state==2 and input=="+":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="-":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="*":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="/":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="=":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="<":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==">":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==":":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==";":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==",":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="[":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="]":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="(":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==")":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="{":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="}":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input==".":
			state="arithmitikiStathera"
			type="number"
		elif state==2 and input=="\n":
			state="arithmitikiStathera" 
			type="number"
			line=line+1
			
		elif state==3 and (input==" " or input=="\t"):
			state="<"
			type="relOperation"
		elif state==3 and input.isalpha()==True:
			state="<"
			type="relOperation"
		elif state==3 and input.isdigit()==True:
			state="<"
			type="relOperation"
		elif state==3 and input=="+":
			state="<"
			type="relOperation"
		elif state==3 and input=="-":
			state="<"
			type="relOperation"
		elif state==3 and input=="*":
			state="<"
			type="relOperation"
		elif state==3 and input=="/":
			state="<"
			type="relOperation"
		elif state==3 and input=="=":
			state="<="
			type="relOperation"
		elif state==3 and input=="<":
			state="<"
			type="relOperation"
		elif state==3 and input==">":
			state="<>"
			type="relOperation"
		elif state==3 and input==":":
			state="<"
			type="relOperation"
		elif state==3 and input==";":
			state="<"
			type="relOperation"
		elif state==3 and input==",":
			state="<"
			type="relOperation"
		elif state==3 and input=="[":
			state="<"
			type="relOperation"
		elif state==3 and input=="]":
			state="<"
			type="relOperation"
		elif state==3 and input=="(":
			state="<"
			type="relOperation"
		elif state==3 and input==")":
			state="<"
			type="relOperation"
		elif state==3 and input=="{":
			state="<"
			type="relOperation"
		elif state==3 and input=="}":
			state="<"
			type="relOperation"
		elif state==3 and input==".": 
			state="<"
			type="relOperation"
		elif state==3 and input=="\n":
			state="<"
			type="relOperation"	
			line=line+1
		
		elif state==4 and (input==" " or input=="\t"):
			state=">"
			type="relOperation"
		elif state==4 and input.isalpha()==True:
			state=">"
			type="relOperation"
		elif state==4 and input.isdigit()==True:
			state=">"
			type="relOperation"
		elif state==4 and input=="+":
			state=">"
			type="relOperation"
		elif state==4 and input=="-":
			state=">"
			type="relOperation"
		elif state==4 and input=="*":
			state=">"
			type="relOperation"
		elif state==4 and input=="/":
			state=">"
			type="relOperation"
		elif state==4 and input=="=":
			state=">="
			type="relOperation"
		elif state==4 and input=="<":
			state=">"
			type="relOperation"
		elif state==4 and input==">":
			state=">"
			type="relOperation"
		elif state==4 and input==":":
			state=">"
			type="relOperation"
		elif state==4 and input==";":
			state=">"
			type="relOperation"
		elif state==4 and input==",":
			state=">"
			type="relOperation"
		elif state==4 and input=="[":
			state=">"
			type="relOperation"
		elif state==4 and input=="]":
			state=">"
			type="relOperation"
		elif state==4 and input=="(":
			state=">"
			type="relOperation"
		elif state==4 and input==")":
			state=">"
			type="relOperation"
		elif state==4 and input=="{":
			state=">"
			type="relOperation"
		elif state==4 and input=="}":
			state=">"
			type="relOperation"
		elif state==4 and input==".": 
			state=">"
			type="relOperation"
		elif state==4 and input=="\n":
			state=">"
			type="relOperation"	
			line=line+1
			
		elif state==5 and (input==" " or input=="\t"): 
			state=":"
		elif state==5 and input.isalpha()==True:
			state=":"
		elif state==5 and input.isdigit()==True:
			state=":"
		elif state==5 and input=="+":
			state=":"
		elif state==5 and input=="-":
			state=":"
		elif state==5 and input=="*":
			state=":"
		elif state==5 and input=="/":
			state=":"
		elif state==5 and input=="=":
			state=":="
			type="assignment"
		elif state==5 and input=="<":
			state=":"
		elif state==5 and input==">":
			state=":"
		elif state==5 and input==":":
			state=":"
		elif state==5 and input==";":
			state=":"
		elif state==5 and input==",":
			state=":"
		elif state==5 and input=="[":
			state=":"
		elif state==5 and input=="]":
			state=":"
		elif state==5 and input=="(":
			state=":"
		elif state==5 and input==")":
			state=":"
		elif state==5 and input=="{":
			state=":"
		elif state==5 and input=="}":
			state=":"
		elif state==5 and input==".":
			state=":"
		elif state==5 and input=="\n":
			state=":" 
			line=line+1
		
		elif state==6:
			if(input=="#"):
				state=0
			elif(input=="\n"):
				line=line+1
				state=6
			elif input=="":
				print("eof")
				exit(0)
			else:
				state=6

		elif state==7 and (input==" " or input=="\t"):       
			state=7
		elif state==7 and input.isalpha()==True:
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input.isdigit()==True:
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input=="+":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input=="-":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="*":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="/":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="=":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="<":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input==">":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input==":":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input==";":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input==",":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="[":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="]":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input=="(":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input==")":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input=="{":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input=="}":
			print("eop.Unexpected input.")
			exit(0)		
		elif state==7 and input==".":
			print("eop.Unexpected input.")
			exit(0)
		elif state==7 and input=="\n":
			state=7 
			line=line+1
		elif state==7 and input=="#":
			state=6
		elif state==7 and input=="":
			break			
		else:
			print("line %d:unknown input %d #%c#"%(line,state,input))
			exit(0)
		
		#Add input in word (sum up)
		
		if state==0:
			lektikiMonada=""
		elif len(lektikiMonada)<30:
			lektikiMonada=lektikiMonada+input
		elif state==6:
			#No limit for the comment
			continue
		else:
			print("line %d:identifier out of range"%line)
			exit(0)
		
	test=["anagnoristiko","arithmitikiStathera","<",">",":","#"]
	
	if state in test:
		#Moves the cunsor one point left
		keimeno.seek(-1,1)
		#Ingores last input
		lektikiMonada=lektikiMonada[0:len(lektikiMonada)-1]
	
	#Check up with the absolute value of the limit 
	
	if state=="arithmitikiStathera":
		if  int(lektikiMonada) > (2**32-1) :
			print("line %d:number out of range"%line)
			exit(0)
	
	if lektikiMonada=="program":
		state="program"
		type="keyword"
	elif lektikiMonada=="declare":
		state="declare"
		type="keyword"
	elif lektikiMonada=="if":
		state="if"
		type="keyword"
	elif lektikiMonada=="else":
		state="else"
		type="keyword"
	elif lektikiMonada=="while":
		state="while"
		type="keyword"
	elif lektikiMonada=="switchcase":
		state="switchcase"
		type="keyword"
	elif lektikiMonada=="forcase":
		state="forcase"
		type="keyword"
	elif lektikiMonada=="incase":
		state="incase"
		type="keyword"
	elif lektikiMonada=="case":
		state="case"
		type="keyword"
	elif lektikiMonada=="default":
		state="default"
		type="keyword"
	elif lektikiMonada=="not":
		state="not"
		type="keyword"
	elif lektikiMonada=="and":
		state="and"
		type="keyword"
	elif lektikiMonada=="or":
		state="or"
		type="keyword"
	elif lektikiMonada=="function":
		state="function"
		type="keyword"
		flag=1
	elif lektikiMonada=="procedure":
		state="procedure"
		type="keyword"
		flag=2
	elif lektikiMonada=="call":
		state="call"
		type="keyword"
	elif lektikiMonada=="return":
		state="return"
		type="keyword"
	elif lektikiMonada=="in":
		state="in"
		type="keyword"
	elif lektikiMonada=="inout":
		state="inout"
		type="keyword"
	elif lektikiMonada=="input":
		state="input"
		type="keyword"
	elif lektikiMonada=="print":
		state="print"
		type="keyword"

def program():

	#change global 
	global program_name
	if state=="program": 
		lektikosAnalitis()
		if state=="anagnoristiko":
			program_name=lektikiMonada
			lektikosAnalitis()
			record_scope(program_name)
			block(program_name) 
			delete_scope()
		else:
			print("line %d:program name exprected"%line)
			exit(0)
	else:
		print ("line %d:the keyword 'program' was expected"%line)
		exit(0)

def block(name):

	global SymbolArray, flagReturn
	declarations()
	subprograms()
	if name!= program_name:
		#pername pliroforia pros ta pano
		SymbolArray[1][1][len(SymbolArray[1][1]) - 1][0][2] = nextquad()
	genquad("begin_block",name,"_","_")

	flagReturn = False	
	statements()
	#halt kanei mono to program
	if name==program_name:
		genquad("halt","_","_","_")
		if flagReturn==True:
			#elegxo gia ta return
			print("line %d: return found inside program %s"%(line,program_name))
			exit(0)
	else:
		#pername pliroforia pros ta pano
		SymbolArray[1][1][len(SymbolArray[1][1]) - 1][0][3] = SymbolArray[0][2]  
		new_entity,nestingLevelEntity=search_entity(name)
		#elegxo gia ta return
		if new_entity[1][0]=='function' and flagReturn==False:
			print("line %d: return not found inside function %s"%(line,name))
			exit(0)
		elif new_entity[1][0]=='procedure' and flagReturn==True:
			print("line %d: return found inside procedure %s"%(line,name))
			exit(0)      
        
	genquad("end_block",name,"_","_")
	
def declarations():

	while state=="declare":
		lektikosAnalitis()
		varlist()
		if state==";":
			lektikosAnalitis()
		else:
			print("line %d:';'not found"%line)
			exit(0)

def varlist():
	
	#change global
	global variables
	if state=="anagnoristiko":
		variables.append(lektikiMonada)
		offset=SymbolArray[0][2]
		new_entity=[lektikiMonada,'variable',offset]
		record_entity(new_entity,"")
		lektikosAnalitis()
		while state==",":
			lektikosAnalitis()
			if state=="anagnoristiko":
				variables.append(lektikiMonada)
				offset=SymbolArray[0][2]
				new_entity=[lektikiMonada,'variable',offset]
				record_entity(new_entity,"")
				lektikosAnalitis()
			else:
				print("line %d:'anagnoristiko' not found")
				exit(0)
	else:
		print("line %d:'anagnoristiko' not found")
		exit(0)
				
def subprograms(): 
	global typos
	
	while state=="function" or state=="procedure":
		typos = state
		lektikosAnalitis()
		subprogram()
		
def subprogram(): 

	#gia tin anathesi ton arguments
	global typos
	if state=="anagnoristiko":
		#topiki name gia perasma
		name=lektikiMonada
		#otan vro to f/p den gnorizo to offset
		new_entity=[name,'f/p', "", ""]
		record_entity(new_entity, typos)
		record_scope(name)
		lektikosAnalitis()
		if state=="(":
			lektikosAnalitis()
			formalparlist()
			if state==")":
				lektikosAnalitis()		
				block(name)
				delete_scope()
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'(' not found"%line)
			exit(0)
	else:
		print("line %d:'anagnoristiko' not found"%line)
		exit(0)

def formalparlist():

	if state=="in" or state=="inout":
		formalpitem()
		while state==",":
			lektikosAnalitis()
			formalpitem()
		
def formalpitem():

	if state=="in":
		lektikosAnalitis()
		if state=="anagnoristiko":
			offset=SymbolArray[0][2]
			new_entity=[lektikiMonada,'cv',offset]
			record_entity(new_entity,"in")
			lektikosAnalitis()
		else:
			print("line %d:'anagnoristiko' not found"%line)
			exit(0)
	elif state=="inout":
		lektikosAnalitis()
		if state=="anagnoristiko":
			offset=SymbolArray[0][2]
			new_entity=[lektikiMonada,'ref',offset]
			record_entity(new_entity,"io")
			lektikosAnalitis()
		else:
			print("line %d:'anagnoristiko' not found"%line)
			exit(0)
	else:
		print("line %d:'in' or 'inout' not found"%line)
		exit(0)
		
def statements():
	
	if state=="{":
		lektikosAnalitis()	
		statement()
		while state==";":
			lektikosAnalitis()
			statement()
		if state=="}":  
			lektikosAnalitis()
		else:
			print("line %d:'}' not found"%line)
			exit(0)
	else:
		statement()
		
def statement():

	if state=="anagnoristiko":
		#perasma se value
		value=lektikiMonada
		lektikosAnalitis()
		assignStat(value)
	elif state=="if":
		lektikosAnalitis()
		ifStat()
	elif state=="while":
		lektikosAnalitis()
		whileStat()
	elif state=="switchcase":
		lektikosAnalitis()
		switchcaseStat()
	elif state=="forcase":
		forcaseStat()
	elif state=="incase":
		lektikosAnalitis()
		incaseStat()
	elif state=="call":
		callStat()
	elif state=="return":
		lektikosAnalitis()
		returnStat()
	elif state=="input":
		lektikosAnalitis()
		inputStat()
	elif state=="print":
		lektikosAnalitis()
		printStat()
		
def assignStat(anagnoristiko):

	#e erotima simasiologikou
	new_entity, nestingLevelEntity=search_entity(anagnoristiko)
	if new_entity[1][0]=='function' or new_entity[1][0]=='procedure':
		print("line %d: %s is %s"%(line,anagnoristiko,new_entity[1][0]))
		exit(0)
	#pernoume to anagnoristiko san orisma gia na to vlepei h genquad
	if state==":=":		
		lektikosAnalitis()
		e_place=expression()
		genquad(":=",e_place,"_",anagnoristiko) 
	else:
		print("line %d:':=' not found"%line)
		exit(0)
			
def ifStat(): 

	if state=="(":
		lektikosAnalitis()
		true_B,false_B=condition()
		if state==")":
			lektikosAnalitis()
			backpatch(true_B,nextquad())
			statements()
			ifList=makelist(nextquad())
			genquad("jump","_","_","_")
			backpatch(false_B,nextquad())
			elsepart()
			backpatch(ifList,nextquad())
		else:
			print("line %d:')' not found"%line)
			exit(0)
	else:
		print("line %d:'(' not found"%line)
		exit(0)
		
def elsepart():

	if state=="else":
		lektikosAnalitis()
		statements()
		
def whileStat(): 

	Bquad=nextquad()
	if state=="(":
		lektikosAnalitis()
		true_B,false_B=condition()
		if state==")":
			lektikosAnalitis()
			backpatch(true_B,nextquad())
			statements()
			genquad("jump","_","_",Bquad)
			backpatch(false_B,nextquad())
		else:
			print("line %d:')' not found"%line)
			exit(0)
	else:
		print("line %d:'(' not found"%line)
		exit(0)
			
def switchcaseStat(): 

	#vlepei switch opote kalei tin sinartisi amesos kai ftiaxnei to list
	exitlist=emptylist()
	while state=="case":
		lektikosAnalitis()
		if state=="(":
			lektikosAnalitis()
			cond_true,cond_false=condition()
			if state==")":
				backpatch(cond_true,nextquad())
				lektikosAnalitis()
				statements()
				e=makelist(nextquad())
				genquad("jump","_","_","_")
				exitlist=merge(exitlist,e)
				backpatch(cond_false,nextquad())
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'(' not found"%line)
			exit(0)
			
	if state=="default":
		lektikosAnalitis()
		statements()
		backpatch(exitlist,nextquad())
		
def forcaseStat(): 
	
	#kaloume edo ton lektiko gt allios mas emfanize thn epomenh state
	lektikosAnalitis()
	#vlepei forcase opote kalei tin sinartisi amesos kai ftiaxnei to list
	p1Quad=nextquad()
	exitlist=emptylist()
	while state=="case":
		lektikosAnalitis()
		if state=="(":
			lektikosAnalitis()
			cond_true,cond_false=condition()	
			if state==")":
				backpatch(cond_true,nextquad())
				lektikosAnalitis()
				statements()
				lektikosAnalitis()
				#prepei na do ti kanei to default
				#mazevo pliroforia
				e=makelist(nextquad())
				genquad("jump","_","_",p1Quad)
				exitlist=merge(exitlist,e)				
				backpatch(cond_false,nextquad())
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'(' not found"%line)
			exit(0)
	
	#opos me tin switch alla kanei jump se diaforetika simia
	if state=="default":
		lektikosAnalitis()
		statements()
		genquad("jump","_","_","_")
		backpatch(exitlist,nextquad())
		
def incaseStat(): 
	
	w=newtemp()
	p1Quad=nextquad()
	genquad(":=","1","_",w)
	while state=="case":
		lektikosAnalitis()
		if state=="(":
			lektikosAnalitis()
			cond_true,cond_false=condition()			
			if state==")":
				lektikosAnalitis()
				backpatch(cond_true,nextquad())
				genquad(":=","0","_",w)
				statements()
				backpatch(cond_false,nextquad())
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'(' not found"%line)
			exit(0)
	genquad("=",w,0,p1Quad)
			
def returnStat(): 

	global flagReturn 
	flagReturn=True
	if state=="(":
		lektikosAnalitis()
		e_place=expression()
		if state==")":
			lektikosAnalitis()
			genquad("retv",e_place,"_","_") 
		else:
			print("line %d:')' not found"%line)
			exit(0)
	else:
		print("line %d:'(' not found"%line)
		exit(0)
			
def callStat(): 

	#kaloume edo ton lektiko gt allios mas emfanize thn epomenh state
	lektikosAnalitis()
	if state=="anagnoristiko":
		new_entity, nestingLevelEntity=search_entity(lektikiMonada)
		if new_entity[1][0]!='procedure':
			print("line %d: %s is not procedure"%(line,lektikiMonada))
			exit(0)
		help=lektikiMonada
		lektikosAnalitis()
		if state=="(":
			lektikosAnalitis()
			actualparlist()
			new=newtemp()
			genquad("par",new,"RET","_")
			genquad("call",help,"_","_")
			if state==")":
				lektikosAnalitis()
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'(' not found"%line)
			exit(0)
	else:
		print("line %d:'anagnoristiko' not found"%line) 
		exit(0)
	return new
	
def printStat(): 

	if state=="(":
		lektikosAnalitis()
		e_place=expression()
		genquad("out",e_place,"_","_")
		if state==")":
			lektikosAnalitis()
		else:
			print("line %d:')' not found"%line)
			exit(0)
	else:
		print("line %d:'(' not found"%line)
		exit(0)
			
def inputStat(): 
	
	if state=="(":
		lektikosAnalitis()
		if state=="anagnoristiko":
			#theloume to value tou anagnoristikou ara tin lektiki monada
			genquad("inp",lektikiMonada,"_","_")
			lektikosAnalitis()
			if state==")":
				lektikosAnalitis()
			else:
				print("line %d:')' not found"%line)
				exit(0)
		else:
			print("line %d:'anagnoristiko' not found"%line)
			exit(0)
	else:
		print("line %d:'(' not found"%line)
		exit(0)
		
def actualparlist():

	if state=="in" or state=="inout":
		actualparitem()
		while state == ",":
			lektikosAnalitis()
			actualparitem()
			
def actualparitem(): 

	if state=="in":
		lektikosAnalitis()
		#thelo na paro to onoma tis metavlitis
		onoma=expression()
		genquad("par",onoma,"CV","_")
	elif state=="inout":
		lektikosAnalitis()
		if state=="anagnoristiko":
			#theloume to value tou anagnoristikou ara tin lektiki monada
			genquad("par",lektikiMonada,"REF","_")
			lektikosAnalitis()
		else:
			print("line %d:'anagnoristiko' not found"%line)
			exit(0)
	else:
		print("line %d:'in' or 'inout' not found"%line)
		exit(0)

def condition():

	true_q1,false_q1=boolterm()
	while state=="or":
		backpatch(false_q1,nextquad())
		lektikosAnalitis()
		true_q2,false_q2=boolterm()		
		true_q1=merge(true_q1,true_q2)
		false_q1=false_q2
	#thelo na mou dinei
	true=true_q1
	false=false_q1
	return true,false
			
def boolterm():

	true_r1,false_r1=boolfactor()
	while state=="and":
		backpatch(true_r1,nextquad())
		lektikosAnalitis()
		true_r2,false_r2=boolfactor()	
		true_r1=true_r2
		false_r1=merge(false_r1,false_r2)
	#thelo na mou dinei
	true=true_r1
	false=false_r1
	return true,false
		
def boolfactor():

	if state=="not":
		lektikosAnalitis()
		if state=="[":
			lektikosAnalitis()
			true_B,false_B=condition()		
			if state=="]":
				lektikosAnalitis()
				true_R=false_B
				false_R=true_B
				return true_R,false_R
			else:
				print("line %d:']' not found"%line)
				exit(0)
		else:
			print("line %d:'[' not found"%line)
			exit(0)
	elif state=="[":
		lektikosAnalitis()
		true_B,false_B=condition()		
		if state=="]":
			lektikosAnalitis()
			true_R=true_B
			false_R=false_B
			return true_R,false_R
		else:
			print("line %d:']' not found"%line)
			exit(0)
	else:
		e1_place=expression()
		relop=REL_OP()
		e2_place=expression()
		true_R=makelist(nextquad())
		genquad(relop,e1_place,e2_place,"_")
		false_R=makelist(nextquad())
		genquad("jump","_","_","_")
		return true_R,false_R	
		
def expression(): 

	optionalSign()
	t1_place=term()
	while state=="+" or state=="-":
		if state=="+":
			operator="+"
		else:
			operator="-"
		lektikosAnalitis()
		t2_place=term()
		w=newtemp()
		genquad(operator,t1_place,t2_place,w)
		t1_place=w
	#thelo na mou dinei
	e_place=t1_place
	return e_place
	
def term(): 

	f1_place=factor()
	while state=="*" or state=="/":
		if state=="*":
			operator="*"
		else:
			operator="/"
		lektikosAnalitis()
		f2_place=factor()
		w=newtemp()
		genquad(operator,f1_place,f2_place,w)
		f1_place=w
	#thelo na mou dinei
	t_place=f1_place
	return t_place
		
		
def factor(): 
	
	if state=="arithmitikiStathera":
		#pernoume to value tis staferas
		f_place=lektikiMonada
		lektikosAnalitis()
		return f_place
	elif state=="(":
		lektikosAnalitis()
		f_place=expression()         
		if state==")":
			lektikosAnalitis()
			#to valame edo giati xtipouse gia {
			return f_place
		else:
			print("line %d:')' not found"%line)
			exit(0)
	elif state=="anagnoristiko":
		f_place=lektikiMonada
		lektikosAnalitis()
		f_place=idtail(f_place)
		return f_place
	else:
		print("line %d:'arithmitikiStathera' not found"%line)
		exit(0)
		
def idtail(f_place): 

	#e erotima simasiologikou
	new_entity, nestingLevelEntity=search_entity(f_place)	
	#xrisi gia klisi synartisis ara otan kalite prepei na vlepei to onona tis
	if state=="(":
		if new_entity[1][0]!='function':
			print("line %d: %s is not function"%(line,f_place))
			exit(0)
		lektikosAnalitis()
		actualparlist()
		new=newtemp()
		genquad("par",new,"RET","_")
		genquad("call",f_place,"_","_")
		if state==")":
			lektikosAnalitis()
		else:
			print("line %d:')' not found"%line)
			exit(0)
	else:
		if new_entity[1][0]=='function' or new_entity[1][0]=='procedure':
			print("line %d: %s is %s"%(line,f_place,new_entity[1][0]))
			exit(0)
		return f_place
	#to valame edo gt ekane return prin parei ton epomeno lektiko kai eixe state tin parenthesi eno thelame operator
	return new

def optionalSign():

	if state=="+" or state=="-":
		lektikosAnalitis()
		
def REL_OP():

	if state=="=":
		relational_operation="="
	elif state=="<=":
		relational_operation="<="
	elif state==">=":
		relational_operation=">="
	elif state==">":
		relational_operation=">"
	elif state=="<":
		relational_operation="<"
	elif state=="<>":
		relational_operation="<>"
	else:
		print("line %d:'relational_operation' not found"%line)
		exit(0)
	lektikosAnalitis()
	return relational_operation
	
def nextquad():

	return etiketa
	
def genquad(op,x,y,z):

	#To change global variables
	global tetrades_me_etiketa,etiketa
	
	new_tme=[etiketa,op,x,y,z]
	tetrades_me_etiketa.append(new_tme)
	etiketa=etiketa+1
	
def newtemp():
	
	#To change global variables
	global metritis,temporary_variables
	
	new_tv= "T_" + str(metritis)
	temporary_variables.append(new_tv)
	metritis=metritis+1
	
	offset=SymbolArray[0][2]
	new_entity=[new_tv,'temporary_variable',offset]
	record_entity(new_entity,"")
	
	return new_tv
	
def emptylist():

	return []
	
def makelist(x):

	return [x]
	
def merge(l1,l2):

	return l1+l2
	
def backpatch(list,z):

	#To change global variables
	global tetrades_me_etiketa
	#trexei tis listes kai tsekarei ta koina oste na kanei thn allagi
	for i in list:
		for j in range(len(tetrades_me_etiketa)):
			if tetrades_me_etiketa[j][0]==i:
				tetrades_me_etiketa[j][4]=z
				break
				
def get_program_C():

	if (flag==1 or flag==2):
		print("Function or procedure found so no c-file made")
		return
	else:
		#allazo kataliksi
		new_file_name=((sys.argv[1][:len(sys.argv[1])-3])+".c")
		new_file=open(new_file_name,"w+")
		#write 'main'
		new_file.write("int main(){\n")
		#write variables
		for i in range(len(variables)):
			new_file.write("int " + variables[i] + "\n")
		for j in range(len(temporary_variables)):
			new_file.write("int " + temporary_variables[j] + "\n")
		#write lists
		for k in range(len(tetrades_me_etiketa)):
			if tetrades_me_etiketa[k][1]=="+" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+str(tetrades_me_etiketa[k][4])+"="+str(tetrades_me_etiketa[k][2])+"+"+str(tetrades_me_etiketa[k][3])+";\n")
			elif tetrades_me_etiketa[k][1]=="-" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+str(tetrades_me_etiketa[k][4])+"="+str(tetrades_me_etiketa[k][2])+"-"+str(tetrades_me_etiketa[k][3])+";\n")	
			elif tetrades_me_etiketa[k][1]=="*" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+str(tetrades_me_etiketa[k][4])+"="+str(tetrades_me_etiketa[k][2])+"*"+str(tetrades_me_etiketa[k][3])+";\n")
			elif tetrades_me_etiketa[k][1]=="/" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+str(tetrades_me_etiketa[k][4])+"="+str(tetrades_me_etiketa[k][2])+"/"+str(tetrades_me_etiketa[k][3])+";\n")
			elif tetrades_me_etiketa[k][1]=="<" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+"<"+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]=="<=" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+"<="+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]==">" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+">"+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]==">=" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+">="+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]=="<>" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+"!="+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]=="=" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"if("+str(tetrades_me_etiketa[k][2])+"=="+str(tetrades_me_etiketa[k][3])+") goto L"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]==":=" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+str(tetrades_me_etiketa[k][4])+"="+str(tetrades_me_etiketa[k][2])+";\n")
			elif tetrades_me_etiketa[k][1]=="jump" :
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+": "+"goto L_"+str(tetrades_me_etiketa[k][4])+";\n")
			elif tetrades_me_etiketa[k][1]=="inp":
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+":scanf("+str(tetrades_me_etiketa[k][2])+");\n")
			elif tetrades_me_etiketa[k][1]=="out":
				new_file.write("//("+str(tetrades_me_etiketa[k][1])+","+str(tetrades_me_etiketa[k][2])+","+str(tetrades_me_etiketa[k][3])+","+str(tetrades_me_etiketa[k][4])+")\n")
				new_file.write("L_"+str(tetrades_me_etiketa[k][0])+":printf("+str(tetrades_me_etiketa[k][2])+");\n")
		new_file.write("}")
		new_file.close()
		return
		
def get_intermediate_program(): 

	#allazo kataliksi
	new_file_name=((sys.argv[1][:len(sys.argv[1])-2])+"int")
	new_file=open(new_file_name,"w+")
	for i in range(len(tetrades_me_etiketa)): 
		new_file.write(str(tetrades_me_etiketa[i])+"\n")
	new_file.close()
	
def record_scope(name_scope):

	#change global
	global SymbolArray,nestingLevel
	#vazoume edo to 12 gia na exei arxiki timi kathe scope
	new_scope=[nestingLevel,[],12,name_scope]
	#prostheto to new sthn stiva
	SymbolArray=[new_scope]+SymbolArray
	nestingLevel=nestingLevel+1
    
def delete_scope():

	#change global
	global SymbolArray,nestingLevel
	new_file_name=((sys.argv[1][:len(sys.argv[1])-2])+"txt")
	new_file=open(new_file_name,"w+")
	nestingLevel=nestingLevel-1
	new_file.write("\n\n\n" + str(len(SymbolArray))+"\n")	
	i = 0
	while i < len(SymbolArray):
		string = ""
		string = str(SymbolArray[i][0])+" " + str(SymbolArray[i][2])+" " +SymbolArray[i][3]
		new_file.write(string.strip())
		string = "\t"
		for j in range(len(SymbolArray[i][1])):
			string = string + str(SymbolArray[i][1][j])+ " "
		new_file.write(string)
		i = i + 1
	#get mips edo gt eimaste prin tin diagrafi
	get_MIPS_program()
	SymbolArray=SymbolArray[1:len(SymbolArray)]
	new_file.close()
	
def record_entity(name_entity,arguments):

	#change global
	global SymbolArray
	new_entity=[name_entity,[arguments]]
	#d erotima simasiologikou
	for j in range(len(SymbolArray[0][1])):
		if name_entity[0]==SymbolArray[0][1][j][0][0]:
			print("line %d: same name (%s) found"%(line, name_entity[0]))
			exit(0)
	#vazo to 0 gt o pinakas einai dio disdiastatos kai uelv to proto scope
	SymbolArray[0][1].append(new_entity)
	if (arguments!="function" and arguments!="procedure"):
		SymbolArray[0][2]=SymbolArray[0][2]+4
		
def search_entity(entity):

	#change global
	global SymbolArray
	for i in range(len(SymbolArray)):
		for j in range(len(SymbolArray[i][1])):
			if entity==SymbolArray[i][1][j][0][0]:
				return SymbolArray[i][1][j], SymbolArray[i][0]
	print("Entity not found")
	exit(0)
	
def gnlvcode(entity):

	#change global
	global MIPS_file, nestingLevel
	MIPS_file.write("lw $t0,-4($sp)\n")
	new_entity, nestingLevelEntity=search_entity(entity)
	i=SymbolArray[0][0]-nestingLevelEntity-1
	while(i > 0):
		MIPS_file.write("lw $t0,-4($t0)\n")
		i=i-1
	MIPS_file.write("add $t0,$t0,-"+str(new_entity[0][2])+"\n")
	
def loadvr(v,r):

	#change global
	global MIPS_file
	if v.isdigit():
		MIPS_file.write("li "+r+","+v+"\n")
	else:
		new_entity, nestingLevelEntity=search_entity(v)
		if(nestingLevelEntity==0):
			MIPS_file.write("lw "+r+",-"+str(new_entity[0][2])+"($s0)\n")
		elif(nestingLevelEntity==SymbolArray[0][0]):
			if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
				MIPS_file.write("lw "+r+",-"+str(new_entity[0][2])+"($sp)\n")
			else:
				MIPS_file.write("lw $t0,-"+str(new_entity[0][2])+"($sp)\n")
				MIPS_file.write("lw "+r+",($t0)\n")
		else:
			gnlvcode(v)
			if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
				MIPS_file.write("lw "+r+",($t0)\n")
			else:
				MIPS_file.write("lw $t0,($t0)\n")
				MIPS_file.write("lw "+r+",($t0)\n")

def storerv(r,v):

	#change global
	global MIPS_file
	new_entity, nestingLevelEntity=search_entity(v)
	if(nestingLevelEntity==0):
		MIPS_file.write("sw "+r+",-"+str(new_entity[0][2])+"($s0)\n")
	elif(nestingLevelEntity==SymbolArray[0][0]):
		if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
			MIPS_file.write("sw "+r+",-"+str(new_entity[0][2])+"($sp)\n")
		else:
			MIPS_file.write("lw $t0,-"+str(new_entity[0][2])+"($sp)\n")
			MIPS_file.write("sw "+r+",($t0)\n")
	else:
		gnlvcode(v)
		if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
			MIPS_file.write("sw "+r+",($t0)\n")
		else:
			MIPS_file.write("lw $t0,($t0)\n")
			MIPS_file.write("sw "+r+",($t0)\n")
	
def get_MIPS_program(): 

	#change global
	global MIPS_file, thesh_MIPS
	prwth_parametros = True
	j=0
	for i in range(thesh_MIPS, len(tetrades_me_etiketa)):
		#print(tetrades_me_etiketa[i])
		MIPS_file.write("L_" + str(tetrades_me_etiketa[i][0]) +": "+"\n")		
		if tetrades_me_etiketa[i][1]=="jump":
			if tetrades_me_etiketa[i][4] == "_":
				MIPS_file.write("b L_"+str(tetrades_me_etiketa[i+1][0])+"\n")
			else :
				MIPS_file.write("b L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]=="=":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("beq $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]=="<=":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("ble $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]==">=":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("bge $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]==">":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("bgt $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]=="<":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("blt $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]=="<>":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("bne $t1,$t2,L_"+str(tetrades_me_etiketa[i][4])+"\n")
		elif tetrades_me_etiketa[i][1]==":=":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			storerv('$t1',tetrades_me_etiketa[i][4])
		elif tetrades_me_etiketa[i][1]=="+":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("add $t1,$t1,$t2"+"\n")
			storerv('$t1',tetrades_me_etiketa[i][4])
		elif tetrades_me_etiketa[i][1]=="-":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("sub $t1,$t1,$t2"+"\n")
			storerv('$t1',tetrades_me_etiketa[i][4])	
		elif tetrades_me_etiketa[i][1]=="*":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("mul $t1,$t1,$t2"+"\n")
			storerv('$t1',tetrades_me_etiketa[i][4])
		elif tetrades_me_etiketa[i][1]=="/":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			loadvr(tetrades_me_etiketa[i][3],'$t2')
			MIPS_file.write("div $t1,$t1,$t2"+"\n")
			storerv('$t1',tetrades_me_etiketa[i][4])
		elif tetrades_me_etiketa[i][1]=="out":
			MIPS_file.write("li $v0,1"+"\n")
			loadvr(tetrades_me_etiketa[i][2],'$a0')
			MIPS_file.write("syscall"+"\n")
		elif tetrades_me_etiketa[i][1]=="inp":
			MIPS_file.write("li $v0,5"+"\n")
			MIPS_file.write("syscall"+"\n")
			storerv('$v0',tetrades_me_etiketa[i][2])
		elif tetrades_me_etiketa[i][1]=="retv":
			loadvr(tetrades_me_etiketa[i][2],'$t1')
			MIPS_file.write("lw $t0,-8($sp)"+"\n")
			MIPS_file.write("sw $t1,($t0)"+"\n")
		elif tetrades_me_etiketa[i][1]=="par":
			if prwth_parametros==True:
				for k in range(i+1,len(tetrades_me_etiketa)):
					if tetrades_me_etiketa[k][1]=="call":
						new_entity,nestingLevelEntity=search_entity(tetrades_me_etiketa[k][2])
						MIPS_file.write("addi $fp,$sp,"+str(new_entity[0][3])+"\n")
						prwth_parametros=False
						break
			
			if tetrades_me_etiketa[i][3]=="CV":
				loadvr(tetrades_me_etiketa[i][2],'$t0')
				MIPS_file.write("sw $t0,"+str((-12-4*j))+"($fp)"+"\n")
			elif tetrades_me_etiketa[i][3]=="REF":
				new_entity,nestingLevelEntity=search_entity(tetrades_me_etiketa[i][2])
				if(nestingLevelEntity==SymbolArray[0][0]):
					if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
						MIPS_file.write("add $t0, $sp, -"+str(new_entity[0][2])+"\n")
						MIPS_file.write("sw $t0,"+str((-12-4*j))+"($fp)"+"\n")
					else:
						MIPS_file.write("lw $t0,-"+str(new_entity[0][2])+"($sp)\n")
						MIPS_file.write("sw $t0,"+str((-12-4*j))+"($fp)"+"\n")
				else:
					gnlvcode(v)
					if(new_entity[0][1] == 'cv' or new_entity[0][1] == 'temporary_variable' or new_entity[0][1] == 'variable'):
						MIPS_file.write("sw $t0,"+str((-12-4*j))+"($fp)"+"\n")
					else:
						MIPS_file.write("lw $t0,($t0)\n")
						MIPS_file.write("sw $t0,"+str((-12-4*j))+"($fp)"+"\n")
			elif tetrades_me_etiketa[i][3]=="RET":
				new_entity,nestingLevelEntity=search_entity(tetrades_me_etiketa[i][2])
				MIPS_file.write("addi $t0,$sp,-"+str(new_entity[0][2])+"\n")
				MIPS_file.write("sw $t0,-8($fp)"+"\n")		
			j=j+1
			
		elif tetrades_me_etiketa[i][1]=="call":
			prwth_parametros=True
			j=0
			new_entity,nestingLevelEntity=search_entity(tetrades_me_etiketa[i][2])
			if SymbolArray[0][0]-1==nestingLevelEntity:
				MIPS_file.write("lw $t0,-4($sp)"+"\n")
				MIPS_file.write("sw $t0,-4($fp)"+"\n")
			else:
				MIPS_file.write("sw $sp,-4($fp)"+"\n")
			MIPS_file.write("addi $sp,$sp,"+str(new_entity[0][3])+"\n")
			MIPS_file.write("jal L_"+str(new_entity[0][2])+"\n")
			MIPS_file.write("addi $sp,$sp,-"+str(new_entity[0][3])+"\n")
		elif tetrades_me_etiketa[i][1]=="begin_block":
			if(tetrades_me_etiketa[i][2]!=program_name):
				MIPS_file.write("sw $ra,($sp)"+"\n")
			else:
				MIPS_file.write("LMain: "+"\n")				
				MIPS_file.write("addi $sp,$sp,"+str(SymbolArray[0][2])+"\n")
				MIPS_file.write("move $s0,$sp"+"\n")
		elif tetrades_me_etiketa[i][1]=="end_block":
			if(tetrades_me_etiketa[i][2]!=program_name):
				MIPS_file.write("lw $ra,($sp)"+"\n")
				MIPS_file.write("jr $ra"+"\n")
                
	thesh_MIPS=len(tetrades_me_etiketa)

#Main method 
if boolextention: 
	lektikosAnalitis()
	program()
	get_program_C()
	get_intermediate_program()
else: 
	#if file extention not '.ci' print error
	print("Wrong file input")
	exit(0)
