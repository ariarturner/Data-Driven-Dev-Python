'''
Created on Jan 26, 2021
@author: Aria Turner
Title: Assignment 1
Description: calculate facts about jet fuel

'''

#print program description
print("This program takes the following amount of jet fuel in gallons and calculates the following:\n\t1. Equivalent number of liters\n\t2. Number of barrels of oil required\n\t3. Pounds of Carbon Dioxide produce\n\t4. BTUs produced\n\t5. Weight in pounds\n\t6. Total price in US dollars\n\t7. Flight time of a 787\n")


#request value for jet fuel to be purchased
jetFuelGal = round(eval(input("Please enter the number of gallons of jet fuel you wish to purchase: ")), 2)


#name constants (per gallon of jet fuel unless otherwise named)
LITER = 3.7854
BARREL = 42
OIL = 4
CO2 = 21.095
BTU = 128100
WEIGHT = 6.7
PRICE = 1.88
BURN_RATE = 1600


#convert amount of jet fuel in gallons to liters
jetFuelLtr = jetFuelGal * LITER


#calculate the number of barrels of oil needed for jet fuel
oilBarrels = jetFuelGal / OIL


#calculate the pounds of CO2 produced
CO2Produced = jetFuelGal * CO2


#calculate the BTUs produced
BTUProduced = jetFuelGal * BTU


#calculate the weight of jet fuel
totalWeight = jetFuelGal * WEIGHT


#calculate the price in US $
totalPrice = jetFuelGal * PRICE


#calculate the time that a 787 could fly
flightTotal = jetFuelGal / BURN_RATE * 60

#find just the hour portion of time
flightHour = flightTotal // 60

#find the remaining minute portion of time
flightMin = int(flightTotal) % 60


#print and format summary of results
print("\n------")
print(f"Original number of gallons is: {jetFuelGal:,.2f}")
print(f"{jetFuelGal:,.2f} gallons of jet fuel is equivalent of {jetFuelLtr:,.2f} Liters")
print(f"{jetFuelGal:,.2f} gallons of jet fuel requires {oilBarrels:,.2f} barrels of oil")
print(f"{jetFuelGal:,.2f} gallons of jet fuel produces {CO2Produced:,.2f} pounds of CO2")
print(f"{jetFuelGal:,.2f} gallons of jet fuel produces {BTUProduced:,.2f} BTUs of energy")
print(f"{jetFuelGal:,.2f} gallons of jet fuel weighs {totalWeight:,.2f} Pounds")
print(f"{jetFuelGal:,.2f} gallons of jet fuel costs ${totalPrice:,.2f}")
print("------")
print(f"Total flight time of a 787 aircraft: {flightHour:>2n} Hours {flightMin:>2n} Minutes")





