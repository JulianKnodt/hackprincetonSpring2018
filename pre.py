# Handles initially processing the music
from music21 import *
import numpy as np
import pandas as pd
import csv
from tensorflow import SparseTensor

phrase_positions = []



def split_into_phrases(phrase_positions, notesList):
    phrases = [notesList[x:y] for x, y in zip(phrase_positions, phrase_positions[1:])]


def on_off_representation(stream):

    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))

    step = 0
    current_notes = []
    indices = []
    data = []
    for note in stream.notes:
        thirty_two_length = int(note.quarterLength * 8)
        if (thirty_two_length != 0):
            current_notes.append(note)
            for n in current_notes:
                string_rep = str(n.pitch) + str(n.quarterLength)
                indices.append([int(note_dict[string_rep]),step])
                indices.append([int(note_dict[string_rep]),step + thirty_two_length - 1])
                data += [1,1]
            step += thirty_two_length
            current_notes = []
        else:
            current_notes += note
    print(indices)
    print(data)
    phrase = SparseTensor(indices, data, (len(note_dict), int(stream.duration.quarterLength * 8)))
    return phrase


s1 = stream.Stream()
s1.append(note.Note('C#4', type='half'))
s1.append(note.Note('D5', type='quarter'))

on_off_representation(s1)
