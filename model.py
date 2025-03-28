from datetime import datetime

class Note:
    def __init__(self, text: str):
        self.text = text
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.date}] {self.text}"

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, text: str):
        note = Note(text)
        self.notes.append(note)

    def get_notes(self):
        return self.notes
