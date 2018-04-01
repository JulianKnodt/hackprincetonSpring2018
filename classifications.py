import numpy as np
import music21 as m21
import math

def classify_phrase(phrase):
  minV = math.inf
  maxV = -math.inf
  note_range = 0
  length = 0
  mean_value = 0
  for note in phrase:
    length += note.duration.quarterLength/4
    if isinstance(note, m21.note.Rest):
      continue
    minV = min(note.pitch.frequency, minV)
    maxV = max(note.pitch.frequency, maxV)
    mean_value += note.pitch.frequency
  mean_value /= len(phrase)
  note_range = maxV-minV
  return {
    'length': length,
    'min_value': minV,
    'note_range': note_range,
    'mean_value': mean_value
  }

def is_accelerating(phrase):
  durations = map(lambda note: note.duration.quarterLength, phrase)
  for first, second in zip(durations, durations[1:]):
    if second - first > 0.5:
      return False
  return True

def is_deccelerating(phrase):
  durations = map(lambda note: note.duration.quarterLength, phrase)
  for first, second in zip(durations, durations[1:]):
    if second - first > - 0.5:
      return False
  return True

def summary_statistics(raw_notes, classification_states):
  current_phrase = []
  result = np.array([])
  i = 0
  for part in raw_notes:
    for note in part.notesAndRests.stream():
      i += 1
      if i in classification_states:
        result = np.append(result, current_phrase)
        current_phrase = []
      else:
        current_phrase += [note]

  if len(current_phrase) != 0:
    result = np.append(result, current_phrase)
  return result


classification_functions = [is_accelerating, is_deccelerating]
def concat_phrases(phrases):
  result = []
  for phrase in phrases:
    data = {
      "summary": classify_phrase(phrase),
      "classifications": map(lambda c: c(phrase), classification_functions),
      "phrase": phrase,
    }
    result += [data]
  return result

# TEST:
print(summary_statistics(m21.converter.parse('988-v01.mid'), [10]))
