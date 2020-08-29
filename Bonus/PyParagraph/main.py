import os
import csv
import re
inputfile1=os.path.join('raw_data','paragraph_1.txt')
outputfile1 = os.path.join('paragraph_1_analysis.txt')


file1=open(inputfile1,'r')
para_1=file1.read()
letters1=0
for i in para_1:
    if i.isalpha():
        letters1=letters1+1
word1=para_1.split(sep=" ")
print("Paragraph Analysis")
print("------------------------------")
print("Appoximate word count : " + str(len(word1)))

sentence1=re.split("(?<=[.!?]) +",para_1)
#sen=para_1.split("\n\n")
#sen=re.split('. |! |? |\n\n',para_1)
#print(sentence[2])
print("Approximate sentence count : " + str(len(sentence1)))
#print(sentence)
lettercount1=letters1/len(word1)
print(f"Average Letter Count:  {lettercount1:.3}")
print(f"Average Sentence Length : {len(word1)/len(sentence1)}")

file2=open(outputfile1,'w')
file2.write("Paragraph Analysis\n")
file2.write("------------------------------\n")
file2.write("Appoximate word count : " + str(len(word1))+"\n")
file2.write("Approximate sentence count : " + str(len(sentence1))+"\n")
file2.write(f"Average Letter Count:  {lettercount1:.3}\n")
file2.write(f"Average Sentence Length : {len(word1)/len(sentence1)}\n")


inputfile2=os.path.join('raw_data','paragraph_2.txt')
outputfile2 = os.path.join('paragraph_2_analysis.txt')
print("\n\n")


file3=open(inputfile2,'r')
para_2=file3.read()
letters2=0
for i in para_2:
    if i.isalpha():
        letters2=letters2+1
word2=para_2.split(sep=" ")
print("Paragraph Analysis")
print("------------------------------")
print("Appoximate word count : " + str(len(word2)))

#sentence2=re.split("(?<=[.!?]) +",para_2)
sentence2=para_2.split("\n\n")
#sen=re.split('. |! |? |\n\n',para_1)
#print(sentence[2])
print("Approximate sentence count : " + str(len(sentence2)))
#print(sentence)
lettercount2=letters2/len(word2)
print(f"Average Letter Count:  {lettercount2:.3}")
print(f"Average Sentence Length : {len(word2)/len(sentence2)}")

file4=open(outputfile2,'w')
file4.write("Paragraph Analysis\n")
file4.write("------------------------------\n")
file4.write("Appoximate word count : " + str(len(word2))+"\n")
file4.write("Approximate sentence count : " + str(len(sentence2))+"\n")
file4.write(f"Average Letter Count:  {lettercount2:.3}\n")
file4.write(f"Average Sentence Length : {len(word2)/len(sentence2)}\n")