from Bingo import *
print("Non-parameterized constructor testing")
for i in range(0, 20):
    a = Bingo()
    a.String_toString()

print("\nParameterized constructor testing")
a1 = Bingo("B", 2)
a2 = Bingo("B", 15)
a3 = Bingo("B", 10)
a4 = Bingo("I", 16)
a5 = Bingo("I", 20)
a6 = Bingo("I", 28)
a7 = Bingo("N", 31)
a8 = Bingo("N", 37)
a9 = Bingo("N", 45)
a10 = Bingo("G", 46)
a11 = Bingo("G", 50)
a12 = Bingo("G", 60)
a13 = Bingo("O", 61)
a14 = Bingo("O", 70)
a15 = Bingo("O", 75)
a1.String_toString()
a2.String_toString()
a3.String_toString()
a4.String_toString()
a5.String_toString()
a6.String_toString()
a7.String_toString()
a8.String_toString()
a9.String_toString()
a10.String_toString()
a11.String_toString()
a12.String_toString()
a13.String_toString()
a14.String_toString()
a15.String_toString()

print("\nIllegal character testing")
b = Bingo("Q")
b.String_toString()
print("\nIllegal number testing")
c = Bingo(89)
c.String_toString()

print("\nUnmatched sets testing")

d1 = Bingo()
d1.setLetter("B")
d1.setNumber(60)
d1.String_toString()

d2 = Bingo()
d2.setLetter("I")
d2.setNumber(10)
d2.String_toString()

d3 = Bingo()
d3.setLetter("N")
d3.setNumber(15)
d3.String_toString()

d4 = Bingo()
d4.setLetter("G")
d4.setNumber(70)
d4.String_toString()

d5 = Bingo()
d5.setLetter("O")
d5.setNumber(1)
d5.String_toString()



