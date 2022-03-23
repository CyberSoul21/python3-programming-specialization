#The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

credits=0
for x in Junior:
    credits = credits + Junior[x]
print(credits)



#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq={}
for x in str1:
    if x not in freq:
        freq[x]=0
    freq[x] = freq[x] + 1
print(freq)



#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"
counts={}
for x in s1:
    if x not in counts:
        counts[x]=0
    counts[x] = counts[x] + 1


    #Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

    str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
l_str = str1.split()
print(l_str)

for x in l_str:
    if x not in freq_words:
        freq_words[x]=0
    freq_words[x] = freq_words[x] + 1


    #Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

    sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d ={}
l_sent = sent.split()
for x in l_sent:
    if x not in wrd_d:
        wrd_d[x]=0
    wrd_d[x] = wrd_d[x] + 1

    #Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.


    sally = "sally sells sea shells by the sea shore"
characters = {}
for x in sally:
    if x not in characters:
        characters[x]=0
    characters[x] = characters[x] + 1
c=0
best_char=0
maxi=0
for k in characters:
    if c == 0:
        maxi = characters[k]
    if characters[k] > maxi:
        best_char = k
        maxi = characters[k]
    c += 1    
print(best_char)


#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.


sally = "sally sells sea shells by the sea shore and by the road"
characters={}
for x in sally:
    if x not in characters:
        characters[x]=0
    characters[x] = characters[x] + 1
c=0
min_value=0
for k in characters:
    if c == 0:
        min_value = characters[k]
    if characters[k] < min_value:
        min_value = k
    c += 1
worst_char = min_value    
print(worst_char)


#Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
low_str = string1.lower()
print(low_str)
letter_counts ={}
for x in low_str:
    if x not in letter_counts:
        letter_counts[x]=0
    letter_counts[x] = letter_counts[x] + 1



    #Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.


    p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_p = p.lower()
print(low_p)
low_d ={}
for x in low_p:
    if x not in low_d:
        low_d[x]=0
    low_d[x] = low_d[x] + 1


    