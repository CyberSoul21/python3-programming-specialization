#Lists################################################

#A list is a sequential collection of Python data 
#values, where each value is identified by an index. 
#The values that make up a list are called its elements. 
#Lists are similar to strings, which are ordered collections 
#of characters, except that the elements of a list can 
#have any type and for any one list, the items can be 
#of different types.

[10, 20, 30, 40]
["spam", "bungee", "swallow"]

["hello", 2.0, 5, [10, 20]]

#Tuples################################################

#A tuple, like a list, is a sequence of items of any type.
#The printed representation of a tuple is a 
#comma-separated sequence of values, enclosed in 
#parentheses. In other words, the representation is 
#just like lists, except with parentheses () instead of 
#square brackets [].


julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

#The key difference between lists and tuples is that a 
#tuple is immutable, meaning that its contents can’t be 
#changed after the tuple is created. We will examine the 
#mutability of lists in detail in the chapter on Mutability.


#Index Operator: Working with the Characters of a String#########

#   0     1      2    3     4     5
#|  w  |  i  |  l  |  s  |  o  |  n  |
#  -6    -5     -4   -3    -2    -1

school = "wilson"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)


numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])


prices = (1.99, 2.00, 5.50, 20.95, 100.98)
print(prices[0])
print(prices[-1])
print(prices[3-5])


#Disabmiguating []: creation vs indexing#########################

new_lst = []

new_lst = ["NFLX", "AMZN", "GOOGL", "DIS", "XOM"]
part_of_new_lst = new_lst[0]

lst = [0]
n_lst = lst[0]

print(lst)
print(n_lst)

#Length#################################################

fruit = "Banana"
print(len(fruit))


fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print(lastch)


fruit = "grape"
midchar = fruit[len(fruit)//2]
# the value of midchar is "a"

alist =  ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))


s = "python rocks"
print(len(s))

#The Slice Operator####################################

singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])


fruit = "banana"
print(fruit[:3])
print(fruit[3:])


#List Slices##########################################

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

#Tuple Slices########################################


julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)


#Concatenation and Repetition##########################

fruit = ["apple","orange","banana","cherry"]
print([1,2] + [3,4])
print(fruit+[6,7,8,9])

print([0] * 4)

alist = [1,3,5]
print(alist * 3)

#Count and Index########################################

a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))


music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

#Splitting and Joining Strings #######################################

#Two of the most useful methods on strings involve 
#lists of strings. The split method breaks a string 
#into a list of words. By default, any number of 
#whitespace characters is considered a word boundary.

song = "The rain in Spain..."
wds = song.split()
print(wds)


song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

#The inverse of the split method is join. You choose 
#a desired separator string, (often called the glue) 
#and join the list with the glue between each of the 
#elements.

wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))
















