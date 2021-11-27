# Import modules
import os
import csv

# Create variables to hold data
voter_id = []
candidate = []
candidate_names = []
percentage = []
vote_count = []
winner = 0
winner_candidate = ""

# create output variable to hold data to print
output = (
        f"Election Results\n"
        f"---------------------\n")

# Specify the file path for csv file
csv_path = os.path.join("Resources", "election_data.csv")

# Read the csv file
with open(csv_path, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header first
    csv_header = next(csvreader)

    # Read the rows to put data in the lists
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

    # Calculate the total by counting voter id's and print the result
    total_votes = len(voter_id)
    
    # add results to output variable
    output = output + (f"Total Votes: {total_votes}\n" 
        f"---------------------\n")
    
    # Create a list to keep candidate names
    for row in candidate: 
        if row not in candidate_names:
            candidate_names.append(row)

    # Count each candidates votes and calculate percentage
    for name in candidate_names:
        count = 0
        for row in candidate:
            if name == row:
                count += 1
                percent = float(count) / float(total_votes) * 100
            if count > winner:
                winner = count
                winner_candidate = name
        
        # Put data to the lists
        percentage.append(percent)
        vote_count.append(count) 

        # Grab the name's indexes for corresponding percentage and count variables
        j = candidate_names.index(name)
              
        # keep building the output
        output = output + (f"{candidate_names[j]}: {percentage[j]:.3f}% ({vote_count[j]})\n")

    output = output + (f"----------------------\n"
        f"Winner : {winner_candidate}\n"
        f"----------------------\n")
    # print the output to the terminal
    print(output, end="")
    
    # Create an output path to write data
    output_file = os.path.join("Resources", "vote_analysis.txt")

    # Write the output file 
    with open(output_file, "w") as text:
        text.write(output)