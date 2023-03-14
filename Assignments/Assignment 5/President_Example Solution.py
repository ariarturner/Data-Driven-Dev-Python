'''
Created on March 29, 2021
@author: ruded
'''
import pandas as pd
import csv
from colorama import Fore

# pd.describe_option('display')
# Ensure the data frames completely when they are printed
pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.width', 2000)  # or 199

  
def prepareData(): 
    '''
    This section of code reads in the two csv files that contain the main presidential data. When the data is read only
    use the columns of data used is state, county, candidate, part, and total_votes from president_county_candidate.csv (dfpres1)
    and state, county and total_votes from president_county.csv (dfpres2). The total_votes column in the president_county.csv is renamed
    to total_votes_county before executing the pandas merge method.
    '''
    dfpres1 = pd.read_csv('president_county_candidate.csv', usecols=['state', 'county', 'candidate', 'party', 'total_votes'])
    dfpres2 = pd.read_csv('president_county.csv', usecols=['state', 'county', 'total_votes'])  
    dfpres2.rename(columns={'total_votes':'total_votes_county'}, inplace=True)
    votes = electoralVotes()
    return dfpres1, dfpres2, votes
    
    
def filterData(dfpres1, dfpres2):
    '''
    The next section of code creates a new dataframe called dfpres4 from the dfpres1 dataframe to filter down just
    candidate and party data. The dfDem and dfRep are used to get the names of the democratic candidate and the 
    republican candidate (demCandidate and repCandidate).
    '''
    dfpres4 = dfpres1[['candidate', 'party']]
    dfCandParty = dfpres4[:2]
    demCandidate = dfCandParty.loc[0]['candidate']
    repCandidate = dfCandParty.loc[1]['candidate']
    
    '''
    Merge dfpres1 and dfpres2 using an inner join, join columns are state and county
    Produce a new Dataframe called dfpres3. This will be the main dataframe to extract
    data from in later code.
    '''
    dfpres3 = dfpres1.merge(dfpres2, how='inner', on=['state', 'county'])
    dfpres16 = dfpres1.merge(dfpres2, how='inner', on=['state', 'county'])
    return dfpres3, dfpres16, demCandidate, repCandidate

    
