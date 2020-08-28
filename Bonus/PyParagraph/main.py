import os
import csv
import re
#inputfile=os.path.join('raw_data','paragraph_1.txt')
output_path = os.path.join('paragraph_1_analysis.txt')

file1=open("raw_data/paragraph_1.txt",'r')
para_1=file1.read()
#print(para_1)
letters=0
for i in para_1:
    if i.isalpha():
        letters=letters+1

word=para_1.split()
print("Paragraph Analysis")
print("------------------------------")
print("Appoximate word count : " + str(len(word)))
sentence=re.split("(?<=[.!?]) +",para_1)
print("Approximate sentence count : " + str(len(sentence)))
lettercount=letters/len(word)
print(f"Average Letter Count:  {lettercount:.3}")
print(f"Average Sentence Length : {len(word)/len(sentence)}")

