#Add dependencies
import os
import csv
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to write to
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Init total vote coutnter
total_votes = 0
# Declare new list for getting candidate names
candidate_options= []
# empty dictionary for candidate votes
candidate_votes = {}
#winning candidate and winnign count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #to-do: read and analyze the data here
    #read the filw object with the reader function.
    file_reader = csv.reader(election_data)
   #Print the header row.
    headers = next(file_reader)
    #Print each row
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0        
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            if (votes > winning_count) and  (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winngin Percentage: {winning_percentage:.1f}\n"
        f"-----------------------\n"
    )
    print(winning_candidate_summary)

