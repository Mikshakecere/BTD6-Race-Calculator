import time

#Race Calculator by Mikshake BTD6
#Credits to:
#https://topper64.co.uk/nk/btd6/rounds/regular - resource for finding BTD6 round lengths and etc.
#Also credit to tobi bot for race calculator idea (and also for having no rrtime)
def rtimeCalc(roundsType, longestRound, initialRound, initialTime):
    if roundsType == "regular":
        if longestRound >= 78:
            return float(90 + (0.2 * (78 - (int(initialRound) + 1))) + float(initialTime))

        elif longestRound >= 74:
            return float(82.39 + (0.2 * (74 - (int(initialRound) + 1))) + float(initialTime))

        elif longestRound >= 65:
            return float(62 + (0.2 * (65 - (int(initialRound) + 1))) + float(initialTime))

        elif longestRound >= 48:
            return float(55.72 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

    # alternate bloons rounds calculations
    elif roundsType == "alternate":
        if longestRound >= 78:
            return float(79.4 + (0.2 * (78 - (int(initialRound) + 1))) + float(initialTime))

        elif longestRound == 77:
            return float(58.92 + (0.2 * (77 - (int(initialRound) + 1))) + float(initialTime))

        elif longestRound >= 48:
            return float(52 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

    # another filter for bad inputs
    else:
        print("Please input the rounds type correctly. Use the lowercase words 'regular' and 'alternate' for regular rounds and ABR respectively.")
        rtime()

def rrtimeCalc(roundsType, longestRound, winningTime, initialRound):
    if roundsType == "regular":
        if longestRound >= 78:
            return float(winningTime - 90 - (0.2 * (78 - (int(initialRound) + 1))))
        elif longestRound >= 74:
            return float(winningTime - 82.39 - (0.2 * (74 - (int(initialRound) + 1))))
        elif longestRound >= 65:
            return float(winningTime - 62 - (0.2 * (65 - (int(initialRound) + 1))))
        elif longestRound >= 48:
            return float(winningTime - 55.72 - (0.2 * (48 - (int(initialRound) + 1))))
    # alternate bloons rounds calculations
    elif roundsType == "alternate":
        if longestRound >= 78:
            return float(winningTime - 79.4 - (0.2 * (78 - (int(initialRound) + 1))))
        elif longestRound == 77:
            return float(winningTime - 58.92 - (0.2 * (77 - (int(initialRound) + 1))))
        elif longestRound >= 48:
            return float(winningTime - 52 - (0.2 * (48 - (int(initialRound) + 1))))
    else:
        print("Please input the rounds type correctly. Use the lowercase words 'regular' and 'alternate' for regular rounds and ABR respectively.")
        rrtime()

def timeInMS(winningTimeInput):
    winCalculated = float(winningTimeInput)
    winCalculated = round(winCalculated, 2)
    winCalcDecimal = round((round((winCalculated % 1), 2)) * 100)

    if winCalcDecimal <= 9:
        winCalcDecimal = str(winCalcDecimal)
        winCalcDecimal = "0" + winCalcDecimal
    else:
        winCalcDecimal = str(winCalcDecimal)

    return str(time.strftime("%M:%S", time.gmtime(winCalculated))) + "." + str(winCalcDecimal)

#Gets info about rounds and time
def rtime():
    print("BTD6 race time calculator")
    print("Input values in order of this: ")
    print("fullsend time, fullsend from what round, fullsend to what round, 'regular' or 'alternate' rounds")
    initialTimeInput, initialRoundInput, longestRoundInput, roundsType = input("Input values:").split()
    timeCalculated = 0
    initialTime = float(initialTimeInput)
    initialRound = int(initialRoundInput)
    longestRound = int(longestRoundInput)

    # Calculating the amount of time in seconds for the race to end, with perfect cleanup
    # checking for bad inputs
    # apparently min time breaks it a bit, so ima fix it rq
    if initialTime == 0:
        initialTime = 0.2

    if initialRound >= longestRound:
        print("Please input valid rounds")
        rtime()

    elif initialTime < 0:
        print("Please input a correct time")
        rtime()

    else:
        # calculations
        timeCalculated = rtimeCalc(roundsType, longestRound, initialRound, initialTime)

    # 60.6 if you send from 80
    timeLeft = timeCalculated - 60.6

    timeCalculated = timeInMS(timeCalculated)
    timeLeft = timeInMS(timeLeft)

    print("If you clean perfectly, you will get a time of " + timeCalculated)
    if(longestRound >= 83):
        print("Also you have until " + timeLeft + " to send for r83")

    restart = input("Would you like to calculate another time?").lower()
    if restart == "yes":
        print("")
        rtime()
    else:
        main()

def rrtime():
    print("BTD6 reverse race time calculator")
    print("Input values in order of this: ")
    print("winning time, fullsend from what round, fullsend to what round, 'regular' or 'alternate' rounds")
    winningTimeInput, initialRoundInput, longestRoundInput, roundsType = input("Input values:").split()

    fullsend = 0
    winningTime = float(winningTimeInput)
    initialRound = int(initialRoundInput)
    longestRound = int(longestRoundInput)

    # Calculating the amount of time in seconds for the race to end, with perfect cleanup
    # checking for bad inputs
    # apparently min time breaks it a bit, so ima fix it rq
    #calculate the min time and see if it equals, then you can basically skip the whole program
    if initialRound >= longestRound:
        print("Please input valid rounds")
        rrtime()

    else:
        # calculations
        # regular rounds calculations
        fullsend = rrtimeCalc(roundsType, longestRound, winningTime, initialRound)

    # converts winning time input into ms format
    winCalculated = timeInMS(winningTimeInput)
    fullsendMS = timeInMS(fullsend)

    #try including a calculation for inputting win time lower than min time

    print("To end with a time of " + winCalculated + ", you would need to start fullsending at " + fullsendMS)

    restart = input("Would you like to calculate another time?").lower()
    if restart == "yes":
        print("")
        rrtime()
    else:
        main()

def main():
    time = input("Calculate from when to fullsend? '1' for Yes or '0' for No ")
    try:
        time = bool(int(time))
        if(time):
            rrtime()
        else:
            rtime()
    except TypeError or ValueError:
        #not true or false exception handler
        print("pls put valid boolean")
        main()

main()