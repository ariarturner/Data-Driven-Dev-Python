'''
Created on 1/23/2019 @author: DRUDE
 
Starting code for PA2. Place the rest of the code below the comment line 
'''

def fromFile(file):
    file = open(file, 'r')
    line = file.read() 
    return line 

#txtfile = input("Please enter the name of the file containing the text: ")
txtfile = 'text2.txt'
textOrig = fromFile(txtfile)
print('Contents of file',txtfile)
print()
print (textOrig)

input('\nHit Enter')
print()

modifiedOrigText = textOrig.lower()
textOrigNoCRNL = textOrig.replace('\n', ' ')
print(textOrigNoCRNL + ' (Original Text No CR/NL)')

input('\nHit Enter')
print()
modifiedOrigText = modifiedOrigText.replace('\n', ' ')
print(modifiedOrigText + ' (Original Text Lowercase)')

# Used to find sentence that keyword is in
modifiedOrigText = modifiedOrigText.replace(',', ' ')
modifiedOrigText = modifiedOrigText.replace('!','.')
modifiedOrigText = modifiedOrigText.replace('?','.')
modifiedOrigText = modifiedOrigText.replace(';',' ')
modifiedOrigText = modifiedOrigText.replace(':',' ')
modifiedOrigText = modifiedOrigText.replace('-',' ')


input('\nHit Enter')
print()

print(modifiedOrigText + ' (Modified Original Text \",!?;:\-" changed or removed)') 
modifiedOrigTextNoPeriods = modifiedOrigText.replace('.',' ') # Used to search for keyword and create dot schema

input('\nHit Enter')
print()
print(modifiedOrigTextNoPeriods + ' (Modified Original Text No Periods)')

input('\nHit enter')
print()
stringToFind = input("\nEnter a key word: ").lower()
stringToFind += ' '
exist = stringToFind in modifiedOrigTextNoPeriods
print(exist)

if exist:
    foundIndex = modifiedOrigTextNoPeriods.find(stringToFind)
    print(foundIndex)
else:
    print('terminating....')
    print()
    print()


# your code goes here