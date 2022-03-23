#Booleans and Conditionals


#rainfall_mi is a string that contains the average number of inches of rainfall in
#Michigan for every month (in inches) with every month separated by a comma. 
#Write code to compute the number of months that have more than 3 inches of rainfall. 
#Store the result in the variable num_rainy_months. In other words, count the number of 
#items with values > 3.0.



rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
new_rainfall = rainfall_mi.split(',')
count = 0
num_rainy_months = 0.0
for x in new_rainfall:
    conv = float(x) 
    if conv > 3.0:
        num_rainy_months += 1
        
print(count)        



#The variable sentence stores a string. Write code to determine how many words in 
#sentence start and end with the same letter, including one-letter words. 
#Store the result in the variable same_letter_count.
#Hard-coded answers will receive no credit.



sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# Write your code here.
new_sentence = sentence.split(' ')
same_letter_count = 0
for x in new_sentence:
    if x[0] == x[-1]:
        same_letter_count += 1
        
print(same_letter_count)  


#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

#HINT 1: Use the accumulation pattern!

#HINT 2: the in operator checks whether a substring is present in a string.

#Hard-coded answers will receive no credit.


items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0;
f=0
for i in items:
    f = 0
    for j in i:
        if j == 'w' and f == 0:
            f = 1
            acc_num += 1
print(acc_num)


#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

#Note 1: be sure to not double-count words that contain both an a and an e.

#HINT 1: Use the in operator.

#HINT 2: You can either use or or elif.

#Hard-coded answers will receive no credit.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for i in sentence.split():
    if ('a' in i) or ('e' in i):
        num_a_or_e += 1
        
print(num_a_or_e)    

#Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

# Write your code here.

num_vowels = 0
for i in s:
    if (i in vowels):
        num_vowels += 1
        
print(num_vowels)      
