import os
import csv

#Store the contents of election_data.csv in the variable csvpath
csvpath=os.path.join('.','election_data.csv')
vote={}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header =next(csvreader)

    print(f"Header: {csv_header}")

    
    for row in csvreader:
        candidate = str(row[2])
        vote[candidate] = vote.get(candidate, 0) + 1

for candidate in vote:
    print(candidate,vote[candidate])
winner=""
top_votes=0
total_votes=0
for candidate in vote:
    total_votes +=vote[candidate]
    if vote[candidate]>top_votes:
        winner=candidate
        top_votes=vote[candidate]
print(winner)
print(top_votes)
print(total_votes)












