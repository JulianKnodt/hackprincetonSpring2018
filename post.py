from datetime import datetime
import music21 as m21

def convertNote(note):
  if isinstance(note, m21.note.Note):
    return note
  return m21.note.Note(note)

def convertToRawNotes(listPhrases=list()):
  result = m21.stream.Stream()
  for phrase in listPhrases:
    for note in phrase:
      result.append(convertNote(note))

  return result

def writeToMidi():
  now = str(datetime.now())
  result.write('midi', "/output/{now}")
