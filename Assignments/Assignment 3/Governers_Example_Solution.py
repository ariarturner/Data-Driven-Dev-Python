'''
Created on Feb 7, 2021
@author: ruded
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

def whichState(allStatesList, totalVoteCountyList, totalVoteStateList):
    validState = False
    
    validStates = [] 
    for stateItem in totalVoteStateList:
        if stateItem[0] == 'state':
            continue
        if stateItem[0] not in validStates:
            validStates.append(stateItem[0])
    
    while not validState:
        state = input('\nEnter State Name for Governor Election Results: ').title()
        if state  not in validStates:
            print('Invalid state selection, try again!')
        else:
            validState = True
    #state = 'Washington'
    stateAllCounty = [item for item in allStatesList if item[0] == state and (item[3] == "DEM" or item[3] == 'REP')]
    stateCountyList = []
    for item in totalVoteStateList:
        if item[0] == state:
            stateCountyList.append(item[0])
            stateCountyList.append(item[1])
            stateCountyList.append(item[2])
            
    return stateAllCounty, stateCountyList, state

def whichCounty(allStatesList, totalVoteCountyList, totalVoteStateList):
    validState = False
    validCounty = False
    
    validStates = [] 
    for stateItem in totalVoteStateList:
        if stateItem[0] not in validStates:
            validStates.append(stateItem[0])
    
    while not validState:
        state = input('\nEnter State Name for Governor Election Results: ').title()
        if state  not in validStates:
            print('Invalid state selection, try again!')
        else:
            validState = True
            
    validCounties = [] 
    for countyItem in totalVoteCountyList:
        if countyItem[0] == state and countyItem[1] not in validCounties:
            validCounties.append(countyItem[1]) 
           
    while not validCounty:
        county = input('Enter County Name for Governor Election Results: ').title()
        if county not in validCounties:
            print('Invalid county selection, try again!')
        else:
            validCounty = True 
               
    stateAllCounty = [item for item in allStatesList if item[0] == state and item[1] == county and (item[3] == "DEM" or item[3] == 'REP')]
    
    stateCountyList = []
    for item in totalVoteCountyList:
        if item[0] == state and item[1] == county:
            stateCountyList.append(item[0])
            stateCountyList.append(item[1])
            stateCountyList.append(item[2])
    return stateAllCounty, stateCountyList, state, county

def overallStateResults(totalVoteStateList, stateAllCounty, state):
    stateTotalVotes = eval(totalVoteStateList[1])
    dTotalVotes = 0
    rTotalVotes = 0
    dCandidate =''
    rCandidate =''
    dFound = False
    rFound = False
    dCountyVote = 0
    rCountyVote = 0
    dCountyCount = 0
    rCountyCount = 0

    for items in stateAllCounty: 
        if items[3] == 'DEM':
            dCandidate = items[2]
            dCountyVote = (int)(items[4])
            dTotalVotes += dCountyVote
            dFound = True
        elif items[3] == 'REP':
            rCandidate = items[2]
            rCountyVote = (int)(items[4])
            rTotalVotes += rCountyVote
            rFound = True
        if dFound and rFound:
            if dCountyVote > rCountyVote:
                dCountyCount += 1
            else:
                rCountyCount += 1
            dFound = False
            rFound = False
            
    print(f'\nResults for Governor Race in the State of {state.upper()}')  
    print('=' * 92)      
    if dTotalVotes > rTotalVotes:
        print(f'Total Votes for:{dCandidate:>18} {"Democrat":>11} is {dTotalVotes:>10,}   {(dTotalVotes/stateTotalVotes)*100:5.2f}%  Counties Won:{dCountyCount:>4} (Won)')
        print(f'Total Votes for:{rCandidate:>18} {"Republican":>11} is {rTotalVotes:>10,}   {(rTotalVotes/stateTotalVotes)*100:5.2f}%  Counties Won:{rCountyCount:>4}')
    else:
        print(f'Total Votes for:{rCandidate:>18} {"Republican":>11} is {rTotalVotes:>10,}   {(rTotalVotes/stateTotalVotes)*100:5.2f}%  Counties Won:{rCountyCount:>4} (Won)')
        print(f'Total Votes for:{dCandidate:>18} {"Democrat":>11} is {dTotalVotes:>10,}   {(dTotalVotes/stateTotalVotes)*100:5.2f}%  Counties Won:{dCountyCount:>4}')

def overallCountyResults(totalVoteCountyList, stateAllCounty, state, county):
    countyTotalVotes = 0
    countyTotalVotes = eval(stateAllCounty[2])
        
    dCandidate =''
    rCandidate =''
    dCountyVote = 0
    rCountyVote = 0

    for items in totalVoteCountyList:        
        if items[3] == 'DEM':
            county = items[1]
            dCandidate = items[2]
            dCountyVote = (int)(items[4])
   
        if items[3] == 'REP':
            county = items[1]
            rCandidate = items[2]
            rCountyVote = (int)(items[4])
    
    print(f'\nResults for Governor Race in the County of {county.upper()} in {state.upper()}')  
    print('=' * 92)      
    if dCountyVote > rCountyVote:
        print(f'Total Votes for:{dCandidate:>18} {"Democrat":>11} is {dCountyVote:>10,}   {(dCountyVote/countyTotalVotes)*100:5.2f}%  (Won)')
        print(f'Total Votes for:{rCandidate:>18} {"Republican":>11} is {rCountyVote:>10,}   {(rCountyVote/countyTotalVotes)*100:5.2f}%')
    else:
        print(f'Total Votes for:{rCandidate:>18} {"Republican":>11} is {rCountyVote:>10,}   {(rCountyVote/countyTotalVotes)*100:5.2f}%  (Won)')
        print(f'Total Votes for:{dCandidate:>18} {"Democrat":>11} is {dCountyVote:>10,}   {(dCountyVote/countyTotalVotes)*100:5.2f}%')
    
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
        if mmSelection != 'S' and mmSelection != 's' and mmSelection != 'C' and mmSelection != 'c' and mmSelection != 'T' and mmSelection != 't':
            print('Invalid selection, try again!')
            mmSelection = mainMenu
        if mmSelection == 'S' or mmSelection == 's':
            wsStateCountyList, wsStateAllCounty, wsState = whichState(pdAllStatesList, pdTotalVoteCountyList, pdTotalVoteStateList)
            overallStateResults(wsStateAllCounty, wsStateCountyList, wsState)
        elif mmSelection == 'C' or mmSelection == 'c':
            wcStateAllCounty, wcStateCountyList, wcState, wcCounty = whichCounty(pdAllStatesList, pdTotalVoteCountyList, pdTotalVoteStateList)
            overallCountyResults(wcStateAllCounty, wcStateCountyList, wcState, wcCounty)
        elif mmSelection =='T' or mmSelection == 't':
            print('Terminating program...')
            exit()
    
main()