import music21 as m21

with open('final_samples_20.txt') as inc:
  for index, line in enumerate(inc):
    song = m21.stream.Stream()
    for word in line.split():
      midifile = f'{word}.mid'
      score = m21.converter.parse(midifile)
      for part in score:
        for note in part.notesAndRests.stream():
          if note.isRest:
            continue
          song.append(note)
    mf = m21.midi.translate.streamToMidiFile(song)
    mf.open(f'./final{index}.mid', 'wb')
    mf.write()
    mf.close()
