import os
import csv


voter_id_list = []
candidate_list = []
votecount = {}
winner_vote = 0


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"csv Header: {csv_header}")

    for row in csvreader:
        candidate = row["Candidate"]
        voter_id_list.append(row["Voter ID"])
        
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            votecount[candidate] = 1
        else:
            votecount[candidate] += 1

    # total number of votes
    total_votes = len(voter_id_list)
    #print(total_votes)
    #print(votecount)
       
    # calculate percentage
    candidate_percentage = {candidate : votecount[candidate] / total_votes for candidate in candidate_list}
    #print(candidate_percentage)

    #calculate winner  
    for item in candidate_percentage.items():
        if item[1] > winner_vote:
            winner_vote = item[1]
            winner = item[0]
        #print(winner) 

    rows = []
    row1 = f"Election Results" +"\n"
    rows.append(row1)
    row2 = f"-----------------------\n"
    rows.append(row2)
    row3 = f"Total Votes:  {total_votes}" +"\n"     
    rows.append(row3)
    row4 = f"------------------------\n"
    rows.append(row4)

    #for loop to get each candidate info 
    for candidate in candidate_list:
        row5 = ("{}: ".format(candidate) + "{:.3%}".format(candidate_percentage[candidate]) + " ({})".format(votecount[candidate]))
        rows.append(row5)
        #print(row5)
    
    row6 ="\n"+ "-"*25 + "\n"
    rows.append(row6)
    row7 = f"Winner: {winner}" + "\n"
    rows.append(row7)
    rows.append(f"-"*25)

    for row in rows:
        print(row)

# set variable for output  file
output_file = os.path.join("analysis", "election_result")

#write to the output file
with open(output_file, "w") as datafile:
     for row in rows:
         datafile.write(f"{row}\n")