#Mutability
#Some Python collection types - strings and lists so far - 
#are able to change and some are not. If a type is able to change, 
#then it is said to be mutable. If the type #is not able to change then it is said to be immutable. 

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)


alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)


alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

#We can even insert elements into a list by squeezing them into an empty slice at the desired location.

alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

#Strings are Immutable

#One final thing that makes strings different from some 
#other Python collection types is that you are not 
#allowed to modify the individual characters in the
# collection.

greeting = "Hello, world!"
greeting[0] = 'J'            # ERROR!
print(greeting)

#which means you cannot change an existing string. 
#The best you can do is create a new string that is a 
#variation on the original.

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was


phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"

print(excited_phrase_complete)

#Tuples are Immutable



#List Element Deletion##################################

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

#Objects and References################################

a = "banana"
b = "banana"


#we know that a and b will refer to a string with the letters "banana". But we don’t know yet whether they point to the same string.

#In one case, a and b refer to two different string objects that have the same value. In the second case, they refer to the same object. Remember that an object is something a variable can refer to.

#We can test whether two names refer to the same object using the is operator. The is operator will return true if the two references are to the same object. In other words, the references are the same. Try our example from above.

a = "banana"
b = "banana"

print(a is b)

#The answer is True. This tells us that both a and b refer to the same object, and that it is the second of the two reference diagrams that describes the relationship. Python assigns every object a unique id and when we ask a is b what python is really doing is checking to see if id(a) == id(b).


a = "banana"
b = "banana"

print(id(a))
print(id(b))

#Since strings are immutable, the Python interpreter often optimizes resources by making two names that refer to the same string value refer to the same object. You shouldn’t count on this (that is, use == to compare strings, not is), but don’t be surprised if you find that two variables,each bound to the string “banana”, have the same id..

#This is not the case with lists, which never share an id just because they have the same contents. Consider the following example. Here, a and b refer to two different lists, each of which happens to have the same element values. They need to have different ids so that mutations of list a do not affect list b.



a = [81,82,83]
b = [81,82,83]

print(a is b)

print(a == b)

print(id(a))
print(id(b))

#a and b have equivalent values but do not refer to the same object. Because their contents are equivalent, a==b evaluates to True; because they are not the same object, a is b evaluates to False.


#Aliasing##########################################

#Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:

a = [81, 82, 83]
b = a
print(a is b)

#Because the same list has two different names, 
#a and b, we say that it is aliased. 
#Changes made with one alias affect the other. 
#In the codelens example below, you can see that a 
#and b refer to the same list after executing the 
#assignment statement b = a.

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

#Although this behavior can be useful, it is 
#sometimes unexpected or undesirable. In general, 
#it is safer to avoid aliasing when you are working 
#with mutable objects. Of course, for immutable objects, 
#there’s no problem. That’s why Python is free to alias 
#strings and integers when it sees an opportunity to 
#economize.




#Cloning Lists#####################################

#If we want to modify a list and also keep a copy 
#of the original, we need to be able to make a copy 
#of the list itself, not just the reference. 
#This process is sometimes called cloning, to avoid 
#the ambiguity of the word copy.


a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

#Now we are free to make changes to b without 
#worrying about a. Again, we can clearly see in 
#codelens that a and b are entirely different list 
#objects.


#Mutating Methods###################################

#List Methods########################################

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)


mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   #probably an error
print(mylist)


#Append versus Concatenate##############################

origlist = [45,32,88]

origlist.append("cat")
print(origlist)


origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used






st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)


st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)

#Non-mutating Methods on Strings#################

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)



ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)


food = "banana bread"
print(food.upper())4




s = "python rocks"
print(s[1]*s.index("n"))


#String Format Method####################3


name = "Rodney Dangerfield"
score = -1  # No respect!
print("Hello " + name + ". Your score is " + str(score))


scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))


    scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))



    scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))


person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)



person = input('Enter your name: ')
print('Hello {}!'.format(person))




origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)



origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)


name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.
