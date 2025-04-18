class Text_Input:
    '''This is the most simple class, it is used to get a text input from the user.'''
    def __init__(self):
        pass


    def get_input(self) -> str:
        question = str(input("> "))
        return question