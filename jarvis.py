from generator import Generator
from text_input import Text_Input
from converter import Converter
from memory import Memory


class Jarvis:
    '''This is the main class of Jarvis where all other classes get combined
    in order to build different conservation modes.
    '''

    def __init__(self):
        self.generator = Generator()
        self.text_input = Text_Input()
        self.converter = Converter()
        self.memory = Memory()


    def text_conversation(self):
        '''This function gets text inputs and returned a text answer.'''
        print("Hello Sir, how can I help you today?")

        while True:
            question = self.text_input.get_input().strip()
            if not question:
                continue
            self.memory.add_entry("User", question)
            answer = self.generator.gen_answer(self.memory)
            self.memory.add_entry("Jarvis", answer)
            print("")
            print(answer)

    def speech_to_text(self):
        '''This function gets the user input over audio and return a text answer.'''
        print("Hello Sir, how can I help you today?")

        while True:
            question = self.converter.STT().strip()
            if not question:
                continue
            self.memory.add_entry("User", question)
            print(f"> {question}")
            answer = self.generator.gen_answer(self.memory)
            self.memory.add_entry("Jarvis", answer)
            print("")
            print(answer)

    def text_to_speech(self):
        '''This function gets the user input by text while retuning answers by audio.'''
        print("Hello Sir, how can I help you today?")
        self.converter.TTS("Hello Sir, how can I help you today?")

        while True:
            question = self.text_input.get_input().strip()
            if not question:
                continue
            self.memory.add_entry("User", question)
            answer = self.generator.gen_answer(self.memory)
            self.memory.add_entry("Jarvis", answer)
            print("")
            print(answer)
            self.converter.TTS(answer)

    def speech_conservation(self):
        '''This function will get the user input by audio and return the answer also by audio.'''
        print("Hello Sir, how can I help you today?")
        self.converter.TTS("Hello Sir, how can I help you today?")

        while True:
            question = self.converter.STT().strip()
            if not question:
                continue
            self.memory.add_entry("User", question)
            print(f"> {question}")
            answer = self.generator.gen_answer(self.memory)
            self.memory.add_entry("Jarvis", answer)
            print("")
            print(answer)
            self.converter.TTS(answer)