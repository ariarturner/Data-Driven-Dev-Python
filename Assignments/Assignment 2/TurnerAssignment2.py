'''
Created on Feb 8, 2021
@author: Aria Turner
Title: Assignment 2
Brief description: This is a program that locates the first occurrence of a keyword in a text and outputs 
the sentence in which the keyword appears.
'''

def fromFile(file):
    file = open(file, 'r')
    line = file.read() 
    return line 

txtfile = input("Please enter the name of the file containing the text: ")
#txtfile = 'text2.txt'
textOrig = fromFile(txtfile)
print('Contents of file',txtfile)
print()
print (textOrig)


'''
Modify Original text file so that we can search for word more easily without having to think of each 
individual case (i.e., all lowercase, replace punctuation with spaces, etc.).
'''

#change all text to be lowercase
modifiedOrigText = textOrig.lower()

#make new lines spaces instead
modifiedOrigText = modifiedOrigText.replace('\n', ' ')


#replace most punctuation with spaces; used to find sentence that keyword is in
modifiedOrigText = modifiedOrigText.replace(',', ' ')
modifiedOrigText = modifiedOrigText.replace('!','.')
modifiedOrigText = modifiedOrigText.replace('?','.')
modifiedOrigText = modifiedOrigText.replace(';',' ')
modifiedOrigText = modifiedOrigText.replace(':',' ')
modifiedOrigText = modifiedOrigText.replace('-',' ')

#make periods spaces
modifiedOrigTextNoPeriods = modifiedOrigText.replace('.',' ') # Used to search for keyword


#ask user to provide a keyword
keyword = input("\nEnter a key word: ").lower()

#add spaces on either side of keyword (eliminates the possibility of another word containing keyword)
keyword = ' ' + keyword + ' '
#number of characters in keyword (helpful for later indices)
keywordLength = len(keyword.strip())

#see if keyword exists in the text file (excluding very first word because of leading space in keyword)
exist = keyword in modifiedOrigTextNoPeriods


#see if keyword exists at the very beginning of text file (no space before)
if exist == False:
    #remove leading space
    keyword = keyword.lstrip()
    #create second test for existence of word with no leading space
    exist2 = keyword in modifiedOrigTextNoPeriods
    #we only want to use this if it exists at the very beginning of the text file
    if exist2:
        #check if its index is 0 (very beginning of text file)
        foundIndex = modifiedOrigTextNoPeriods.find(keyword)
        if foundIndex == 0:
            #update main test of existence
            exist = True
        else:
            exist = False


'''
Output the sentence of the text containing the first occurrence of the specified keyword (appearing in 
possibly different combination of capital and lowercase letters). Show the keyword in all capitals.
'''

#find starting index of keyword
if exist:
    foundIndex = modifiedOrigTextNoPeriods.find(keyword)
    #ask user to provide line length for schema
    lineLength = eval(input("Enter the line length for the schema output: "))
#find index for start of sentence
    #if foundIndex = 0, then it is at the beginning of the very first sentence and there is no period before it
    if foundIndex == 0:
        #startIndex is sentence start
        startIndex = 0
    else:
        #use rfind to find period BEFORE keyword
        startIndex = modifiedOrigText.rfind('.', 0, foundIndex) + 1
        
