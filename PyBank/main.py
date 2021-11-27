#Dependencies
import csv
import os

#files I need to load
cvspath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")

#variables i need to work with

#total month needs to be set to 0 so I can count 
totalMonth = 0
totalRevenue = 0
previousRevenue = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 99999999999]
changes=0

#Read the budget_data.csv file
with open(cvspath) as csvfile:
   reader = csv.reader(csvfile)

   csv_header=next(reader)
#I need to loop through the data to collect the answers
   for row in reader:

       #Totaling
          
           
           totalMonth = totalMonth + 1
           totalRevenue = totalRevenue + int(row[1])
           
           if totalMonth!= 1:
                changes+=int(row[1]) - previousRevenue
#changes of revenue calculations
           revenue_change = int(row[1]) - previousRevenue
           previousRevenue = int(row[1])
           month_of_change = month_of_change + [row[0]]

           #Greatest Increase value
           if (revenue_change > greatestIncrease[1]):
               greatestIncrease[1] = revenue_change
               greatestIncrease[0] = row[0]

           if (revenue_change < greatestDecrease[1]):
               greatestDecrease[0] = row[0]
               greatestDecrease[1] = revenue_change
            
        
# calculate the average revenue outside of the loop
revenue_avg = changes / (totalMonth-1)

#print the outcomes
output = (
    f"Total Months: {totalMonth}\n"
    f"Total Revenue: {totalRevenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest increase in Revenue: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest decrease in Revenue: {greatestDecrease[0]} ${greatestDecrease[1]}\n"
)

print(output)

#Write to the text path
with open(pathout, "w") as txt_file:
    txt_file.write(output)

