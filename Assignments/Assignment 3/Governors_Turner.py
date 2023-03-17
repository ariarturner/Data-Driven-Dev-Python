'''
Created on Mar 13, 2021
@author: Aria Turner
Title: Assignment 3
Description: output governor election results
'''
import csv

def processDataFiles():
    fileName = 'governors_county_candidate.csv'
    with open(fileName) as f:
        reader = csv.reader(f)
        allStatesList = list(reader)
    f.close()

    fileName = 'governors_county_total.csv'
    with open(fileName) as f:
        reader = csv.reader(f)
        totalVoteCountyList = list(reader)
    f.close()

    fileName = 'governors_state_total.csv'
    with open(fileName) as f:
        reader = csv.reader(f)
        totalVoteStateList =list(reader)
    f.close()
    return allStatesList, totalVoteCountyList, totalVoteStateList

'''
The required methods are:
whichState()
whichCounty()
overallStateResults()
overallCountyResults()
'''

def whichState(allStatesList, totalVoteStateList):
    #sentinal value
    valid = False
    #input state until valid state is entered
    while valid == False:
        state = input("\nEnter State Name for Governor Election Results: ").title()
        #create a list with data for selected state
        stateList = []
        #cycle through all data
        for i in range(len(allStatesList)):
            #skip lists that are not for selected state
            if state != allStatesList[i][0]:
                continue
            else:
                #if find state in list, then mark entry as valid
                valid = True
                #add this list to the state list
                stateList.append(allStatesList[i])
        #get total votes for state
        for j in range(len(totalVoteStateList)):
            #if state matches in state totals list
            if totalVoteStateList[j][0] == state:
                stateVotes = eval(totalVoteStateList[j][1])
        #if valid isn't set to True in loop, print error message
        if valid == False:
            print(f"{state} is not a valid state")
    return state.upper(), stateList, stateVotes



def whichCounty(allStatesList, totalVoteStateList, totalVoteCountyList):
    #get selected state and state info
    state, stateList, stateVotes = whichState(allStatesList, totalVoteStateList)
    #set sentinel value for county
    valid = False
    #ask for county until valid county is entered
    while valid == False:
        county = input("Enter County Name for Governor Election Results: ").title()
        #create county list that holds all the data for the selected county
        countyList = []
        #cycle through all state data
        for i in range(len(stateList)):
            #skip lists that are not for selected county
            if county != stateList[i][1]:
                continue
            else:
                #if county is found in list, mark entry as valid
                valid = True
                #add this list to the county list
                countyList.append(stateList[i])
        #get total votes for county
        for j in range(len(totalVoteCountyList)):
            #if county name matches in county totals list
            if totalVoteCountyList[j][1] == county:
                countyVotes = eval(totalVoteCountyList[j][2])
        #if entry not found in for loop, print error message
        if valid == False:
            print(f"{county} is not a valid county in the state of {state}")
    return state.upper(), stateList, county.upper(), countyList, countyVotes



def countiesWonCount(candidateList):
    #set sentinel value
    countiesWon = 0
    for i in range(len(candidateList)):
        #for each True (represents won county), add one
        if candidateList[i][5] == "TRUE":
            countiesWon += 1
        else:
            continue
    return countiesWon



