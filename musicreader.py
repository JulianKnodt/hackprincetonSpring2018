from music21 import *
import csv
import sys
import os

orig_stdout = sys.stdout
orig_stdout = sys.stdout
d = open('notedata.txt', 'w')

# sys.stdout = d

f = open('GoldbergShortLong.csv', 'r')
reader = csv.reader(f)

streamstream = stream.Stream()
firstrow = True
for row in reader:
    counter = 2
    if (firstrow):
        firstrow = False
        continue
    if (str(row)[2:5] != 'end' and str(row)[2:7] != "Notes"):
        nPitch = str(row)[counter]
        counter = counter+1
        nPitch += str(row)[counter]
        if (str(row)[3] == '#' or str(row)[3] == '-'):
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

print(len(streamstream))
print("Reached")


fp = streamstream.write('midi', 'test.mid')
print("written")
