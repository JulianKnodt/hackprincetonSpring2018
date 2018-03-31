from music21 import *
import csv
import sys
import os
from collections import defaultdict
import csv

# indexes should be a list of ints, the output from the neural network
def convert_indexes_to_notes(indexes):
    with open('indexes.csv', 'r', encoding='utf-8') as csv_file:
        note_dict = dict(csv.reader(csv_file))
    
    int_dict = dict((int, note) for note, int in note_dict.items())
    for index in indexes:
        print(int_dict[str(index)])


orig_stdout = sys.stdout
f = open('GoldbergVariationsRawData.csv', 'w')

sys.stdout = f



path = r'C:\Users\Nick Kim\Downloads\Music'
print('Notes')
for filename in os.listdir(path):
    s = converter.parse(r'C:\Users\Nick Kim\Downloads\Music\\' + filename)
    for i in s:
        for thisNote in i.getElementsByClass(note.Note):
            print(str(thisNote.pitch) + str(thisNote.quarterLength))
    print('end')
