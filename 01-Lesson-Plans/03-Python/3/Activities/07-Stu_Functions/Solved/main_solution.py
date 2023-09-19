# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

def average(numbers):
    return sum(numbers) / len(numbers)


# Test your function with the following:
print(average([1, 2, 3, 4 , 5]))
print(average(range(11)))
list(range(11))