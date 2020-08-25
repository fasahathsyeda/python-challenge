
import os
import csv



input_path=os.path.join('Resources','election_data.csv')
output_path = os.path.join('output.txt')
voterId=[]
candidates=[]
representatives=[]
representativeVotes=[]


with open(input_path) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        voterId.append(row[0])
        candidates.append(row[2])
        representatives=list(set(candidates))
    print(representatives)
        
        
    print("Total votes :"+str(len(voterId)))
    print(len(candidates))

    representativeVotes=[]
    
        
        #print(len(representatives))
        #for j in range(len(representatives)):   
            #print(f"{representative[j]} : {(representativeVotes[j]/len(voterId))*100} ({representativeVotes[j]}) ")

  
winner=representatives(representativeVotes.index(max(representativeVotes)))
print(f("Winner : {winner}"))