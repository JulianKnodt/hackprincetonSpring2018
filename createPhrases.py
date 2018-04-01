import json
import music21 as m21
from pre import parseStream
import classifications as cl

samples = ['http://www.jsbach.net/midi/bwv988/988-aria.mid', 'http://www.jsbach.net/midi/bwv988/988-v01.mid', 'http://www.jsbach.net/midi/bwv988/988-v02.mid', 'http://www.jsbach.net/midi/bwv988/988-v03.mid', 'http://www.jsbach.net/midi/bwv988/988-v04.mid', 'http://www.jsbach.net/midi/bwv988/988-v05.mid', 'http://www.jsbach.net/midi/bwv988/988-v06.mid', 'http://www.jsbach.net/midi/bwv988/988-v07.mid', 'http://www.jsbach.net/midi/bwv988/988-v08.mid', 'http://www.jsbach.net/midi/bwv988/988-v09.mid', 'http://www.jsbach.net/midi/bwv988/988-v10.mid', 'http://www.jsbach.net/midi/bwv988/988-v11.mid', 'http://www.jsbach.net/midi/bwv988/988-v12.mid', 'http://www.jsbach.net/midi/bwv988/988-v13.mid', 'http://www.jsbach.net/midi/bwv988/988-v14.mid', 'http://www.jsbach.net/midi/bwv988/988-v15.mid', 'http://www.jsbach.net/midi/bwv988/988-v16.mid', 'http://www.jsbach.net/midi/bwv988/988-v17.mid', 'http://www.jsbach.net/midi/bwv988/988-v18.mid', 'http://www.jsbach.net/midi/bwv988/988-v19.mid', 'http://www.jsbach.net/midi/bwv988/988-v20.mid', 'http://www.jsbach.net/midi/bwv988/988-v21.mid', 'http://www.jsbach.net/midi/bwv988/988-v22.mid', 'http://www.jsbach.net/midi/bwv988/988-v23.mid', 'http://www.jsbach.net/midi/bwv988/988-v24.mid', 'http://www.jsbach.net/midi/bwv988/988-v25.mid', 'http://www.jsbach.net/midi/bwv988/988-v26.mid', 'http://www.jsbach.net/midi/bwv988/988-v27.mid', 'http://www.jsbach.net/midi/bwv988/988-v28.mid', 'http://www.jsbach.net/midi/bwv988/988-v29.mid', 'http://www.jsbach.net/midi/bwv988/988-v30.mid', 'http://www.jsbach.net/midi/vp1-1al.mid', 'http://www.jsbach.net/midi/vp1-2ald.mid', 'http://www.jsbach.net/midi/vp1-3co.mid', 'http://www.jsbach.net/midi/vp1-4cod.mid', 'http://www.jsbach.net/midi/vp1-5sa.mid', 'http://www.jsbach.net/midi/vp1-6sad.mid', 'http://www.jsbach.net/midi/vp1-7tb.mid', 'http://www.jsbach.net/midi/vp1-8tbd.mid', 'http://www.jsbach.net/midi/vp2-1all.mid', 'http://www.jsbach.net/midi/vp2-2cou.mid', 'http://www.jsbach.net/midi/vp2-3sar.mid', 'http://www.jsbach.net/midi/vp2-4gig.mid', 'http://www.jsbach.net/midi/vp2-5cha.mid', 'http://www.jsbach.net/midi/vp3-1pre.mid', 'http://www.jsbach.net/midi/vp3-2lou.mid', 'http://www.jsbach.net/midi/vp3-3gav.mid', 'http://www.jsbach.net/midi/vp3-4min.mid', 'http://www.jsbach.net/midi/vp3-5bou.mid', 'http://www.jsbach.net/midi/vp3-6gig.mid', 'http://www.jsbach.net/midi/vs1-1ada.mid', 'http://www.jsbach.net/midi/vs1-3sic.mid', 'http://www.jsbach.net/midi/vs1-4prs.mid', 'http://www.jsbach.net/midi/vs2-1gra.mid', 'http://www.jsbach.net/midi/vs2-2fug.mid', 'http://www.jsbach.net/midi/vs2-3and.mid', 'http://www.jsbach.net/midi/vs2-4alg.mid', 'http://www.jsbach.net/midi/vs3-1ada.mid', 'http://www.jsbach.net/midi/vs3-2fug.mid', 'http://www.jsbach.net/midi/vs3-3lar.mid']
for url in samples:
  song = m21.converter.parse(url)
  startIndeces = parseStream(song)
  phrases = cl.phrases(song, startIndeces)
  detailed_phrases = list(cl.concat_phrases(phrases))
  representations = cl.extract_classifications(detailed_phrases)
  for index, value in enumerate(representations):
    streamOutput = m21.stream.Stream()
    phrase = list(detailed_phrases)[index]['phrase']
    for note in phrase:
      streamOutput.append(note)
    mf = m21.midi.translate.streamToMidiFile(streamOutput)
    mf.open(f'./{value}.mid', 'wb')
    mf.write()
    mf.close()
  print(representations)

