def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

# Stopped at 3.9 page 45

# if __name__ == '__main__':
#    app.run(debug=true)


def right_justify(s):
    number_spaces = 70 - len(s) # number of spaces needed
    print((" " * number_spaces) + s)


right_justify("Lucas DEV")
right_justify("Lucas DEV")
right_justify("Lucas DEV")
right_justify("Lucas DEV")