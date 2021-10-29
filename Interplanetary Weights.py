# Prompt/input for your name ? - string
# Prompt/input for your age? - float
# Earth Weight * Surface Gravity Factor

# Our weight on our Solar System's Planets Calculator
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066
 
#1. Prompt/Input:
sMyName = input("What is your name?: ")
fWeight = float(input("What is your weight?: ") )

#2. Calculate:
fWeight1 = fWeight * nMERCURY
fWeight2 = fWeight * nVENUS
fWeight3 = fWeight * nMOON
fWeight4 = fWeight * nMARS
fWeight5 = fWeight * nJUPITER
fWeight6 = fWeight * nSATURN
fWeight7 = fWeight * nURANUS
fWeight8 = fWeight * nNEPTUNE
fWeight9 = fWeight * nPLUTO


#3. Output:
print(sMyName, "here are your weights on our Solar System's planets")
print(format("Weight on Mercury:","25s"),format(fWeight1,'10.2f') )
print(format("Weight on Venus:","25s"),format(fWeight2,'10.2f') )
print(format("Weight on Moon:","25s"),format(fWeight3,'10.2f') )
print(format("Weight on Mars:","25s"),format(fWeight4,'10.2f') )
print(format("Weight on Jupiter:","25s"),format(fWeight5,'10.2f') )
print(format("Weight on Saturn:","25s"),format(fWeight6,'10.2f') )
print(format("Weight on Uranus:","25s"),format(fWeight7,'10.2f') )
print(format("Weight on Neptune:","25s"),format(fWeight8,'10.2f') )
print(format("Weight on Pluto:","25s"),format(fWeight9,'10.2f') )


