from music21 import *
import csv
import sys
import os

orig_stdout = sys.stdout
f = open('GoldbergFirstOneHundred.csv', 'w')

sys.stdout = f


previousDurations30 = []
previousChanges24 = []
phraseStarts = [0.0]
noteCounter = 0


path = r'C:\Users\Nick Kim\Downloads\Music'
print('Notes')
# for filename in os.listdir(path):
for i in range(1):
    # s = converter.parse(r'C:\Users\Nick Kim\Downloads\Music\\' + filename)
    s = converter.parse(r'C:\Users\Nick Kim\Downloads\Music\988-v01.mid')
    for i in s:
        previousNote = note.Note("C8")
        # stream2 = i
        # for thing in i.notesAndRests.stream():
        #     print(thing)
        #     print(type(thing))
        #     if(str(type(thing)) == str("<class 'music21.note.Note'>")):
        #         print("THIS IS A NOTE INDEED")
        #     if(str(type(thing)) == str("<class 'music21.note.Rest'>")):
        #         print("THIS IS A REST")
    # FIGURE OUT TYPE EQUIVALENCE AND THINGS
        for thisNote in i.getElementsByClass(note.Note):
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
            if (n > 12 and previousChanges24[n-2] == previousChanges24[n-8]):
                if (n > 12 and previousChanges24[n-3] == previousChanges24[n-9]):
                    if (n > 12 and previousChanges24[n-4] == previousChanges24[n-10]):
                        if (n > 12 and previousChanges24[n-5] == previousChanges24[n-11]):
                            if (n > 12 and previousChanges24[n-6] == previousChanges24[n-12]):
                                #print("Phrase End 6")
                                phraseStarts.append(noteCounter)
                                previousChanges24 = []
            n = len(previousChanges24)

            # if (n > 8 and previousChanges24[n-2] == previousChanges24[n-6]):
            #     if (n > 8 and previousChanges24[n-3] == previousChanges24[n-7]):
            #         if (n > 8 and previousChanges24[n-4] == previousChanges24[n-8]):
            #             if (thisNote.quarterLength != 0.25):
            #                 print("Phrase End 8")
            #                 previousChanges24 = []

            n = len(previousChanges24)
            if (n > 20 and previousChanges24[n-2] == previousChanges24[n-12]):
                if (n > 20 and previousChanges24[n-3] == previousChanges24[n-13]):
                    if (n > 20 and previousChanges24[n-4] == previousChanges24[n-14]):
                        if (n > 20 and previousChanges24[n-5] == previousChanges24[n-15]):
                            if (n > 20 and previousChanges24[n-6] == previousChanges24[n-16]):
                                if (n > 20 and previousChanges24[n-7] == previousChanges24[n-17]):
                                    if (n > 20 and previousChanges24[n-8] == previousChanges24[n-18]):
                                        if (n > 20 and previousChanges24[n-9] == previousChanges24[n-19]):
                                            if (n > 20 and previousChanges24[n-10] == previousChanges24[n-20]):
                                                if (n > 20 and previousChanges24[n-11] == previousChanges24[n-21]):
                                                    # print("Phrase End 10")
                                                    phraseStarts.append(noteCounter)
                                                    previousChanges24 = []

            if (n > 24 and previousChanges24[n-2] == previousChanges24[n-12]):
                if (n > 20 and previousChanges24[n-3] == previousChanges24[n-13]):
                    if (n > 20 and previousChanges24[n-4] == previousChanges24[n-14]):
                        if (n > 20 and previousChanges24[n-5] == previousChanges24[n-15]):
                            if (n > 20 and previousChanges24[n-6] == previousChanges24[n-16]):
                                if (n > 20 and previousChanges24[n-7] == previousChanges24[n-17]):
                                    if (n > 20 and previousChanges24[n-8] == previousChanges24[n-18]):
                                        if (n > 20 and previousChanges24[n-9] == previousChanges24[n-19]):
                                            if (n > 20 and previousChanges24[n-10] == previousChanges24[n-20]):
                                                if (n > 20 and previousChanges24[n-11] == previousChanges24[n-21]):
                                                    # print("Phrase End 12")
                                                    phraseStarts.append(noteCounter)
                                                    previousChanges24 = []

            print(str(thisNote.pitch) + str(thisNote.quarterLength))
            if (thisNote.quarterLength == 1.0 or thisNote.quarterLength == 2.0):
                if (previousDurations30[bb-5] == 0.25 and previousDurations30[bb-4] == 0.25 and previousDurations30[bb-3] == 0.25 and previousDurations30[bb-2] == 0.25):
                    # print("Phrase End quarter after sixteenths")
                    phraseStarts.append(noteCounter)
            noteCounter = noteCounter + 1
            previousNote = thisNote
