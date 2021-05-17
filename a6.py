#Mujtaba Mujtaba
#101167348

#instructions

def main():
	quit = "y"
	board()
	newboard = input("Do you want to make a new board?(enter y to continue)")
	if newboard == "y" or newboard == "Y":
		board()
#	if move yes:
#	if newboard:
#	if quit yes:
#		break

		

def validate(userinput):
	letters = "kKqQrRnNbBpP-"
	if len(userinput) == 8:
		
		for i in userinput:
			if i not in letters:
				return False

		return True

	else:
		return False

def board():
	
	chessboard = []
	
	for i in range(8):		
		print("enter your row")	
		row = input("enter a row.")
		while not validate(row):
			row = input("Enter the row again as the length or piece was in invalid.")
		
		chessboard.append(row)
	for i in chessboard:
		print(i)
		
	score(chessboard)
	moves(chessboard)		


def score(chessboard):
	wscore = 0
	bscore = 0
	white = []
	black = []
#uppercase = black
#lowercase = white
#k,K = 0
#q,Q = 10
#r,R = 5 
#n,N = 3.5
#b,B = 3
#p,P = 1
	for x in chessboard:
		for i in x:
			if i == "K":
				black.append(0)
			if i == "Q":
				black.append(10)
			if i == "R":
				black.append(5)
			if i == "N":
				black.append(3.5)
			if i == "B":
				black.append(3)
			if i == "P":
				black.append(1)
			if i == "k":
				white.append(0)
			if i == "q":
				white.append(10)
			if i == "r":
				white.append(5)
			if i == "n":
				white.append(3.5)
			if i == "b":
				white.append(3)
			if i == "p":
				white.append(1)


	for b in range(len(black)):
		bscore += black[b]
	print("Black pieces score is :", bscore)
	for w in range(len(white)):
		wscore += white[w]
	print("White pieces score is :", wscore)

def moves(chessboard):
	newlist = []
	for i in chessboard:
		piece = input("enter the piece you want to move.\t")
		for x in i:
			if x == piece:
				i = int(input("enter the row you want it in.\t"))
				x = int(input("enter the column you want it in.\t"))
				newlist.append(chessboard[i][x])
	print(newlist)
			
				


	



		







		
		
	

			
			


	


main()
