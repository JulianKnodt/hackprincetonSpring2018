import pandas as pd
from collections import defaultdict
import csv

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

training_notes = pd.read_csv("GoldbergVariationsRawData.csv", index_col=None)
build_note_dict(training_notes)
convert_notes_to_indexes(training_notes)
