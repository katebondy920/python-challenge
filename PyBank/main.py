import csv

fi = open('C:/Users/kateb/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

import os


csvpath = os.path.join("Desktop", "python-challenge", "PyBank","Resources", "budget_data.csv")
pathout = os.path.join("Desktop", "python-challenge", "PyBank", "Analysis", "budget_analysis.txt")

Total_Month = 0
Total_Revenue = 0
Previous_Revenue = 0
Revenue_Change = 0
Revenue_Change_List = []
Month_of_Change = []
Greatest_Increase = ["",0]
Greatest_Decrease = ["",999999999999999999999]

with open(csvpath) as revenueData:
   reader = csv.reader(fi)
   next(reader, None) 

print(f'text')
print(f'Financial Analysis')
print(f'-------------------------------------------')

for row in reader:

    Total_Month = Total_Month + 1
    Total_Revenue = Total_Revenue + int(row[1])
    Revenue_Change = int(row[1]) - Previous_Revenue
    Previous_Revenue = int(row[1])
    Month_of_Change = Month_of_Change + [row[0]]

    if (Revenue_Change > Greatest_Increase[1]):
        Greatest_Increase[1] = Revenue_Change
        Greatest_Increase[0] = row[0]
    
    if (Revenue_Change < Greatest_Decrease[1]):
        Greatest_Decrease[1] = Revenue_Change
        Greatest_Decrease[0] = row[0]

    Revenue_Change_List.append(int(row[1]))

Revenue_Average = sum(Revenue_Change_List) / len(Revenue_Change_List)

output = (
f"Total Months: {Total_Month}\n"
f"Total Revenue: ${Total_Revenue}\n"
f"Average Revenue Change: ${Revenue_Average}\n"
f"Greatest Increase in Revenue: {Greatest_Increase[0]} ${Greatest_Increase[1]}\n"
f"Greatest Decrease in Revenue: {Greatest_Decrease[0]} ${Greatest_Decrease[1]}\n"
)

print(output)

with open(pathout, "w") as txt_file:
    txt_file.write(output)
