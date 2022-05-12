print("Hello world.")
# Getting to know types
print(type(2))
print(type("2"))
print(type(42.0))
print(type([1,1,0]))

def totalSeconds(hours, minutes, seconds):
  hoursInMinutes = 60 * hours
  secondsInMinutes = seconds / 60
  return hoursInMinutes + minutes + secondsInMinutes

def milesToKilometers(kilometers):
  oneMileInKilometers = 1.61
  return kilometers / oneMileInKilometers

# questions that need code
print ("Number 1 - How many seconds are there in 42 minutes 42 seconds?")
formatSeconds = "{:,.2f}".format(totalSeconds(0, 42, 42))
print("The answer is " + formatSeconds + " seconds")

print("Number 2 - How many miles are there in 10 kilometers?")
# Hint: there are 1.61 kilometers in a mile
formatTotalMiles = "{:,.2f}".format(milesToKilometers(10))
#formatKilometers = "{:,.2f}".format(kilometers)
print("There is " + formatTotalMiles + " miles in " + "{:,.2f}".format(10) + " kilometers")

print("Number 3 - If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?")
