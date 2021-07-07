temperature = int(input('What is the temperature outside?'))

if temperature > 80:
    print("Turn on the AC")

else:
    print("Open the windows")

#3.4.1 learning
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print(f"The time right now is {now}")