def totalSeconds(hours, minutes, seconds):
    hoursInSeconds = hours * 60 * 60
    minutesInSeconds = minutes * 60
    return hoursInSeconds + minutesInSeconds + seconds


def kilometerToMile(kilometers):
    oneMileInKilometers = 1.61
    return kilometers / oneMileInKilometers


def secondsToMinutesAndSeconds(totalSeconds):
    minutes = totalSeconds // 60
    seconds = totalSeconds % 60
    result = "{:,}".format(minutes) + " minute(s) and " + \
        "{:,}".format(seconds) + " second(s)"
    return result


def main():
    print("Hello world.")
    # Getting to know types
    print(type(2))
    print(type("2"))
    print(type(42.0))
    print(type([1, 1, 0]))
    # END
    print("\n")

    # questions that need code
    print("Number 1\nHow many seconds are there in 42 minutes 42 seconds?")
    formatSeconds = "{:,.2f}".format(totalSeconds(0, 42, 42))
    print("The answer is " + formatSeconds + " seconds")
    print("\n")

    print("Number 2\nHow many miles are there in 10 kilometers?")
    # Hint: there are 1.61 kilometers in a mile
    formatTotalMiles = "{:,.2f}".format(kilometerToMile(10))
    #formatKilometers = "{:,.2f}".format(kilometers)
    print("There is " + formatTotalMiles + " miles in " +
          "{:,.2f}".format(10) + " kilometers")
    print("\n")

    print("Number 3\nIf you run a 10 kilometer race in 42 minutes 42 seconds, \n what is your average pace (time per mile in minutes and seconds)?\nWhat is your average speed in miles per hour?")
    miles = kilometerToMile(10)
    paceInSeconds = totalSeconds(0, 42, 42)
    paceInMinutesAndSeconds = "The 'raw' pace is " + \
        secondsToMinutesAndSeconds(paceInSeconds) + \
        " per " + "{:,.2f}".format(miles) + " miles"
    print(paceInMinutesAndSeconds)
    # 42'42'' --- 6.21
    #  3,600  --- x
    paceInMinutesAndSeconds = miles * 3600 / paceInSeconds
    print("Your pace is " + "{:.2f}".format(paceInMinutesAndSeconds) + " mi/h")
    print("\n")


if __name__ == '__main__':
    main()
