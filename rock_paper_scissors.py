import random;

def play(option):
	if (choice=="Y"):
		player = input("Enter your choice (rock/paper/scissors):")
		player=player.lower()
		while (player != "rock" and player!= "paper" and player!="scissors"):
			print(player)
			player=input ("Please enter a valid choice\n")
			player=player.lower()

		computerInt=random.randint(0,2)
		if (computerInt == 0):
			computer="rock"
		elif (computerInt==1):
			computer="paper"
		elif(computerInt==2):
			computer="scissors"
		else:
			computer="Error"
		print("Computer:" + computer)

		if (player==computer):
			print("Draw!")
		elif(player=="rock"):
			if (computer=="paper"):
				print("Computer wins!")
			else:
				print("You win")
		elif(player=="paper"):
			if(computer=="scissors"):
				print("Computer wins")
			else:
				print("You win")
		elif(player=="scissors"):
			if(computer=="rock"):
				print("Computer wins")
			else:
				print ("You win")
			
	ready=input("Play again:(Y/N)")
	if (ready=="Y"):
		play(ready);
	else:
		print("Thank you for playing!")
print("Welcome User! :)")
choice=input("Ready to play the game!(Y/N)")
if(choice=="Y"):
	play(choice);
else:
	print("Thank you!")

	
	