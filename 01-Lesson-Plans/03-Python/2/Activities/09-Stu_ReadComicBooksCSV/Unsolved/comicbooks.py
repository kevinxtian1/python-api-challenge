# Modules
import os
import csv

# Prompt user for title lookup

# Set path for file
csvpath = os.path.join("..", "Resources", "comic_books.csv")

# Set variable to check if we found the video

# Open the CSV using the UTF-8 encoding
find_title = "A castle's in England"
find_title = 'A castle\'s in England'
find_title = input("What is the movie title? ")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    print(headers)


    # Loop through looking for the video
    for row in csvreader:
        if find_title==row[0]:
        #     print("Found it", row)
            print(f"{row[0]} was published by {row[8]} in {row[9]}")

            # Set variable to confirm we have found the video

    # If the book is never found, alert the user
