import os
import csv

#Open and store the content of budget_data.csv in the variable csvreader
csvpath=os.path.join('.','budget_data.csv')

month = []
revenue = []
revenue_change = []
monthly_change = []

with open(csvpath)as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		print(csvreader)
		csv_header =next(csvreader)
		print(f"Header: {csv_header}")

#Append month and profit/loss to their corresponding lists
		for row in csvreader:
			month.append(row[0])
			revenue.append(row[1])
			print(len(month))


# Take the difference between two months and append to monthly change in profit
		i= 0
		for i in range(len(revenue) - 1):
			profit_loss = int(revenue[i+1]) - int(revenue[i])

# append profit_loss
			revenue_change.append(profit_loss)

total_revenue_change= sum(revenue_change)
#print(revenue_change) #to check that the calculation work
monthly_change = total_revenue_change/ len(revenue_change)
#print(monthly_change) #to check

#calculate greatest increase
profit_increase = max(revenue_change)
print(profit_increase)
k = revenue_change.index(profit_increase)
month_increase = month[k+1]

#calculate greatest decrease
profit_decrease = min(revenue_change)
print(profit_decrease)
j = revenue_change.index(profit_decrease)
month_decrease = month[j+1]

#Print Statements
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue_change))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
















# Obtain the max and min of the the montly profit change list
#max_increase_value = max(monthly_profit_change)
#max_decrease_value = min(monthly_profit_change)

#We use the plus 1 at the end because the month associated with change is the next month
#max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
#max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 























