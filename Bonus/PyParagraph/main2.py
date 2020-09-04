import os
import csv
import re
inputfile1=os.path.join('raw_data','paragraph_1.txt')
outputfile1 = os.path.join('paragraph_3_analysis.txt')




inputfile2=os.path.join('raw_data','paragraph_2.txt')
outputfile2 = os.path.join('paragraph_4_analysis.txt')
print("\n\n")


def para_analysis(inputfile,outputfile):
    readfile=open(inputfile,'r')
    para=readfile.read()
    letters=0
    for i in para:
        if i.isalpha():
            letters=letters+1
    word=para.split(sep=" ")
    print("Paragraph Analysis")
    print("------------------------------")
    print("Appoximate word count : " + str(len(word)))

    sentence=re.split("(?<=[.!?'\n\n']) +",para)
    #sen=para_1.split("\n\n")
    #sen=re.split('. |! |? |\n\n',para_1)
    #print(sentence[2])
    print("Approximate sentence count : " + str(len(sentence)))
    #print(sentence)
    lettercount=letters/len(word)
    print(f"Average Letter Count:  {lettercount:.3}")
    print(f"Average Sentence Length : {len(word)/len(sentence)}")

    writefile=open(outputfile,'w')
    writefile.write("Paragraph Analysis\n")
    writefile.write("------------------------------\n")
    writefile.write("Appoximate word count : " + str(len(word))+"\n")
    writefile.write("Approximate sentence count : " + str(len(sentence))+"\n")
    writefile.write(f"Average Letter Count:  {lettercount:.3}\n")
    writefile.write(f"Average Sentence Length : {len(word)/len(sentence)}\n")


para_analysis(inputfile1,outputfile1)

para_analysis(inputfile2,outputfile2)
