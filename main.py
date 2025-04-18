from jarvis import Jarvis

jarvis = Jarvis()

def choose():
    '''Welcome function to choose between the modes Jarvis know.'''

    print("All systems online, Sir.")
    print("Which mode would you like to use today?")
    print("")
    print("[1] Text conversation")
    print("[2] Speech to Text")
    print("[3] Text to Speech")
    print("[4] Speech conversation")
    print("")
    mode = int(input("Please select the right number: "))

    if mode == 1:
        jarvis.text_conversation()
    elif mode == 2:
        jarvis.speech_to_text()
    elif mode == 3:
        jarvis.text_to_speech()
    elif mode == 4:
        jarvis.speech_conservation()
    else:
        print("error: you have to pick one of the displayed numbers.")



def main():
    try:
        choose()
    except KeyboardInterrupt:
        print("")
        print("Goodbye, Sir.")

if __name__ == "__main__":
    main()