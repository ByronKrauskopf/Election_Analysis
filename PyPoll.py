# Data needed
# 1. The total number of votes
# 2. Complete list of candidates who received votes
# 3. The total number of votes each candidate received
# 4. The percentage of votes each candidate received
# 5. The winner of the election based on the popular vote

#Add dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt") 

# Initialize a total vote counter
total_votes = 0

#create candidate options list
candidate_options = []

#declare candidate_votes dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote counter
        total_votes = total_votes + 1
        
        #Print the candidate name from each row
        candidate_name = row[2]
        
        #If candiate_name does not exist in candidate_options
        if candidate_name not in candidate_options:
            #Add candidate_name to candidate_options list
            candidate_options.append(candidate_name)
            #intialize candidate_votes count
            candidate_votes[candidate_name] = 0
        #add votes to candidate_votes
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Determine the percentage votes for each candidate
#loop through the candiate list
for candidate_name in candidate_votes:
    #retrieve vote count for candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print candidate_name, vote_count and vote_percentage to terminal 
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if votes is greater then the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning_candidate = candidate_name
        winning_candidate = candidate_name

#print winning candidate
winning_candidate_summary = (f"------------------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"------------------------------------")
print(winning_candidate_summary)

#Print the total votes
print(f"{total_votes} total votes cast")

