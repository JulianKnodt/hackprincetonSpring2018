from collections import defaultdict
import csv

def convert_indexes_to_notes(indexes):
    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))

    int_dict = dict((int, note) for note, int in note_dict.items())
    for index in indexes:
        print(int_dict[str(index)])

indexes = [100,200]
convert_indexes_to_notes(indexes)
