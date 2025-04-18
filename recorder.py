import sounddevice as sd
import numpy as np
import queue
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="whisper")


class Recorder_PTT:
    '''This class is used to record audio. It is controlled with the users button inputs.'''
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate
        self.channels = 1
        self.dtype = 'float32'
        self.audio_q = queue.Queue()
        self.recording = False
        self.debug = False

    def _callback(self, indata, frames, time, status):
        if self.recording:
            self.audio_q.put(indata.copy())

    def record(self):
        if self.debug:
            print("Press [Enter] to start the recording...")
        input()
        self.recording = True
        if self.debug:
            print("recording... press [Enter] again, to stop.")

        with sd.InputStream(samplerate=self.sample_rate,
                            channels=self.channels,
                            dtype=self.dtype,
                            callback=self._callback):
            input()
            self.recording = False
        if self.debug:
            print("Recording completed.")
        audio_data = []
        while not self.audio_q.empty():
            audio_data.append(self.audio_q.get())
        return np.concatenate(audio_data, axis=0)
