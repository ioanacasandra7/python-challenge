import os
import csv

#Store the contents of election_data.csv in the variable csvpath
csvpath=os.path.join('/Users/ioanahancu/python-challenge/PyPoll/Resources/election_data.csv')
votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []
khan_votes=[]
correy_votes=[]
li_votes=[]
otooley=[]

with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header =next(csvreader)

    print(f"Header: {csv_header}")

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
#calculate total votes
total_votes = (len(votes))
print(total_votes)

#calculate votes per candidate
for candidate in candidates:
        if candidate == "Khan":
            khan.append(row[2])
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(row[2])
            correy_votes= len(correy)
        elif candidate == "Li":
             li.append(row[2])
             li_votes = len(li)
        else:
            otooley.append(row[2])
            otooley_votes =len(otooley)

        print(khan_votes)
        print(correy_votes)
        print(li_votes)
        print(otooley_votes)






#column 2 contains the candidates, so we can loop through it and count the total votes for each candidate
#if row[2] == "Khan": 
 ##  khan_votes +=1
#elif row[2] == "Correy":
 #  correy_votes +=1
#elif row[2] == "Li": 
 #  li_votes +=1
#elif row[2] == "O'Tooley":
 #  otooley_votes +=1

#we create a dictionary containing both the candidates and the total number of votes for each candidate:
#candidates = ["Khan", "Correy", "Li","O'Tooley"]
#votes = [khan_votes, correy_votes,li_votes,otooley_votes]
#dict_candidates_and_votes = dict(zip(candidates,votes))

# Get the winner by using the max function of the dictionary 
#key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print the votes as percentage
#khan_percent = (khan_votes/total_votes) *100
#correy_percent = (correy_votes/total_votes) * 100
#li_percent = (li_votes/total_votes)* 100
#otooley_percent = (otooley_votes/total_votes) * 100

