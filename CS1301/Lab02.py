"""
HOMEWORK PROBLEM 1.
Function Name: rainbowPattern()
Parameters: aString (str), colorList (list), output filename (str)
Returns: None (NoneType)
Description: Write a function called 'rainbowPattern' that takes a string and assigns it an alternating color from a 
list of colors 'colorList'. The function will print out each lettter of the string individually with a 
dash and its respective color. For example, "W - Red". Make sure that a color is NOT assigned to a space but
continues to follow the alternating pattern. 
"""
### SOLUTION:
# def rainbowPattern(aString, colorList):
#     for index in range(len(aString)):
#         if aString[index] != " ":
#             print(aString[index] + " - " + colorList[index % len(colorList)])
#         else:
#             print(aString[index])

# def rainbowPattern(aString,colorList):
#     if len(aString) == 0:
#         return 
#     else:
#         if aString[0] == " ":
#             print(aString[0])
#             rainbowPattern(aString[1:], colorList[1:] + [colorList[0]])
#         else:
#             print(aString[0] + " - " + colorList[0])
#             rainbowPattern(aString[1:], colorList[1:] + [colorList[0]]) 

### TEST CASE(S):
# colorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
# rainbowPattern("Holiday Lights", colorList)

# H - Red
# o - Orange
# l - Yellow
# i - Green
# d - Blue
# a - Purple
# y - Red 
# 
# L - Yellow
# i - Green
# g - Blue
# h - Purple
# t - Red
# s - Orange

# colorList = ['Red', 'White', 'Blue']
# rainbowPattern("Fireworks", colorList)

# F - Red
# i - White
# r - Blue
# e - Red
# w - White
# o - Blue
# r - Red
# k - White
# s - Blue


"""
HOMEWORK PROBLEM 2. 
Function Name: evenOddChecker()
Parameters: binaryList (list)
Returns: dictionary of a list of decimal numbers mapped to either 'even' or 'odd' (dict)
Description: Write a function that takes in a list of a binary number strings and 
tests if the equivalent decimal number is even or odd. Even numbers should have 
their decimal equivalent appended to a list mapped to 'even' in a dictionary. 
Odd numbers should have their decimal equivalent appended to a list mapped to 'odd' 
in a dictionary. A dictionary containing all these mappings should be 
returned at the end.
"""

### SOLUTION:
# def evenOddChecker(binaryList):
#     strValue = 0
#     valList=[]
#     numDict = {'even':[],'odd':[]}
#     for num in binaryList:
#         for value in range(len(num)):
#             valList.append(2**value)
#         for index,value in enumerate(num[::-1]):
#             strValue += int(value) * (valList[index])
#         if num[-1]=='0':
#             numDict['even'].append(strValue)
#         else:
#             numDict['odd'].append(strValue)
#         strValue = 0
#         valList=[]
#     return numDict
### TEST CASE(S):
# print(evenOddChecker(["1100","1010101","10010","101101"]))
# {'even': [12, 18], 'odd': [85, 45]}
# print(evenOddChecker(["1010"]))
# {'even': [10], 'odd': []} 


"""
HOMEWORK PROBLEM 3.
Function Name: classReservation()
Parameters: filename (str), lectureCRN (str), recitationCRN (str)
Returns: string that says whether registration occurred or not (str)
Description: Given the CRN for a lecture and a CRN for a recitation from the 
cs1331.csv file, check if registration is allowed based on class space and section. 
You must take into account if the class is already full or not by looking at 
'Cap', 'Act', and 'Rem'. 'Cap' is the maximum class size, 'Act' is the number of 
people who have already enrolled in the class, and 'Rem' is the number of seats 
remaining. You must also account for the section each recitation and lecture are in. 
For example, if you the lecture is section A, then you must register for a recitation
is in either A01, A02, A03, A04, or A05. If registration is not possible, return 
"An error occurred during registration." Otherwise, return "You're registered!".
Note: The CRNs will always be a lecture and a recitation.
Note: Time for a lecture and corresponding recitation will never overlap.
Note: If an incorrect CRN is entered, return "An error occurred during registration."
"""

### SOLUTION:
# def classReservation(filename,lectureCRN,recitationCRN):
#     infile = open(filename,'r')
#     header = infile.readline()
#     data = infile.readlines()
#     infile.close()
    
#     infoDict = {}
#     regString = "You're registered!"
#     noString = "An error occurred during registration."
#     try:

