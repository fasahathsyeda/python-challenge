import os
import csv
#inputfile=os.path.join('raw_data','paragraph_1.txt')
output_path = os.path.join('paragraph_1_analysis.txt')

file1=open("raw_data/paragraph_1.txt",'r')
para_1=file1.read()
print(para_1)
word_count=para_1.split()
print("Appoximate word count : " + str(len(word_count)))
