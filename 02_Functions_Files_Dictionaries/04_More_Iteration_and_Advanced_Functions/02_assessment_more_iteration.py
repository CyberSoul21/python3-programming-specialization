#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(l):
    c=0
    sl=[]
    while l[c] != 5:
        sl.append(l[c])
        c += 1
        if c == len(l):
            break
    return sl

g=[1,2,3,4,5]
print(sublist(g))


#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


def check_nums(l):
    c=0
    sl=[]
    while l[c] != 7:
        sl.append(l[c])
        c += 1
        if c == len(l):
            break
    return sl

g=[1,2,3,4,5,7]
print(check_nums(g))



#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).


def sublist(l):
    c=0
    sl=[]
    while l[c] != "STOP":
        sl.append(l[c])
        c += 1
        if c == len(l):
            break
    return sl

g=["FREE","TD","STOP","H","JO"]
print(sublist(g))


#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.



def stop_at_z(l):
    c=0
    sl=[]
    while l[c] != "z":
        sl.append(l[c])
        c += 1
        if c == len(l):
            break
    return sl

g=["FREE","TD","z","H","po"]
print(stop_at_z(g))


#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.


sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
    
y = 0
sum2=0
while y < len(lst):
    sum2 = sum2 + lst[y]
    y += 1
print(sum2)  