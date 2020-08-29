import os
import csv
import re
inputfile=os.path.join('raw_data','paragraph_1.txt')
output_path = os.path.join('paragraph_1_analysis.txt')

def Para_analysis(inputfile,outputfile):
    file1=open(inputfile,'r')
    para_1=file1.read()
    #print(para_1)
    letters=0
    for i in para_1:
        if i.isalpha():
            letters=letters+1
    word=para_1.split(sep=" ")
    print("Paragraph Analysis")
    print("------------------------------")
    print("Appoximate word count : " + str(len(word)))
    
    a="\n\n"
    sen=para_1.split("\n\n")
    sentence=re.split("(?<=[.!?]) +",para_1)
    
    #print(sentence[2])
    print("Approximate sentence count : " + str(len(sentence)))
    #print(sentence)
    lettercount=letters/len(word)
    print(f"Average Letter Count:  {lettercount:.3}")
    print(f"Average Sentence Length : {len(word)/len(sentence)}")

    file2=open(outputfile,'w')
    file2.write("Paragraph Analysis\n")
    file2.write("------------------------------\n")
    file2.write("Appoximate word count : " + str(len(word))+"\n")
    file2.write("Approximate sentence count : " + str(len(sentence))+"\n")
    file2.write(f"Average Letter Count:  {lettercount:.3}\n")
    file2.write(f"Average Sentence Length : {len(word)/len(sentence)}\n")
#Para_analysis("raw_data/paragraph_1.txt","paragraph_1_analysis.txt")
Para_analysis("raw_data/paragraph_2.txt","paragraph_2_analysis.txt")
