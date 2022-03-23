#We can accumulate values into a list rather than accumulating a 
#single numeric value. Consider, for example, the following program 
#which transforms a list into a new list by squaring each of the values

nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)


#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

ing=[]
for i in verbs:
    ings = i + "ing"
    ing.append(ings)
    
print(ing)    


#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.

numbs = [5, 10, 15, 20, 25]

newlist=[]
for i in numbs:
    inc = i + 5
    newlist.append(inc)
    
print(newlist)    


#Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.

numbs = [5, 10, 15, 20, 25]

temp = numbs
c=0
for i in numbs:
    inc = i + 5
    numbs[c]=inc
    c += 1
    
print(numbs) 




#For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.

lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

larger_nums=[]
for i in lst_nums:
    inc = i * 2
    larger_nums.append(inc)
    
print(larger_nums)  

#For each character in the string saved in ael, append that character to a list that should be saved in a variable app.

ael = "python!"
app=[]
for i in ael:
    app.append(i)
    print(i)
    
print(app) 



#For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.


wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds=[]
for i in wrds:
    past = i + "ed"
    past_wrds.append(past)
    
print(past_wrds)    









