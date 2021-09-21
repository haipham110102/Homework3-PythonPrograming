
import os
import csv

# Lists to result name
month_year_list = []
revenue_list = []
total_revenue = 0
total_revenue_change = 0

min_revenue_change =[' ', 0] 
max_revenue_change =[' ', 0]


csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"csv Header: {csv_header}")

    for row in csvreader:
        month_year = row[0]
        revenue = float(row[1])
        month_year_list.append(month_year)
        revenue_list.append(revenue)
        total_revenue = total_revenue + revenue
    #print(total_revenue)
    #print(month_year_list)

    #Calculate the revenue change for each month and compare to excel calculation to verify data
    total_month = len(month_year_list)
    
    #print(total_month)
    
    for x in range(1, len(month_year_list)):
        revenue_change = revenue_list[x] - revenue_list[x-1]
        #print(revenue_change)
        total_revenue_change += revenue_change
        #print(total_revenue_change)
        if revenue_change > max_revenue_change[1]:
            max_revenue_change = [month_year_list[x], revenue_change]
        elif revenue_change < min_revenue_change[1]:
              min_revenue_change = [month_year_list[x], revenue_change]

    average_change = total_revenue_change / (total_month-1)
    #print("${:.2f}".format(average_change))
    #print(min_revenue_change[0] + " (" + "${:.0f}".format(min_revenue_change[1]) +")")
    #print(max_revenue_change[0] + " ($" + str(round(max_revenue_change[1]))+ ")")

#put result in the list
rows = []
row1 = f"Financial Analysis"
rows.append(row1)
row2 = f"--------------------------"
rows.append(row2)
row3 = f"Total months: " + str(total_month)
rows.append(row3)
row4 = f"Average Change: " + "${:.2f}".format(average_change)
rows.append(row4)
row5 = f"Greatest Increase in Profits: " + max_revenue_change[0] + " ($" + str(round(max_revenue_change[1]))+")"
rows.append(row5)
row6 = f"Greatest Decrease in Profits: " + min_revenue_change[0] + " ($" + str(round(min_revenue_change[1]))+")"
rows.append(row6)

#for loop to test result
for row in rows:
    print(row)


# set variable for output  file
output_file = os.path.join("analysis", "budget_result")

#open and write to the output file
with open(output_file, "w") as datafile:
     for row in rows:
         datafile.write(f"{row}\n\n")
         
