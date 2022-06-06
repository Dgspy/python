#simple method to use ternary operator
# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)

print(10 if 10 > 20 else 20)

#Direct Method by using tuples, Dictionary, and lambda
print()

# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# elif [a<b] is false then value of False key will print
print({True: a, False: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())

#Ternary operator can be written as nested if-else:
print()

# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is big than a")
print()

# Python program to demonstrate nested ternary operator
a, b = 10, 20

if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")

print()
#To use print function in ternary operator be like:- 

a=5
b=7

# [statement_on_True] if [condition] else [statement_on_false]

print(a,"is greater") if (a>b) else print(b,"is Greater")
print()

# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)
