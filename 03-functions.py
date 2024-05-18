print("-----  START  -----")
print(type(42))
print("\n")
int(32)
int(3.9999)
int(-2.9999)
float(32)
float("3.14159")

import math
print(math)


#ratio = signal_power / noise_power
#decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)


def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

print_lyrics()

print("Number 1\nWrite a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.\n\n>>> right_justify('monty')\nmonty\n\nHint: Use string concatenation and repetition. Also, Python provides a built-in function called len that returns the length of a string, so the value of len('monty') is 5.")

def right_justify(s):
  range_array = range(70 - len(s))
  spaces = ""
  for x in range_array:
    spaces = spaces + " "
  print(spaces + s)

right_justify("a")

print("Number 2\nA function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:\ndef do_twice(f):\nf()\nf()\n\nHere’s an example that uses do_twice to call a function named print_spam twice.\ndef print_spam():\nprint('spam')\ndo_twice(print_spam)\n\n1. Type this example into a script and test it.\n2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.\n3. Copy the definition of print_twice from earlier in this chapter to your script.\n4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.\n5. Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.")

print("-----  END  -----")