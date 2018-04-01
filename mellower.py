from music21 import *

#
def mellower(notes):
    returnNotes1 = []
    returnNotes2 = []
    notesNext = []
    counter = 0
    previousNote = note.Note('c8')
    runner = True
    for i in notes:
        if (runner):
            runner = False
            continue
        notesNext.append(i)
    for thisNote in notes:
        if(str(type(thisNote)) == str("<class 'music21.note.Rest'>")):
            returnNotes1.append(thisNote)
            counter = counter + 1
        else:
            avg = 0
            if (counter == 0):
                if (str(type(notesNext[counter])) == str("<class 'music21.note.Rest'>")):
                    avg = thisNote.pitch.diatonicNoteNum
                else:
                    avg = (thisNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum) / 2
            elif (counter < len(notes) - 1):
                print("COUNTER IS " + str(counter))
                if (str(type(notesNext[counter])) == str("<class 'music21.note.Rest'>")):
                    avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
                else:
                    avg = (previousNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 3
            if (counter >= len(notes) - 1):
                avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
            if (int(avg) - thisNote.pitch.diatonicNoteNum != 0):
                returnNotes1.append(thisNote.transpose(interval.GenericInterval(int(avg) - thisNote.pitch.diatonicNoteNum)))
            else:
                returnNotes1.append(thisNote)
            counter = counter + 1
            previousNote = thisNote
    counter = 0
    print("First size " + str(len(returnNotes1)))

    for thisNote in reversed(returnNotes1):
        if(str(type(thisNote)) == str("<class 'music21.note.Rest'>")):
            returnNotes2.append(thisNote)
            counter = counter + 1
        else:
            avg = 0
            if (counter == 0):
                if (str(type(notesNext[counter])) == str("<class 'music21.note.Rest'>")):
                    avg = thisNote.pitch.diatonicNoteNum
                else:
                    avg = (thisNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum) / 2
            elif (counter < len(notes) - 1):
                if (str(type(notesNext[counter])) == str("<class 'music21.note.Rest'>")):
                    avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
                else:
                    avg = (previousNote.pitch.diatonicNoteNum + notesNext[counter].pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 3
            if (counter >= len(notes) - 1):
                avg = (previousNote.pitch.diatonicNoteNum + thisNote.pitch.diatonicNoteNum) / 2
            if (int(avg) - thisNote.pitch.diatonicNoteNum != 0):
                returnNotes2.append(thisNote.transpose(interval.GenericInterval(int(avg) - thisNote.pitch.diatonicNoteNum)))
            else:
                returnNotes2.append(thisNote)
            counter = counter + 1
            previousNote = thisNote
    return reversed(returnNotes2)

notes = converter.parse("transposed3350.mid")
better = mellower(notes[0].notesAndRests)
streamstream = stream.Stream()
#for n in better:
#    print(n)
#    streamstream.append(n)
#better = mellower(streamstream.notesAndRests)
#streamstream = stream.Stream()
for n in better:
    print(n)
    streamstream.append(n)
streamstream.write('midi', 'test.mid')

#
# n1 = note.Rest()
# n2 = note.Note('e3')
# n3 = note.Rest()
# n4 = note.Note('g2')
# n5 = note.Note('b4')
# n6 = note.Note('e3')
# n7 = note.Rest()
#
# noteos = [n1, n2, n3, n4, n5, n6, n7]
# for i in noteos:
#     if(str(type(i)) != str("<class 'music21.note.Rest'>")):
#         print(i.pitch.diatonicNoteNum)
# new = mellower(noteos)
# for i in new:
#     if(str(type(i)) != str("<class 'music21.note.Rest'>")):
#         print(i.pitch.diatonicNoteNum)




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
