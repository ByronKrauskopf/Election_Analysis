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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)