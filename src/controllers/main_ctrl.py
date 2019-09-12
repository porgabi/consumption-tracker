# accepts user's inputs, delegates data representation to a view and data
# handling to a model
from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # catches signal from model
    @pyqtSlot(int)
    # function name same as one from model
    def add_water(self, value):
        self._model.add_user(value)
