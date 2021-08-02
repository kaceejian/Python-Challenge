import os
import csv

# Define variables
total_votes = 0
otooley_totalvotes = 0
correy_totalvotes = 0
li_totalvotes = 0
khan_totalvotes = 0


# path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Read into CSV file
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
# Read the header row first 
#(skip this step if there is no header)
    csv_header = next(csvfile)

    for row in csv_reader:
        
        # Calculate total votes
        total_votes += 1
        
        # Calculate total votes for each candidate
        if (row[2] == "Khan"):
            khan_totalvotes += 1
        elif (row[2] == "Correy"):
            correy_totalvotes += 1
        elif (row[2] == "Li"):
            li_totalvotes += 1
        else:
            otooley_totalvotes += 1
            

# calculate each percentage
    kahn_percent = khan_totalvotes / total_votes
    correy_percent = correy_totalvotes / total_votes
    li_percent = li_totalvotes / total_votes
    otooley_percent = otooley_totalvotes / total_votes
    
    # identify the winner
    winner = max(khan_totalvotes, correy_totalvotes, li_totalvotes, otooley_totalvotes)

    if winner == khan_totalvotes:
        winner_name = "Khan"
    elif winner == correy_totalvotes:
        winner_name = "Correy"
    elif winner == li_totalvotes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 
        
        
        
output = f'''
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
Khan: {kahn_percent:.3%} ({khan_totalvotes})
Correy: {correy_percent:.3%} ({correy_totalvotes})
Li: {li_percent:.3%} ({li_totalvotes})
O'Tooley: {otooley_percent:.3%} ({otooley_totalvotes})
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
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_totalvotes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_totalvotes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_totalvotes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_totalvotes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
