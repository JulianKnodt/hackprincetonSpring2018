from music21 import *
import csv
import sys
import os
import numpy as np

def convert_generated_to_indexes(generated):
    notes_int = []
    nz = np.sort(np.transpose(np.nonzero(generated)),axis=0,)
    for row in nz:
      notes_int += [row[0]]
    return notes_int

test = np.ceil(np.random.rand(4,4))
print(test)
print(convert_generated_to_indexes(test))

def convert_int_to_string(ints):
    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))
    note_dict_reversed = dict((intVal, note) for note, intVal in note_dict.items())

    string_reps = []
    for i in ints:
        string_reps += [note_dict_reversed[str(i+1)]]

    return string_reps



def read_to_midi(generated, fileName):
    streamstream = stream.Stream()
    strings = convert_int_to_string(convert_generated_to_indexes(generated))
    for row in strings:
        counter = 0
        nPitch = str(row)[counter]
        counter = counter+1
        nPitch += str(row)[counter]
        if (str(row)[1] == '#' or str(row)[1] == '-'):
            counter = counter+1
            nPitch += str(row)[counter]
        nDuration = ''
        counter = counter+1

        for c in str(row)[counter:]:
            if (c != "'" and c != "]"):
                nDuration += c
        if (nPitch == 'R0'):
            noteNew = note.Rest(nDuration)
        else:
            try:
                noteNew = note.Note(nPitch)
            except:
                break
        for c in nDuration:
            if (c == "/"):
                numerator = ""
                denominator = ""
                for c2 in nDuration:
                    if (c2 == "/"):
                        break
                    numerator += c2
                start = False
                for c2 in nDuration:
                    if (c2 == "'"):
                        break
                    if (start):
                        denominator += c2
                    if (c2 == "/"):
                        start = True
                nDuration = float(float(numerator)/float(denominator))

        noteNew.quarterLength = float(nDuration)
        streamstream.append(noteNew)
    fp = streamstream.write('midi', fileName + '.mid')
    print("written" + fileName)


read_to_midi(test, 'TESTIN_CODE')