#find index for end of sentence
    #use find to find period AFTER keyword
    #endIndex is sentence end
    endIndex = modifiedOrigText.find('.', foundIndex) + 1
    
    #use length(keyword) to find last index of keyword
    keywordEnd = foundIndex + (len(keyword) - 1)
    
    #split sentence into halves to keep capitalization the same as original.
    firstSentenceHalf = textOrig[startIndex:foundIndex]
    secondSentenceHalf = textOrig[keywordEnd:endIndex]
    #use strip to get rid of extra whitespace before and after keyword.
    #capitalize keyword only
    capitalKeyword = keyword.upper().strip()
    
    #recombine sentence and strip any additional white space
    if foundIndex == 0:
        keywordSentence = (firstSentenceHalf + capitalKeyword + secondSentenceHalf).strip()
    else:
        keywordSentence = (firstSentenceHalf + ' ' + capitalKeyword + secondSentenceHalf).strip()

    #print line separator
    print("\n--------------\nOutputting the sentence\n*****")
    #print sentence containing keyword
    print(keywordSentence)

    
    '''
    Create schema feature that displays information about where they keyword falls within the entire text.
    '''
    #number of characters in original file
    fileLength = len(textOrig)
    #number of FULL length lines
    noOfFullLines = int(fileLength // lineLength)
    #number of total lines
    if fileLength % lineLength != 0:
        noOfLines = noOfFullLines + 1
        #number of characters left in final line
        finalLineLength = int(fileLength % lineLength)
    else:
        noOfLines = noOfFullLines
        #number of characters left in final line
        finalLineLength = lineLength
    #the line that keyword begins in
    keywordStartLineNo = int(foundIndex // lineLength)
    #the line that the keyword ends in
    keywordEndLineNo = int(keywordEnd // lineLength)
    #the standard string of dots (not keyword line(s) or final line)
    stringOfDots = '\n' + '.' * lineLength
    #the string of dots for the final line
    finalDots = '.' * finalLineLength
    #the index relative to the beginning of the line for the keyword
    keywordLineStartIndex = int(foundIndex % lineLength)
    #on the line of the keyword, the dots that appear before the keyword
    introDots = '.' * (keywordLineStartIndex)
    #situation if keyword is entirely on one line (not split)
    if keywordStartLineNo == keywordEndLineNo:
        #situation if keyword is on one line AND it is on the very last line (not necessarily a full line)
        if keywordEndLineNo == noOfFullLines:
            #dots after keyword
            outroDots = '.' * (finalLineLength - (len(introDots) + keywordLength + 1))
            #combine the whole schema in one print statement
            print(f"\nOutputting the schema based on {lineLength} characters per line:\n*****{stringOfDots * (keywordStartLineNo)}\n{introDots}{capitalKeyword}{outroDots}")
        #situation if keyword is one one line and it is NOT the last line
        else:
            #dots after keyword
            outroDots = '.' * (lineLength - (len(introDots) + keywordLength))
            #combine the whole schema in one print statement
            print(f"\nOutputting the schema based on {lineLength} characters per line:\n*****{stringOfDots * (keywordStartLineNo)}\n{introDots}{capitalKeyword}{outroDots}{stringOfDots * (noOfFullLines - (keywordStartLineNo + 1))}\n{finalDots}")
    #situation if keyword is split between lines
    else:
        #situation if keyword is split between the lines AND the keyword ends on the final line
        if keywordEndLineNo == noOfFullLines:
            #create a string that contains the dots before the keyword and the keyword
            tempString = introDots + capitalKeyword
            #use the string to slice just the portion that goes in the first keyword line
            keywordStartLine = tempString[0:lineLength]
            #use the string to slice just the portion that goes on the second keyword line
            keywordRemainder = tempString[lineLength:]
            #add the dots to the remainder of the keyword to fill out the final line length
            keywordEndLine = keywordRemainder + ('.' * (finalLineLength - len(keywordRemainder)))
            #combine the whole schema in one print statement
            print(f"\nOutputting the schema based on {lineLength} characters per line:\n*****{stringOfDots * keywordStartLineNo}\n{keywordStartLine}\n{keywordEndLine}")
        #situation if keyword is split between the lines and the keyword does NOT end on the final line
        else:
            #create a string that contains the dots before the keyword and the keyword
            tempString = introDots + '.' + capitalKeyword
            #use the string to slice just the portion that goes in the first keyword line
            keywordStartLine = tempString[0:lineLength]
            #use the string to slice just the portion that goes on the second keyword line
            keywordRemainder = tempString[lineLength:]
            #add the dots to the remainder of the keyword to fill out the final line length
            keywordEndLine = keywordRemainder + ('.' * (lineLength - len(keywordRemainder)))
            #combine the whole schema in one print statement
            print(f"\nOutputting the schema based on {lineLength} characters per line:\n*****{stringOfDots * keywordStartLineNo}\n{keywordStartLine}\n{keywordEndLine}{stringOfDots * (noOfFullLines - (keywordStartLineNo + 2))}\n{finalDots}")

    
#if keyword is not found, print following statements
else:
    print(f'\'{keyword.strip()}\' does not appear in the text...')
    print()
