from abc import ABC, abstractmethod

class NotebookView(ABC):
    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def get_user_input(self, prompt: str) -> str:
        pass

class ConsoleNotebookView(NotebookView):
    def display_notes(self, notes):
        if not notes:
            print("Записная книжка пуста.")
        else:
            print("\nСписок заметок:")
            for note in notes:
                print(note)

    def get_user_input(self, prompt: str) -> str:
        return input(prompt)
