global constantFirst8CharactersofCSEBranch
constantFirst8CharactersofCSEBranch = "24RA1A05"
def returnTheRollNumbers(startSeries,startNumber,endSeries,endNumber):
    listOfRollNumbers = []  # CSE - C Roll Numbers Starts From 24RA1A05D6 to 24RA1A05J2, CSE - D Roll Numbers Starts From 24RA1A05J3 to 24RA1AP6 and similarly CSE - E Roll Numbers Starts From 24RA1A05P7 to 24RA1A05W0.
    currentSeries = startSeries
    NumberOfStudentsInTheClass = 64
    count = 0
    while(True):
        i = 0
        while(i <= 9):
            if(currentSeries == startSeries):
                if (i >= startNumber):
                    listOfRollNumbers.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                    count+=1
                else:
                    i+=1
                    continue
            elif(currentSeries  == endSeries):
                if(i <= endNumber):
                    listOfRollNumbers.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                    count+=1
            else:
                listOfRollNumbers.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                count+=1
            i+=1
        ordOfCurrentSeries = ord(currentSeries)
        currentSeries = chr(ordOfCurrentSeries + 1)
        if count == NumberOfStudentsInTheClass:
            break
    return listOfRollNumbers
    
def rollNumbersGeneratorBasedOnSection(section,startSeries = None,startNumber = 0,endSeries = None,endNumber = 0):
    if (section.lower() == 'c' or section.lower() == 'd' or section.lower() == 'e'):
        startSeries = startSeries.upper()
        endSeries = endSeries.upper()
        if(section.lower() == 'c'):
            rollNumbersOfCSection = returnTheRollNumbers(startSeries,startNumber,endSeries,endNumber)
            return rollNumbersOfCSection   
        elif(section.lower() == 'd'):
            rollNumbersOfDSection = returnTheRollNumbers(startSeries,startNumber,endSeries,endNumber)
            return rollNumbersOfDSection
        else:
            rollNumbersOfESection = returnTheRollNumbers(startSeries,startNumber,endSeries,endNumber)
            return rollNumbersOfESection

    elif(section.lower() == 'f'):
        rollNumbersOfFsection = []
        currentSeries = startSeries
        flag = True 
        while(flag):
            i = 0
            while(i <= 9):
                if(currentSeries == startSeries):
                    if (i >= startNumber):
                        rollNumbersOfFsection.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                    else:
                        i+=1
                        continue
                elif(currentSeries  == "Z"):
                    if(i < 9):
                        rollNumbersOfFsection.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                    else:
                        rollNumbersOfFsection.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                        flag = False
                        break
                else:
                    rollNumbersOfFsection.append(constantFirst8CharactersofCSEBranch + currentSeries + str(i))
                i+=1
            ordOfCurrentSeries = ord(currentSeries)
            currentSeries = chr(ordOfCurrentSeries + 1)
        againStartWith = 'A'
        for i in range(65, 88): # F Section Only has 62 Students So , That is The Reason of The Roll Numbers Range => 24RA1A05W1 to 24RA1A05AW.
            toAppendRollNumber = constantFirst8CharactersofCSEBranch + 'A' + chr(i)
            rollNumbersOfFsection.append(toAppendRollNumber)
        return rollNumbersOfFsection
    elif(section.lower() == 'a'):
        rollNumbersOfAsection = []
        for i in range(1,64 + 1): # CSE - A Has 64 Students and i.e., From 24RA1A0501 to 24RA1A0564
            if i < 10:
                rollNumbersOfAsection.append(constantFirst8CharactersofCSEBranch + '0' + str(i))
            else:
                rollNumbersOfAsection.append(constantFirst8CharactersofCSEBranch + str(i))
        return rollNumbersOfAsection
    else:
        print(f"Currently Roll Numbers for Section {section} is Not Generatable!")        
if __name__ == "__main__":
    
    # At Present I Only Need The Roll Numbers of The CSE - E and CSE - C.
    
    # rollNumbersOfASectionList = rollNumbersGeneratorBasedOnSection("A")
    rollNumbersOfCSectionList = rollNumbersGeneratorBasedOnSection("C",'C',9,'J',2)
    # rollNumbersOfDSectionList = rollNumbersGeneratorBasedOnSection("D",'J',3,'P',6)
    rollNumbersOfESectionList = rollNumbersGeneratorBasedOnSection("E",'P',7,'W',0)
    # rollNumbersOfFSectionList = rollNumbersGeneratorBasedOnSection("F",'W',1)
    
    print("\n\n\n\n")
    
    # print("A section Roll Numbers List: ")
    # print(rollNumbersOfASectionList,end = '\n\n\n\n\n') 
    print("C section Roll Numbers List: ")
    print(rollNumbersOfCSectionList,end = '\n\n\n\n\n')
    # print("D section Roll Numbers List: ")
    # print(rollNumbersOfDSectionList,end = '\n\n\n\n\n')
    print("E section Roll Numbers List: ")
    print(rollNumbersOfESectionList,end = '\n\n\n\n\n') 
    # print("F section Roll Numbers List: ")
    # print(rollNumbersOfFSectionList,end = '\n\n\n\n\n') 
    
    