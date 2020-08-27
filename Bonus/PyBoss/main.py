# importing modules
import os
import csv


state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

inputpath=os.path.join('employee_data.csv')
outputpath=os.path.join("employee_data_formatted.csv")
employeeid=[]
fullname=[]
firstname=[]
lastname=[]
birthdate=[]
newssn=[]
state=[]

#output_path = os.path.join('output.txt')
with open(inputpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    for row in csvreader:
        employeeid.append(row[0])
        fullname=row[1].split(" ")
        firstname.append(fullname[0])
        lastname.append(fullname[1])
        birthdate.append(row[2])
        ssn=row[3].split("-")
        newssn.append("***-***"+ssn[2])
        state.append(state_abbrev[row[4]])


with open(outputpath,"w",newline = '') as outputfile:
    csvwriter=csv.writer(outputfile, delimiter=',')
    csvwriter.writerow(['Employee id','First Name', 'Last Name','Date of Birth', 'SSN','State'])
    for i in range(len(employeeid)):
        #print(employeeid[i])
        csvwriter.writerow([employeeid[i],firstname[i],lastname[i],birthdate[i],newssn[i],state[i]])
