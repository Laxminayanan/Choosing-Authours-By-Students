import pandas as pd
import availableDictionaryOfAuthours 
import remainingAuthourCodes
import siNo
dictionaryofAuthoursForReference  = availableDictionaryOfAuthours.remainingAuthorsDict
import os
import registeredStudentsTillNow
import registeredRollNumbersTillNow


def AppendReposesofTheStudentsFromTheSecondRun(name, newRowData):
    # Convert new row to DataFrame
    new_df = pd.DataFrame([newRowData],columns=[ 'SI.No ','NameOfTheStudent', 'RollNumberOfTheStudent', 'Branch', 'Section', 'ChoosenAuthourName'])

    excel_filename = f"{name}.xlsx"

    try:
        if os.path.exists(excel_filename):
            # Read the existing file
            existing_df = pd.read_excel(excel_filename, engine='openpyxl')
            # Append new data
            updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        else:
            return -1
        # Save back to Excel
        updated_df.to_excel(excel_filename, index=False, engine='openpyxl')
        return 0
    except Exception as e:
        return -1

# Student Information

def validateEnteredName(enteredName):
    if (len(enteredName) == 0):
        return False
    elif (checkForMoreThanOneSpace(enteredName) == False):
        return False
    elif (checkIfOnlyAlphabetsOrSpaceArePresentInTheString(enteredName) == False):
        return False
    else:
        dupOfRegisteredStudentsTillNow = registeredStudentsTillNow.registeredTillNow
        for i in dupOfRegisteredStudentsTillNow:
            if enteredName ==  i:
                return False
            
        # OverWrittingregisteredStudentsTillNow
        dupOfRegisteredStudentsTillNow.append(enteredName)
        toOverwriteDupOfRegisteredStudentsTillNow = dupOfRegisteredStudentsTillNow
        with open('registeredStudentsTillNow.py', 'w') as f:
            f.write(f'registeredTillNow = {toOverwriteDupOfRegisteredStudentsTillNow}\n')
        return True


def checkForMoreThanOneSpace(string):
    count = 0
    for i in string:
        asciiOfi = ord(i)
        if asciiOfi == 32:
            count+=1
    if (count == 1 or count == 0):
        return True
    else:
        return False
def checkIfOnlyAlphabetsOrSpaceArePresentInTheString(string):
    for i in string:
        asciiOfi = ord(i)
        if ((asciiOfi >= 65 and asciiOfi <= 90) or (asciiOfi >= 97 and asciiOfi <= 122) or (' ')):
            continue
        else:
            return False
    return True


def validateRollNumber(rollNumber):
    if (len(rollNumber) == 10):
        listToCheck  = ['2','4','r','a','1','a'] # Validating The First 6 Characters Of The rollNumber For Only First Year Students.
        count = 0
        while(count <= 5):
            if(listToCheck[count] == rollNumber[count]):
                count+=1
                continue
            else:
                return False
        dupOfRegisteredRollNumbersTillNow = registeredRollNumbersTillNow.registedRollNumbers
        for i in dupOfRegisteredRollNumbersTillNow:
            if rollNumber ==  i:
                return False
            
        # OverWrittingregisteredRollNumbersTillNow
        dupOfRegisteredRollNumbersTillNow.append(rollNumber)
        toOverwriteDupOfRegisteredRollNumbersTillNow = dupOfRegisteredRollNumbersTillNow
        with open('registeredRollNumbersTillNow.py', 'w') as f:
            f.write(f'registedRollNumbers = {toOverwriteDupOfRegisteredRollNumbersTillNow}\n')
        return True
    else:
        return False


def checkIfOnlyLowerAlphabetsArePresentInTheString(string):
    for i in string:
        asciiOfi = ord(i)
        if ((asciiOfi >= 97 and asciiOfi <= 122)):
            continue
        else:
            return False
    return True


def validateBranch(branch):
    if(len(branch) <= 2):
        return False
    else:
        branchesAvailable = "CSE/CSD/CSM/ECE/MECH/CIVIL".split('/') # Add More Branches In The Future If Needed
        branchesInLowerCase = []
        for i in branchesAvailable:
            branchesInLowerCase.append(i.lower())
        for i in branchesInLowerCase:
            if branch == i:
                return True
            else:
                continue
        return False


