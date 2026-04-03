#request user input for a sentence
sentence = input("Please enter a sentence")
#save users response in a variable called str_manip
str_manip = sentence
#calculate the length of the sentence and print it  
print(len(sentence))
#find the last letter of the sentence and replace every occurence of this letter with a "@" and print it 
last_letter = sentence[-1]
replaced_sentence = sentence.replace(last_letter, "@")
print(replaced_sentence)
#print last 3 letters of the sentence backwards
print(sentence[-1:-4:-1])
#Create a five-letter word that is made up of the first three characters and the last two characters in str_manip. Print the word.
five_letter_word = sentence[0:3] + sentence[-2:]
print(five_letter_word)
