time = 1
sentence = ""
while time ==1:
	new = input("Please enter a word in the sentence (enter . ! or ? to end.): ")
	sentence = sentence + " " + new
	if new == "." or new =="!" or new =="?":
		time = 0
		print("-->", sentence)
	else:
		print(sentence)
