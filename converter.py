import tempfile
import whisper
from scipy.io.wavfile import write
import subprocess

from recorder import Recorder_PTT
from player import Player



class Converter:
    '''This class is used to convert text to audio or audio to text
    dependent on the called function.
    '''

    def __init__(self):

        self.recorder_ptt = Recorder_PTT()
        self.player = Player()

        self.SAMPLE_RATE = 16000
        self.FRAME_DURATION = 30  # ms
        self.FRAME_SIZE = int(self.SAMPLE_RATE * self.FRAME_DURATION / 1000)
        self.MAX_RECORDING = 60  # Maximal recording time
        self.whisper_model = whisper.load_model("base")

        self.debug = False


    def _speech_to_text(self, audio, fs=16000) -> str:# fs=self.SAMPLE_RATE
        '''This function turns any given audio file in a transcript.'''
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            write(f.name, fs, audio)
            result = self.whisper_model.transcribe(f.name, task="transcribe", language=None)
            if self.debug:
                print(f"Language recognized: {result['language']}")
            return result["text"]
        

    def STT(self) -> str:
        '''This function records audio and turn it to text.'''
        audio = self.recorder_ptt.record()
        text = self._speech_to_text(audio)
        return text
    
    

                                                          #input user name
    def _text_to_speech(self, text: str, voice_path="/home/user/.local/share/piper/voices/en/alan-medium/en_GB-alan-medium.onnx") -> str:
        '''This function turns any given text into an audio file.'''

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            output_path = tmp_file.name

        try:
            result = subprocess.run([
                "piper-tts",
                "--model", voice_path,
                "--output_file", output_path
            ], input=text.encode("utf-8"), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


        except subprocess.CalledProcessError as e:
            print(f"error while speaking: {e}")
            return ""

        return output_path

    
    def TTS(self, text):
        '''This function takes any given text and play the audio of it afterwards.'''
        audio = self._text_to_speech(text)
        self.player.play_audio(audio)