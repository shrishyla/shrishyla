import random
r={1:'r',2:'p',3:'s'}
a=0
b=0
while a<3 and b<3:
	comp=r[random.randint(1,3)]
	print("enter r for rock, p for paper, s for scissors")
	p=input("enter your option")
	print(comp)
	if(comp==p):
		print("its a draw")
	elif(comp=='r'):
		if(p=='p'):
			print("you win")
			a+=1
		else:
			print("computer wins")
			b+=1	
	elif(comp=='p'):
		if(p=='r'):
			print("computer wins")
			b+=1
		else:
			print("you win")
			a+=1
	elif(comp=='s'):
		if(p=='r'):
			print("you win")
			a+=1
		else:
			print("computer wins")
			b+=1
	if(b==3):
		print("computer wins")
	elif(a==3):
		print("player wins")	
	