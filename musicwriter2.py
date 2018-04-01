from music21 import *
import csv
import sys
import os
from collections import defaultdict

for i in range(1):
    previousDurations30 = []
    previousChanges24 = []
    phraseStarts = [0]
    phraseTypes = []
    noteCounter = 0
    path = r'C:\Users\Nick Kim\Downloads\Music'
#Test with multiple things in a row
    for filename in os.listdir(path):
    #for i in range(1):
        # s = converter.parse(r'C:\Users\Nick Kim\Downloads\Music\988-v01.mid')
        s = converter.parse(r'C:\Users\Nick Kim\Downloads\Music\\' + str(filename))

        for i in s:
            previousNote = note.Note("C8")
            currentpLength = 0
            count = 0
            timeSig = ""
            keySig = ""
            for thing in i:
                if (isinstance(thing,key.KeySignature)):
                    keySig = str((thing))
                if (isinstance(thing,meter.TimeSignature)):
                    timeSig = str((thing))
                    count = count + 1
                if (count > 3):
                    break
            num1 = ""
            den1 = ""
            read1 = True
            read2 = False
            for c in timeSig[29:]:
                if (c == ">"):
                    read2 = False
                if (read2):
                    den1 += c
                if (c == "/"):
                    read1 = False
                if (read1):
                    num1 += c
                else:
                    read2 = True

            num1 = float(num1)
            den1 = float(den1)
            breako = num1 * (4.0 / den1)
            aNote = note.Note('c4')
            if (len(keySig) > 0):
                notestr = keySig[0].lower() + '4'
                bNote = note.Note(notestr)
            intervalo = interval.notesToInterval(bNote, aNote)

            phraseStarts.append(noteCounter)
            phraseTypes.append(77)
            currentpLength = 0
            previousChanges24 = []

            for thisNote in i.notesAndRests.stream():

                if(str(type(thisNote)) == str("<class 'music21.note.Rest'>")):
                    print("R0" + str(thisNote.quarterLength))
                    noteCounter = noteCounter + 1
                if(str(type(thisNote)) == str("<class 'music21.note.Note'>")):
                    offseto = thisNote.offset
                    thisNote = interval.transposeNote(thisNote, intervalo)

                    previousDurations30.append(thisNote.quarterLength)
                    previousChanges24.append(str(interval.Interval(thisNote, previousNote))[len(str(interval.Interval(thisNote, previousNote))) - 2])
                    if (len(previousChanges24) > 24):
                        del previousChanges24[0]
                    if (len(previousDurations30) > 30):
                        del previousDurations30[0]
                    n = len(previousChanges24)
                    bb = len(previousDurations30)
                    # if (n > 7):
                    #    print(previousChanges24[n-6:])


                    # Test last 12 notes equal
                    counter = 0
                    if (n > 12 and previousChanges24[n-6:n-1] == previousChanges24[n-12:n-7] and (offseto % breako == 0 or offseto % breako == 1)):
                        phraseStarts.append(noteCounter - 1)
                        phraseTypes.append(1)
                        currentpLength = 0
                        previousChanges24 = []

                    # if (n > 8 and previousChanges24[n-2] == previousChanges24[n-6]):
                    #     if (n > 8 and previousChanges24[n-3] == previousChanges24[n-7]):
                    #         if (n > 8 and previousChanges24[n-4] == previousChanges24[n-8]):
                    #             if (thisNote.quarterLength != 0.25):
                    #                 print("Phrase End 8")
                    #                 previousChanges24 = []

                    n = len(previousChanges24)
                    if (n > 20 and previousChanges24[n-11:n-1] == previousChanges24[n-21:n-11] and (offseto % breako == 0 or offseto % breako == 1)):
                        phraseStarts.append(noteCounter - 1)
                        phraseTypes.append(2)
                        previousChanges24 = []
                        currentpLength = 0


                    print(str(thisNote.pitch) + str(thisNote.quarterLength))

                    if ((thisNote.quarterLength == 1.0) and (offseto % breako == 0 or offseto % breako == 1)):
                        if (len(previousDurations30) > 5 and previousDurations30[bb-5] == 0.25 and previousDurations30[bb-4] == 0.25 and previousDurations30[bb-3] == 0.25 and previousDurations30[bb-2] == 0.25):
                            # print("Phrase End quarter after sixteenths")
                            phraseStarts.append(noteCounter)
                            phraseTypes.append(3)
                            currentpLength = 0
                            previousChanges24 = []

                    if (thisNote.quarterLength >= 2.0):
                        if (len(previousDurations30) > 3 and previousDurations30[bb-2] < 1 and previousDurations30[bb-3] < 1):
                            phraseStarts.append(noteCounter)
                            phraseTypes.append(4)
                            currentpLength = 0
                            previousChanges24 = []

                    if (currentpLength >= 50 and offseto % breako == 0):
                        phraseStarts.append(noteCounter)
                        phraseTypes.append(5)
                        currentpLength = 0
                        previousChanges24 = []

                    noteCounter = noteCounter + 1
                    previousNote = thisNote
                    currentpLength = currentpLength + 1


    sys.stdout = orig_stdout
