#SAN LUIS, Jillian Joy C.
#CMSC 11 U-3L
#Project: trivia/quiz game

def randomize(x):
	file1 = open(x, "r")
	listB = []
	for line in file1:
		listI = []
		line = line [0:-1]
		if line != "":
			data = line.split(";")
			q = data[0]
			a = data[1]
			b = data[2]
			c = data[3]
			d = data[4]
			ans = data[5]
			listI.append(q)
			listI.append(a)
			listI.append(b)
			listI.append(c)
			listI.append(d)
			listI.append(ans)
			listB.append(listI)
	file1.close()
	import random
	random.shuffle(listB)
	file2 = open (x, "w")
	for e in listB:
		file2.write(e[0] + ";" + e[1] + ";" + e[2] + ";" + e[3] + ";" + e[4] + ";" + e[5] + ";" + "\n")
	file2.close()

def viewTopScores():
	print ("----------LEADERBOARD----------")
	file1 = open ("topScores.txt", "r")
	for line in file1:
		line = line [0:-1]
		if line != "":
			data = line.split(";")
			print (data[0])
			player = data[1]
			score = data [2]
			print (player, "     ", score)
	file1.close()

def scoreCheck():
	dictio = {}
	file2 = open ("topScores.txt", "r")
	for line in file2:
		line = line[0:-1]
		if line != "":
			data = line.split(";")
			cat = data[0]
			pla = data[1]
			sco = int(data[2])
			dictio[cat] = []
			dictio[cat].append(pla)
			dictio[cat].append(sco)
	file2.close()
	for k,v in dictio.items():
		if k == categ:
			if finalScore > v[1]:
				v[0] = player
				v[1] = finalScore
				print ("Congratulations! You got the highest score!")
	file3 = open ("topScores.txt", "w")
	for k,v in dictio.items():
		v[1] = str(v[1])
		file3.write(k + ";" + v[0] + ";" + v[1] + "\n")
	file3.close()

def gameEasy(x):
	print ("----------EASY----------")
	scoreEasy = 0
	print ("Input the letter of your answer. :)")
	if x == 1:
		fh = "FRtestEasy.txt"
	if x == 2:
		fh = "CMtestEasy.txt"
	if x == 3:
		fh = "CPtestEasy.txt"
	if x == 4:
		fh = "TYtestEasy.txt"
	if x == 5:
		fh = "EDtestEasy.txt"
	file1 = open(fh, "r")
	for line in file1:
		line = line [0:-1]
		if line != "":
			data = line.split(";")
			print (data[0])
			print (data[1])
			print (data[2])
			print (data[3])
			print (data[4])
			answer = str(input("Answer: "))
			if answer == data[5]:
				print ("Your answer is correct!")
				scoreEasy = scoreEasy + 1
			else:
				print ("Wrong! The correct answer is ", data[5], ".")
	file1.close()
	randomize(fh)
	return scoreEasy

def gameAverage(x):
	print ("----------AVERAGE----------")
	scoreAverage = 0
	print ("Input the letter of your answer. :)")
	if x == 1:
		fh = "FRtestAverage.txt"
	if x == 2:
		fh = "CMtestAverage.txt"
	if x == 3:
		fh = "CPtestAverage.txt"
	if x == 4:
		fh = "TYtestAverage.txt"
	if x == 5:
		fh = "EDtestAverage.txt"
	file1 = open(fh, "r")
	for line in file1:
		line = line [0:-1]
		if line != "":
			data = line.split(";")
			print (data[0])
			print (data[1])
			print (data[2])
			print (data[3])
			print (data[4])
			answer = str(input("Answer: "))
			if answer == data[5]:
				print ("Your answer is correct!")
				scoreAverage = scoreAverage + 2
			else:
				print ("Wrong! The correct answer is ", data[5], ".")
	file1.close()
	randomize(fh)
	return scoreAverage

def gameDifficult(x):
	print ("----------DIFFICULT----------")
	scoreDifficult = 0
	print ("Input the letter of your answer. :)")
	if x == 1:
		fh = "FRtestDifficult.txt"
	if x == 2:
		fh = "CMtestDifficult.txt"
	if x == 3:
		fh = "CPtestDifficult.txt"
	if x == 4:
		fh = "TYtestDifficult.txt"
	if x == 5:
		fh = "EDtestDifficult.txt"
	file1 = open(fh, "r")
	for line in file1:
		line = line [0:-1]
		if line != "":
			data = line.split(";")
			print (data[0])
			print (data[1])
			print (data[2])
			print (data[3])
			print (data[4])
			answer = str(input("Answer: "))
			if answer == data[5]:
				print ("Your answer is correct!")
				scoreDifficult = scoreDifficult + 3
			else:
				print ("Wrong! The correct answer is ", data[5], ".")
	file1.close()
	randomize(fh)
	return scoreDifficult

while True:
	print ("----------Menu----------")
	print ("[1] New Game")
	print ("[2] Leaderboard")
	print ("[3] Exit")
	choice = str(input ("Choice: "))

	if choice == "1":
		print ("----------Categories----------")
		print ("[1] FRIENDS-zoned")
		print ("[2] CMSC 11")
		print ("[3] Coldplaying")
		print ("[4] Swift Mania")
		print ("[5] Sheeran Fetish")

		category = int(input ("Choice: "))
		if category == 1:
			categ = "----------FRIENDS-zoned----------"
		elif category == 2:
			categ = "----------CMSC 11----------"
		elif category == 3:
			categ = "----------Coldplaying----------"
		elif category == 4:
			categ = "----------Swift Mania----------"
		elif category == 5:
			categ = "----------Sheeran Fetish----------"

		print ("----------Level----------")
		print ("[1] Easy")
		print ("[2] Average")
		print ("[3] Difficult")

		level = int(input ("Choice: "))
		player = str(input("Enter your name: "))

		if level == 1:
			score1 = gameEasy(category)
			score2 = 0
			score3 = 0
			print ("----------OPTIONS----------")
			print ("[1] Proceed to the next level")
			print ("[2] Back to Menu")
			decision = int(input ("Choice: "))

			if decision == 1:
				score2 = gameAverage(category)
				print ("----------OPTIONS----------")
				print ("[1] Proceed to the next level")
				print ("[2] Back to Menu")
				decision = int(input ("Choice: "))
				if decision == 1:
					score3 = gameDifficult(category)
			finalScore = score1 + score2 + score3
			print ("Your score is ", finalScore, ".")

		elif level == 2:
			score2 = gameAverage(category)
			score3 = 0
			print ("----------OPTIONS----------")
			print ("[1] Proceed to the next level")
			print ("[2] Back to Menu")
			decision = int(input ("Choice: "))
			if decision == 1:
				score3 = gameDifficult(category)
			finalScore = score2 + score3
			print ("Your score is ", finalScore, ".")

		elif level == 3:
			finalScore = gameDifficult(category)
			print ("Your score is ", finalScore, ".")             
		scoreCheck()

	elif choice == "2":
		V = viewTopScores()

	elif choice == "3":
		print ("Bye!")
		break
