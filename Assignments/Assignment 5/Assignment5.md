# Programming Assignment 5

## Summary
The project requires knowledge of numpy and pandas to manipulate and access data. This project should output the presidential popular vote election results and the individual state presidential election results.

## Data Overview
This project involves data the 2020 U.S. Presidential election. The data includes:
- president_county_candidate.csv
    - state: name of US state
    - county: name of county in US state
    - candidat: presidential candidate
    - party: presidential candidate party
    - total_votes: votes received by candidate in county
- president_county.csv
    - state: name of US state
    - county: name of county in US state
    - total_votes: total votes cast in county
- electoral_votes.csv
    - state: name of US state
    - votes: electoral votes awarded if candidate wins US state
- validStates: a python set that contains all US states and the District of Columbia

## Requirements
This program should do the following:
- Prompt the user to input the name of a valid U.S. State or the District of Columbia.
- Validate the input. If the input is invalid:
    - Print out the error message "Invalid state, enter a valid state: "
    - Prompt the user to input a valid US state
    - Repeat this process until you get a valid US state
- Print out the results for state and US presidential election
    - US state presidential election results which include:
        - Vote counts for the Democratic and Republican candidates
            - Winner listed first in output
        - Vote percentages for the Democratic and Republican candidates
        - Which candidate won the state
        - Electoral Votes awarded
        - Vote count difference
        - Vote percentage difference
        - All numbers formatted with commas and all number percentages with two digits to the right of the decimal point
    - US presidential election popular vote results which include:
        - Vote counts for the Democratic and Republican candidates
            - Winner listed first in output
        - Vote percentages for the Democratic and Republican candidates
        - Which candidate won the U.S popular vote
        - Vote count difference
        - Vote percentage difference
        - All numbers formatted with commas and all number percentages with two digits to the right of the decimal point
