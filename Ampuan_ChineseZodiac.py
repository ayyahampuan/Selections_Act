#Find chinese zodiac sign.

year = eval(input("Input birth year: "))

#base year is 2000.

if(year - 2000) % 12 == 0:
    zodiac = "Dragon"
elif(year - 2000) % 12 == 1:
    zodiac = "Snake"
elif(year - 2000) % 12 == 2:
    zodiac = "Horse"
elif(year - 2000) % 12 == 3:
    zodiac = "Sheep"
elif(year - 2000) % 12 == 4:
    zodiac = "Monkey"
elif(year - 2000) % 12 == 5:
    zodiac = "Rooster"
elif(year - 2000) % 12 == 6:
    zodiac = "Dog"
elif(year - 2000) % 12 == 7:
    zodiac = "Pig"
elif(year - 2000) % 12 == 8:
    zodiac = "Rat"
elif(year - 2000) % 12 == 9:
    zodiac = "Ox"
elif(year - 2000) % 12 == 10:
    zodiac = "Tiger"
elif(year - 2000) % 12 == 11:
    zodiac = "Rabbit"

print(f"The Chinese Zodiac sign for this is year of the {zodiac}.")
