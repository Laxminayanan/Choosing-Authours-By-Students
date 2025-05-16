def validateEnteredName(enteredName):
    if (len(enteredName) == 0):
        return False
    elif (checkForMoreThanOneSpace(enteredName) == False):
        return False
    elif (checkIfOnlyAlphabetsOrSpaceArePresentInTheString(enteredName) == False):
        return False
    else:
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

# Defing The Class For The Collecting The Student Information
class StudentInformation:
    def __init__(self):
        self.name = None
        self.rollNumber = None
        self.branch= None
        self.section = None

    # Student Name
    def takeTheNameOfTheStudent(self):
        self.name = input("Enter Your Name: ").strip()
        while(validateEnteredName(self.name) != True):
            self.name = input("It's Seems To Be Entered \'Name\' is Not Valid!, So Please Enter Your Name Again: ").strip()

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




if __name__ == "__main__":
    #  Creating The Instance/Object of The Class
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