def validateSection(section):
    if(len(section) != 1):
        return False
    else:
        sectionsAvailable = "A/B/C/D/E/F".split('/') # Add More Sections In The Future If Needed
        sectionsInLowerCase = []
        for i in sectionsAvailable:
            sectionsInLowerCase.append(i.lower())
        for i in sectionsInLowerCase:
            if section == i:
                return True
            else:
                continue
        return False

# Defining The Class For The Collecting The Student Information
class StudentInformation:
    def __init__(self):
        self.name = None
        self.rollNumber = None
        self.branch= None
        self.section = None

    # Student Name
    def takeTheNameOfTheStudent(self):
        self.name = input("Please enter your Full Name (including your surname): ").strip()
        while(validateEnteredName(self.name) != True):
            self.name = input("It's Seems To Be Entered \'Name\' is Not Valid!, So Please Enter Your Full Name Again: ").strip()

    # Student Roll Number
    def takeTheRollNumberOfTheStudent(self):
        self.rollNumber = input("Enter Your Full Roll Number like (24RA1A....): ").strip().lower()
        while(validateRollNumber(self.rollNumber) != True):
            self.rollNumber = input("It's Seems To Be Entered \'Roll Number\' is Not Valid!, So Please Enter Your Full Roll Number Like (24RA1A....) Again: ").strip().lower()


    # Student Branch

    def takeTheBranchOfTheStudent(self):
        self.branch = input("Enter Your Branch (CSE/CSD/CSM/ECE/MECH/CIVIL): ").strip().lower() # Add More Branches In The prompt Section In Future If Needed.
        while(validateBranch(self.branch) != True):
            self.branch = input("It's Seems To Be Entered \'Branch\' is Not Valid!, So Please Enter Your Branch Again: ").strip().lower()

    # Student Section
    def takeTheSectionOfTheStudent(self):
        self.section = input("Enter Your Section (A/B/C/D/E/F): ").strip().lower() # Add More Sections In The prompt Section In Future If Needed.
        while(validateSection(self.section) != True):
            self.section = input("It's Seems To Be Entered \'Section\' is Not Valid!, So Please Enter Your Section Again: ").strip().lower()


def appendFirstResponsesOfTheStudentsToExcel(name,listOfResponsesForEachQuestion):

    # Converting To The DataFrame
    df = pd.DataFrame([listOfResponsesForEachQuestion], columns=[ 'SI.No ','NameOfTheStudent', 'RollNumberOfTheStudent', 'Branch', 'Section', 'ChoosenAuthourName'])
    # Saving to Excel
    excel_filename = f"{name}.xlsx"
    try:
        df.to_excel(excel_filename, index=False, engine='openpyxl')
        return 0
    except Exception as e:
        return -1



def removeTheAuthourFromTheDictionary(key,dictionary):
    del dictionary[key]




def printAvaialbleListofAuthours(tillNowAvailableDictionaryOfAuthours):
    print()
    print()
    print()
    print("These Are The List of Authors Avaiable Right Now!")
    print()
    print("\033[1mCorresponing Code Of The Authour   |  Authour Name\033[0m")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾",end="\n")
    print()
    
    for key, value in tillNowAvailableDictionaryOfAuthours.items():
        if key >= 10 and key <= 99:
            print(key,end = '                                 |  ')
            print(value,end = ".\n\n")
        elif key >= 100:
            print(key,end = '                                |  ')
            print(value,end = ".\n\n")
        else:
            print(key,end = '                                  |  ')
            print(value,end = ".\n\n")
        



listofCodesofAuthours = remainingAuthourCodes.remainingAuthourCode

def checkIfTheStringIsPresentInTheList(string, listOfStrings):
    stringLower = string.lower()
    return any(stringLower == item.lower() for item in listOfStrings)