def overallStateResults(allStatesList, totalVoteStateList):
    #get state
    state, stateList, stateVotes = whichState(allStatesList, totalVoteStateList)
    #create list of candidates for each party
    repCandidateList = []
    demCandidateList = []
    #go through state list
    for i in range(len(stateList)):
        #if republican, then add to republican list
        if stateList[i][3] == "REP":
            repCandidateList.append(stateList[i])
        #if democrat, the add to democrat list
        elif stateList[i][3] == "DEM":
            demCandidateList.append(stateList[i])
        #otherwise move to next item
        else:
            continue
    #sum votes in rep list
    repTotalVotes = sum([eval(row[4]) for row in repCandidateList])
    #sum votes in dem list
    demTotalVotes = sum([eval(row[4]) for row in demCandidateList])
    #count counties won by rep
    repCountiesWon = countiesWonCount(repCandidateList)
    #count counties won by dem
    demCountiesWon = countiesWonCount(demCandidateList)
    #percent won by rep
    repPerWon = repTotalVotes / stateVotes
    #percent won by dem
    demPerWon = demTotalVotes / stateVotes
    #print results
    print(f"\nResults for Governor Race in the State of {state}")
    print("=" * 93)
    if repTotalVotes > demTotalVotes:
        print(f"Total Votes for: {repCandidateList[0][2]:>17s}{'Republican is':>15s}{repTotalVotes:>11,}\t{repPerWon:.2%}\tCounties Won: {repCountiesWon:>3} (Won)")
        print(f"Total Votes for: {demCandidateList[0][2]:>17s}{'Democrat is':>15s}{demTotalVotes:>11,}\t{demPerWon:.2%}\tCounties Won: {demCountiesWon:>3}")
    elif repTotalVotes < demTotalVotes:
        print(f"Total Votes for: {repCandidateList[0][2]:>17s}{'Republican is':>15s}{repTotalVotes:>11,}\t{repPerWon:.2%}\tCounties Won: {repCountiesWon:>3}")
        print(f"Total Votes for: {demCandidateList[0][2]:>17s}{'Democrat is':>15s}{demTotalVotes:>11,}\t{demPerWon:.2%}\tCounties Won: {demCountiesWon:>3} (Won)")



def overallCountyResults(allStatesList, totalVoteStateList, totalVoteCountyList):
    #get county
    state, stateList, county, countyList, countyVotes = whichCounty(allStatesList, totalVoteStateList, totalVoteCountyList)
    #create list of candidates for each party
    repCountyCandidateList = []
    demCountyCandidateList = []
    #go through state list
    for i in range(len(countyList)):
        #if republican, then add to republican list
        if countyList[i][3] == "REP":
            repCountyCandidateList.append(countyList[i])
        #if democrat, the add to democrat list
        elif countyList[i][3] == "DEM":
            demCountyCandidateList.append(countyList[i])
        #otherwise move to next item
        else:
            continue
    #sum votes in rep list
    repCountyTotalVotes = sum([eval(row[4]) for row in repCountyCandidateList])
    #sum votes in dem list
    demCountyTotalVotes = sum([eval(row[4]) for row in demCountyCandidateList])
    #percent won by rep
    repCountyPerWon = repCountyTotalVotes / countyVotes
    #percent won by dem
    demCountyPerWon = demCountyTotalVotes / countyVotes
    #print results
    print(f"\nResults for Governor Race in the County of {county} in {state}")
    print("=" * 93)
    if repCountyTotalVotes > demCountyTotalVotes:
        print(f"Total Votes for: {repCountyCandidateList[0][2]:>17s}{'Republican is':>15s}{repCountyTotalVotes:>11,}\t{repCountyPerWon:.2%}\t(Won)")
        print(f"Total Votes for: {demCountyCandidateList[0][2]:>17s}{'Democrat is':>15s}{demCountyTotalVotes:>11,}\t{demCountyPerWon:.2%}")
    elif repCountyTotalVotes < demCountyTotalVotes:
        print(f"Total Votes for: {repCountyCandidateList[0][2]:>17s}{'Republican is':>15s}{repCountyTotalVotes:>11,}\t{repCountyPerWon:.2%}")
        print(f"Total Votes for: {demCountyCandidateList[0][2]:>17s}{'Democrat is':>15s}{demCountyTotalVotes:>11,}\t{demCountyPerWon:.2%} (Won)")



def mainMenu():
    print()
    print('+' * 40)
    print('\t(S)tate Governor Results') 
    print('\t(C)ounty Governor Results')
    print('\t(T)erminate Program')  
    print('+' * 40)
    selection = input('Make Selection: ') 
    return selection

            
def main():
    again = True
    
    pdAllStatesList, pdTotalVoteCountyList, pdTotalVoteStateList = processDataFiles()
    
    while again:
        mmSelection = mainMenu()
        '''
        The rest of your main method code
        goes below here
        '''
        
        if mmSelection == 'S' or mmSelection == 's':
            overallStateResults(pdAllStatesList, pdTotalVoteStateList)

        if mmSelection == 'C' or mmSelection == 'c':
            overallCountyResults(pdAllStatesList, pdTotalVoteStateList, pdTotalVoteCountyList) 
        
        '''
        The rest of your main method code
        goes above here
        '''
        if mmSelection =='T' or mmSelection == 't':
            print('Terminating program...')
            exit()
    
main()