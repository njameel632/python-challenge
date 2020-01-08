# importing the necessary libraries and modules

import os
import csv

# creating an object and setting path to the file

budget_data = os.path.join("budget_data.csv")

total_months = 0
total_revenue = 0
current_reveue = 0
change_revenue = 0
dates = []
profits = []

# Reading csv file

with open (budget_data, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

# Reading the header row

    csv_header = next(csvreader)

# Readeing the first row

    first_row = next(csvreader)
    total_months += 1
    total_revenue += int(first_row[1])
    current_revenue = int(first_row[1])

    # Setting up a for loop to loop through all the rows

    for row in csvreader:

        dates.append(row[0])

        # Calculating the change in profit and loss month over month

        change = int(row[1])-current_revenue
        profits.append(change)
        current_revenue = int(row[1])
        total_months += 1

        # Total revenue over the entire period

        total_revenue = total_revenue + int(row[1])


    # Calculating the greatest increase in profit and the month which had the greatest profit

    greatest_profit = max(profits)
    greatest_index = profits.index(greatest_profit)
    greatest_date = dates[greatest_index]

    # Greatest Decrease in profits and the corresponding the month

    greatest_loss = min(profits)
    lowest_index = profits.index(greatest_loss)
    lowest_date = dates[lowest_index]

    # Average revenue over the entire period

    average_revenue = sum(profits)/len(profits)


print("Finalcial Analysis")
print("------------------------------")
print(f"Total Months : {str(total_months)}")
print(f"Total Revenue : {str(total_revenue)}")
print(f"Average Change :${str(round(average_revenue,2))}")
print(f"Greatest Increase in Profits : {greatest_date} (${str(greatest_profit)})")
print(f"Greatest Decrease in Profits : {lowest_date} (${str(greatest_loss)})")


#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_revenue)}")
line5 = str(f"Average Change: ${str(round(average_revenue,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_profit)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_loss)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))