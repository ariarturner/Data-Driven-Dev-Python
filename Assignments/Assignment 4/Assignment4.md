# Programming Assignment 4

## Summary
The project requires knowledge of working with files and directories and using dictionaries, tuples, sets, and lists. This project should output the number of eligible bands and the number of bands that have already played in the selected city.

## Data Overview
This project involves data on cities that musical bands could play at. The data includes:
- A list of states that includes the state abbreviation, the city code, and city names. Thefilenames are listed below:
    - state1.txt : CA (Cities in California)
    - state2.txt : FL (Cities in Florida)
    - state3.txt : TX (Cities in Texas)
    - state4.txt : NY (Cities in New York)
- City prerequisites structure. This data determines what cities a band had to play first, to be able to play another city in the same state. If a city code does not appear in this data, then no tour prerequisites are required for a ban to play in some given city. The file is tourprereqs.txt. The contents is listed below:
    - C5: C1 C2 (To Play San Francisco, a band must play in Los Angeles, and Bakersfield)
    - T5: T3 T4 (To Play Dallas, a band must play in Austin and Houston)
    - N5: N2 N4 (To Play New York, a band must play in Buffalo and Albany)
    - F5: F2 F3 (To Play Miami, a band must play in Pensacola and Jacksonville)
- City/Band text files. This data contains the city code and the bands that have played that city. Each city/band list comes in a separate file, the first line of which includes the city code, followed by separate lines that are band names. Each one of these files store records of bands that have already played in a given city.

## Requirements
This program uses this data to estimate the number of bands who would be eligible to play in a city in some state. An eligible band:
- has completed all tour prerequisites for that city, and
- has not already played in that city

This program must:
- Ask the user to specify the subfolder in the current working directory, where the files are stored
- Ask the user for a city code, outputting the number of eligible bands that can play that city in respones. Incorrect city codes should be ignored and the program should go on. When the user does not specify any city code, and presses enter instead, the program should stop running.
- Not use any global variables or any code outside of function defintions (except for a single call to `main`)
- Use device-independent handling of paths
- Use data structures effectively

## Required Functions
The program should define and use the following functions:
- `processStateFiles()` function with a single parameter of type str, which provides the path to state files. The function should construct a dictionary called `stateCityDict`, based on the information in the state files. The dictionary should have keys equal to the city codes, and values equal to the corresponding city names. The function must return a tuple, consisting of the state name and the created dictionary `stateCityDict`
- `processTourPrereqsFile()` function with a single parameter of type str, providing the path to a file defining tour city prerequisites. The function should construct a dictionary called `tourPrereqDict`, based on the information in the tourprereqs.txt file. The dictionary should have keys equal to the citycode that has prereqs, and values equal to the corresponding prerequisite city codes. Only cities that have tour prerequisites should be included in this dictionary. The function must return the constructed dictionary `tourPrereqDict`
- `processRockBandCityFiles()` function with a single parameter, defining the subfolde rwith the city/band text files, as outlined in the Data and Program Overview section above.The function should construct a dictionary called `rockBandDict` by reading the text files that contain the city code and the band names that have already played that city. The keys corresponding to the city codes, and the values for each key must be equal to the set of bands who have played the city designated by the key. The function must return the constructed dictionary `rockBandDict`
- `initFromFiles()` function with a single parameter, defining the subfolder with the files. The method should call the functions specified above to process data provided in the files. The function should return a tuple with the constructed dictionaries for city codes and city names, a list of bands that have played per city code, and band tour prerequisites
- `determineBands()` function which will be passed a city code and other parameters as needed, and will return a count of bands who are eligible to play in the city that was selected (city code). It will also return a count of the bands that have already played in the city that was selected (city code). If the parameter does not refer to a valid city code, the function should return an empty list. Note: this function should not be working with the text files, but should get all needed information from the appropriate data structures (tuples, dictionaries, and sets) that were created from the other functions that read the data from the text files
- `getStateName()` function which will be passed the state/city dictionary and city code and return the state abbreviation
- `getCityName()` function which will be passed the state/city dictionary and the city code and returns the city name
- `main()` function which will be called to start the program and works according to design

## Data Reference/Information Appendix

### City & State Code Info
| City Code | City Name | State |
| --- | --- | --- |
| C1 | Los Angeles | California |
| C2 | Bakersfield | California |
| C3 | Sacramento | California |
| C4 | San Diego | California |
| C5 | San Francisco | California |
| F1 | Orlando | Florida |
| F2 | Pensacola | Florida |
| F3 | Jacksonville | Florida |
| F4 | Tampa | Florida |
| F5 | Miami | Florida |
| N1 | Niagara Falls | New York |
| N2 | Buffalo | New York |
| N3 | Syracuse | New York |
| N4 | Albany | New York |
| N5 | New York | New York |
| T1 | Alamo | Texas |
| T2 | Fort Worth | Texas |
| T3 | Austin | Texas |
| T4 | Houston | Texas |
| T5 | Dallas | Texas |

### Tour PreReq City Codes
| City Code | City Name | Prereq City Code | Prereq City Name | Prereq City Code | Prereq City Name |
| --- | --- | --- | --- | --- | --- |
| C5 | San Francisco, CA | C1 | Los Angeles, CA | C2 | Bakersfield, CA |
| F5 | Miami, FL | F2 | Pensacola, FL | F3 | Jacksonville, FL |
| N5 | New York, NY | N2 | Buffalo, NY | N4 | Albany, NY |
| T5 | Dallas, TX | T3 | Austin, TX | T4 | Houston, TX |