from music21 import *
import csv
import sys
import os
import numpy as np


def convert_generated_to_indexes(generated):
    notes_int = []
    for i,j in np.nonzero(generated):
        notes += i
    return notes_int


def convert_int_to_string(ints):
    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))
    note_dict_reversed = dict((intVal, note) for note, intVal in note_dict.iteritems())

    string_reps = []
    for i in ints:
        string_reps += [note_dict_reversed[i]]

    return string_reps


def read_to_midi(generated):
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
        noteNew = note.Note(nPitch)
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
    fp = streamstream.write('midi', 'test.mid')
    print("written")
