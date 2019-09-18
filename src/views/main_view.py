from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from views.main_view_ui import Ui_MainWindow
import CT_stylesheets
import sys


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        ###
        # connect ui-widget to controller
        # if ui changes, it sends a signal to a slot on which we connect a controller class.
        # therefore we can recive the signal in the controller
        ###


        # self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # # Lambda to execute function with value
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))
        # self._ui.pushButton_add.clicked.connect(lambda: self._main_controller.add_water(self.add_glass()))
        


        # this works but is this how it should be done?
        # could set up all default values here, but then it's certainly wrong
        if self._model._light_on is True:
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
        
            dark_icon = QtGui.QIcon()
            dark_icon.addPixmap(QtGui.QPixmap("CT_icons/darken.png"))
            self._ui.appearance_button.setIcon(dark_icon)
            self._ui.appearance_button.setToolTip('Darken')

            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_light)
            self._ui.sub_water_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.glass_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.small_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.large_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.sub_calories_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.sandwich_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.eggs_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.meat_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_light)
            self._ui.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self._ui.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self._ui.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_light)

            self._ui.hour_edit.setStyleSheet("background: rgb(255, 255, 255); font: 20pt \"Segoe UI\"""; color: black")
            self._ui.min_edit.setStyleSheet("background: rgb(255, 255, 255); font: 20pt \"Segoe UI\"""; color: black")
            sub_cal_icon_dark = QtGui.QIcon()
            sub_cal_icon_dark.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
            self._ui.sub_calories_button.setIcon(sub_cal_icon_dark)
            # + body

        # dark
        else:
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_dark)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_dark)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))

            light_icon = QtGui.QIcon()
            light_icon.addPixmap(QtGui.QPixmap("CT_icons/lighten.png"))
            self._ui.appearance_button.setIcon(light_icon)
            self._ui.appearance_button.setToolTip('Lighten')

            self._ui.sub_water_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.glass_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.small_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.large_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.sub_calories_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.sandwich_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.eggs_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.meat_button.setStyleSheet(CT_stylesheets.background_dark)

            self._ui.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_dark)
            self._ui.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)
            self._ui.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)

            self._ui.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_dark)
            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_dark)

            # ??????
            self._ui.hour_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")
            self._ui.min_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")

            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self._ui.sub_calories_button.setIcon(run_light_icon)
            # + body






        self._ui.large_bottle_button.clicked.connect(
            lambda: self._main_controller.add_water(1000)
        )
        self._ui.small_bottle_button.clicked.connect(
            lambda: self._main_controller.add_water(500)
        )
        self._ui.glass_button.clicked.connect(
            lambda: self._main_controller.add_water(200)
        )
        self._ui.sub_water_button.clicked.connect(
            lambda: self._main_controller.sub_water(100)
        )

        self._ui.meat_button.clicked.connect(
            lambda: self._main_controller.add_calories(1000)
        )
        self._ui.eggs_button.clicked.connect(
            lambda: self._main_controller.add_calories(500)
        )
        self._ui.sandwich_button.clicked.connect(
            lambda: self._main_controller.add_calories(200)
        )
        self._ui.sub_calories_button.clicked.connect(
            lambda: self._main_controller.sub_calories(100)
        )

        # use something like this for switch appearance button
        self._ui.appearance_button.triggered.connect(
            lambda: self._main_controller.change_light(self._model._light_on)
        )
        # self._ui.pushButton_delete.clicked.connect(lambda: self._main_controller.delete_user(self._ui.listWidget_names.currentRow()))

        ###
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # # if model sends/emits a signal the ui gets notified
        ###

        # CONNECT model signal to corresponding main_view slot
        self._model.water_changed.connect(self.on_water_changed)
        self._model.calories_changed.connect(self.on_calories_changed)
        self._model.human_bar_changed.connect(self.on_human_bar_changed)
        self._model.light_changed.connect(self.on_light_changed)

        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # self._model.users_changed.connect(self.on_list_changed)

        # set a default value
        # self._main_controller.change_amount(42)

    @pyqtSlot(int)
    def on_water_changed(self, value):
        print('main view on water changed')
        print('value:', value)
        self._ui.water_bar.setProperty('value', value)
        self._ui.water_number.setProperty('intValue', value/100)


    @pyqtSlot(int)
    def on_calories_changed(self, value):
        print('MV on calories changed')
        print(value)
        self._ui.cal_bar.setProperty('value', value)
        self._ui.cal_number.setProperty('intValue', value/100)


    @pyqtSlot(int)
    def on_human_bar_changed(self, value):
        print('MV on human bar changed')
        print(value)
        self._ui.human_bar.setProperty('value', value)





    @pyqtSlot(bool)
    def on_light_changed(self, value):
        if value == True:
            print('MV value false')
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
            
            dark_icon = QtGui.QIcon()
            dark_icon.addPixmap(QtGui.QPixmap("CT_icons/darken.png"))
            self._ui.appearance_button.setIcon(dark_icon)
            self._ui.appearance_button.setToolTip('Darken')

            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_light)
            self._ui.sub_water_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.glass_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.small_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.large_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.sub_calories_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.sandwich_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.eggs_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.meat_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_light)
            self._ui.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self._ui.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self._ui.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_light)

            self._ui.hour_edit.setStyleSheet("background: rgb(255, 255, 255); font: 20pt \"Segoe UI\"""; color: black")
            self._ui.min_edit.setStyleSheet("background: rgb(255, 255, 255); font: 20pt \"Segoe UI\"""; color: black")
            sub_cal_icon_dark = QtGui.QIcon()
            sub_cal_icon_dark.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
            self._ui.sub_calories_button.setIcon(sub_cal_icon_dark)
            # + body

        # DARK 
        else:
            print('MV value true')
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_dark)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_dark)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))

            light_icon = QtGui.QIcon()
            light_icon.addPixmap(QtGui.QPixmap("CT_icons/lighten.png"))
            self._ui.appearance_button.setIcon(light_icon)
            self._ui.appearance_button.setToolTip('Lighten')

            self._ui.sub_water_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.glass_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.small_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.large_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.sub_calories_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.sandwich_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.eggs_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.meat_button.setStyleSheet(CT_stylesheets.background_dark)

            self._ui.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_dark)
            self._ui.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)
            self._ui.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)

            self._ui.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_dark)
            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_dark)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_dark)

            # ??????
            self._ui.hour_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")
            self._ui.min_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")

            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self._ui.sub_calories_button.setIcon(run_light_icon)
            
            # how the fuck
            # + body

    # def add_glass(self):
    #     return int(self._ui.lineEdit_name.text())




    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)






    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)

    # @pyqtSlot(list)
    # def on_list_changed(self, value):
    #     print('mainview on list changed method')
    #     self._ui.listWidget_names.clear()
    #     self._ui.listWidget_names.addItems(value)