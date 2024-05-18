fin = open("words.txt")
words = fin.read().split("\n")

### Write a program that reads words.txt and prints only the words with more than 20
### characters (not counting whitespace).
#for i in words:
#    if len(i.strip()) > 20:
#        print(i)

### Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
### it.
def has_no_e(word):
    return not ("e" in word)

total = 0
total_has_e = 0
total_has_no_e = 0

for i in words:
    if len(i.strip()) > 0:
        total = total + 1
        if has_no_e(i.strip()):
            total_has_no_e = total_has_no_e + 1
            print(i)
        else:
            total_has_e = total_has_e + 1

print("Total words: " + str(total))
print("Total has e: " + str(total_has_e) + " " + str(total_has_e / total * 100) + "%")
print("Total has no e: " + str(total_has_no_e) + " " + str(total_has_no_e / total * 100) + "%")