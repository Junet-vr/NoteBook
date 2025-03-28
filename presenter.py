from model import Notebook
from view import NotebookView

class NotebookPresenter:
    def __init__(self, model: Notebook, view: NotebookView):
        self.model = model
        self.view = view

    def add_note(self):
        text = self.view.get_user_input("Введите текст заметки: ")
        self.model.add_note(text)
        print("Заметка добавлена!")

    def show_notes(self):
        notes = self.model.get_notes()
        self.view.display_notes(notes)

    def run(self):
        while True:
            command = self.view.get_user_input("\nКоманды: add - добавить, show - показать, exit - выход\nВведите команду: ").strip().lower()
            if command == "add":
                self.add_note()
            elif command == "show":
                self.show_notes()
            elif command == "exit":
                print("Выход из программы.")
                break
            else:
                print("Неизвестная команда, попробуйте снова.")
