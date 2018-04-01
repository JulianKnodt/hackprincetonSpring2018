import urllib.request as req
import numpy as np
import music21 as m21
import math
from phraseReader import phraseReader

def classify_phrase(phrase):
  minV = math.inf
  maxV = -math.inf
  note_range = 0
  length = 0
  mean_value = 0
  for note in phrase:
    length += note.duration.quarterLength/4
    if not(isinstance(note, m21.note.Note)):
      continue
    minV = min(note.pitch.frequency, minV)
    maxV = max(note.pitch.frequency, maxV)
    mean_value += note.pitch.frequency
  if length != 0:  mean_value /= len(phrase)
  note_range = maxV-minV
  return {
    'length': length,
    'min_value': minV,
    'note_range': note_range,
    'mean_value': mean_value
  }

def is_accelerating(phrase):
  durations = list(map(lambda note: note.duration.quarterLength, phrase))
  for first, second in zip(durations, durations[1:]):
    if second - first > 0.5:
      return False
  return True

def is_deccelerating(phrase):
  durations = list(map(lambda note: note.duration.quarterLength, phrase))
  for first, second in zip(durations, durations[1:]):
    if second - first > - 0.5:
      return False
  return True

def phrases(raw_notes, classification_states):
  current_phrase = []
  result = []
  i = 0
  for part in raw_notes:
    for note in part.notesAndRests.stream():
      i += 1
      if i in classification_states:
        result += [current_phrase]
        current_phrase = []
      else:
        current_phrase += [note]

  if len(current_phrase) != 0:
    result += [current_phrase]
  return result

def generate_csv(midi_path):
  result = []
  raw_notes = m21.converter.parse(midi_path)
  for part in raw_notes:
    for note in part.notesAndRests.stream():
      if isinstance(note, m21.note.Note):
        result += [f"{note.pitch.name}, {note.pitch.octave}, {note.duration.quarterLength/4}"]
      else:
        result += [f"R, 0, {note.duration.quarterLength/4}"]
  return '\n'.join(result)

url = 'http://www.bachcentral.com/sinfon'
#for i in range(1, 15):
#  print(generate_csv(url + f'/sinfon{i}.mid'))

classification_functions = [is_accelerating, is_deccelerating]
def classifications_for(phrase):
  result = 0
  for note in phrase:
    if note.isRest or note.isChord: continue
    result += note.pitch.diatonicNoteNum * note.offset/len(phrase) + (note.pitch.accidental == None)
  return [round(result)]
#  phraseClassifications = phraseReader(phrase)
#  return phraseClassifications + list(map(lambda c: c(phrase), classification_functions))


def concat_phrases(phrases):
  return map(lambda phrase: {
      "summary": classify_phrase(phrase),
      "classifications": classifications_for(phrase),
      "phrase": phrase,
    }, phrases)

def extract_classifications(output_concat_phrases):
  result = []
  for phrase in output_concat_phrases:
    sum = 0
    for i, y in enumerate(phrase['classifications']):
      sum += (y << i)
    result += [sum]
  return result

# TEST:
#print(extract_classifications(concat_phrases(phrases(m21.converter.parse('http://www.bachcentral.com/WTCBkI/Fugue1.mid'), [10]))))
