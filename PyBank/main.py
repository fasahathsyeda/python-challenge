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


with open(output_path,"w",newline = '') as output_file:
  
    output_file.write ("Financial Analysis\n")
    print("Financial analysis")
    output_file.write (".........................\n")
    print (".........................")
    output_file.write ("Total number of months "+ str(len(months))+"\n")
    print ("Total number of months "+ str(len(months)))
    output_file.write ("Total profit and loss "+ str(sum(revenue))+"\n")
    print ("Total profit and loss "+ str(sum(revenue)))
    output_file.write ("Average changes "+ str(averagechange)+"\n")
    print ("Average changes "+ str(averagechange))
    output_file.write ("Greatest Increase in " + (months[revenuechange.index(max(revenuechange)) +1] + " " + "(" + str(greatestincrease) +")")+"\n")
    print ("Greatest Increase in " + (months[revenuechange.index(max(revenuechange)) +1] + " " + "(" + str(greatestincrease) +")"))
    output_file.write ("Greatest Decrease in " + (months[revenuechange.index(min(revenuechange)) +1] + " " + "(" + str(greatestdecrease)+")")+"\n") 
    print ("Greatest Decrease in " + (months[revenuechange.index(min(revenuechange)) +1] + " " + "(" + str(greatestdecrease)+")"))




