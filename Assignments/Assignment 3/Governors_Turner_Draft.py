'''
Created on <Enter a start date>
@author: <Enter Your Full Name>
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
All our required methods for this program
should be started here. The required methods are:
whichState()
whichCounty()
overallStateResults()
overallCountyResults()
'''

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
        goes here
        '''
        if mmSelection =='T' or mmSelection == 't':
            print('Terminating program...')
            exit()
    
main()