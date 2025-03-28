from typing import List
import string

from ..utils import check_str, check_empty
from .phonetic_algorithm import PhoneticAlgorithm


class NYSIIS(PhoneticAlgorithm):
    """
    The NYSIIS algorithm.

    [Reference]: https://en.wikipedia.org/wiki/New_York_State_Identification_and_Intelligence_System & http://www.dropby.com/NYSIIS.html
    [Authors]: 
    """
    def __init__(self):
        super().__init__()

    # vowel array defined outside of function as not to recreate when used in loops
    __vowels : List[str ]= ["A","E","I","O","U"]

    # Python should have this functionality built in, replacing at an index
    def __replaceAt(self, input : str, index : int, replace : str = "") -> str :
        return input[:index] + replace + input[(len(replace) or 1) + index:]

    def phonetics(self, word : str) -> str | None:
        check_str(word)
        check_empty(word)

        input : str = word

        # fail fast if there isn't an input value to code (code defensively)
        if (input is None or not input) :
            return None
        
        # strip leading and trailing whitespace
        input = input.strip()

        # make input uppercase (wiki algorithm doen't mention this as first step)
        input = input.upper()

        # Step 1.
        if input.startswith("MAC") :
            input = "MCC" + input.removeprefix("MAC")
        elif input.startswith("KN") :
            input = "NN" + input.removeprefix("KN")
        elif input.startswith("K") :
            input = "C" + input.removeprefix("K")
        elif input.startswith("PH") :
            input = "FF" + input.removeprefix("PH")
        elif input.startswith("PF") :
            input = "FF" + input.removeprefix("PF")
        elif input.startswith("SCH") :
            input = "SSS" + input.removeprefix("SCH")

        # Step 2.
        if input.endswith("EE") :
            input = input.removesuffix("EE") + "Y"
        elif input.endswith("IE") :
            input = input.removesuffix("IE") + "Y"
        for item in ["DT","RT","RD","NT","ND"] :
            if input.endswith(item) :
                input = input.removesuffix(item) + "D"

        # Steps 3-4.
        idx : int = 1

        while idx < len(input) :
    
            # Step 5. (1)
            # only process letters, skip all other characters including spaces
            if input[idx] not in string.ascii_letters : 
                input = self.self.__replaceAt(input,idx)
                # keeps current index and restarts
                continue

            # Step 5. (2)
            if input[idx] in self.__vowels :
                if input[idx:idx+2] == "EV" :
                    input = self.__replaceAt(input,idx,"EV")
                else :
                    input = self.__replaceAt(input,idx,"A")

            # Step 5. (3)
            elif input[idx] == "Q" :
                input = self.__replaceAt(input,idx,"G")
            elif input[idx] == "Z" :
                input = self.__replaceAt(input,idx,"S")
            elif input[idx] == "M" :
                input = self.__replaceAt(input,idx,"N")

            # Step 5. (4)
            elif input[idx:idx+2] == "KN" :
                input = self.__replaceAt(input,idx,"N")
            elif input[idx] ==  "K" :
                input = self.__replaceAt(input,idx,"C")

            # Step 5. (5)
            elif input[idx:idx+2] == "PH" :
                input = self.__replaceAt(input,idx,"FF")

            # Step 5. (6)
            elif input[idx] == "H" and (input[idx - 1] not in self.__vowels or input[idx:idx+1] not in self.__vowels) :
                input = self.__replaceAt(input,idx,input[idx - 1])

            # Step 5. (7)
            elif input[idx] == "W" and input[idx - 1]  in self.__vowels :
                input = self.__replaceAt(input,idx,input[idx - 1])

            # Step 6.
            if input[idx] == input[idx - 1] :
                input = self.__replaceAt(input,idx,"")
                continue
                
            idx += 1

        # Step 7.
        if input.endswith("S") :
            input = input.removesuffix("S")
        
        # Step 8.
        if input.endswith("AY") :
            input = self.__replaceAt(input,idx,"AY") + "Y"

        # Step 9.
        if input.endswith("A") :
            input = input.removesuffix("A")
        
        # Step 10. Ensure the output includes at minimum the first letter of the input
        if len(input) < 1:
            input = word[0].upper()

        return input[0:6] + f'[{input[6:]}]' if len(input) > 6 else input
