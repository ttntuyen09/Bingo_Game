import random
class Bingo:
    lst = ["B", "I", "N", "G", "O"]

    def __init__(self, ltr=None, num=None):
       if ltr == "B" and num in range(1, 16):
           self.letter = ltr
           self.number = num
       elif ltr == "I" and num in range(16, 31):
           self.letter = ltr
           self.number = num
       elif ltr == "N" and num in range(31, 46):
           self.letter = ltr
           self.number = num
       elif ltr == "G" and num in range(46, 61):
           self.letter = ltr
           self.number = num
       elif ltr == "O" and num in range(61, 76):
           self.letter = ltr
           self.number = num
       elif num is None and ltr is not None:
           if str(ltr).isdigit():
               self.character = "FREE"
           else:
               self.character = "N"
       elif num is None and ltr is None:
           self.letter = self.lst[random.randint(0, 4)]
           if self.letter == "B":
               self.number = random.randint(1, 16)
           elif self.letter == "I":
               self.number = random.randint(16, 31)
           elif self.letter == "N":
               self.number = random.randint(31, 46)
           elif self.letter == "G":
               self.number = random.randint(46, 61)
           elif self.letter == "O":
               self.number = random.randint(61, 76)
       else:
           self.letter = "N"
           self.number = "FREE"


    def setNumber(self, n):
        if self.letter == "B" and n in range(1, 16):
            self.number = n
        elif self.letter == "I" and n in range(16, 31):
            self.number = n
        elif self.letter == "N" and n in range(31, 46):
            self.number = n
        elif self.letter == "G" and n in range(46, 61):
            self.number = n
        elif self.letter == "O" and n in range(61, 76):
            self.number = n
        else:
            self.number = "FREE"
            self.letter = "N"

    def setLetter(self, l):
        self.letter = l


    def String_toString(self):
        if hasattr(self, "letter") and hasattr(self, "number"):
            print(self.letter + ",", self.number)
        elif hasattr(self, "character"):
            print(self.character)















