#define variables
months = []
pl_changes = []
month_count = 0
profit_loss = 0
previous_month_pl = 0 
current_month_pl = 0 
pl_change = 0

#import dependencies
import os 
import csv

#link to csv file
pybankcsv = os.path.join("Resources", "budget_data.csv")

#read csv file
with open(pybankcsv) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

    #read the header row first 
    csv_header = next(csvfile)
    
    #print("csv_header")
        #this prints Header: Date,Profit/Losses

    #read through each row of data after the header 
    for row in csv_reader: 
        
        #total number of months included in the dataset
        month_count += 1

        #total amount of Profit/Losses over the entire period
            #row count starts at 0 so the row we are summing is 1
        current_month_pl = int(row[1])
        profit_loss += current_month_pl

    #if/else statement to read through months 
        if (month_count == 1):
            previous_month_pl = current_month_pl
            continue
        else:
            #compute profit loss changes 
            pl_change = current_month_pl - previous_month_pl

            #add the additional month to months
            months.append(row[0])

            #add the profit loss change to profit loss changes
            pl_changes.append(pl_change)

            #make the current month loss to the previous month loss for the next loop 
            previous_month_pl = current_month_pl

    #find the sum and average of the changes in profits and losses over the period
    sum_pl = sum(pl_changes)
    average_pls = round(sum_pl/(month_count -1), 2)
        #test to see if calculations are working 
            #print(average_profit_loss)
    
    #calculate/assign the highest/lowest changes
    highest_change = max(pl_changes)
    lowest_change = min(pl_changes)

    #find/assign the months of the highest and lowest changes
    high_month = pl_changes.index(highest_change)
    low_month = pl_changes.index(lowest_change)

    #designate as worst/best month 
    best = months[high_month]
    worst = months[low_month]

#print results in the terminal
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_pls}")
print(f"Greatest Increase in Profits:  {best} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst} (${lowest_change})")

#export resutls in a text file 
summary_file = os.path.join("Output", "PyBank_Summary.txt")
with open(summary_file, "w") as outfile: 
    outfile.write("Financial Analysis\n")
    outfile.write("--------------------\n")
    outfile.write(f"Total Months: {month_count}\n")
    outfile.write(f"Total: ${profit_loss}\n")
    outfile.write(f"Average Change: ${average_pls}\n")
    outfile.write(f"Greatest Increase in Profits:  {best} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst} (${lowest_change})\n")

