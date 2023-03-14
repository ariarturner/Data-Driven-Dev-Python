'''
Created on 4/5/2021
@author: Aria Turner
'''
import pandas as pd
import csv

# pd.describe_option('display')
# Ensure the data frames completely when they are printed
pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.width', 1000)  # or 199
    
'''
This section of code reads in the two csv files that contain the main presidential data. When the data is read only
the columns of data used is state, county, candidate, party, and total_votes from president_county_candidate.csv (dfpres1)
and state, county and total_votes from president_county.csv (dfpres2).
'''
dfPres1 = pd.read_csv('president_county_candidate.csv', usecols=['state', 'county', 'candidate', 'party', 'total_votes'])
dfPres2 = pd.read_csv('president_county.csv', usecols=['state', 'county', 'total_votes'])  
print(dfPres1)  # Remove this line when your code is complete and working
print(dfPres2)  # Remove this line when your code is complete and working

'''
Read in the data from the Electoral_votes.csv 
file and creates a dictionary called eVotes.
This can be used in your program code.
'''
eVotes = {}
with open('Electoral_votes.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for data in reader:
        key, value = data
        eVotes[key] = int(value)
print(eVotes)  # Remove this line when your code is complete and working

'''
Creates a set that contains all the valid state names
that will be used to validate the users state input.
This set can also be used for other purposes in your code
'''    
validStates = set()
for state in dfPres1['state']:
    validStates.add(state)
print(validStates)  # Remove this line when your code is complete and working

'''
Prompt the user for a valid state name and check to see if it
is valid. If not valid prompt the user to enter the state name
until it is valid.
'''
validity = False
while validity == False:
    stateChoice = input('Enter a state name: ').title()
    if stateChoice in validStates:
        return stateChoice
        validity = True
        break
    else:
        print("Invalid state, enter a valid state.")

'''
Place the rest of your code below to accomplish the requirements
of project assignment 5.
'''
        
#create new dataframe that only contains Dem and Rep candidates
newdfPres1 = dfPres1[dfPres1["party"] == "DEM"]
newdfPres2 = dfPres1[dfPres1["party"] == "REP"]
newdfPres = newdfPres1.append(newdfPres2)


dfGrouped = newdfPres.groupby(by = ["state", "candidate"])



dfCanSum = dfGrouped.sum()
dfCanSum = dfCanSum[dfCanSum["state" == state]]

