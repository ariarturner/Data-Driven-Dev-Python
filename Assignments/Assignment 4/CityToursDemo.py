'''
Created on Nov 4, 2020
@author: ruded
'''
import os
import sys

def main ():
    '''Read user input, init the data structures and
      and run a loop responding to user queries on band tours
    '''
    
    subfolder= input('Please enter the name of the sub-folder with files: ')
  
    stateCityDict, tourPrereqDict, bandDict, allBandSet = initFromFiles(subfolder)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def initFromFiles(subfolder):
    ''' intializes  data structures from files in subfolder
        Returns a tuple containing
            - States dictionary describes states and cities
            - tour prerequisites dictionary - cities and tour prerequisites
            - rock band dictionary - bands and cities they have been to
    '''
    # separate the files into lists
    files = os.listdir(os.path.join(os.getcwd(), subfolder))
    stateFiles = [f for f in files if f if f.startswith ('state')]
    
    # create a summary of cities in a dictionary
    stateDict = {}
    for stateFile in stateFiles: 
        stateName, stateCityDict = processStateFiles(os.path.join(os.getcwd(), subfolder, stateFile))
        stateDict [stateName] = stateCityDict
        #print(stateDict)
    
    #create a dictionary of tour prerequisites 
    tourPrereqDict = processTourPrereqsFile(os.path.join(os.getcwd(), subfolder, 'tourprereqs.txt'))
    
        #create a dictionary of rock bands who are on tour
    rockBandDict, allBandSet = processRockBandCityFiles(subfolder)
    
    return stateDict, tourPrereqDict, rockBandDict, allBandSet
























def processStateFiles(stateFile):
    '''stateFile must be a path to file containing state titles followed by a 
    a a set of lines listing  city codes and city names. 
    Read stateFile to construct a dictionary, with stateCode: CityTitle items
    Return tuple: state name , state city dictionary
    '''
    stateCityDict = {}
    with open(stateFile, 'r') as sf:
        stateName = sf.readline().strip() # program name is on the first line of the file
        for line in sf:
            cityCode, cityName = line.strip().split(' ', 1)
            stateCityDict [cityCode.strip()] = cityName.strip().title()
    sf.close()
    #print(stateName, stateCityDict)
    return stateName, stateCityDict





















def processTourPrereqsFile(prereqsFile):
    ''' prereqsFile contains information about what
       tour cities that a band have to go to first before
       they can go to the final city in the state. All final
       cities in a state have  5 in the code (example:
       C5 for San Francisco, CA.) This function reads the 
       tourprereq file and returns the tour pre-req dictionary
    '''
    tourPrereqDict = {}
    with open(prereqsFile, 'r') as tpf:
        for line in tpf:
            tourCode, prereqsStr = line.split(':')
            tourPrereqDict[tourCode] = prereqsStr.split();
    tpf.close()
    return tourPrereqDict
























def processRockBandCityFiles(subfolder):
    ''' Read city file lists, creating a dictionary, which for each city code, 
     there is a list of bands who have played that city. 
      '''
    files = os.listdir(os.path.join(os.getcwd(), subfolder))
    bandFiles = [f for f in files if not f.startswith('state') 
                 and f != 'tourprereqs.txt']

    BandSet = set()
    rockBandDict = dict()
    for bandFileName in bandFiles:
        #print(bandFileName, bandFiles)
        with open(os.path.join(os.getcwd(), subfolder, bandFileName), 'r') as cf:
            cityCode =  cf.readline().strip()[0:]
            #print (bandFileName, '--', cityCode) # print out the filename and city code
            bandNameSet = {line.strip() for line in cf }                
        
            for bandName in bandNameSet:
                BandSet.add(bandName)
                #print(BandSet)
        

        if cityCode not in rockBandDict:
            rockBandDict [cityCode] = bandNameSet
        else: 
            rockBandDict [cityCode] = rockBandDict[cityCode].union(bandNameSet)
        #print(bandNameSet)
    return rockBandDict, BandSet


main()