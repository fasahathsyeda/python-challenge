# importing modules
import os
import csv


months=[]
revenue=[]

bank_csv=os.path.join('Resources','budget_data.csv')
output_path = os.path.join('output.txt')

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        months.append(row[0])
        revenue.append(float(row[1]))
        revenuechange=[]
        for i in range(1,len(revenue)):
            revenuechange.append(float(revenue[i])-float(revenue[i-1]))
            averagechange=sum(revenuechange)/len(revenuechange)
            greatestincrease = max(revenuechange)
            greatestdecrease= min(revenuechange)
print ("Financial Analysis")
print (".........................")
print ("Total number of months "+ str(len(months)))#Q1
print ("Total profit and loss "+ str(sum(revenue)))#Q2
print ("Average changes "+ str(averagechange))#Q3
print ("Greatest Increase in " + (months[revenuechange.index(max(revenuechange)) +1] + " " + "(" + str(greatestincrease) +")"))#Q4
print ("Greatest Decrease in " + (months[revenuechange.index(min(revenuechange)) +1] + " " + "(" + str(greatestdecrease)+")")) #Q5


with open(output_path,"w",newline = '') as output_file:
  
    output_file.write ("Financial Analysis\n")
    output_file.write (".........................\n")
    output_file.write ("Total number of months "+ str(len(months))+"\n")
    output_file.write ("Total profit and loss "+ str(sum(revenue))+"\n")
    output_file.write ("Average changes "+ str(averagechange)+"\n")
    output_file.write ("Greatest Increase in " + (months[revenuechange.index(max(revenuechange)) +1] + " " + "(" + str(greatestincrease) +")")+"\n")
    output_file.write ("Greatest Decrease in " + (months[revenuechange.index(min(revenuechange)) +1] + " " + "(" + str(greatestdecrease)+")")+"\n") 





