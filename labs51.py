import random
print("welcome to a game of snake and ladder")
count=0
while(count<=100):
 	a=input("enter r to roll the dice")
 	if(a=='r'):
 		r=random.randint(1,6)
 		print(r)
 		count=count+r
 		print("your score is",count)
 		if(count<=100):
 			if(count==100):
 				print("you have won")
 			elif(count==8):
 				print("you have climbed the ladder")
 				count=37
 				print("your score is",count)
 			elif(count==11):
 				print("you have got bitten by the snake")
 				count=2
 				print("your score is",count)
 			elif(count==13):
 				print("you have climbed the ladder")
 				count=34
 				print("your score is",count)
 			elif(count==25):
 				print("you have got bitten by the snake")
 				count=4
 				print("your score is",count)
 			elif(count==38):
 				print("you have got bitten by the snake")
 				count=9
 				print("your score is",count)
 			elif(count==40):
 				print("you have climbed the ladder")
 				count=68
 				print("your score is",count)
 			elif(count==52):
 				print("you have climbed the ladder")
 				count=81
 				print("your score is",count)
 			elif(count==65):
 				print("you have got bitten by the snake")
 				count=46
 				print("your score is",count)
 			elif(count==76):
 				print("you have climbed the ladder")
 				count=97
 				print("your score is",count)
 			elif(count==89):
 				print("you have got bitten by the snake")
 				count=70
 				print("your score is",count)
 			elif(count==93):
 				print("you have climbed the ladder")
 				count=64
 				print("your score is",count)
 	else:
 		break
