#bankscript
#import the necessary dependecies for os.path.join()
import os
import csv

#read in csv file
csvpath = os.path.join('..' ,'PyBank' , 'Resources' , 'budget_data.csv')

#print name of document
print("Financial Analysis")
print("------------------------")
#setting initial value of the counter to zero
total = 0
rowcount = 0
#create lists
change_from_previous =  []
months = []
#Reading of CSV file
with open(csvpath) as csvfile:
        #csv reader specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    previous_revenue= 0

    #iterate through the whole file
    for row in csvreader:
        rowcount += 1
        total += int(row[1])
        change_from_previous.append(int(row[1])-previous_revenue)
        months.append(row[0])
        previous_revenue = int(row[1])

    #printing the result
    print(f'Total Months: {rowcount}')
    print(f'Total: ${total:,}')
    #print(change_from_previous)
    print(f'Average Change: ${sum(change_from_previous[1:])/(len(change_from_previous)-1):,.2f}')
    maxvalue= max(change_from_previous)
    minvalue= min(change_from_previous)
    print (f'Greatest Increase in Profits: {months[change_from_previous.index(maxvalue)]} (${maxvalue:,})')
    print (f'Greatest Decrease in Profits: {months[change_from_previous.index(minvalue)]} (${minvalue:,})')
#print to txt file
with open("output.txt", "w") as output:
    print("Financial Analysis", file=output)
    print("------------------------", file=output)
    print(f'Total Months: {rowcount}', file=output)
    print(f'Total: ${total:,}', file=output)
    print(f'Average Change: ${sum(change_from_previous[1:])/(len(change_from_previous)-1):,.2f}', file=output)
    print (f'Greatest Increase in Profits: {months[change_from_previous.index(maxvalue)]} (${maxvalue:,})', file=output)
    print (f'Greatest Decrease in Profits: {months[change_from_previous.index(minvalue)]} (${minvalue:,})', file=output)