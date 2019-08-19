board = []

for i in range(3):
	l = []
	for j in range(3):
		l.append(" ")
	board.append(l)
	
def showboard(board):
	print(board[0][0]+" | "+board[0][1]+" | "+board[0][2])
	print(board[1][0]+" | "+board[1][1]+" | "+board[1][2])
	print(board[2][0]+" | "+board[2][1]+" | "+board[2][2])
	print()
		
def CheckNextWinning(board,s):
	for i in range(3):
		for j in range(3):
			if j==0:
				if board[i][0] == " " and board[i][1] == s and board[i][2] == s:
					return i,0
			if j==1:
				if board[i][0] == s and board[i][1] == " " and board[i][2] == s:
					return i,1
			if j==2:
				if board[i][0] ==s and board[i][1] == s and board[i][2] ==" ":
					return i,2
	for i in range(3):
		for j in range(3):
			if j==0:
				if board[0][i] == " " and board[1][i] == s and board[2][i] == s:
					return 0,i
			if j==1:
				if board[0][i] == s and board[1][i] == " " and board[2][i] == s:
					return 1,i
			if j==2:
				if board[0][i] == s and board[1][i] == s and board[2][i] == " ":
					return 2,i
	for i in range(3):
		if i==0:
			if board[0][0] == " " and board[1][1] == s and board[2][2] == s:
				return 0,0
		elif i==1:
			if board[0][0] == s and board[1][1] == " " and board[2][2] == s:
				return 1,1
		elif i==2:
			if board[0][0] == s and board[1][1] == s and board[2][2] == " ":
				return 2,2
	for i in range(3):
		if i==0:
			if board[0][2] == " " and board[1][1] == s and board[2][0] == s:
				return 0,2
		elif i==1:
			if board[0][2] == s and board[1][1] == " " and board[2][0] == s:
				return 1,1
		elif i==2:
			if board[0][2] == s and board[1][1] == s and board[2][0] == " ":
				return 2,0
	return -1,-1

def isManCorner(board):
	if board[0][0] == "X" or board[0][2] == "X" or board[2][0] == "X" or board[2][2] == "X":
		return True
	return False

def isManSide(board):
	if board[0][1] == "X" or board[1][0] == "X" or board[2][1] == "X" or board[1][2] == "X":
		return True
	return False
	
def GiveWinSidePos(board):
	if board[1][0]==" " and board[1][2]==" ":
		return 1,0
	return 0,1
	
def FirstEmpty(board):
	for i in range(3):
		for j in range(3):
			if board[i][j] == " ":
				return i,j
	return -1,-1

def CheckValidInput(board,i,j):
	if board[i-1][j-1] != " ":
		return False
	return True
	
def CornerMovePlay(board,count):
	while count<9:
		count += 1
		if count%2==1:
			print("Enter Your Move")
			print()
			s = input()
			index = s.split(" ")
			i,j = int(index[0]),int(index[1])
			while not CheckValidInput(board,i,j):
				print("Enter A Valid Input")
				print()
				s = input()
				index = s.split(" ")
				i,j = int(index[0]),int(index[1])
			board[i-1][j-1] = "X"
		elif count//2 == 1:
			board[1][1] = "O"
		elif count//2 == 2:
			k1,k2 = CheckNextWinning(board,"X")
			if k1 == -1 and k2 == -1:
				if isManCorner(board):
					board[0][1] = "O"
				else:
					k1,k2 = GiveWinSidePos(board)
					board[k1][k2] = "O"
			else:
				board[k1][k2] = "O"
		elif count//2 == 3 or count//2 == 4:
			k1,k2 = CheckNextWinning(board,"O")
			if k1==-1 and k2==-1:
				k1,k2 = CheckNextWinning(board,"X")
				if k1==-1 and k2==-1:
					k1,k2 = FirstEmpty(board)
					board[k1][k2] = "O"
				else:
					board[k1][k2] = "O"
			else:
				board[k1][k2] = "O"
				showboard(board)
				print("Computer Wins....")
				return
		showboard(board)
	print("Match Draw")


def CenterMovePlay(board,count):
	while count<9:
		count += 1
		if count%2==1:
			print("Enter Your Move")
			print()
			s = input()
			index = s.split(" ")
			i,j = int(index[0]),int(index[1])
			while not CheckValidInput(board,i,j):
				print("Enter A Valid Input")
				print()
				s = input()
				index = s.split(" ")
				i,j = int(index[0]),int(index[1])
			board[i-1][j-1] = "X"
		elif count//2 == 1:
			board[0][0] = "O"
		elif count//2 == 2:
			if board[2][2] == "X":
				board[2][0] = "O"
			else:
				k1,k2 = CheckNextWinning(board,"X")
				board[k1][k2] = "O"
		elif count//2 == 3 or count//2 == 4:
			k1,k2 = CheckNextWinning(board,"O")
			if k1==-1 and k2==-1:
				k1,k2 = CheckNextWinning(board,"X")
				if k1==-1 and k2==-1:
					k1,k2 = FirstEmpty(board)
					board[k1][k2] = "O"
				else:
					board[k1][k2] = "O"
			else:
				board[k1][k2] = "O"
				showboard(board)
				print("Computer Wins....")
				return
		showboard(board)
	print("Match Draw")
	
def CheckAdjSide(board):
	if board[1][0]=="X" and board[0][1]=="X":
		return 0,0
	elif board[0][1]=="X" and board[1][2]=="X":
		return 0,2
	elif board[1][2]=="X" and board[2][1]=="X":
		return 2,2
	elif board[2][1]=="X" and board[1][0]=="X":
		return 2,0
	return -1,-1
	
def SideMovePlay(board,count):
	while count<9:
		count += 1
		if count%2==1:
			print("Enter Your Move")
			print()
			s = input()
			index = s.split(" ")
			i,j = int(index[0]),int(index[1])
			while not CheckValidInput(board,i,j):
				print("Enter A Valid Input")
				print()
				s = input()
				index = s.split(" ")
				i,j = int(index[0]),int(index[1])
			board[i-1][j-1] = "X"
		elif count//2 == 1:
			board[1][1] = "O"
		elif count//2 == 2:
			k1,k2 = CheckAdjSide(board)
			if k1==-1 and k2==-1:
				k1,k2 = GiveWinSidePos(board)
				board[k1][k2] = "O"
			else:
				board[k1][k2] = "O"
		elif count//2 == 3 or count//2 == 4:
			k1,k2 = CheckNextWinning(board,"O")
			if k1==-1 and k2==-1:
				k1,k2 = CheckNextWinning(board,"X")
				if k1==-1 and k2==-1:
					k1,k2 = FirstEmpty(board)
					board[k1][k2] = "O"
				else:
					board[k1][k2] = "O"
			else:
				board[k1][k2] = "O"
				showboard(board)
				print("Computer Wins....")
				return
		showboard(board)
	print("Match Draw")
	
def PlayerOneManual():
	count = 1
	print("Enter Your Move")
	print()
	s = input()
	index = s.split(" ")
	i,j = int(index[0]),int(index[1])
	board[i-1][j-1] = "X"
	showboard(board)
	if (i==1 or i==3) and (j==1 or j==3):
		CornerMovePlay(board,count)
	elif i==2 and j==2:
		CenterMovePlay(board,count)
	else:
		SideMovePlay(board,count)

PlayerOneManual()
	