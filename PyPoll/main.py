import csv

fi = open('C:/Users/kateb/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

import os


csvpath = os.path.join("Desktop", "python-challenge", "PyPoll","Resources", "election_data.csv")
pathout = os.path.join("Desktop", "python-challenge", "PyPoll", "Analysis", "election_analysis.txt")

Total_Number_Votes = 0
Unique_Candidates = []
Vote_Count = []

with open(csvpath) as election_data:
   reader = csv.reader(fi)
   next(reader, None) 

for row in reader:
    Total_Number_Votes += 1
    Candidate = (row[2])
    if Candidate in Unique_Candidates:
        Candidate_Index = Unique_Candidates.index(Candidate)
        Vote_Count[Candidate_Index] = Vote_Count[Candidate_Index] + 1
    else:
        Unique_Candidates.append(Candidate)
        Vote_Count.append(1)


Percentage = []
Max_Votes = Vote_Count[0]
Max_Index = 0

for x in range(len(Unique_Candidates)):
    
    Vote_Percentage = round(Vote_Count[x]/Total_Number_Votes*100, 2)
    Percentage.append(Vote_Percentage)
    
    if Vote_Count[x] > Max_Votes:
        Max_Votes = Vote_Count[x]
        Max_Index = x

Winner = Unique_Candidates[Max_Index] 

print('--------------------')
print('Election Results')
print('--------------------')
print(f'Total Votes: {Total_Number_Votes}')
print('--------------------')
for x in range(len(Unique_Candidates)):
    print(f'{Unique_Candidates[x]} : {Percentage[x]}% ({Vote_Count[x]})')
print('--------------------')
print(f'Election winner: {Winner.upper()}')
print('--------------------')


with open(pathout, "w") as txt_file:
    txt_file.write
    txt_file.write('-------------------\n')
    txt_file.write('Election Results\n')
    txt_file.write('--------------------\n')
    txt_file.write(f'Total Votes: {Total_Number_Votes}\n')
    txt_file.write('--------------------\n')
    for x in range(len(Unique_Candidates)):
        txt_file.write(f'{Unique_Candidates[x]} : {Percentage[x]}% ({Vote_Count[x]})\n')
    txt_file.write('--------------------\n')
    txt_file.write(f'Election winner: {Winner.upper()}\n')
    txt_file.write('--------------------\n')

