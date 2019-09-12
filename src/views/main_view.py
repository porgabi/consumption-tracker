# presents data to the user, doesn't call its own methods

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow
import tkinter as tk
from tkinter import filedialog
import sys, pyautogui, os, datetime, json, webbrowser
# import fix_qt_import_error    # uncomment when making an exe with pyinstaller
from PyQt5 import QtCore, QtGui, QtWidgets
import CT_stylesheets


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

    def save_data(self):
        hourRaw = str(self.hour_edit.time())
        minRaw = str(self.min_edit.time())
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

        self.last_day = datetime.datetime.now().day
        self.last_month = datetime.datetime.now().month
        self.last_year = datetime.datetime.now().year

        saved_data = {}
        saved_data['current_water'] = self.current_water
        saved_data['current_calories'] = self.current_calories
        saved_data['meal_logger_presses'] = self.meal_logger_presses
        saved_data['light_on'] = str(self.light_on)
        saved_data['ss_directory'] = self.ss_directory
        saved_data['first_meal'] = self.first_meal
        saved_data['second_meal'] = self.second_meal
        saved_data['third_meal'] = self.third_meal
        saved_data['fourth_meal'] = self.fourth_meal
        saved_data['fifth_meal'] = self.fifth_meal
        saved_data['sixth_meal'] = self.sixth_meal
        saved_data['saved_hour'] = int(hour)
        saved_data['saved_minute'] = int(minutes)
        saved_data['current_body'] = self.current_body
        saved_data['reset_app_value'] = str(self.reset_app_value)
        saved_data['last_time'] = (self.last_day, self.last_month, self.last_year)
        saved_data['max_water'] = self.max_water
        saved_data['max_calories'] = self.max_calories

        with open('saved_data.json', 'w') as outfile:
            json.dump(saved_data, outfile, indent=4)


    # menu_bar FUNCTIONS
    def select_directory(self):
        root = tk.Tk()
        root.withdraw()
        self.ss_directory_new = filedialog.askdirectory()
        if self.ss_directory_new == "":
            pass
        else:
            self.ss_directory = self.ss_directory_new
            self.save_data()


    def reset_app_toggler(self, state):
        if state:
            self.reset_app_value = True
        else:
            self.reset_app_value = False
        self.save_data()


    def set_water(self):
        self.max_human_value = self.max_water + self.max_calories
        if self.max_water <= self.current_water:
            self.current_water = self.max_water
        self.water_bar.setMaximum(self.max_water)
        self.water_bar.setProperty('value', self.current_water)
        self.human_bar.setMaximum(self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.water_number.setProperty('intValue', (self.current_water / 100))
        self.max_water_number.setProperty("intValue", self.max_water / 100)
        self.save_data()


    def set_water_to_10dl(self):
        self.max_water = 1000
        set_water(self)

    def set_water_to_15dl(self):
        self.max_water = 1500
        set_water(self)


    def set_water_to_20dl(self):
        self.max_water = 2000
        set_water(self)


    def set_water_to_25dl(self):
        self.max_water = 2500
        set_water(self)


    def set_water_to_30dl(self):
        self.max_water = 3000
        set_water(self)


    def set_water_to_35dl(self):
        self.max_water = 3500
        set_water(self)


    def set_water_to_40dl(self):
        self.max_water = 4000
        set_water(self)


    def set_calories(self):
        self.max_human_value = self.max_water + self.max_calories
        if self.max_calories <= self.current_calories:
            self.current_calories = self.max_calories
        self.cal_bar.setMaximum(self.max_calories)
        self.cal_bar.setProperty('value', self.current_calories)
        self.human_bar.setMaximum(self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.cal_number.setProperty('intValue', self.current_calories)
        self.max_calories_number.setProperty("intValue", self.max_calories)
        self.save_data()


    def set_calories_to_1000(self):
        self.max_calories = 1000
        set_calories(self)


    def set_calories_to_1500(self):
        self.max_calories = 1500
        set_calories(self)


    def set_calories_to_2000(self):
        self.max_calories = 2000
        set_calories(self)


    def set_calories_to_2500(self):
        self.max_calories = 2500
        set_calories(self)


    def set_calories_to_3000(self):
        self.max_calories = 3000
        set_calories(self)


    def set_calories_to_3500(self):
        self.max_calories = 3500
        set_calories(self)


    def set_calories_to_4000(self):
        self.max_calories = 4000
        set_calories(self)


    def open_about(self):
        if self.light_on is False:
            app.setStyleSheet(CT_stylesheets.app_open_about1)
            QtWidgets.QMessageBox.information(MainWindow,
                'About CT', 
                "Version: v1.0.0\nRelease date: 03/09/2019\nMade in: Python 3.6.0/PyQt5 5.13.0\nTested on: Windows 10 (x64)",
                QtWidgets.QMessageBox.Ok)
            app.setStyleSheet(CT_stylesheets.app_open_about2)
        else:
            QtWidgets.QMessageBox.information(MainWindow,
                'About CT', 
                "Version: v1.0.0\nRelease date: 03/09/2019\nMade in: Python 3.6.0/PyQt5 5.13.0\nTested on: Windows 10 (x64)",
                QtWidgets.QMessageBox.Ok)


    def open_project_page(self):
        if self.light_on is False:
            app.setStyleSheet(CT_stylesheets.app_open_project1)          
            choice = QtWidgets.QMessageBox.question(MainWindow, 
                'View project page', 'This will open a new browser tab.', 
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Ok:
                webbrowser.open_new_tab('https://github.com/porgabi/consumption-tracker')
            app.setStyleSheet(CT_stylesheets.app_open_project2)
        else:
            choice = QtWidgets.QMessageBox.question(MainWindow, 
                'View project page', 'This will open a new browser tab.', 
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Ok:
                webbrowser.open_new_tab('https://github.com/porgabi/consumption-tracker')



    # tool bar functions
    def reset_app(self):
        self.current_water = 0
        self.water_bar.setProperty('value', self.current_water)
        self.water_number.setProperty('intValue', self.current_water)
        self.current_calories = 0
        self.cal_bar.setProperty('value', self.current_calories)
        self.cal_number.setProperty('intValue', self.current_calories)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.meal_text.setText(self.null_meal)
        self.meal_logger_presses = 0
        self.saved_hour = QtCore.QTime(8, 0)
        self.saved_min = QtCore.QTime(8, 0)
        self.hour_edit.setTime(QtCore.QTime(8, 0))
        self.min_edit.setTime(QtCore.QTime(8, 0))
        self.save_data()


    def take_screenshot(self):
        # frame_pos_raw = str(MainWindow.frameGeometry())   
        frame_pos_string = self.frame_pos_raw.replace('PyQt5.QtCore.QRect', '')
        frame_pos = eval(frame_pos_string)        
        ss = pyautogui.screenshot(imageFilename=None, region=frame_pos)
        current_time_raw = datetime.datetime.now()
        current_time = current_time_raw.strftime('%H-%M-%S_%d-%m-%Y')
        
        if self.ss_directory == "":
            try:
                os.mkdir(self.home_path + '\\CT_screenshots')
            except FileExistsError:
                pass
            self.ss_directory = self.home_path + '\\CT_screenshots'            
            ss.save(self.ss_directory + '\\' + current_time + '.png')
        else:
            ss.save(self.ss_directory + '\\' + current_time + '.png')
        self.save_data()


    def switch_appearance(self):
        if self.light_on == True:
            self.light_on = False
            light_icon = QtGui.QIcon()
            light_icon.addPixmap(QtGui.QPixmap("CT_icons/lighten.png"))
            self.appearance_button.setIcon(light_icon)
            self.appearance_button.setToolTip('Lighten')
            self.dark_palette = QtGui.QPalette()
            self.dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(90, 90, 90))
            app.setPalette(self.dark_palette)
            
            self.sub_water_button.setStyleSheet(CT_stylesheets.background_dark)
            self.glass_button.setStyleSheet(CT_stylesheets.background_dark)
            self.small_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self.large_bottle_button.setStyleSheet(CT_stylesheets.background_dark)
            self.sub_calories_button.setStyleSheet(CT_stylesheets.background_dark)
            self.sandwich_button.setStyleSheet(CT_stylesheets.background_dark)
            self.eggs_button.setStyleSheet(CT_stylesheets.background_dark)
            self.meat_button.setStyleSheet(CT_stylesheets.background_dark)
            self.water_bar.setStyleSheet(CT_stylesheets.water_bar_dark)
            self.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_dark)

            app.setStyleSheet(CT_stylesheets.tooltip_dark)
            self.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_dark)

            # TODO include water menu style in menu_bar stylesheet
            self.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)
            self.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_dark)

            self.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_dark)
            self.meal_time_button.setStyleSheet(CT_stylesheets.background_dark)
            self.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_dark)

            self.hour_edit.setStyleSheet(CT_stylesheets.time_edit_dark)
            self.min_edit.setStyleSheet(CT_stylesheets.time_edit_dark)
            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self.sub_calories_button.setIcon(run_light_icon)
            
            if self.human_image_is_malebodylight == True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))
                self.human_image_is_malebodydark = True
                self.current_body = 'male_dark'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodydark.png"))
                self.current_body = 'female_dark'
            self.save_data()
        else:
            self.light_on = True
            dark_icon = QtGui.QIcon()
            dark_icon.addPixmap(QtGui.QPixmap("CT_icons/darken.png"))
            self.appearance_button.setIcon(dark_icon)
            self.appearance_button.setToolTip('Darken')
            self.light_palette = QtGui.QPalette()
            self.light_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))
            app.setPalette(self.light_palette)
            app.setStyleSheet(CT_stylesheets.tooltip_light)

            self.meal_time_button.setStyleSheet(CT_stylesheets.background_light)
            self.get_current_time_button.setStyleSheet(CT_stylesheets.time_edit_light)
            self.sub_water_button.setStyleSheet(CT_stylesheets.background_light)
            self.glass_button.setStyleSheet(CT_stylesheets.background_light)
            self.small_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self.large_bottle_button.setStyleSheet(CT_stylesheets.background_light)
            self.sub_calories_button.setStyleSheet(CT_stylesheets.background_light)
            self.sandwich_button.setStyleSheet(CT_stylesheets.background_light)
            self.eggs_button.setStyleSheet(CT_stylesheets.background_light)
            self.meat_button.setStyleSheet(CT_stylesheets.background_light)
            self.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
            self.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
            self.menu_bar.setStyleSheet(CT_stylesheets.menu_bar_light)
            self.set_water_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self.set_calories_menu.setStyleSheet(CT_stylesheets.secondary_menu_light)
            self.tool_bar.setStyleSheet(CT_stylesheets.tool_bar_light)

            self.hour_edit.setStyleSheet(CT_stylesheets.time_edit_light)
            self.min_edit.setStyleSheet(CT_stylesheets.time_edit_light)
            sub_cal_icon_dark = QtGui.QIcon()
            sub_cal_icon_dark.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
            self.sub_calories_button.setIcon(sub_cal_icon_dark)
            
            if self.human_image_is_malebodydark == True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
                self.human_image_is_malebodydark = False
                self.human_image_is_malebodylight = True
                self.current_body = 'male_light'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodylight.png"))
                self.human_image_is_malebodydark = False
                self.human_image_is_malebodylight = False
                self.current_body = 'female_light'
            self.save_data()


    def swap_body_image(self):
        if self.light_on is True:
            if self.human_image_is_malebodylight is True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodylight.png"))
                self.human_image_is_malebodylight = False
                self.current_body = 'female_light'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
                self.human_image_is_malebodylight = True
                self.current_body = 'male_light'
        else:
            if self.human_image_is_malebodydark is True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodydark.png"))
                self.human_image_is_malebodydark = False
                self.current_body = 'female_dark'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))
                self.human_image_is_malebodydark = True
                self.current_body = 'male_dark'
        self.save_data()


    # WATER MANAGEMENT functions
    def subtract_water(self):
        self.current_water -= 100
        self.water_bar.setProperty('value', self.current_water)
        if self.current_water <= 0:
            self.water_bar.setProperty('value', 0)
            self.current_water = 0
        if self.current_water + self.current_calories <= 0:
            self.human_bar.setProperty('value', 0)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.water_number.setProperty('intValue', (self.current_water / 100))
        self.save_data()


    def water_adder(self):
        self.water_bar.setProperty('value', self.current_water)
        if self.current_water >= self.max_water:
            self.water_bar.setProperty('value', self.max_water)
            self.current_water = self.max_water
        if self.current_water + self.current_calories >= self.max_human_value:   
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.water_number.setProperty('intValue', (self.current_water / 100))
        self.save_data()


    def add_glass(self):
        self.current_water += 200
        water_adder(self)


    def add_small_bottle(self):
        self.current_water += 500
        water_adder(self)


    def add_large_bottle(self):
        self.current_water += 1000
        water_adder(self)


    def subtract_calories(self):
        self.current_calories -= 100
        self.cal_bar.setProperty('value', self.current_calories)
        if self.current_calories <= 0:
            self.cal_bar.setProperty('value', 0)
            self.current_calories = 0
        else:
            self.human_bar.setProperty('value', self.current_water + self.current_calories)
        if self.current_water + self.current_calories <= 0:
            self.human_bar.setProperty('value', 0)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.cal_number.setProperty('intValue', self.current_calories)
        self.save_data()


    def calories_adder(self):
        self.cal_bar.setProperty('value', self.current_calories)
        if self.current_calories >= self.max_calories:
            self.cal_bar.setProperty('value', self.max_calories)
            self.current_calories = self.max_calories
        if self.current_water + self.current_calories >= self.max_human_value:    
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.cal_number.setProperty('intValue', self.current_calories)
        self.save_data()


    def add_sandwich(self):
        self.current_calories += 200
        calories_adder(self)


    def add_eggs(self):
        self.current_calories += 500
        calories_adder(self)


    def add_meat(self):
        self.current_calories += 1000
        calories_adder(self)


    # MEAL TIME LOGGING functions
    def set_time_to_present(self):
        current_time_raw = datetime.datetime.now()
        hour_now_raw = current_time_raw.strftime('%H')
        minute_now_raw = current_time_raw.strftime('%M')
        hour_now = int(hour_now_raw)
        minute_now = int(minute_now_raw)
        hh = QtCore.QTime(hour_now, 0)
        mm = QtCore.QTime(0, minute_now)
        self.min_edit.setTime(mm)
        self.hour_edit.setTime(hh)
        self.save_data()


    def meal_logger(self):
        self.meal_logger_presses += 1
        hourRaw = str(self.hour_edit.time())
        minRaw = str(self.min_edit.time())
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
        if self.meal_logger_presses == 1:
            self.first_meal = '1. ' + meal_time
            self.meal_text.setText(self.first_meal)
        elif self.meal_logger_presses == 2:
            self.second_meal = self.first_meal + '\n\n2. ' + meal_time
            self.meal_text.setText(self.second_meal)
        elif self.meal_logger_presses == 3:
            self.third_meal = self.second_meal + '\n\n3. ' + meal_time
            self.meal_text.setText(self.third_meal)
        elif self.meal_logger_presses == 4:
            self.fourth_meal = self.third_meal + '\n\n4. ' + meal_time
            self.meal_text.setText(self.fourth_meal)
        elif self.meal_logger_presses == 5:
            self.fifth_meal = self.fourth_meal + '\n\n5. ' + meal_time
            self.meal_text.setText(self.fifth_meal)
        elif self.meal_logger_presses == 6:
            self.sixth_meal = self.fifth_meal + '\n\n6. ' + meal_time
            self.meal_text.setText(self.sixth_meal)
        elif self.meal_logger_presses > 6:
            self.meal_logger_presses = 6
        self.save_data()
