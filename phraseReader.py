from music21 import *
import csv
import sys
import os
from collections import defaultdict


# Returns a value 1, 2, 3, 4, or 5 depending on the phrase identified
def phraseReader(notees):
    phraseDefinition = 0
    previousDurations30 = []
    previousChanges24 = []
    noteCounter = 0
    currentpLength = 0
    previousNote = note.Note('c8')
    n = len(previousChanges24)
    bb = len(previousDurations30)
    for thisNote in notees:
        if(str(type(thisNote)) == str("<class 'music21.note.Rest'>")):
            noteCounter = noteCounter + 1
        if(str(type(thisNote)) == str("<class 'music21.note.Note'>")):
            offseto = thisNote.offset
            previousDurations30.append(thisNote.quarterLength)
            previousChanges24.append(str(interval.Interval(thisNote, previousNote))[len(str(interval.Interval(thisNote, previousNote))) - 2])
            if (len(previousChanges24) > 24):
                del previousChanges24[0]
            if (len(previousDurations30) > 30):
                del previousDurations30[0]


            if (n > 12 and previousChanges24[n-6:n-1] == previousChanges24[n-12:n-7]):
                phraseDefinition = 1
                currentpLength = 0
                previousChanges24 = []
            n = len(previousChanges24)

            if (n > 20 and previousChanges24[n-11:n-1] == previousChanges24[n-21:n-11]):
                currentpLength = 0
                previousChanges24 = []
                phraseDefinition = 2

            if ((thisNote.quarterLength == 1.0)):
                if (len(previousDurations30) > 5 and previousDurations30[bb-5] == 0.25 and previousDurations30[bb-4] == 0.25 and previousDurations30[bb-3] == 0.25 and previousDurations30[bb-2] == 0.25):
                    # print("Phrase End quarter after sixteenths")
                    currentpLength = 0
                    phraseDefinition = 3

            if (thisNote.quarterLength >= 2.0):
                if (len(previousDurations30) > 3 and previousDurations30[bb-2] < 1 and previousDurations30[bb-3] < 1):
                    phraseDefinition = 4
                    currentpLength = 0
                    previousChanges24 = []

            if (phraseDefinition == 0):
                phraseDefinition = 5



        noteCounter = noteCounter + 1
        previousNote = thisNote
        currentpLength = currentpLength + 1
    return phraseDefinition
