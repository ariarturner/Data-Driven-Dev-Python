# Programming Assignment 3

## Summary
The project requires knowledge of loops and defining methods. This project should output overall governor state election results and output the overall governor state county election results of an individual county in the state.

## Requirements
This program should do the following:
- Generate a menu of choices that the user can select from
    - S or s to output the results of a governor race in a state
    - C or c to output the results of a governor race in a state county
    - T or t to terminate the program
- If the user selects S or s from the menu, the program should:
    - Prompt the user for which state you want to see the results from
    - Output the governor election results for the state selected
    - Display the menu of choices and prompt the user for another selection
- If the user selects C or c from the menu, the program should:
    - Prompt the user for which state you want to see the results from
    - Prompt the user for which county you want to see the results from
    - Output the governor election results for the state county selected
    - Display the menu of choices and prompt the user for another selection
- If the user selects T or t from the menu, the program should:
    - Output a message that the program is being terminated
    - Terminate the program

## Required Methods
The program should contain the following methods:
- A `main` method that will run the program. This will be the driver program and make method calls to all the other required methods. It should include the following:
    - A call to the processDataFiles method which returns the 3 data lists
    - A while loop which contains the code that drives the execution of the program
- A `processDataFiles` method that reads in the data from the 3 CSV files into 3 lists. The method will return the 3 multi-dimensional lists to the calling program. The 3 multi-dimensional lists that are created from this method are:
    - `allStateList`: List that contains all the election data results for all states, all counties in the governor races for 2020
    - `totalVoteCountyList`: List that contains the totals votes cast for each county in each state in the governor races for 2020
    - `totalVoteStateList`: List that contains the totals votes cast for each state in the governor races for 2020
- A `mainMenu` method that creates the selection menu and allows the user to make a selection from it. This method returns the selection the user selected
- A `whichState` method that prompts the user for the name of a valid state in the 2020 governor races. This method must return, back to the calling method, the state name entered by the user.
    - The selected state must be validated as a valid state. If it is not a valid state, an error message should be output to the console and prompt the user to enter a valid state.
- A `whichCounty` method that prompts the user for the name of a valid state and a valid county from that state in the 2020 governor races. This method must return, back to the calling method, the state name and the county name entered by the user.
    - The selected county must be validated as a valid county from the selected state. If it is not a valid county, an error message should be output to the console and prompt the user to enter a valid county.
- A `overallStateResults` method that processes the state election data, which does include each vote count from each county, for the user selected state, and outputs the results for governor election for the selected state.
- A `overallCountyResults` method that processes the state election data for the user selected state and county, and outputs the results for governor election for the selected county from the selected state.
