# Add out dependencies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Declare a new list candidate_options
candidate_options = []

# Declar a empty dictionary 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count =  0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate then add the name
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1    
    #iterate through the candidate list. 
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes) * 100
        # to do: Print out each candidate's name, vote count, and percentage of vote to
        # the terminal
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        
        # Determine the winning vote cout and candidate
        # Determine if the votes are greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

# To do: print out 
winning_candidate_summary = (f"----------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"---------------------------")
print(winning_candidate_summary)