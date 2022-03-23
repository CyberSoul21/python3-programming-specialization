#Values and Data Types

print(3.2)
print("Hello, World!")


#Operators and operands

20 + 32
5 ** 2
(5 + 9) * (15 - 7)

#If you want truncated division, which ignores the remainder, you can use the // operator (for example, 5//2 is 2).



print(9 / 5)
print(5 / 9)
print(9 // 5)

print(7 // 3)    # This is the integer division operator
print(7 % 3)     # This is the remainder or modulus operator

# Order of Operations

    # Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, 2 * (3-1) is 4, and (1+1)**(5-2) is 8. You can also use parentheses to make an expression easier to read, as in (minute * 100) / 60: in this case, the parentheses don’t change the result, but they reinforce that the expression in parentheses will be evaluated first.

    #Exponentiation has the next highest precedence, so 2**1+1 is 3 and not 4, and 3*1**3 is 3 and not 27. Can you explain why?

    #Multiplication and both division operators have the same precedence, which is higher than addition and subtraction, which also have the same precedence. So 2*3-1 yields 5 rather than 4, and 5-2*2 is 1, not 6.

    #Operators with the same precedence are evaluated from left-to-right. In algebra we say they are left-associative. So in the expression 6-3+2, the subtraction happens first, yielding 3. We then add 2 to get the result 5. If the operations had been evaluated from r

print(2 ** 3 ** 2)     # the right-most ** operator gets done first!
print((2 ** 3) ** 2)   # use parentheses to force the order you want!


16 - 2 * 5 // 3 + 1

# Function Calls

def square(x):
   return x * x

def sub(x, y):
   return x - y

print(square(3))
square(5)
print(sub(6, 4))
print(sub(5, 9))


print(square(3) + 2)
print(sub(square(3), square(1+1))) # Function calls as part of complex expressions

print(square)
print(square(3))

#Data Types

print(type("Hello, World!"))
print(type(17))
print("Hello, World")
print(type(3.2))


print(type("17"))
print(type("3.2"))


print(type('This is a string.'))
print(type("And so is this."))
print(type("""and this."""))
print(type('''and even this...'''))

print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')


print("""This message will span several lines of the text.""")

print(42500)
print(42,500)


print(42, 17, 56, 34, 11, 4.35, 32)
print(3.4, "hello", 45)

#Type conversion functions ##########################################################


print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
print(int("23bottles"))


print(float("123.45"))
print(type(float("123.45")))


print(str(17))
print(str(123.45))
print(type(str(123.45)))


#Variables ###########################################################################

message = "What's up, Doc?"
n = 17
pi = 3.14159

Variables

print(message)
print(n)
print(pi)

#Variable Names and Keywords #########################################################

76trombones = "big parade"
more$ = 1000000
# class = "Computer Science 101" #Error

#Variable Names and Keywords ########################################################


#######################################################
# and      as       assert  break    class   continue #
# def      del      elif    else     except  exec     #
# finally  for      from    global   if      import   #
# in       is       lambda  nonlocal not     or       #
# pass     raise    return  try      while   with     #
# yield    True     False    None                     #
#######################################################

#Reassignment #############################################################################

bruce = 5
print(bruce)
bruce = 7
print(bruce)

a = 5
b = a    # after executing this line, a and b are now equal
print(a,b)
a = 3    # after executing this line, a and b are no longer equal
print(a,b)

#Statements and Expressions ##############################################################


print(1 + 1 + (2 * 3))
print(len("hello"))

print(2 * len("hello") + len("goodbye"))

print(square(y + 3))
print(square(y + square(x)))
print(sub(square(y), square(x)))

x = 5
y = 7
add(square(y), square(x))


#Updating Variables########################################################################

x = x + 1

x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)

x = 6        # initialize x
print(x)
x += 3       # increment x by 3; same as x = x + 3
print(x)
x -= 1       # decrement x by 1
print(x)


s = 1
print(s)
s = s + 2
print(s)
s = s + 3
print(s)
s = s + 4
print(s)
s = s + 5
print(s)
s = s + 6
print(s)
s = s + 7
print(s)
s = s + 8
print(s)
s = s + 9
print(s)
s = s + 10
print(s)

x = 12
x = x - 1
print(x)

#Input ###########################################

n = input("Please enter your name: ")

print("Hello", n)

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)


