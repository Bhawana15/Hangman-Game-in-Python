import random
words = ["cat", "elephant", "fox", "monkey", "deer", "wolf", "lion", "tiger", "rat", "cow", "zebra", "horse", "sheep", "bear", ]
print ("...........  !!!!!  HANGMAN  GAME  !!!!!  ...........")
  
while True:
    my_choice = random.choice(words)
    length = len(my_choice)
    word = ""

    for i in range(0, length):
        word += "-" 
    print ("I have chosen the name of an animal. You have to guess what I have chosen by guessing a letter at a time.")
    print ("The length of the word is " + str(length))
    print("You will get " + str(2*(length)) + " chances/attempts to guess the name of the animal.")

    for i in range(1, 2*length+1):
        guess = input("(Attempt-" + str(i) + ") Guess one letter: ")

        if guess in my_choice:
            for j in range(0, length):
                if(my_choice[j] == guess and word[j] != guess):
                    word = word[:j] + guess + word[j+1 :]
                    break
            print("GREAT !!! Your guess is CORRECT.")

        else:
            print("ALAS !!! Your guess is INCORRECT.") 

        print("The word is: " + word)

        if(word == my_choice):
            print("...........  !!!!!  YOU WIN  !!!!!  ...........")
            break
       
        if(word != my_choice and i == 2*length+1):
            print("...........  YOU LOSE  ...........")
            print("The word I chose was : " + my_choice)
            break
    
    inp = input("Do you want to play again? Enter Y/N : ")

    if(inp == "Y"):
        continue

    elif(inp == "N"):
        print("...........  !!!!!  GAME OVER  !!!!!  ........... ")
        break