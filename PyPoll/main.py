import os
import csv
num_votes = []
candidate = []
individualVotes=[]
representatives=[]


inputfile = os.path.join( "Resources", "election_data.csv")
output_path = os.path.join('output.txt')
	

with open(inputfile, newline='') as myCsvFile:
    csvReader =  csv.reader(myCsvFile, delimiter=',')
    next(csvReader)
    for row in csvReader:
	    num_votes.append(row[0])
	    candidate.append(row[2])
    representatives=list(set(candidate))
   
    

    for i in representatives:
        representativevotes=0
        
        for j in range(len(num_votes)):
            if(candidate[j]==i):
                representativevotes=representativevotes+1
        individualVotes.append(representativevotes)
    #print(individualVotes)
    #for k in range(len(representatives)):
        #print(f"{representatives[k]} : {individualVotes[k]/len(num_votes):.3%}%   ({individualVotes[k]})")
    #print("--------------------------------------")
    #print(f"Winner: { representatives[individualVotes.index(max(individualVotes))]}")

with open(output_path,"w",newline = '') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------------------\n")
    output_file.write(f"Total Votes : {len(num_votes)}\n")
    output_file.write("--------------------------------------\n")
    print("Election Results")
    print("--------------------------------------")
    print(f"Total Votes : {len(num_votes)}")
    print("--------------------------------------")

    for k in range(len(representatives)):
        print(f"{representatives[k]} : {individualVotes[k]/len(num_votes):.3%}%   ({individualVotes[k]})")
        output_file.write(f"{representatives[k]} : {individualVotes[k]/len(num_votes):.3%}%   ({individualVotes[k]})\n")
    print("--------------------------------------")
    output_file.write("--------------------------------------\n")
    print(f"Winner: { representatives[individualVotes.index(max(individualVotes))]}")
    output_file.write(f"Winner: { representatives[individualVotes.index(max(individualVotes))]}")


	    
	
	    