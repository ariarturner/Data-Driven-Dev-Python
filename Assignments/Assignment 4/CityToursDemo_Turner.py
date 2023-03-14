'''
Created on Mar 22, 2021
Assignment 4
@author: Aria Turner
Description: Determine number of bands that are eligible to play at a city and how many bands have already played in that city
'''

import os

def main ():
    '''Read user input, init the data structures and
      and run a loop responding to user queries on band tours
    '''
    #subfolder = "tour\\files-small"
    subfolder = input('Please enter the name of the sub-folder with files: ')
    cityCode = "Invalid City Code"
    while cityCode != "\n":
        stateCityDict, tourPrereqDict, bandDict, allBandSet = initFromFiles(subfolder)
    
        cityCode = input("\nPlease enter a city code or press enter to stop: ").capitalize()
        if cityCode == '':
            print("Program terminated...")
            break
        
        #print(f"stateCityDict: {stateCityDict}")
        #print(f"tourPrereqDict: {tourPrereqDict}")
        #print(f"bandDict: {bandDict}")
        #print(f"allBandSet: {allBandSet}")
    
        stateAbbr = getStateName(stateCityDict, cityCode)
        if stateAbbr == "Invalid City Code":
            cityCode = stateAbbr
            print(cityCode)
            continue
        else:
            cityName = getCityName(stateCityDict, cityCode)
            eligibleBandsSet, eligibleBands, bandsPlayedSet, bandsPlayed = determineBands(cityCode, tourPrereqDict, bandDict, allBandSet)
            print(f"\nThere are {eligibleBands} band(s) who are eligible to play at {cityName}, {stateAbbr} ({cityCode}).")
            #print(f"\nEligible Bands:\n===============")
            #for i in range(eligibleBands):
                #print(eligibleBandsSet[i], end=" : ")
            #print()
            print(f"\n{bandsPlayed} band(s) have already played at {cityName}, {stateAbbr} ({cityCode}).")
            #print(f"\nBands Already Performed:\n=======================")
            #for i in range(bandsPlayed):
                #print(bandsPlayedSet[i], end=" : ")
            #print()
    
    
    
    
    
    
    
    
def initFromFiles(subfolder):
    ''' intializes  data structures from files in subfolder
        Returns a tuple containing
            - States dictionary describes states and cities
            - tour prerequisites dictionary - cities and tour prerequisites
            - rock band dictionary - bands and cities they have been to
    '''
    # separate the files into lists
    files = os.listdir(os.path.join(os.getcwd(), subfolder)) #list of all file names in folder
    stateFiles = [f for f in files if f if f.startswith ('state')] #list of files related to states
    
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
            cityCode, cityName = line.strip().split(' ', 1) #split line into city code vs city name and assign to two variables
            stateCityDict [cityCode.strip()] = cityName.strip().title() #add to dictionary
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
            tourCode, prereqsStr = line.split(':') #split city code from prereq cities and assign to variables
            tourPrereqDict[tourCode] = prereqsStr.split(); #add to dictionary
    tpf.close()
    return tourPrereqDict










def processRockBandCityFiles(subfolder):
    ''' Read city file lists, creating a dictionary, which for each city code, 
     there is a list of bands who have played that city. 
      '''
    files = os.listdir(os.path.join(os.getcwd(), subfolder)) #get path for machine
    #list comprehension: create list of file names that do not begin with 'state' and are not prereqs
    bandFiles = [f for f in files if not f.startswith('state') 
                 and f != 'tourprereqs.txt']

    BandSet = set()
    rockBandDict = dict()
    for bandFileName in bandFiles:
        #print(bandFileName, bandFiles)
        with open(os.path.join(os.getcwd(), subfolder, bandFileName), 'r') as cf: #open each file
            cityCode =  cf.readline().strip()[0:] #get city code from first line
            #print (bandFileName, '--', cityCode) # print out the filename and city code
            bandNameSet = {line.strip() for line in cf } #get bands that have played in that city
        
            for bandName in bandNameSet:
                BandSet.add(bandName)
                #print(BandSet)
        
        if cityCode not in rockBandDict:
            rockBandDict [cityCode] = bandNameSet
        else: 
            rockBandDict [cityCode] = rockBandDict[cityCode].union(bandNameSet)
        #print(bandNameSet)
    return rockBandDict, BandSet










def determineBands(cityCode, tourPrereqDict, bandDict, allBandSet):
    #bands that played at city in question
    bandsPlayedSet = set(bandDict.get(cityCode))
    #city prereqs
    prereqs = tourPrereqDict.get(cityCode)

    if prereqs == None:
        #allBandSet - bandDict set for city in question
        eligibleBandsSet = allBandSet.difference(bandsPlayedSet)
    else:
        #bands that played at first prereq city
        bandsPlayedCity1 = set(bandDict.get(prereqs[0]))
        #bands that played at second prereq city
        bandsPlayedCity2 = set(bandDict.get(prereqs[1]))
        #bands that played at both prereq cities and therefore meet prereqs
        bandsPlayedPrereqs = bandsPlayedCity1.intersection(bandsPlayedCity2)
        #bands that played both prereqs and have not played at city in question
        eligibleBandsSet = bandsPlayedPrereqs.difference(bandsPlayedSet)
    #count number of eligible bands and number of bands played
    eligibleBands = len(eligibleBandsSet)
    bandsPlayed = len(bandsPlayedSet)
    
    return sorted(eligibleBandsSet), eligibleBands, sorted(bandsPlayedSet), bandsPlayed

    

    






def getStateName(stateCityDict, cityCode):
    #match city code to state
    for stateKey in stateCityDict:
        stateDict = stateCityDict.get(stateKey)
        stateAbbr = "Invalid City Code"
        if stateDict.get(cityCode) != None:
            stateAbbr = stateKey
            break
    #return state abbreviation
    return stateAbbr
    
    
    
    
    
    
    
    
    
    
def getCityName(stateCityDict, cityCode):
    #match city code to city
    stateAbbr = getStateName(stateCityDict, cityCode)
    if stateAbbr == "Invalid City Code":
        cityName = "Invalid City Code"
    else:
        stateDict = stateCityDict.get(stateAbbr)
        cityName = stateDict.get(cityCode)
    #return city name
    return cityName










main()