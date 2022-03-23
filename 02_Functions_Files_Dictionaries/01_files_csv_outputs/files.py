#Reading a File

fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
fileref.close()

#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

fileref = open("school_prompt2.txt", "r")
text=fileref.read()
print(text[0])
num_char=0
for x in text:
    num_char+=1
    
print(num_char)
 

 #Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

fileref = open("travel_plans2.txt", "r")
list_text = fileref.readlines()
num_lines=len(list_text)
print(num_lines)


#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

fileref = open("emotion_words2.txt", "r")
first_forty = fileref.read(40)
print(first_forty)



#To process all of our olypmics data, we will use a for loop to iterate over the lines of the file. Using the split method, we can break each line into a list containing all the fields of interest about the athlete. We can then take the values corresponding to name, team and event to construct a simple sentence.


olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()



olypmicsfile = open("olypmics.txt", "r")

for aline in olypmicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()



#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

num_lines = sum(1 for line in open('emotion_words.txt'))

#Using with for Files
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code


md = open('mydata.txt', 'r')
for line in md:
    print(line)
md.close()
# continue with other code

#Recipe for Reading and Processing a File

fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


#Writing Text Files

filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()


#Reading in data from a CSV File

fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()

header = lines[0]

field_names = header.strip().split(',')

print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
         print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))
#Also note that we first pass the row through the .strip() method to get rid of the trailing n.



#Writing data to a CSV File


olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()



olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

