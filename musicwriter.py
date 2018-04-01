from music21 import *
import csv
import sys
import os
import pandas as pd
from collections import defaultdict


<<<<<<< HEAD
def parseStream(s):
=======
def parseStream(filename, s):
    orig_stdout = sys.stdout
    f = open("GoldbergVariationsRawData.csv", 'w')

    sys.stdout = f


>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf
    previousDurations30 = []
    previousChanges24 = []
    phraseStarts = [0]
    noteCounter = 0

    # for filename in os.listdir(path):
    for i in range(1):
        for i in s:
            previousNote = note.Note("C8")

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

            aNote = note.Note('c4')
            if (len(keySig) > 0):
                notestr = keySig[0].lower() + '4'
                bNote = note.Note(notestr)
            intervalo = interval.notesToInterval(bNote, aNote)

            for thisNote in i.notesAndRests.stream():

                if(str(type(thisNote)) == str("<class 'music21.note.Rest'>")):
<<<<<<< HEAD
=======
                    print("R0" + str(thisNote.quarterLength))
>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf
                    noteCounter = noteCounter + 1
                if(str(type(thisNote)) == str("<class 'music21.note.Note'>")):
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
<<<<<<< HEAD
=======
                    #    print(previousChanges24[n-6:])
>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf


                    # Test last 12 notes equal
                    counter = 0
                    if (n > 12 and previousChanges24[n-6:n-1] == previousChanges24[n-12:n-7]):
                        phraseStarts.append(noteCounter - 1)
                        previousChanges24 = []

                    # if (n > 8 and previousChanges24[n-2] == previousChanges24[n-6]):
                    #     if (n > 8 and previousChanges24[n-3] == previousChanges24[n-7]):
                    #         if (n > 8 and previousChanges24[n-4] == previousChanges24[n-8]):
                    #             if (thisNote.quarterLength != 0.25):
<<<<<<< HEAD
=======
                    #                 print("Phrase End 8")
>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf
                    #                 previousChanges24 = []

                    n = len(previousChanges24)
                    if (n > 20 and previousChanges24[n-11:n-1] == previousChanges24[n-21:n-11]):
                        phraseStarts.append(noteCounter - 1)
                        previousChanges24 = []

                    if (n > 24 and previousChanges24[n-11:n-1] == previousChanges24[n-21:n-11]):
                        phraseStarts.append(noteCounter - 1)
                        previousChanges24 = []

<<<<<<< HEAD
                    if (thisNote.quarterLength == 1.0 or thisNote.quarterLength == 2.0):
                        if (previousDurations30[bb-5] == 0.25 and previousDurations30[bb-4] == 0.25 and previousDurations30[bb-3] == 0.25 and previousDurations30[bb-2] == 0.25):
=======
                    print(str(thisNote.pitch) + str(thisNote.quarterLength))
                    if (thisNote.quarterLength == 1.0 or thisNote.quarterLength == 2.0):
                        if (previousDurations30[bb-5] == 0.25 and previousDurations30[bb-4] == 0.25 and previousDurations30[bb-3] == 0.25 and previousDurations30[bb-2] == 0.25):
                            # print("Phrase End quarter after sixteenths")
>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf
                            phraseStarts.append(noteCounter)
                    noteCounter = noteCounter + 1
                    previousNote = thisNote

    sys.stdout = orig_stdout
    return phraseStarts


def build_note_dict(notes):

    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))

    noteList = []
    for key, note in notes.itertuples():
        if note not in note_dict:
            noteList.append(note)
    possible_vals = sorted(set(noteList))
    startIndex = len(note_dict) + 1
    note_dict.update(dict([(note, index + startIndex) for index, note in enumerate(possible_vals)]))

    with open('indexes.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, note in note_dict.items():
            writer.writerow([key, note])

    return note_dict

def convert_notes_to_indexes(notes):

    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))

    noteIndexes = []
    for key, note in notes.itertuples():
        noteIndexes.append(note_dict[note])
    X = zip(noteIndexes[0::1], noteIndexes[2::1])
    Y = noteIndexes[1::1]

    return X, Y

<<<<<<< HEAD
=======



filename = r'988-v01.mid'
phrase_divisions = parseStream(filename)
training_notes = pd.read_csv("GoldbergVariationsRawData.csv", index_col=None)
build_note_dict(training_notes)
convert_notes_to_indexes(training_notes)
>>>>>>> 2c4c91b216a59b129bdc605037edeb3baa1fefcf
