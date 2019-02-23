#import OS and CSV libraries
import os
import csv

#create variables for calculations
count_months = 0
total_revenue = 0
total_revenue_change = 0

# create file path and save as file
budgetfile = os.path.join(".", "budget_data.csv")

#open file and create file handle
with open(budgetfile, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #skip header row
    line = next(csvread,None)

    #grab data from first line
    line = next(csvread,None)
    max_month = line[0]
    min_month = line[0]
    revenue = float(line[1])
    min_revenue = revenue
    max_revenue = revenue
    previous_revenue = revenue
    count_months = 1
    total_revenue = float(line[1])
    total_revenue_change = 0

    #go through data to process revenue
    for line in csvread:

        #increase counter for number of months in dataset
        count_months = count_months + 1

        revenue = float(line[1])

        #add to sum of revenue for data set
        total_revenue = round(total_revenue + revenue)

        #find change in revenue between this month and last month
        revenue_change = revenue - previous_revenue

        #add change in revenue to net change in revenue for data set
        total_revenue_change = total_revenue_change + revenue_change

        #determine if change in revenue is a max or min for data set thus far
        if revenue_change > max_revenue:
            max_month = line[0]
            max_revenue = revenue_change

        if revenue_change < min_revenue:
            min_month = line[0]
            min_revenue = revenue_change

        #set previous revenue to revenue
        previous_revenue = revenue

    #averages
    average_revenue = total_revenue/count_months
    average_revenue_change = round(total_revenue_change/(count_months-1),2)
    
    #print to terminal
    print(f"Financial Analysis:")
    print("-------------------------------------------------------")
    print(f"Total Months: {count_months}")
    print(f"Net Total Profit or Loss: ${total_revenue}")
    print(f"Average Change: ${average_revenue_change}")
    print(f"Greatest Increase in Profits: {max_month} ${round(max_revenue)}")
    print(f"Greatest Decrease in Profits: {min_month} ${round(min_revenue)}")
    print("")
    
    #print analysis to file

    with open('PyBank.txt', 'w') as text_file:
        print(f"Financial Analysis:\n")
        print("-------------------------------------------------------\n")
        print(f"Total Months: {count_months}\n")
        print(f"Net Total Profit or Loss: ${total_revenue}\n")
        print(f"Average Change: ${average_revenue_change}\n")
        print(f"Greatest Increase in Profits: {max_month} ${round(max_revenue)}\n")
        print(f"Greatest Decrease in Profits: {min_month} ${round(min_revenue)}\n")
        print("")