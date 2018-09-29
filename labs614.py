import random
gamelist={1:'rock',2:'paper',3:'scissors'}
while True:
	a=int(input("enter 1 for game against computer and 2 for game against player 2"))
	if(a==1):
		r=random.randint(1,3)
		c=gamelist(r)
		p=int(input("enter your option"))
		if(c==p):
			print("its a draw")
		elif(c==1):
			if(p==2):
				print("you win")
			else:
				print("computer wins")	
		elif(c==2)
			if(p==1):
				print("computer wins")
			else:
				print("you win")
		elif(c==3):
			if(p==1):
				print("you win")
			else:
				print("computer wins")
		else:
			break
	elif(a==2):
		p1=int(input("enter your option"))
		p2=int(input("enter your option"))
		if(p1==p2):
			print("its a draw")
		elif(p1==1):
			if(p2==2):
				print("you win")
			elif(p2==3):
				print("computer wins")	
		elif(p1==2)
			if(p2==1):
					print("computer wins")
			elif(p2==3):
					print("you win")
		elif(p1==3):
			if(p2==1):
					print("you win")
			elif(p2==2)
					print("computer wins")
		else:
			break
	else:
		break