#         for line in data:
#             pieces = line.strip().split(',')
#             crn = pieces[0]
#             sec = pieces[3]
#             rem = pieces[12]
#             if crn == lectureCRN:
#                 infoDict[crn] = [sec,rem]
#             if crn == recitationCRN:
#                 infoDict[crn] = [sec,rem]
#         if infoDict[lectureCRN][0] == infoDict[recitationCRN][0][0] and (int(infoDict[lectureCRN][1]) > 0 and int(infoDict[recitationCRN][1]) > 0):
#                 return regString 
#         else:
#             return noString
#     except:
#         return noString
### TEST CASE(S):

# print(classReservation("cs1331.csv", "25761", "28443"))
# You're registered!

# print(classReservation("cs1331.csv","21980","28453"))
# An error occured during registration.

# print(classReservation("cs1331.csv","219",'fdd'))
# An error occured during registration.


"""
HOMEWORK PROBLEM 4.
Function Name: daysOfChristmas()
Parameters: day (int), fileName (str), outfileName (str)
Returns: None (NoneType)
Description: Using the "twelvedaysofchristmas.txt" file, write the lyrics of the 
tune based on the given number of days in the first parameter into a new file 
named "lyrics.txt". The first line of the output file will always be
"On the first day of Christmas, my true love sent to me:"
Note: Day will never be greater than 12 or less than 0
Note: If day = 1, include "and" at the beginning of the day 1 string. 
This is shown in the test case.
"""

### SOLUTION:

# def daysOfChristmas(day,fileName,outfileName):
#     infile = open(fileName,'r')
#     data = infile.readlines()
#     infile.close()
#     outfile = open('lyrics.txt','w')
#     outfile.write("On the first day of Christmas, my true love sent to me:\n")
    
#     for line in data[::-1]:
#         line = line.strip().split(' - ')
#         if int(line[0]) <=  day and int(line[0]) >1:
#             outfile.write(line[0]+' '+line[1]+'\n')
#         elif int(line[0]) == 1 and day > 1:
#             outfile.write('and A Partridge in a Pear Tree')
#         elif int(line[0]) == 1 and day == 1:
#             outfile.write('A Partridge in a Pear Tree')
#     outfile.close()

### TEST CASE(S):

# daysOfChristmas(1, "twelvedaysofchristmas.txt", "lyrics.txt")
# On the first day of Christmas, my true love sent to me:
# A Partridge in a Pear Tree

# daysOfChristmas(4, "twelvedaysofchristmas.txt", "lyrics.txt")
# On the first day of Christmas, my true love sent to me:
# 4 Calling Birds
# 3 French Hens
# 2 Turtle Doves
# and A Partridge in a Pear Tree


"""
HOMEWORK PROBLEM 5.
Function Name: treeDecorator()
Parameters: fileName (str)
Returns: None (NoneType)
Description: Using the unfinished Christmas Tree made up of "X"s, decorate the Christmas Tree with ornaments: "O"
by replacing the original "X" with the "O". "O"s cannot be adjacent to one another and must be separated 
by a single "X" in the pattern shown: XOXOXOXOX. Always skip between lines of all "Xs" and the given pattern. 
The first and last "X" of the line must not be changed. If there are only three "X"s in a row on a file line, 
do not add an ornament. 
"""

### SOLUTION:

# def treeDecorator(filename):
#     infile = open(filename,'r')
#     data = infile.readlines()
#     infile.close()
#     line_count=1
#     datanew=''
#     totallines=len(data)
#     for line in data:
#         if (line_count%2==0 or line_count in range(totallines-2,totallines+1)):
#             datanew+=line
#         else:
#             xcount=1
#             newline=''
#             for char in line:
#                 if(char=='X'):
#                     xcount=1-xcount
#                     if(xcount==1):
#                         newline+='O'
#                     else:
#                         newline+='X'
#                 else:
#                     newline+=char
#             datanew+=newline
#         line_count+=1
#     print(datanew)
                    

### TEST CASE(S):
#                O
# 		        XXX
# 		       XOXOX
#             XXXXXXX
#            XOXOXOXOX
#           XXXXXXXXXXX
#          XOXOXOXOXOXOX
#         XXXXXXXXXXXXXXX
#          XOXOXOXOXOXOX
#         XXXXXXXXXXXXXXX
#        X0X0X0X0X0X0X0X0X
#       XXXXXXXXXXXXXXXXXXX
#      X0X0X0XOXOXOXOXOXOXOX
#     XXXXXXXXXXXXXXXXXXXXXXX
#       XOXOXOXOXOXOXOXOXOX
#      XXXXXXXXXXXXXXXXXXXXX
#     XXXXXXXXXXXXXXXXXXXXXXX
#    XXXXXXXXXXXXXXXXXXXXXXXXX
#   XXXXXXXXXXXXXXXXXXXXXXXXXXX
#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
#              XXX
# 		       XXX
#              XXX

 

