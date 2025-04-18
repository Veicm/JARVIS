# audio_player.py

import sounddevice as sd
import soundfile as sf

class Player:
    '''This class can play audio files.'''
    def __init__(self):
        pass

    
    def play_audio(self, file_path: str):
        '''Plays an audio file.'''
        try:
            data, samplerate = sf.read(file_path, dtype='float32')
            sd.play(data, samplerate)
            sd.wait()
        except Exception as e:
            print(f"error while playing audio: {e}")