def electoralVotes():
    '''
    Read in the data from the Electoral_votes.csv 
    file and create a dictionary called votes.
    '''
    votes = {}
    with open('Electoral_votes.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for data in reader:
            key, value = data
            votes[key] = int(value)
    return votes

     
def getStates(dfpres3): 
    '''
    Create a set that contains all the valid state names
    that will be used to validate the users state input.
    '''    
    validState = set()
    for state in dfpres3['state']:
        validState.add(state)
    return validState

    
def filterDemRepCandidate(dfpres3, demCandidate, repCandidate, stateChoice):
    '''
    This section creates a dataframe that only contains the data
    for democratic and republican candidates, it is called dfpres6 or dfpres7
    depending on which code is used below.
    Two code options to select only the candidates Joe Biden and Donald Trump
    for US vote counts, and state vote counts.
    '''
    # This code creates a Dataframe dfpres6, gets the data for both candidates, 
    # used to extract total US data to calculate US vote counts
    options = [demCandidate, repCandidate]
    dfpres6 = dfpres3[dfpres3['candidate'].isin(options)]
    
    # This code creates a Dataframe dfpres7, gets the data for both candidates, 
    # used to extract total state data to calculate state vote counts
    dfpres7 = dfpres3[((dfpres3['candidate'] == demCandidate) | (dfpres3['candidate'] == repCandidate)) & (dfpres3['state'] == stateChoice)]
    dfpres17 = dfpres3[((dfpres3['candidate'] == demCandidate) | (dfpres3['candidate'] == repCandidate))]
    
    return dfpres6, dfpres7, dfpres17


def countElectoralVotesCandidate(dfpres17, votes):
    dfpres18 = dfpres17.groupby(['state', 'party'], as_index=False)[['total_votes']].sum()
    
    demEV = 0
    repEV = 0
    for i in range(0, len(dfpres18), 2):
        state1, party1, votes1 = dfpres18.loc[i]
        state2, party2, votes2 = dfpres18.loc[i + 1]
        votes1 = (int)(votes1)
        votes2 = (int)(votes2)
        ev = votes.get(state1)
        if (party1 == 'DEM') and (votes1 > votes2):
            demEV += ev
        elif (party2 == 'REP') and (votes2 > votes1):
            repEV += ev
        else:
            demEV += ev
    return demEV, repEV


def determineUSData(dfpres6):
    '''
     This section of code creates dataframe dfpres5 by using the pandas groupby method
     on the candidate column and sums total_votes, and total_votes_county for total US
     numbers. It than adds a new column (Series) to the dataframe that contains the 
     percentage data. Then performs a sort on the dataframe to sort the total_votes 
     column in descending order.
    '''
    dfpres5 = dfpres6.groupby(['candidate'])[['total_votes', 'total_votes_county']].sum()
    dfpres5['vote_Percentage_US'] = (dfpres5['total_votes'] / dfpres5['total_votes_county']) * 100
    dfpres5.rename(columns={'total_votes_county':'total_votes_US'}, inplace=True)
    dfpres5.sort_values(by=['total_votes'], ascending=False, inplace=True)
    return dfpres5


def determineStateData(dfpres7):
    '''
     This section of code creates dataframe dfpres5 by using the pandas groupby method
     on the candidate column and sums total_votes, and total_votes_county for total state
     numbers. It than adds a new column (Series) to the dataframe that contains the 
     percentage data. Then performs a sort on the dataframe to sort the total_votes 
     column in descending order.
    '''
    dfpres9 = dfpres7.groupby(['candidate'])[['total_votes', 'total_votes_county']].sum()
    dfpres9['vote_Percentage_US'] = (dfpres9['total_votes'] / dfpres9['total_votes_county']) * 100
    dfpres9.rename(columns={'total_votes_county':'total_votes_State'}, inplace=True)
    dfpres9.sort_values(by=['total_votes'], ascending=False, inplace=True)
    return dfpres9


def extractUSVoteData(dfpres5, demCandidate, repCandidate): 
    '''
    Extract the data out of the dataframe dfpres5 for the
    US vote values to display in the final output.
    '''
    # test = dfpres5.index
    # demName = test[0]
    # repName = test[1]
    # print(demName)
    # print(repName)
    dVotesUS = (int)(dfpres5.loc[demCandidate]['total_votes'])
    rVotesUS = (int)(dfpres5.loc[repCandidate]['total_votes'])
    dVotesPercentUS = dfpres5.loc[demCandidate]['vote_Percentage_US']
    rVotesPercentUS = dfpres5.loc[repCandidate]['vote_Percentage_US']
    for index, row in dfpres5.iterrows():
        if index == demCandidate:
            dVotesUS = (int)(row['total_votes'])
            dVotesPercentUS = row['vote_Percentage_US']
        elif index == repCandidate:
            rVotesUS = (int)(row['total_votes'])
            rVotesPercentUS = row['vote_Percentage_US']
    return dVotesUS, rVotesUS, dVotesPercentUS, rVotesPercentUS

    
def extractStateVoteData(dfpres9, demCandidate, repCandidate):
    '''
    Extract the data out of the dataframe dfpres9 for the
    STATE vote values to display in the final output.
    '''
    # dVotesState = (int)(dfpres9.loc[demCandidate]['total_votes'])
    # rVotesState = (int)(dfpres9.loc[repCandidate]['total_votes'])
    # dVotesPercentState = dfpres9.loc[demCandidate]['vote_Percentage_US']
    # rVotesPercentState = dfpres9.loc[repCandidate]['vote_Percentage_US']
    for index, row in dfpres9.iterrows():
        if index == demCandidate:
            dVotesState = (int)(row['total_votes'])
            dVotesPercentState = row['vote_Percentage_US']
        elif index == repCandidate:
            rVotesState = (int)(row['total_votes'])
            rVotesPercentState = row['vote_Percentage_US']
    return dVotesState, rVotesState, dVotesPercentState, rVotesPercentState


def printUSResults(stateChoice, stateUpper, votes, demCandidate, repCandidate, dVotesUS, rVotesUS, dVotesPercentUS, rVotesPercentUS): 
    '''
    This section performs all the print formatting to display
    both the US Presidential Total vote output, and the State Presidential
    Total vote output.
    '''
    # State output heading
    if stateChoice != 'District Of Columbia':
        print()
        print(f'State Presidential Vote for the state of {stateUpper}.')
    else:
        print()
        print(f'Presidential Vote for the {stateUpper}.')
    print('=' * 76)
    print(f'{"Candidate":24}{"Votes":13}{"Percentage":8}')
    print('=' * 76)
    
    stateVoteDiff = 0  # used to hold the vote count different for state output
    if dVotesUS > rVotesUS:
        # Output for state, if candidate winner is democratic
        print(f'{demCandidate:15} {dVotesUS:15,} {dVotesPercentUS:10.2f}%        (Won) Electoral Votes: {votes[stateChoice]} ')
        print(f'{repCandidate:15} {rVotesUS:15,} {rVotesPercentUS:10.2f}%')
        USVoteDiff = dVotesUS - rVotesUS
        USPercentDiff = dVotesPercentUS - rVotesPercentUS
    else:
        # Output for state, if candidate winner is republican
        print(f'{repCandidate:15} {rVotesUS:15,} {rVotesPercentUS:10.2f}%        (Won) Electoral Votes: {votes[stateChoice]}')
        print(f'{demCandidate:15} {dVotesUS:15,} {dVotesPercentUS:10.2f}%')
        USVoteDiff = rVotesUS - dVotesUS
        USPercentDiff = rVotesPercentUS - dVotesPercentUS
       
    # Output of the state vote difference and state percentage difference 
    print('*' * 76)
    print(f'Vote Difference: {USVoteDiff:,}   Percentage Difference: {USPercentDiff:.2f}%')
    print('*' * 76)


def printStateResults(stateChoice, stateUpper, demCandidate, repCandidate, demEV, repEV, dVotesUS, rVotesUS, dVotesPercentUS, rVotesPercentUS): 
    # US output heading
    print()
    print('US Presidential Popular Vote and Electoral College Vote')
    print('=' * 76)
    print(f'{"Candidate":21}{"Votes":16}{"Percentage":16}{"Electoral Votes"}')
    print('=' * 76)
    
    USVoteDiff = 0  # used to hold the vote count different for US output
    if dVotesUS > rVotesUS:
        # Output for state, if candidate winner is democratic
        print(f'{demCandidate:15} {dVotesUS:15,} {dVotesPercentUS:10.2f}%          {demEV:>3} (Won)')
        print(f'{repCandidate:15} {rVotesUS:15,} {rVotesPercentUS:10.2f}%          {repEV:>3}')
        USVoteDiff = dVotesUS - rVotesUS
        USPercentDiff = dVotesPercentUS - rVotesPercentUS
    else:
        # Output for state, if candidate winner is republican
        print(f'{repCandidate:15} {rVotesUS:15,} {rVotesPercentUS:10.2f}%          {repEV:>3} (Won)')
        print(f'{demCandidate:15} {dVotesUS:15,} {dVotesPercentUS:10.2f}%          {demEV:>3}')
        USVoteDiff = rVotesUS - dVotesUS
        USPercentDiff = rVotesPercentUS - dVotesPercentUS
    
    # Output of the US vote difference and US percentage difference  
    print('*' * 76)
    print(f'Vote Difference: {USVoteDiff:,}   Percentage Difference: {USPercentDiff:.2f}%')
    print('*' * 76)

    
def swingStates(dfpres16, demCandidate, repCandidate, votes):
    dfpres16['vote_Percentage'] = (dfpres16['total_votes'] / dfpres16['total_votes_county']) * 100
    option1 = [demCandidate]
    option2 = [repCandidate]
    dfpres10 = dfpres16[dfpres16['candidate'].isin(option1)]
    dfpres11 = dfpres16[dfpres16['candidate'].isin(option2)]

    demPres12 = dfpres10.groupby(['state', 'candidate', 'party'], as_index=False)[['total_votes', 'total_votes_county']].sum()
    repPres13 = dfpres11.groupby(['state', 'candidate', 'party'], as_index=False)[['total_votes', 'total_votes_county']].sum()
    demPres12['Dem_Percentage'] = (demPres12['total_votes'] / demPres12['total_votes_county']) * 100
    repPres13['Rep_Percentage'] = (repPres13['total_votes'] / repPres13['total_votes_county']) * 100
    demPres12.sort_values(by=['state'], ascending=True, inplace=True)
    repPres13.sort_values(by=['state'], ascending=True, inplace=True)
    dfpres14 = demPres12.merge(repPres13, how='inner', on=['state'])

    dfpres14['percentDiff'] = (dfpres14['Dem_Percentage'] - dfpres14['Rep_Percentage']).abs()
    dfpres15 = dfpres14[['state', 'candidate_x', 'party_x', 'candidate_y', 'party_y', 'Dem_Percentage', 'Rep_Percentage', 'percentDiff']]
    print()
    pct = (float)(input('Enter a whole number percentage to evaluate for swing states: '))
    
    dfpres15 = dfpres15[dfpres15['percentDiff'] < pct]
    dfpres15['party_x'] = 'Democrat'
    dfpres15['party_y'] = 'Republican'
    dfpres15.reset_index(drop=True, inplace=True)
    
    print(f'\nPresidential Election Swing States (Less than: {pct:.1f}% difference)')
    print('=' * 72)
    print(f'{"State":22}{"Percentage":15}{"Winning Party":20}{"Electoral Votes"}')
    print('=' * 72)
    for item in range(0, len(dfpres15)):
        state, dem_cand, p_dem, rep_cand, p_rep, demPct, repPct, pctDiff = dfpres15.loc[item]
        # p_dem = 'Democrat'
        # p_rep = 'Republican'
        result = pctDiff
        if demPct > repPct:
            print(f'{state:20}{result:>6.2f}% {p_dem.title():>20}{votes[state]:>18}')
        else:
            print(f'{state:20}{result:>6.2f}% {p_rep.title():>20}{votes[state]:>18}')


def main():
    runSwing = True
    runAgain = True
    dfpres1, dfpres2, votes = prepareData()
    dfpres3, dfpres16, demCandidate, repCandidate = filterData(dfpres1, dfpres2) 
    validState = getStates(dfpres3) 
      
    '''
    Prompt the user for a valid sate name and check to see if it
    is valid. If not valid prompt the user to enter the state name
    until it is valid.
    '''
    while runAgain:
        stateChoice = input(f'Enter a state name: ').title()
        while stateChoice not in validState:
            stateChoice = input('Invalid state, enter a state name: ').title()
        stateUpper = stateChoice.upper()  #  Uppercase the state name entered by the user. Used later in output
    
        '''
        Add a new column called vote_percentage , values will be the result
        of the calculation total_votes candidate / total_votes_county.
        '''
        dfpres3['vote_Percentage'] = (dfpres3['total_votes'] / dfpres3['total_votes_county']) * 100
        dfpres6, dfpres7, dfpres17 = filterDemRepCandidate(dfpres3, demCandidate, repCandidate, stateChoice)    
        demEV, repEV = countElectoralVotesCandidate(dfpres17, votes)
    
        dfpres5 = determineUSData(dfpres6)
        dfpres9 = determineStateData(dfpres7)  
    
        dVotesUS, rVotesUS, dVotesPercentUS, rVotesPercentUS = extractUSVoteData(dfpres5, demCandidate, repCandidate) 
        dVotesState, rVotesState, dVotesPercentState, rVotesPercentState = extractStateVoteData(dfpres9, demCandidate, repCandidate)
    
        printUSResults(stateChoice, stateUpper, votes, demCandidate, repCandidate, dVotesState, rVotesState, dVotesPercentState, rVotesPercentState)
        printStateResults(stateChoice, stateUpper, demCandidate, repCandidate, demEV, repEV, dVotesUS, rVotesUS, dVotesPercentUS, rVotesPercentUS)
    
        if runSwing:
            swingStates(dfpres16, demCandidate, repCandidate, votes)
            
        answer = input("Another state? (Y or N): ")
        if answer == 'N' or answer == 'n':
            runAgain = False
            print('Terminating the program...')

                 
main()
