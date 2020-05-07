from pydub import AudioSegment
from mutagen.wavpack import WavPack


audio = AudioSegment.from_wav('test.wav')
time = audio.info.length

#audio = AudioSegment('test.wav')
for i in range(len(time) * 1000):
    new_audio = audio[i : i + 49]
    i += 50
    new_audio.export(str(i) + '.wav', format='wav')
