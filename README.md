# CodonClock
A new featured digital clock with taste of biology

# For persian guys you can see https://vrgl.ir/70E4O and https://vrgl.ir/3ku41 for some crude documents.
# Preview 

![alt GUI version (written with C#)](https://files.virgool.io/upload/users/472403/posts/fatwu01a3frt/aoobxfvhkeif.gif)\
GUI (with c#)

![alt console version (python 3)](https://files.virgool.io/upload/users/472403/posts/fatwu01a3frt/wktyyn8jr0zb.gif)\
console (with python)

Compeleted documentation will be available.

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
