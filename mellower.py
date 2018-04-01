from music21 import *

#
def mellower(notes):
    print("MELLOWER: notes length " + str(len(notes)))
    returnNotes1 = []
    returnNotes2 = []
    notesNext = []
    counter = 0
    previousNote = note.Note('c8')
    for i in notes:
        if (i != notes[0]):
            notesNext.append(i)
    for thisNote in notes:
        avg = 0
        if (counter == 0):
            avg = (thisNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum) / 2
        elif (counter < len(notes) - 1):
            avg = (previousNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 3
        if (counter == len(notes) - 1):
            avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
        returnNotes1.append(thisNote.transpose(interval.GenericInterval(int(avg) - thisNote.pitch.diatonicNoteNum)))
        counter = counter + 1
        previousNote = thisNote
    counter = 0
    for thisNote in reversed(returnNotes1):
        avg = 0
        if (counter == 0):
            avg = (thisNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum) / 2
        if (counter < len(notes) - 1):
            avg = (previousNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 3
        if (counter == len(notes) - 1):
            avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
        returnNotes2.append(thisNote.transpose(interval.GenericInterval(int(avg) - thisNote.pitch.diatonicNoteNum)))
        counter = counter + 1
        previousNote = thisNote
    return reversed(returnNotes2)

n1 = note.Note("c2")
n2 = note.Note('e3')
n3 = note.Note('f3')
n4 = note.Note('g2')
n5 = note.Note('b4')
n6 = note.Note('b5')
n7 = note.Note('c4')

noteos = [n1, n2, n3, n4, n5, n6, n7]
print (noteos)
for i in noteos:
    print(i.pitch.diatonicNoteNum)
new = mellower(noteos)
print (new)
for i in new:
    print(i.pitch.diatonicNoteNum)

# c4 = note.Note("c4")
# print(c4.pitch.diatonicNoteNum)
# e4 = note.Note("e4")
# print(e4.pitch.diatonicNoteNum)
# c3 = note.Note('c3')
# print(c3.pitch.diatonicNoteNum)
#
# avg = (c4.pitch.diatonicNoteNum + e4.pitch.diatonicNoteNum + c3.pitch.diatonicNoteNum) / 3
# print(int(avg) - c4.pitch.diatonicNoteNum)
# c4 = c4.transpose(interval.GenericInterval(int(avg) - c4.pitch.diatonicNoteNum))
# print(c4)
