#from PyDictionary import is_word
#from PyDictionary import PyDictionary
from dataclasses import dataclass


# define a data structure of 4 paired sets to hold letters for selection
# one set, used, and another unused.
# whenever we remove an element from the unused set, we add it to the used set
# when we have no more unused letters, we have achieved the win condition
@dataclass
class LetterSet:
    used: set
    unused: set
    is_last_used: bool

    # define __contains__ to check if a letter is in either set
    def __contains__(self, letter):
        return letter in self.used or letter in self.unused

    # define a method to remove a letter from the unused set and add it to the used set
    def remove_letter(self, letter):
        self.used.add(letter)
        self.unused.remove(letter)

#we associate the words with the entire set of associated matches, not the LetterSet instance
class WordSet:
    def __init__(self, characters):
        self.words = []
        self.A = LetterSet(set(), set(characters[0]), False)
        self.B = LetterSet(set(), set(characters[1]), False)
        self.C = LetterSet(set(), set(characters[2]), False)
        self.D = LetterSet(set(), set(characters[3]), False)
    
    def get_unused_letters(self):
        return (self.A.unused if not self.A.is_last_used else set()) | (self.B.unused if not self.B.is_last_used else set()) | (self.C.unused if not self.C.is_last_used else set()) | (self.D.unused if not self.D.is_last_used else set())
    
    def used_letters_to_pick(self):
        return (self.A.used if not self.A.is_last_used else set()) | (self.B.used if not self.B.is_last_used else set()) | (self.C.used if not self.C.is_last_used else set()) | (self.D.used if not self.D.is_last_used else set())
    
    # define a property to get used letters irrespective of the last used set
    @property
    def used_letters(self):
        return self.A.used | self.B.used | self.C.used | self.D.used
    
    def remove_letter(self, letter):
        if letter in self.A:
            if letter in self.A.unused:
                self.A.remove_letter(letter)
            self.A.is_last_used = True
            self.B.is_last_used = False
            self.C.is_last_used = False
            self.D.is_last_used = False
        elif letter in self.B:
            if letter in self.B.unused:
                self.B.remove_letter(letter)
            self.A.is_last_used = False
            self.B.is_last_used = True
            self.C.is_last_used = False
            self.D.is_last_used = False
        elif letter in self.C:
            if letter in self.C.unused:
                self.C.remove_letter(letter)
            self.A.is_last_used = False
            self.B.is_last_used = False
            self.C.is_last_used = True
            self.D.is_last_used = False
        elif letter in self.D:
            if letter in self.D.unused:
                self.D.remove_letter(letter)
            self.A.is_last_used = False
            self.B.is_last_used = False
            self.C.is_last_used = False
            self.D.is_last_used = True
