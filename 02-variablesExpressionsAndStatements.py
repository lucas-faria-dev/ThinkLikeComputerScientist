# It is legal to use uppercase letters, but it is conventional to use only lower case for variables names. (page 10)
#import secondsToMinutesAndSeconds
# from ../01/basicCommands import secondsToMinutesAndSeconds
from cmath import pi
import sys
sys.path.append("/Projects/ThinkLikeComputerScientist/01/")
import basicCommands as basic


print("-----  START  -----")
first = "throat"
second = "warbler"
print("\n")
print(first + second)
print("\n")
print("Spam " * 3)
print("\n")


print("-  EXCERCISES  -")
print("Number 1\nThe volume of a sphere with radius r is 4/3 πr^3. What is the volume of a sphere with radius 5?")
radius = 5
volume = 4 / 3 * pi * radius ** 3
print("The volume of a sphere with rapdius 5 is " + "{:,.2f}".format(volume))

print("\nNumber 2\nSuppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?")
cover_price = 24.95
discount = 0.4  # bookstores get a 40% discount
number_of_copies = 60
# $3 for the first copy and 75 cents for each additional copy
shipping = 3 + .75 * (number_of_copies - 1)
total_wholesale_cost = cover_price * \
    number_of_copies * (1 - discount) + shipping
print("The total wholesale cost is $" + "{:,.2f}".format(total_wholesale_cost))


print("\nNumber 3\n If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?")
# All times are in seconds
first_time = basic.totalSeconds(0, 8, 15) * 2 # in seconds
second_time = basic.totalSeconds(0, 7, 12) * 3

print(first_time + second_time)
print(basic.secondsToMinutesAndSeconds(first_time + second_time))
print(basic.addSecondsToTime(6, 52, 0, first_time + second_time))
print("-----  END  -----")
