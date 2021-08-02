import pathlib
import csv
csvpath = pathlib.Path('resources/budget_data.csv')

with open(csvpath) as file:
    file_reader = csv.reader(file, delimiter=',')
    line_count = 0
    total_value = 0
    changes = []
    months = []
    
    header = next(file_reader)
    first_row = next(file_reader)
#     print(first_row)
    
    amount = int(first_row[1])

    line_count += 1
    total_value += amount
    
    
    for row in file_reader:
#         print(row[1])
        current_change = int(row[1]) - amount
#         print(row)
        changes.append(current_change)
        months.append(row[0])
        amount = int(row[1])
        
        
        line_count += 1
        total_value += amount
        
        
output = f'''
Financial Analysis
----------------------------
Total Months: {line_count}
Total: ${total_value}
Average  Change: ${(sum(changes)/len(changes))}
Greatest Increase in Profits: {months[changes.index(max(changes))]} (${max(changes)})
Greatest Decrease in Profits: {months[changes.index(min(changes))]} (${min(changes)})
'''

print(output)
# print(months)
# print(line_count)
# print(total_value)
# print(sum(changes)/len(changes))
# print(max(changes))
# print(min(changes))
# len(csvpath[""])