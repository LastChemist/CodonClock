"""
    This python file is created for codon clock project.
    Desceription:
        Codon clock is a new featured digital clock with taste of biology
    
    *** This code is not completly refactored, Thus some comments might be missing. ***
        
    for more information and documantation refer to https://www.github.io/@ilaitayad3h/CodonCock
"""
from datetime import datetime as dt
from os import system
from time import sleep

# index tables
leftOrganicBase = [49, 33, 17, 1]
middleOrganicBase = [11, 7, 3, -1]
rightOrganicBase = [4, 3, 2, 1]


def CodonToIndex(codonInput: str):
    """
    Summary:
        converts codon input into the corresponding number.
    Args:
        codonInput (str): codons from UUU to GGG are acceed

    Returns:
        int: returns corresponding number to the codon.

    Example:
        codonInput = GGC, return = 62
    """
    codonIndexes = [
        leftOrganicBase,
        middleOrganicBase,
        rightOrganicBase,
    ]  # for short and fast access
    organicBaseIndexes = {"U": 0, "C": 1, "A": 2, "G": 3}
    IndexOutPut = 0
    for i in range(3):  # traces the string and extracts the charachter value.
        IndexOutPut += int(codonIndexes[i][organicBaseIndexes[codonInput[i]]])
    return IndexOutPut


def IndexToCodon(indexInput: int):
    """
    Summary:
      converts codon input into the corresponding number.

    Args:
        indexInput (int): an int in interval 0, 64

    Returns:
        str: retruns the corresponding codon to the number.
    """
    if indexInput == 0:
        return 0  # I didn't defined a certain Codon for number 0.
    
    codonDictionary = {0: "G", 1: "A", 2: "C", 3: "U"}
    
    # exceptionIndexes = [4, 8, 12, 20, 24, 28, 36, 40, 44, 52, 56, 60]
    exceptionsDict = {
        4: "UUG",
        8: "UCG",
        12: "UAG",
        20: "CUG",
        24: "CCG",
        28: "CAG",
        36: "AUG",
        40: "ACG",
        44: "AAG",
        52: "GUG",
        56: "GCG",
        60: "GAG",
    }
    exceptionIndexes = list(exceptionsDict.keys())
    initialIndex = indexInput
    codonOutPut = ""  # in each following loops one charachter appends to this string.
    
    for exceptionStepper in range(
        len(exceptionIndexes)
    ):  # if the value was an exception program uses this value to return the answer
        if initialIndex == exceptionIndexes[exceptionStepper]:
            return exceptionsDict[initialIndex]
        else:
            continue

    for leftBaseStepper in leftOrganicBase:
        if indexInput >= int(leftBaseStepper):
            indexInput -= int(leftBaseStepper)
            codonOutPut += str(leftBaseStepper)
            break

    for middleBaseStepper in rightOrganicBase:
        if indexInput >= int(middleBaseStepper):
            indexInput -= int(middleBaseStepper)
            codonOutPut += str(middleBaseStepper)
            break

    for rightBaseStepper in rightOrganicBase:
        if indexInput >= int(rightBaseStepper):
            indexInput -= int(rightBaseStepper)
            codonOutPut += str(rightBaseStepper)
            break
        elif indexInput == 0:
            codonOutPut += codonDictionary[3]
            break
    return codonOutPut


#


def MomentCodonClock():  # Shows system time in codon format
    print(
        f"{IndexToCodon(dt.now().hour)}:{IndexToCodon(dt.now().minute)}:{IndexToCodon(dt.now().second)}"
    )


def MomentNumeralClock():  # Shows system time in ordinary format.
    print(f"{dt.now().hour}:{dt.now().minute}:{dt.now().second}")


def MultiClock():  # shows both codon clock and ordinary digital clock.
    while True:
        MomentCodonClock()
        MomentNumeralClock()
        sleep(1)
        system("cls")


# end of code :)


MultiClock()
