#import the necessary dependecies for os.path.join()
import os
import csv

#read in csv file
csvpath = os.path.join('..' ,'PyPoll' , 'Resources' , 'election_data.csv')
#print(csvpath)

#setting initial value of the counter to zero
totalvotes = 0

#Create a dictionary
candidates = {}

#print name of document 
print("Election Results")
print("------------------------")

#Reading of CSV file
with open(csvpath) as csvfile:
        #csv reader specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

 #iterate through the whole file
    for row in csvreader:
        totalvotes += 1
        can = row[2]
        if can in candidates.keys():
            candidates[can] +=1
        else:
            candidates[can] = 1

    #printing the result
    print(f'Total Votes: {totalvotes:,}')
print("------------------------")
# \n for a new line character

winner = ""
maxvote = 0
for key,value in candidates.items():
    percent = value / totalvotes
    print(f'{key}: {percent:.3%} ({value:,})')
    if value > maxvote:
        maxvote = value
        winner = key

#writing to txt
with open("output.txt", "w") as output:
    print("Election Results", file=output)
    print("------------------------", file=output)
    print(f'Total Votes: {totalvotes:,}', file=output)
    print("------------------------", file=output)
    for key,value in candidates.items():
        percent = value / totalvotes
        print(f'{key}: {percent:.3%} ({value:,})', file=output)
        if value > maxvote:
            maxvote = value
            winner = key
    print("------------------------", file= output)
    print(f'Winner : {winner}', file=output)
    print("------------------------", file=output)



print("------------------------")
print(f'Winner : {winner}')
print("------------------------")