def validateEnteredAuthourCode(stringTypeOfEnteredAuthourCode):
    
    if stringTypeOfEnteredAuthourCode.isdigit() == False:
        return False
    else:
        intTypeofEnteredAuthourCode = int(stringTypeOfEnteredAuthourCode)
        if intTypeofEnteredAuthourCode <= 0 or intTypeofEnteredAuthourCode > 118:
            return False
        else:
            for i in listofCodesofAuthours:
                if intTypeofEnteredAuthourCode == i:
                    return True
            return False



def chooseTheAuthourCode(prompt): 
    choosenAuthourCode = (input(prompt).strip())
    while (validateEnteredAuthourCode(choosenAuthourCode) != True):
        choosenAuthourCode = input("Entered Author Code Not Found, please try again: ").strip()
    return int(choosenAuthourCode)



student1 = StudentInformation()
# Name
student1.takeTheNameOfTheStudent()
print("Entered Name: ",student1.name)
# Roll Number
student1.takeTheRollNumberOfTheStudent()
print("Entered Roll Number: ",student1.rollNumber)
# Branch
student1.takeTheBranchOfTheStudent()
print("Entered Branch: ",student1.branch)
# Section
student1.takeTheSectionOfTheStudent()
print("Entered Section: ",student1.section)

# Printing Left Over Authours Till Now In The Form Of A Table.
printAvaialbleListofAuthours(availableDictionaryOfAuthours.remainingAuthorsDict)
enteredAuthourCode = chooseTheAuthourCode("So Now, Please Enter The Authour Code On Whom You Want To Give The Seminar: ")
print("Choosen Authour: ", dictionaryofAuthoursForReference[enteredAuthourCode], "and His Correspondoing code: ",enteredAuthourCode)

listOfAllResponsesOfEachStudent  = []
for i in range(1,7):
    listOfAllResponsesOfEachStudent.append(None)

listOfAllResponsesOfEachStudent[0] = siNo.siNo
listOfAllResponsesOfEachStudent[1] = student1.name
listOfAllResponsesOfEachStudent[2] = student1.rollNumber
listOfAllResponsesOfEachStudent[3] = student1.branch
listOfAllResponsesOfEachStudent[4] = student1.section
listOfAllResponsesOfEachStudent[5] = dictionaryofAuthoursForReference[enteredAuthourCode]

# Appending All The Responses Of The Student In The Excel File

excelAppendResult = None
if(siNo.siNo == 1):
    excelAppendResult = appendFirstResponsesOfTheStudentsToExcel("StudentsAuthorsChoosenList",listOfAllResponsesOfEachStudent)
else:
    excelAppendResult = AppendReposesofTheStudentsFromTheSecondRun("StudentsAuthorsChoosenList",listOfAllResponsesOfEachStudent)
if (excelAppendResult == 0):
    print("All Your Responses Has Been Saved In Our DataBase🎊🎉, Yo can Leave! Thank You For Your Patience😊!")
else:
    print("Your Responses Has Not Been Saved In Our DataBase⚠️, So Please Inform To The Professor!")




# OverWrittingTheSiNoInTheEveryRubOfTheProgram
dupOfSiNo = siNo.siNo
dupOfSiNo += 1
with open('siNo.py', 'w') as f:
    f.write(f'siNo = {dupOfSiNo}\n')



# OverWrittingThedictionaryOfAuthours
dupOfauthorsDict = availableDictionaryOfAuthours.remainingAuthorsDict
del dupOfauthorsDict[enteredAuthourCode]
leftoverDictionaryofAuthours = dupOfauthorsDict
with open('availableDictionaryofAuthours.py', 'w') as f:
    f.write(f'remainingAuthorsDict = {leftoverDictionaryofAuthours}\n')


# OverWrittingTheListOfAuthourCodes
dupOfListOfAuthoursCodes = remainingAuthourCodes.remainingAuthourCode
dupOfListOfAuthoursCodes.remove(enteredAuthourCode)
leftoverListofAuthoursCodes = dupOfListOfAuthoursCodes
with open('remainingAuthourCodes.py', 'w') as f:
    f.write(f'remainingAuthourCode = {leftoverListofAuthoursCodes}\n')
