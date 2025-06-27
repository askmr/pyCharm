# Convert data in seconds to hours and minutes

Time1 = 8661

hour1 = Time1 // 3600  # because 1 hour is 3600 seconds, for conversion because data is in seconds
sec1 = 8661 % 3600
min1 = sec1 // 60
sec1 = sec1 % 60

print("The time is: \n", hour1, "hrs:", min1, "m:", sec1, "seconds")

# Here the data is taken in run-time (dynamically)

Time2 = int(input("Enter the time(in seconds): \n"))  # 3661

hour2 = Time2 // 3600  # because 1 hour is 3600 seconds, for conversion because data is in seconds
sec2 = Time2 % 3600
min2 = sec2 // 60
sec2 = sec2 % 60

# Using an if-else only for hours if its singular or plural
if hour2 == 1:
    print("The time is: \n", hour2, "hr:", min2, "m:", sec2, "seconds")
else:
    print("The time is: \n", hour2, "hrs:", min2, "m:", sec2, "seconds")
