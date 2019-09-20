from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot, QTime
from PyQt5 import QtGui
from views.main_view_ui import Ui_MainWindow
import CT_stylesheets
import sys, datetime


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



        self._ui.water_number.setProperty(
            'value', self._model._current_water / 100
        )
        self._ui.max_water_number.setProperty(
            'intValue', self._model._max_water / 100
        )
        self._ui.cal_number.setProperty(
            'value', self._model._current_calories
        )        
        self._ui.max_calories_number.setProperty(
            'intValue', self._model._max_calories
        )
        self._ui.water_bar.setProperty(
            'value', self._model._current_water
        )
        self._ui.cal_bar.setProperty(
            'value', self._model._current_calories
        )
        self._ui.human_bar.setMaximum(
            self._model._max_water + self._model._max_calories
        )
        self._ui.human_bar.setProperty(
            'value', self._model._current_water + self._model._current_calories
        )
        
        # place this into dictionary?
        if self._model._meal_logger_presses == 0:
            self._ui.meal_text.setText(self._model._null_meal)
        elif self._model._meal_logger_presses == 1:
            self._ui.meal_text.setText(self._model._first_meal)
        elif self._model._meal_logger_presses == 2:
            self._ui.meal_text.setText(self._model._second_meal)
        elif self._model._meal_logger_presses == 3:
            self._ui.meal_text.setText(self._model._third_meal)
        elif self._model._meal_logger_presses == 4:
            self._ui.meal_text.setText(self._model._fourth_meal)
        elif self._model._meal_logger_presses == 5:
            self._ui.meal_text.setText(self._model._fifth_meal)
        elif self._model._meal_logger_presses == 6:
            self._ui.meal_text.setText(self._model._sixth_meal)

        self._ui.hour_edit.setTime(self._model._saved_hour)
        self._ui.min_edit.setTime(self._model._saved_min)
        self._ui.reset_values_action.setChecked(self._model._reset_app_value)


        if self._model._light_on is True:
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
        
            dark_icon = QtGui.QIcon()
            dark_icon.addPixmap(QtGui.QPixmap("CT_icons/darken.png"))
            self._ui.appearance_button.setIcon(dark_icon)
            self._ui.appearance_button.setToolTip('Darken')

            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.background_light)
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

            self._ui.hour_edit.setStyleSheet(CT_stylesheets.time_edit_light)
            self._ui.min_edit.setStyleSheet(CT_stylesheets.time_edit_light)
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
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.background_dark)
            # ??????
            self._ui.hour_edit.setStyleSheet(CT_stylesheets.time_edit_dark)
            self._ui.min_edit.setStyleSheet(CT_stylesheets.time_edit_dark)

            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self._ui.sub_calories_button.setIcon(run_light_icon)
            # + body
        


        # BUTTON connections

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

        self._ui.get_current_time_button.clicked.connect(
            lambda: self._main_controller.set_to_current_time()
        )

        self._ui.reset_button.triggered.connect(
            lambda: self._main_controller.reset_app()
        )
        self._ui.appearance_button.triggered.connect(
            lambda: self._main_controller.change_light(self._model._light_on)
        )

        self._ui.meal_time_button.clicked.connect(
            lambda: self._main_controller.log_meal()
        )


        self._ui.reset_values_action.triggered.connect(
            lambda: self._main_controller.change_reset_app_value(
                self._model._reset_app_value)
        )

        # MENU BAR ACTIONS
        self._ui.set_water_10dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(1000)
        )
        self._ui.set_water_15dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(1500)
        )
        self._ui.set_water_20dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(2000)
        )
        self._ui.set_water_25dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(2500)
        )
        self._ui.set_water_30dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(3000)
        )
        self._ui.set_water_35dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(3500)
        )
        self._ui.set_water_40dl_action.triggered.connect(
            lambda: self._main_controller.change_max_water(4000)
        )
        self._ui.set_calories_1000cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(1000)
        )
        self._ui.set_calories_1500cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(1500)
        )
        self._ui.set_calories_2000cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(2000)
        )
        self._ui.set_calories_2500cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(2500)
        )
        self._ui.set_calories_3000cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(3000)
        )
        self._ui.set_calories_3500cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(3500)
        )
        self._ui.set_calories_4000cal_action.triggered.connect(
            lambda: self._main_controller.change_max_calories(4000)
        )


        # self.reset_values_action.triggered.connect(self.reset_app_toggler)

        # self._ui.minimize_button.triggered.connect(
        #     lambda: self._main_controller.change_max_water(self._model.max_water_change)
        # )

        # def default_max_water(self): ??? why did i make this
        #     lambda: self._main_controller.change_max_water(self._model.max_water_change)
        # default_max_water(self)
        # self._ui.pushButton_delete.clicked.connect(lambda: self._main_controller.delete_user(self._ui.listWidget_names.currentRow()))

        ###
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # # if model sends/emits a signal the ui gets notified
        ###

        # CONNECT MODEL SIGNAL to corresponding main_view slot
        self._model.water_changed.connect(self.on_water_changed)
        self._model.max_water_changed.connect(self.on_max_water_changed)

        self._model.calories_changed.connect(self.on_calories_changed)
        self._model.max_calories_changed.connect(self.on_max_calories_changed)
        
        self._model.human_bar_changed.connect(self.on_human_bar_changed)
        self._model.light_changed.connect(self.on_light_changed)

        self._model.app_reset.connect(self.on_app_reset)
        self._model.current_time_set.connect(self.on_current_time_set)

        self._model.meal_logged.connect(self.on_meal_logged)


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
        self._ui.water_number.setProperty('intValue', value / 100)

    @pyqtSlot(int)
    def on_max_water_changed(self, value):
        print('main view on MAX water changed')
        print('value:', value)
        self._ui.max_water_number.setProperty('intValue', value / 100)
        if self._model._current_water >= self._model._max_water:
            self._model._current_water = self._model._max_water
            self._ui.water_number.setProperty(
                'intValue', self._model._max_water / 100
            )
            self._ui.water_bar.setProperty('value', self._model._current_water)
        self._ui.human_bar.setMaximum(
            self._model._max_water + self._model._max_calories
        )
        self._ui.water_bar.setMaximum(self._model._max_water)
        self._ui.human_bar.setProperty(
            'value', self._model._current_water + self._model._current_calories
        )


    @pyqtSlot(int)
    def on_max_calories_changed(self, value):
        print('main view on MAX calories changed')
        print('value:', value)
        self._ui.max_calories_number.setProperty('intValue', value)
        if self._model._current_calories >= self._model._max_calories:
            self._model._current_calories = self._model._max_calories
            self._ui.cal_number.setProperty(
                'intValue', self._model._max_calories)
            self._ui.cal_bar.setProperty('value', self._model._current_calories)
        self._ui.human_bar.setMaximum(
            self._model._max_water + self._model._max_calories
        )
        self._ui.cal_bar.setMaximum(self._model._max_calories)
        self._ui.human_bar.setProperty(
            'value', self._model._current_water + self._model._current_calories
        )



    @pyqtSlot(int)
    def on_calories_changed(self, value):
        print('MV on calories changed')
        print(value)
        self._ui.cal_bar.setProperty('value', value)
        self._ui.cal_number.setProperty('intValue', value)


    @pyqtSlot(int)
    def on_human_bar_changed(self, value):
        print('MV on human bar changed')
        print(value)
        self._ui.human_bar.setProperty('value', value)

    
    @pyqtSlot()
    def on_app_reset(self):
        self._model._current_water = 0
        self._ui.water_bar.setProperty('value', self._model._current_water)
        self._ui.water_number.setProperty('intValue', self._model._current_water)
        self._model._current_calories = 0
        self._ui.cal_bar.setProperty('value', self._model._current_calories)
        self._ui.cal_number.setProperty('intValue', self._model._current_calories)
        self._ui.human_bar.setProperty('value', self._model._current_water + self._model._current_calories)
        self._ui.meal_text.setText(self._model._null_meal)
        self._model._meal_logger_presses = 0
        self._model._saved_hour = QTime(8, 0)
        self._model._saved_min = QTime(8, 0)
        self._ui.hour_edit.setTime(QTime(8, 0))
        self._ui.min_edit.setTime(QTime(8, 0))

    @pyqtSlot()
    def on_current_time_set(self):
        current_time_raw = datetime.datetime.now()
        hour_now_raw = current_time_raw.strftime('%H')
        minute_now_raw = current_time_raw.strftime('%M')
        hour_now = int(hour_now_raw)
        minute_now = int(minute_now_raw)
        hh = QTime(hour_now, 0)
        mm = QTime(0, minute_now)
        self._ui.hour_edit.setTime(hh)
        self._ui.min_edit.setTime(mm)


    @pyqtSlot()
    def on_meal_logged(self):

        self._model._meal_logger_presses += 1
        hourRaw = str(self._ui.hour_edit.time())
        minRaw = str(self._ui.min_edit.time())
        if len(hourRaw) == 24:
            hourSliced = hourRaw[19]
        else:
            hourSliced = hourRaw[19] + hourRaw[20]
        if len(hourSliced) == 1:
            hour = hourSliced.replace(hourSliced, "0" + hourSliced)
        else:
            hour = hourSliced
        if len(minRaw) == 24:
            minSliced = minRaw[22]
        else:
            minSliced = minRaw[22] + minRaw[23]
        if len(minSliced) == 1:
            minutes = minSliced.replace(minSliced, "0" + minSliced)
        else:
            minutes = minSliced
        meal_time = f'Meal at {hour}:{minutes}.'
        
        # good grief what is this abomination
        if self._model._meal_logger_presses == 1:
            self._model._first_meal = '1. ' + meal_time
            self._ui.meal_text.setText(self._model._first_meal)
        
        elif self._model._meal_logger_presses == 2:
            self._model._second_meal = self._model._first_meal + '\n\n2. ' + meal_time
            self._ui.meal_text.setText(self._model._second_meal)
        
        elif self._model._meal_logger_presses == 3:
            self._model._third_meal = self._model._second_meal + '\n\n3. ' + meal_time
            self._ui.meal_text.setText(self._model._third_meal)
        
        elif self._model._meal_logger_presses == 4:
            self._model._fourth_meal = self._model._third_meal + '\n\n4. ' + meal_time
            self._ui.meal_text.setText(self._model._fourth_meal)
        
        elif self._model._meal_logger_presses == 5:
            self._model._fifth_meal = self._model._fourth_meal + '\n\n5. ' + meal_time
            self._ui.meal_text.setText(self._model._fifth_meal)
        
        elif self._model._meal_logger_presses == 6:
            self._model._sixth_meal = self._model._fifth_meal + '\n\n6. ' + meal_time
            self._ui.meal_text.setText(self._model._sixth_meal)
        
        elif self._model._meal_logger_presses > 6:
            self._model._meal_logger_presses = 6


    @pyqtSlot(bool)
    def on_light_changed(self, value):
        if value == True:
            print('MV value true')
            self._ui.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self._ui.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self._ui.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
            
            dark_icon = QtGui.QIcon()
            dark_icon.addPixmap(QtGui.QPixmap("CT_icons/darken.png"))
            self._ui.appearance_button.setIcon(dark_icon)
            self._ui.appearance_button.setToolTip('Darken')

            self._ui.meal_time_button.setStyleSheet(CT_stylesheets.background_light)
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.background_light)
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
            print('MV value false')
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
            self._ui.get_current_time_button.setStyleSheet(CT_stylesheets.background_dark)

            # ??????
            self._ui.hour_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")
            self._ui.min_edit.setStyleSheet("background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white")

            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self._ui.sub_calories_button.setIcon(run_light_icon)
            
            # how the fuck
            # + body

    
    @pyqtSlot(bool)
    def on_reset_app_value_changed(self, value):
        self._ui.reset_values_action.setChecked(self._model.reset_app_value)

    

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