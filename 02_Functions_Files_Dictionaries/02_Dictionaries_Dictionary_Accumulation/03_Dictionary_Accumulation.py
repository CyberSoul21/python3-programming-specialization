#Introduction: Accumulating Multiple Results In a Dictionary

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0

    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1

print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")



f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")





f = open('scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))
print(txt_lines[70:85])




#2. Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
s_spl = sentence.split()
print(s_spl)
word_counts = {}

for x in s_spl:
    if x not in word_counts:
        word_counts[x]=0
    word_counts[x] = word_counts[x] + 1
    
print(word_counts)    


#3. Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.

stri = "what can I do"
char_d = {}
for x in stri:
    if x not in char_d:
        char_d[x]=0
    char_d[x] = char_d[x] + 1
print(char_d)      




#1. The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!


travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total=0
for x in travel:
    total = total + travel[x]
print(total)


#2. schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Go through and accumulate the total number of credits that have been earned so far and assign that to the variable total_credits. Do not hardcode

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits=0
for x in schedule:
    total_credits = total_credits + schedule[x]
print(total_credits)



#1. Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.


placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d={}
for x in placement:
    if x not in d:
        d[x]=0
    d[x] = d[x] + 1
c=0
min_value=0
for k in d:
    if c == 0:
        min_value = d[k]
    if d[k] < min_value:
        min_value = k
    c += 1    
print(min_value)


#5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.



product = "iphone and android phones"
lett_d ={}
for x in product:
    if x not in lett_d:
        lett_d[x]=0
    lett_d[x] = lett_d[x] + 1
c=0
max_value=0
max=0
for k in lett_d:
    if c == 0:
        max = lett_d[k]
    if lett_d[k] > max:
        max_value = k
        max = lett_d[k]
    c += 1    
print(max_value)



