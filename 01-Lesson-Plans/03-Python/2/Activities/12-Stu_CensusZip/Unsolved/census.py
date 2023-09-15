import os
import csv

census_csv = os.path.join("..", "Resources", "census_starter.csv")

# Lists to store data
place = []
population = []
income = []
poverty_count = []
poverty_rate = []
county = []
state = []

# "Place,
# Population,
# Median Age
# ,Household Income
# ,Per Capita Income
# ,Employed Civilians
# ,Unemployed Civilians
# ,People in the Military
# ,Poverty Count"

def split_place(place):
    return place.split(", ")
# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(census_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        row[1] = int(row[1])
        row[4] = int(row[4])
        place.append(row[0])
        population.append(row[1])
        income.append(int(row[4]))
        poverty_count.append(row[4])
        poverty_rate.append(round(row[4]/row[1], 2))
        county_state = split_place(row[0])
        county.append(county_state[0])
        state.append(county_state[1])

        # Add place

        # Add population

        # Add per capita income

        # Add poverty count

        # Determine poverty rate to 2 decimal places, convert to string

        # Split the place into county and state

# Zip lists together
all_info = list(zip(place, population, income, poverty_count, poverty_rate, county, state))


# Set variable for output file
output_file = os.path.join("census_final.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Place", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate",
                    "County", "State"])

    # Write in zipped rows
    writer.writerows(all_info)
