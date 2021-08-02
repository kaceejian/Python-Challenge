import os
import csv

# Define variables
total_votes = 0
otooley_votes = 0
correy_votes = 0
li_votes = 0
khan_votes = 0


# path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Read into CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Read the header row first 
#(skip this step if there is no header)
    csv_header = next(csvfile)

    for row in csvreader:
        
        # Calculate total votes
        total_votes += 1
        
        # Calculate total votes for each candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            

# calculate each percentage
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    
    # identify the winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 
        
        
        
output = f'''
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
Khan: {kahn_percent:.3%} ({khan_votes})
Correy: {correy_percent:.3%} ({correy_votes})
Li: {li_percent:.3%} ({li_votes})
O'Tooley: {otooley_percent:.3%} ({otooley_votes})
----------------------------
Winner:{winner_name}
'''

print(output)
 

    
output_file = os.path.join('..', 'election_data_2.text')
with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
