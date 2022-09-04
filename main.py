import math
import time

#Race Calculator by Mikshake
#Credits to:
#https://topper64.co.uk/nk/btd6/rounds/regular - resource for finding BTD6 round lengths and etc.

#Gets info about rounds and time

def main():
    print("BTD6 race time calculator")
    print("To get the most accurate seconds elapsed, use a frame by frame feature to find the exact frame when you send all of the rounds.")
    print("For example, if you full send from round 49, take the time (in seconds) from the first frame where 50 appears.")
    print("Input values in order of this: fullsend time, fullsend from what round, fullsend to what round, 'regular' or 'alternate' rounds")
    initialTimeInput, initialRoundInput, longestRoundInput, roundsType = input("Input values:").split()
    timeCalculated = 0

    initialTime = float(initialTimeInput)
    initialRound = int(initialRoundInput)
    longestRound = int(longestRoundInput)

    #Calculating the amount of time in seconds for the race to end, with perfect cleanup
    #checking for bad inputs
    if initialRound >= longestRound:
        print("Please input valid rounds")
        main()

    elif initialTime < 0:
        print("Please input a correct time")
        main()

    else:
    #calculations

        #regular rounds calculations
        if roundsType == "regular":
            if longestRound >= 78:
                timeCalculated = float(90 + (0.2 * (78 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound >= 74:
                timeCalculated = float(82.39 + (0.2 * (74 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound >= 65:
                timeCalculated = float(62 + (0.2 * (65 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound >= 48:
                timeCalculated = float(55.72 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

        #alternate bloons rounds calculations
        elif roundsType == "alternate":
            if longestRound >= 78:
                timeCalculated = float(79.4 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound == 77:
                timeCalculated = float(58.92 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound >= 62:
                timeCalculated = float(48.29 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

            elif longestRound >= 48:
                timeCalculated = float(52 + (0.2 * (48 - (int(initialRound) + 1))) + float(initialTime))

    #another filter for bad inputs
        else:
            print("Please input the rounds type correctly. Use the lowercase words 'regular' and 'alternate' for regular rounds and ABR respectively.")
            main()

    #Converting time in seconds to time in minutes/seconds
    timeCalculated = round(timeCalculated,2)
    timeCalcDecimal = round((round((timeCalculated%1),2))*100)

    if timeCalcDecimal <= 9:
        timeCalcDecimal = str(timeCalcDecimal)
        timeCalcDecimal = "0"+timeCalcDecimal
    else:
        timeCalcDecimal = str(timeCalcDecimal)

    timeCalculated = str(time.strftime("%M:%S", time.gmtime(timeCalculated)))

    print("If you clean perfectly, you will get a time of " + timeCalculated + "." + timeCalcDecimal)

    restart = input("Would you like to calculate another time?").lower()
    if restart == "yes":
       print("")
       main()
    else:
       exit()

main()