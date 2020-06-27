import os
import csv

#Store the contents of election_data.csv in the variable csvpath
csvpath=os.path.join('/Users/ioanahancu/python-challenge/PyPoll/Resources/election_data.csv')
with open(csvpath)as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  print(csvreader)
  csv_header =next(csvreader)

print(f"Header: {csv_header}")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#for row in csvreader:
  #print(row[0])

#function += retrieved from: https://www.codecademy.com/forum_questions/555729a8d3292f6e7d000655
#use it to count the total votes
#total_votes +=1
#print(total_votes)

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

