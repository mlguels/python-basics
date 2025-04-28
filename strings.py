#escape character example
print("\n")
# t is for tab
me = "C\ta\tl\te\tb\n"



# Single and double quotes
# you can use single quotes
you = 'John'

me = "Caleb" #reset to normal

#passing multiple arguments to print
print(me, you)


#double quotes and single quotes work the same way with the exception of working with quotes inside.
#here are some examples:

single_quotes = 'She said "Hi"'
print(single_quotes)

double_quotes = "She said \"Hi\""
print(double_quotes)

#notice we have to escape the same quote as the surrounding quote

single_quotes = 'I\'m learning!'
print(single_quotes)

double_quotes = "I'm learning!"
print(double_quotes)

# Raw strings ignore escape characters
print(r"as raw as I\'ve ever seen. \/\/ () \/\/. \t")

# String concatenation
add = "World"
string = "Hello" + " " + add
print(string)

# F Strings
name = "Miguel"
last_name = "Rodriguez"

print(F"Hello {name} {last_name}")

# Multi-line strings

#You can also use multiline string
print("""Name: Caleb
Age: 58""")

#skip newline using \ (without it, it would go down a line each line)
print("""\
Name: Caleb. \
Age: 58""")

"""You may see
them as multi-
line comments even
if they technically
are not. 
"""

# Indexes and slices
# Strings are indexed starting at 0

msg = "This is a very important message."
print(msg[0]) # H
print(msg[-2])
print(msg[1:2])
print(msg[-5:])


print(msg[42:43])



# String immutability
msg = "Java is my favorite!"
# msg[0] = 'K' #nope
# You can however generate a new string from the original:
new = "K" + msg[1:]
print(new)

# You can also replace the original
msg = 'K' + msg[1:]
print(msg)

# What about string concatenation? This actually replaces the original string by creating a new string.
language = "Java"
language += " is actually coffee" 
print(language)


# lengths
# len() returns the length of a string
phone = "iPhone"
print(len(phone))
print("Index 4:", phone[4])
print("Last index:", phone[len(phone) - 1])
print([len(phone) - 1])

length = len(phone)
pri = F"Length of {phone} is {length}"
print(pri)