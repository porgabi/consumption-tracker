from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # Takes Signal from UI

    # @pyqtSlot(int)
    # def change_amount(self, value):
    #     self._model.amount = value

    #     # calculate even or odd
    #     self._model.even_odd = 'odd' if value % 2 else 'even'

    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False

    @pyqtSlot(int)
    def add_water(self, value):
        self._model.add_water(value)
        self.change_human_bar(value)
        print('MAIN CTRL add water')

    @pyqtSlot(int)
    def sub_water(self, value):
        self._model.sub_water(value)
        self.change_human_bar(value)
        print('MAIN CTRL sub water')

    @pyqtSlot(int)
    def add_calories(self, value):
        self._model.add_calories(value)
        self.change_human_bar(value)

        print('MAIN CTRL add calories')
    
    @pyqtSlot(int)
    def sub_calories(self, value):
        self._model.sub_calories(value)
        self.change_human_bar(value)
        print('MAIN CTRL sub calories')

    @pyqtSlot(int)
    def change_human_bar(self, value):
        self._model.change_human_bar(value)
        print('MAIN CTRL change human bar')


    @pyqtSlot(bool)
    def change_light(self, value):
        self._model.light_change = False if value else True
        print('MAIN CTRL value', value)

    # @pyqtSlot(int)
    # def water_changed(self, value):
    #     print('do we comeh ere')
    #     Ui.MainWindow.water_bar.setProperty('value', 20) 

    # @pyqtSlot(str)
    # def add_user(self, value):
    #     self._model.add_user(value)
    #     print('main ctrl add user')
        # calculate button enabled state
        #if(self._model.users.count > 0):
        #    self._model.enable_del_user = True if value else False

    # @pyqtSlot(int)
    # def delete_user(self, value):
    #     self._model.delete_user(value)
    #     # calculate button enabled state
    #     #if(self._model.users.count > 0):
    #     #    self._model.enable_del_user = True if value else False