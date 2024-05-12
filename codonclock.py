"""
    File name : CodonClock.py
    Creation date : 2024/05/12 (Sunday May 12)
    Creator : Last Chemist
    GitHub : https://github.com/LastChemist
    License : Apache-2.0 license (https://www.apache.org/licenses/LICENSE-2.0)

    Note : This Python file has been refactored from a previous version.

    Description : 
        For more information, visit https://github.com/LastChemist/CodonClock

        This project aims to build a clock with base64 integer numbers using their corresponding mRNA codons.

        Method Conventions : 
            [1] - Number zero is considered as OOO
            [2] - The valid number interval is [UUU, GGG]
            [3] - There are 12 exceptions for converting numbers into codons that have been handled
            [4] - In the code, the word "index" and its abbreviation are considered as "number",
                  please don't confuse it with "index" in computer science and programming.
        
        Program Structure:
            [1] - The program is separated into 2 different classes: Utilities and Driver
            [2] - Class Utilities can be used for other purposes
            [3] - Class Driver uses the Utilities methods to perform a clock structure

        Further info : 
            Utilities :
                [1] - This class contains functions to convert base64 numbers into codons and vice versa.
                [2] - Note that this program does not support values higher than 64.
"""

from datetime import datetime as dt
from os import system
from time import sleep


class Utilities:
    def __init__(self) -> None:
        # defining indexes

        self.index_left_nucleotide: list[int] = [49, 33, 17, 1]
        self.index_middle_nucleotide: list[int] = [11, 7, 3, -1]
        self.index_right_nucleotide: list[int] = [4, 3, 2, 1]

        # defining codon possibility list

        self.codon_indexes: list[list[int]] = [
            self.index_left_nucleotide,
            self.index_middle_nucleotide,
            self.index_right_nucleotide,
        ]

        self.codon_indexes_reversed: list[list[int]] = [
            self.index_left_nucleotide[::-1],
            self.index_middle_nucleotide[::-1],
            self.index_right_nucleotide[::-1],
        ]

        # defining nucleotides symbol index

        self.index_nucleotide_symbol: dict = {"U": 0, "C": 1, "A": 2, "G": 3}
        self.index_nucleotide_symbol_reversed: dict = {0: "G", 1: "A", 2: "C", 3: "U"}

        # the method fails on the following indexes and to handle it just skip when see these and return the
        # corresponding Codon.

        self.exception_indexes_dict: dict = {
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

        self.exception_indexes_list = list(self.exception_indexes_dict.keys())

    def Codon2Index(self, inputCodon: str):
        """
        Summary:
            Converts input codon into its corresponding number.
        Args:
            inputCodon (str): Codons from UUU to GGG are accepted

        Returns:
            int: Returns corresponding number to the codon.

        Example:
            inputCodon = GGC, return = 62
        """
        index_output: int = 0
        for i in range(3):
            index_output += int(
                self.codon_indexes_reversed[i][self.index_nucleotide_symbol[inputCodon[i]]]
            )
        return index_output

    def Index2Codon(self, inputIndex: int):
        """
        Summary:
        Converts input index into the corresponding codon.

        Args:
            inputIndex (int): An int in interval 0, 64

        Returns:
            str: Returns the corresponding codon to the number.
        """
        if inputIndex == 0:
            return "OOO"

        initial_index: int = inputIndex
        codon_output: str = ""

        for exception_tracker in self.exception_indexes_list:
            if initial_index == exception_tracker:
                return self.exception_indexes_dict[initial_index]

        for codon_index_list_stepper in self.codon_indexes:
            for _, nucleotide_stepper in enumerate(codon_index_list_stepper):
                if inputIndex >= int(nucleotide_stepper):
                    inputIndex -= int(nucleotide_stepper)
                    codon_output += str(self.index_nucleotide_symbol_reversed[_])
                    break
                elif inputIndex == 0:
                    codon_output += self.index_nucleotide_symbol_reversed[3]
                    break
        return codon_output


class Driver:
    def __init__(self) -> None:
        self.util = Utilities()

    def MomentCodonClock(self):
        print(
            "{0}:{1}:{2}".format(
                self.util.Index2Codon(dt.now().hour),
                self.util.Index2Codon(dt.now().minute),
                self.util.Index2Codon(dt.now().second),
            )
        )

    def MomentNumericalClock(self):
        print(
            "{0}:{1}:{2}".format(
                dt.now().hour,
                dt.now().minute,
                dt.now().second,
            )
        )

    def MultiClock(self):
        while True:
            self.MomentCodonClock()
            self.MomentNumericalClock()
            sleep(1)
            system("cls")


Driver().MultiClock()
