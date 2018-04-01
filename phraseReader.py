import music21 as m21
import csv
import sys
import os
from collections import defaultdict


# Returns a value 1, 2, 3, 4, or 5 depending on the phrase identified
def phraseReader(notes):
    phraseDefinition = [False]*16
    pd30 = []
    previousChanges24 = []
    prevNote = m21.note.Note('c8')
    n = len(previousChanges24)
    bb = len(pd30)
    for note in notes:
      if isinstance(note, m21.note.Rest):
        continue
      if isinstance(note, m21.note.Note):
        pd30 += [note.quarterLength]
        previousChanges24 += [prevNote.pitch.diatonicNoteNum - note.pitch.diatonicNoteNum]

        n = len(previousChanges24)
        bb = len(pd30)
        if (n > 12 and previousChanges24[n-6:n-1] == previousChanges24[n-12:n-7]):
            phraseDefinition[0] = True
            previousChanges24 = []
            n = 0

        if n > 20 and previousChanges24[n-11:n-1] == previousChanges24[n-21:n-11]:
            previousChanges24 = []
            n = 0
            phraseDefinition[1] = True

        if note.quarterLength == 1.0:
            if (bb > 5 and pd30[bb-5] == 0.25 and pd30[bb-4] == 0.25 and pd30[bb-3] == 0.25 and pd30[bb-2] == 0.25):
                phraseDefinition[2] = True

        if note.quarterLength >= 2.0:
            if len(pd30) > 3 and pd30[bb-2] < 1 and pd30[bb-3] < 1:
                phraseDefinition[3] = True
                pd30 = []
        prevNote = note

    if not any(phraseDefinition):
        phraseDefinition[4] = True
    phraseDefinition[min(round(len(notes)/2), 10) + 4]
    return phraseDefinition

