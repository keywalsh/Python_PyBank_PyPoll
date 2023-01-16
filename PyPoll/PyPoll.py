#define variables
candidate = []
number_of_votes = []

#import dependencies
import os 
import csv
import collections
from collections import Counter

#link to csv file
pypollcsv = os.path.join("Resources", "election_data.csv")

with open(pypollcsv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

    #read the header row first 
    csv_header = next(csvfile)
        #print(csv_header)
        #this prints Header: Ballot ID,County,Candidate
    
    #read through rows of data after the header 
        #count starts at 0 so row 2 has the voter count data
    for row in csv_reader: 
        candidate.append(row[2])
    
    #sort list by candidate 
    sort_candidates = sorted(candidate)

    #count votes per candidate to add to the list
    count_candidate = Counter (sort_candidates)
    number_of_votes.append(count_candidate.most_common())
        
        #print (number_of_votes)
          
    # calculate the percentage of votes per candicate (3 decimal points)
    for item in number_of_votes:
           
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
   
        #test calculations
            #print(first) 73.812
            #print(second) 23.049
            #print(third) 3.139

#print analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{number_of_votes[0][0][0]}: {first}% ({number_of_votes[0][0][1]})")
print(f"{number_of_votes[0][1][0]}: {second}% ({number_of_votes[0][1][1]})")
print(f"{number_of_votes[0][2][0]}: {third}% ({number_of_votes[0][2][1]})")
print("-------------------------")
print(f"Winner:  {number_of_votes[0][0][0]}")
print("-------------------------")

#explort analysis to text file with the results 
election_data = os.path.join("Output", "PyPoll_Summary.txt")
with open(election_data, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{number_of_votes[0][0][0]}: {first}% ({number_of_votes[0][0][1]})\n")
    outfile.write(f"{number_of_votes[0][1][0]}: {second}% ({number_of_votes[0][1][1]})\n")
    outfile.write(f"{number_of_votes[0][2][0]}: {third}% ({number_of_votes[0][2][1]})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner:  {number_of_votes[0][0][0]}\n")
    outfile.write("-------------------------\n")    