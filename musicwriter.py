from music21 import *
import csv
import sys
import os

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
