import os
import csv

csvpath=os.path.join('/Users/ioanahancu/python-challenge/PyBank/Resources/budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}") 









