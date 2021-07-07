counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}


for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters ")

voting_data = [{'county': 'Arapahoe', 'registered_voters': 422829},
{'county': "Denver", 'registered_voters': 463353},
{'county': "Jefferson", 'registered_voters': 432438}]

#retrive the dictionaries
for county_dict in voting_data:
    print(county_dict)

#retrive the values of county
for county in range(len(voting_data)):
    print(voting_data[county]['county'])

#retrive all the values
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#retrive the county names
for county_dict in voting_data:
    print(county_dict['county'])

#f-stings 3.2.11
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#multiple F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#skill_drill 3.2.11 (1)
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

#skill_drill 3.2.11 (2)
for county_dict in voting_data:
    print(f'{county_dict["county"]} county has {county_dict["registered_voters"]:,} registered voters.')

