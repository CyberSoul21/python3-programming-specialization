#The for Loop

#Write one for loop to print out each character of the string my_str on a separate line

my_str = "MICHIGAN"

for x in my_str:
    print(x)

#Write one for loop to print out each element of the list several_things.
#Then, write another for loop to print out the TYPE of each element of the
#list several_things. To complete this problem you should have written two
#different for loops, each of which iterates over the list several_things,
#but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for x in several_things:
    print(x)

for x in several_things:
    print(type(x))


#Write code that uses iteration to print out the length of each element of the list stored in str_list.

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

# Write your code here.

for x in str_list:
    print(len(x))

#Write code to count the number of characters in original_str using the accumulation pattern and assign
#the answer to a variable num_chars. Do NOT use the len function to solve the problem
#(if you use it while you are working on this problem, comment it out afterward!)


original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars=0

for x in original_str:
    num_chars += 1
   
print(num_chars)    


#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation
#pattern to take the sum of all of the numbers and assigns it to sum_val (an integer).
#(You should use the .split("+") function to split by "+" and int() to cast to an integer).


addition_str = "2+5+10+20"

new_str = addition_str.split('+')
sum_val=0
for x in new_str:
    acc = int(x)
    sum_val = sum_val + acc
print(sum_val)


#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
Write code that uses the accumulation pattern to compute the average (sum divided by number of items)
and assigns it to avg_temp. Do not hard code your answer
(i.e., make your code compute both the sum or the number of items in week_temps_f)
(You should use the .split(",") function to split by "," and float() to cast to a float).


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

new_temps = week_temps_f.split(',')
count=0
sum_temp=0
for x in new_temps:
    count +=1
    x_float = float(x)
    sum_temp = sum_temp + x_float
   
avg_temp = sum_temp/count    
print(avg_temp)



#Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.




list = []

print(list)

for i in range(0, 68):
    list.append(i)
nums = list
print(nums)


#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).


original_str = "The quick brown rhino jumped over the extremely lazy fox"

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
list_original = original_str.split(' ')

for x in list_original:
    num_words_list.append(len(x))
   
print(num_words_list)



#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").




lett = ''
for x in range(7):
    lett += 'b'
    print(lett, end='')





#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)



import turtle

star = turtle.Turtle()
 
#for i in range(50):
#    star.forward(50)
#    star.right(144)
     
#turtle.done()
