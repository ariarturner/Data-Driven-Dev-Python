'''
Created on 1/23/2019 @author: DRUDE
 
Starting code for PA2. Place the rest of the code below the comment line 
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

# your code goes here