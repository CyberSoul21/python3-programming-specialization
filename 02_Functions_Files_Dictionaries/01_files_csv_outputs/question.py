#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

file = open("travel_plans.txt","r")
read_f = file.read()
num = 0
for x in read_f:
    num += 1
print(num)   
file.close()

#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

file = open("emotion_words.txt","r")
read_l = file.read()
read_w = read_l.split()
print(read_w)
num_words = 0
for i in read_w:
    num_words += 1
print(num_words)    


#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

file = open("school_prompt.txt","r")
read_ls = file.readlines()
print(read_ls)
num_lines = 0
for x in read_ls:
    num_lines += 1
print(num_lines)  


#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

file = open("school_prompt.txt","r")
beginning_chars = file.read(30)
print(beginning_chars)

#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.


file = open("school_prompt.txt","r")
read_l = file.readlines()
print(read_l)
three = []
test=[]
for x in read_l:
    test = x.split()
    print(test)
    three.append(test[2])



#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

file = open("emotion_words.txt","r")

emotions=[]
for x in file.readlines():
    word_l = x.split()
    emotions.append(word_l[0])
    print(emotions)


#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

f = open('travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)


#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.


file = open("school_prompt.txt","r")
read = file.read()
word_l = read.split()
print(word_l)
p_words = []
for i in word_l:
    if "p" in i:
        p_words.append(i)
print(p_words)
