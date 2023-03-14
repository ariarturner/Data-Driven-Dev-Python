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
This section of code reads in the two csv files that contain the main presidential data. When the data is read only the 
columns of data used is state, county, candidate, party, and total_votes from president_county_candidate.csv (dfpres1)
and state, county and total_votes from president_county.csv (dfpres2).
'''
def createPresidentialDFs():
    dfPres1 = pd.read_csv('president_county_candidate.csv', usecols=['state', 'county', 'candidate', 'party', 'total_votes'])
    dfPres2 = pd.read_csv('president_county.csv', usecols=['state', 'county', 'total_votes'])  
    #print(dfPres1)  # Remove this line when your code is complete and working
    #print(dfPres2)  # Remove this line when your code is complete and working
    return dfPres1, dfPres2

'''
Read in the data from the Electoral_votes.csv file and creates a dictionary called eVotes. This can be used in your 
program code.
'''
def createElectoralDict():
    eVotes = {}
    with open('Electoral_votes.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for data in reader:
            key, value = data
            eVotes[key] = int(value)
    #print(eVotes)  # Remove this line when your code is complete and working
    return eVotes

'''
Creates a set that contains all the valid state names that will be used to validate the users state input. This set 
can also be used for other purposes in your code
'''    
def createValidStates(dfPres1):
    validStates = set()
    for state in dfPres1['state']:
        validStates.add(state)
    #print(validStates)  # Remove this line when your code is complete and working
    return validStates

'''
Prompt the user for a valid state name and check to see if it is valid. If not valid prompt the user to enter the 
state name until it is valid.
'''
def validateState(validStates):
    #set sentinel value
    validity = False
    while validity == False:
        #prompt for state
        stateChoice = input('Enter a state name: ').title()
        #check if input state is in state set
        if stateChoice in validStates:
            return stateChoice
            validity = True
        else:
            #if state is not in state set, then return error message and restart loop to ask for valid state
            print("Invalid state, enter a valid state.")


'''
Place the rest of your code below to accomplish the requirements of project assignment 5.
'''
            
'''
create a smaller data frame that only includes counts for Republican and Democratic candidates
'''
def limitDF(dfPres1):
    #DataFrame that contains just democrats
    newdfPres1 = dfPres1[dfPres1["party"] == "DEM"]
    #DataFrame that contains just republicans
    newdfPres2 = dfPres1[dfPres1["party"] == "REP"]
    #stack (append) democrat and republican DataFrames
    newdfPres = newdfPres1.append(newdfPres2)
    return newdfPres

'''
calculate the state vote counts
'''
def stateCandidateSum(state, newdfPres):
    #for input state, group DataFrame by candidate and sum total_votes; convert to DataFrame so data can be accessed
    stateSums = pd.DataFrame(newdfPres[newdfPres["state"] == state].groupby(by = "candidate").sum())
    #assign counts to easy-to-call variables
    stateTrumpVotes = stateSums["total_votes"][0]
    stateBidenVotes = stateSums["total_votes"][1]
    return stateTrumpVotes, stateBidenVotes

'''
calculate the percent of state won
'''
def stateCanPer(state, dfPres2, stateTrumpVotes, stateBidenVotes):
    #group DataFrame by state and take sum of total_votes; assign results for input state as new DataFrame
    stateTotals = pd.DataFrame(dfPres2[dfPres2["state"] == state].groupby(by = "state").sum())
    #calculate percent of state won for each candidate and assign to easy-to-call variables
    stateTrumpPer = stateTrumpVotes/stateTotals["total_votes"][0]
    stateBidenPer = stateBidenVotes/stateTotals["total_votes"][0]
    return stateTrumpPer, stateBidenPer
    
'''
calculate all the popular vote related items
'''
def popularVotes(newdfPres, dfPres2):
    #group by candidate to sum total_votes for each candidate; assign to DataFrame
    candidateSums = pd.DataFrame(newdfPres.groupby(by = "candidate").sum())
    #assign values to easy-to-call variables
    trumpVotes = candidateSums['total_votes'][0]
    bidenVotes = candidateSums['total_votes'][1]
    #calculate sum of total_votes
    totalVotes = dfPres2["total_votes"].sum()
    #calculate percent won of popular vote for both candidates
    trumpPer = trumpVotes / totalVotes
    bidenPer = bidenVotes / totalVotes
    return trumpVotes, bidenVotes, trumpPer, bidenPer


def main():
    #read in data and assign to variables
    dfPres1, dfPres2 = createPresidentialDFs()
    #create dictionary with  electoral votes for each state
    eVotes = createElectoralDict()
    #create set with valid states
    validStates = createValidStates(dfPres1)
    #request and validate state
    state = validateState(validStates)
    
    #create a new DataFrame with only relevant candidates
    newdfPres = limitDF(dfPres1)
    
    #calculate candidate votes in state
    stateTrumpVotes, stateBidenVotes = stateCandidateSum(state, newdfPres)
    #calculate candidate percent won in state
    stateTrumpPer, stateBidenPer = stateCanPer(state, dfPres2, stateTrumpVotes, stateBidenVotes)
    
    #calculate candidates' total popular votes and total percent won
    trumpVotes, bidenVotes, trumpPer, bidenPer = popularVotes(newdfPres, dfPres2)

    
    '''
    print out and format all results
    '''
    print(f"\nState Presidential Votes for the state of {state.upper()}")
    print('=' * 71)
    #print winner first
    if stateTrumpVotes > stateBidenVotes:
        print(f"Donald Trump\t{stateTrumpVotes:>15,}\t{stateTrumpPer:11.2%}  (Won) Electoral Votes: {eVotes.get(state)}")
        print(f"Joe Biden\t{stateBidenVotes:>15,}\t{stateBidenPer:11.2%}")
    else:
        print(f"Joe Biden\t{stateBidenVotes:>15,}\t{stateBidenPer:11.2%}  (Won) Electoral Votes: {eVotes.get(state)}")
        print(f"Donald Trump\t{stateTrumpVotes:>15,}\t{stateTrumpPer:11.2%}")
    print('*' * 71)
    print(f"Vote Difference: {abs(stateTrumpVotes - stateBidenVotes):,}\tPercentage Difference: {abs(stateTrumpPer - stateBidenPer):.2%}")
    print('*' * 71)
    print("\nUS Presidential Popular Votes")
    print('=' * 71)
    print(f"Joe Biden\t{bidenVotes:>15,}\t{bidenPer:11.2%}  (Won)")
    print(f"Donald Trump\t{trumpVotes:>15,}\t{trumpPer:11.2%}")
    print('*' * 71)
    print(f"Vote Difference: {abs(trumpVotes - bidenVotes):,}\tPercentage Difference: {abs(trumpPer - bidenPer):.2%}")
    print('*' * 71)

main()