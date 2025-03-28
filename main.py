from model import Notebook
from view import ConsoleNotebookView
from presenter import NotebookPresenter

if __name__ == "__main__":
    model = Notebook()
    view = ConsoleNotebookView()
    presenter = NotebookPresenter(model, view)
    presenter.run()
