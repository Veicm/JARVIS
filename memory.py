class Memory:
    '''This class manages the memory of Jarvis so he can remember a conservation.'''

    def __init__(self):
        self.entries = []

    def add_entry(self, role, content):
        self.entries.append({
            "role": role,
            "content": content.strip()
        })

    def clear(self):
        self.entries.clear()

    def last(self, n=1):
        return self.entries[-n:]
