def totalSeconds(hours, minutes, seconds):
    hours_in_seconds = hours * 60 * 60
    minutes_in_seconds = minutes * 60
    return hours_in_seconds + minutes_in_seconds + seconds

def kilometerToMile(kilometers):
    one_mile_in_kilometers = 1.61
    return kilometers / one_mile_in_kilometers

def secondsToMinutesAndSeconds(totalSeconds):
    minutes = totalSeconds // 60
    seconds = totalSeconds % 60
    result = "{:,}".format(minutes) + " minute(s) and " + \
        "{:,}".format(seconds) + " second(s)"
    return result

def addSecondsToTime(hours, minutes, seconds, additional_seconds):
    total_seconds = seconds + additional_seconds
    seconds = total_seconds % 60
    total_minutes = minutes + total_seconds // 60
    minutes = total_minutes % 60
    hours = hours + (total_minutes // 60)
    newTime = "{00:,}".format(hours) + ":" + "{00:,}".format(minutes) + ":" + "{00:,}".format(seconds)
    return newTime

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
    format_seconds = "{:,.2f}".format(totalSeconds(0, 42, 42))
    print("The answer is " + format_seconds + " seconds")
    print("\n")

    print("Number 2\nHow many miles are there in 10 kilometers?")
    # Hint: there are 1.61 kilometers in a mile
    format_total_miles = "{:,.2f}".format(kilometerToMile(10))
    #formatKilometers = "{:,.2f}".format(kilometers)
    print("There is " + format_total_miles + " miles in " +
          "{:,.2f}".format(10) + " kilometers")
    print("\n")

    print("Number 3\nIf you run a 10 kilometer race in 42 minutes 42 seconds, \n what is your average pace (time per mile in minutes and seconds)?\nWhat is your average speed in miles per hour?")
    miles = kilometerToMile(10)
    pace_in_seconds = totalSeconds(0, 42, 42)
    pace_in_minutes_and_seconds = "The 'raw' pace is " + \
        secondsToMinutesAndSeconds(pace_in_seconds) + \
        " per " + "{:,.2f}".format(miles) + " miles"
    print(pace_in_minutes_and_seconds)
    # 42'42'' --- 6.21
    #  3,600  --- x
    pace_in_minutes_and_seconds = miles * 3600 / pace_in_seconds
    print("Your pace is " +
          "{:.2f}".format(pace_in_minutes_and_seconds) + " mi/h")
    print("\n")


if __name__ == '__main__':
    main()
