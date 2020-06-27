import os
import csv

#Open and store the content of budget_data.csv in the variable csvreader
csvpath=os.path.join('/Users/ioanahancu/python-challenge/PyBank/Resources/budget_data.csv')

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header =next(csvreader)
    print(f"Header: {csv_header}")  

for row in csvreader:
    print(row[0])

#Append month and profit/loss to their corresponding lists
#for row in csvreader:
    #total_months.append(row[0])
    #total_profit.append(row[1])

# Take the difference between two months and append to monthly profit change
#for i in range(1, len(total_profit)):
    #monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Obtain the max and min of the the montly profit change list
#max_increase_value = max(monthly_profit_change)
#max_decrease_value = min(monthly_profit_change)

#We use the plus 1 at the end because the month associated with change is the next month
#max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
#max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 























