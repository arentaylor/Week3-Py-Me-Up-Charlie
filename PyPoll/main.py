#import os and csv files
import os
import csv

#initialize variables
candidates = []
votes_sum = 0
vote_counts = []

# create file path and save as file
pollfile = os.path.join(".", "election_data.csv")

#open the file
with open(pollfile, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #skip the header
    line = next(csvread,None)

    #go through data to process votes
    for line in csvread:

        #add to total number of votes
        votes_sum = votes_sum + 1

        #candidate who received vote
        candidate = line[2]

        #adding to total candidate votes
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else new candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find calculations for output
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/votes_sum*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results to terminal
#cannot get it to display 3 decimal points :(
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes_sum}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {round(percentages[count],3)}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#print analysis to file

with open('PyPoll.txt', 'w') as text_file:
	
    print("Election Results", file=text_file)
    print("--------------------------", file=text_file)
    print(f"Total Votes: {votes_sum}", file=text_file)
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {round(percentages[count],3)}% ({vote_counts[count]})", file=text_file)
    print("---------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print("---------------------------", file=text_file)