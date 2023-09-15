# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
# a >=0 and a < 10
for x in range(0, 10):
    print(x)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
# a >=20 and a < 30
for x in range(20, 30):
    print(x)

# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]

for word in words:
    print(word)

# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes"
while x.lower() == "yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")
