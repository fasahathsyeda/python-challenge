import os
import csv
num_votes = []
candidate = []
individualVotes=[]
representatives=[]


inputfile = os.path.join( "Resources", "election_data.csv")
	

with open(inputfile, newline='') as myCsvFile:
    csvReader =  csv.reader(myCsvFile, delimiter=',')
    next(csvReader)
    for row in csvReader:
	    num_votes.append(row[0])
	    candidate.append(row[2])
    representatives=list(set(candidate))
    #print(representatives)
    print("Election Results")
    print("--------------------------------------")
    print(f"Total Votes : {len(num_votes)}")
    print("--------------------------------------")

    for i in representatives:
        representativevotes=0
        #print(i)
        for j in range(len(num_votes)):
            if(candidate[j]==i):
                representativevotes=representativevotes+1
        individualVotes.append(representativevotes)
    #print(individualVotes)
    for k in range(len(representatives)):
        print(f"{representatives[k]} : {individualVotes[k]/len(num_votes):.3%}%   ({individualVotes[k]})")
    print("--------------------------------------")
    print(f"Winner: { representatives[individualVotes.index(max(individualVotes))]}")


	    
	
	    