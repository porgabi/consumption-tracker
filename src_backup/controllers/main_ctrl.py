# accepts user's inputs, delegates data representation to a view and data
# handling to a model
from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model


    # catches signal from model
    @pyqtSlot(int)
    def add_glass(self, value):
        self._model.add_glass(value)

        print('MAIN CTRL add water')

    @pyqtSlot()
    def change_water_bar(self):
        self._model.change_water_bar(self)
    #     # self._model.

    #     self._ui.water_bar.setProperty('value', value) ##
