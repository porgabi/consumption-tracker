import tkinter as tk
from tkinter import filedialog
import sys, pyautogui, os, datetime, json, webbrowser
# import fix_qt_import_error    # uncomment when making an exe with pyinstaller
from PyQt5 import QtCore, QtGui, QtWidgets


# data saver
def save_data(self):
    hourRaw = str(self.hourEdit.time())
    minRaw = str(self.minEdit.time())
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
    
    data = {}
    data['saved_variables'] = []
    data['saved_variables'].append({
        'current_calories':    self.current_calories,
        'current_water':       self.current_water,
        'meal_logger_presses': self.meal_logger_presses,
        'light_on':        str(self.light_on),
        'ss_directory':        self.ss_directory,
        'first_meal':          self.first_meal,
        'second_meal':         self.second_meal,
        'third_meal':          self.third_meal,
        'fourth_meal':         self.fourth_meal,
        'fifth_meal':          self.fifth_meal,
        'sixth_meal':          self.sixth_meal,
        'saved_hour':      int(hour),
        'saved_minute':    int(minutes),
        'current_body':        self.current_body,
        'reset_app_value': str(self.reset_app_value),
        'last_time': (self.last_day, self.last_month, self.last_year),
        'max_water':           self.max_water,
        'max_calories':        self.max_calories
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


# MENUBAR FUNCTIONS
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
    self.waterBar.setMaximum(self.max_water)
    self.waterBar.setProperty('value', self.current_water)
    self.human_bar.setMaximum(self.max_human_value)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.waterNumber.setProperty('intValue', (self.current_water / 100))
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
    self.calBar.setMaximum(self.max_calories)
    self.calBar.setProperty('value', self.current_calories)
    self.human_bar.setMaximum(self.max_human_value)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.calNumber.setProperty('intValue', self.current_calories)
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


# TOOLBAR functions
def reset_app(self):
    self.current_water = 0
    self.waterBar.setProperty('value', self.current_water)
    self.waterNumber.setProperty('intValue', self.current_water)
    self.current_calories = 0
    self.calBar.setProperty('value', self.current_calories)
    self.calNumber.setProperty('intValue', self.current_calories)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.mealText.setText(self.null_meal)
    self.meal_logger_presses = 0
    self.saved_hour = QtCore.QTime(8, 0)
    self.saved_min = QtCore.QTime(8, 0)
    self.hourEdit.setTime(QtCore.QTime(8, 0))
    self.minEdit.setTime(QtCore.QTime(8, 0))
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


def image_swapper(self):
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
def water_subtractor(self):
    self.current_water -= 100
    self.waterBar.setProperty('value', self.current_water)
    if self.current_water <= 0:
        self.waterBar.setProperty('value', 0)
        self.current_water = 0
    if self.current_water + self.current_calories <= 0:
        self.human_bar.setProperty('value', 0)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.waterNumber.setProperty('intValue', (self.current_water / 100))
    self.save_data()


def water_adder(self):
    self.waterBar.setProperty('value', self.current_water)
    if self.current_water >= self.max_water:
        self.waterBar.setProperty('value', self.max_water)
        self.current_water = self.max_water
    if self.current_water + self.current_calories >= self.max_human_value:   
        self.human_bar.setProperty('value', self.max_human_value)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.waterNumber.setProperty('intValue', (self.current_water / 100))
    self.save_data()


def waterCupAdder(self):
    self.current_water += 200
    water_adder(self)


def smallBottleAdder(self):
    self.current_water += 500
    water_adder(self)


def largeBottleAdder(self):
    self.current_water += 1000
    water_adder(self)


def calSubtractor(self):
    self.current_calories -= 100
    self.calBar.setProperty('value', self.current_calories)
    if self.current_calories <= 0:
        self.calBar.setProperty('value', 0)
        self.current_calories = 0
    else:
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
    if self.current_water + self.current_calories <= 0:
        self.human_bar.setProperty('value', 0)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.calNumber.setProperty('intValue', self.current_calories)
    self.save_data()


def calories_adder(self):
    self.calBar.setProperty('value', self.current_calories)
    if self.current_calories >= self.max_calories:
        self.calBar.setProperty('value', self.max_calories)
        self.current_calories = self.max_calories
    if self.current_water + self.current_calories >= self.max_human_value:    
        self.human_bar.setProperty('value', self.max_human_value)
    self.human_bar.setProperty('value', self.current_water + self.current_calories)
    self.calNumber.setProperty('intValue', self.current_calories)
    self.save_data()


def sandwichAdder(self):
    self.current_calories += 200
    calories_adder(self)


def eggsAdder(self):
    self.current_calories += 500
    calories_adder(self)


def meatAdder(self):
    self.current_calories += 1000
    calories_adder(self)


# MEAL TIME LOGGING functions
def time_to_current_moment(self):
    current_time_raw = datetime.datetime.now()
    hour_now_raw = current_time_raw.strftime('%H')
    minute_now_raw = current_time_raw.strftime('%M')
    hour_now = int(hour_now_raw)
    minute_now = int(minute_now_raw)
    hh = QtCore.QTime(hour_now, 0)
    mm = QtCore.QTime(0, minute_now)
    self.minEdit.setTime(mm)
    self.hourEdit.setTime(hh)
    self.save_data()


def meal_logger(self):
    self.meal_logger_presses += 1
    hourRaw = str(self.hourEdit.time())
    minRaw = str(self.minEdit.time())
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
        self.mealText.setText(self.first_meal)
    elif self.meal_logger_presses == 2:
        self.second_meal = self.first_meal + '\n\n2. ' + meal_time
        self.mealText.setText(self.second_meal)
    elif self.meal_logger_presses == 3:
        self.third_meal = self.second_meal + '\n\n3. ' + meal_time
        self.mealText.setText(self.third_meal)
    elif self.meal_logger_presses == 4:
        self.fourth_meal = self.third_meal + '\n\n4. ' + meal_time
        self.mealText.setText(self.fourth_meal)
    elif self.meal_logger_presses == 5:
        self.fifth_meal = self.fourth_meal + '\n\n5. ' + meal_time
        self.mealText.setText(self.fifth_meal)
    elif self.meal_logger_presses == 6:
        self.sixth_meal = self.fifth_meal + '\n\n6. ' + meal_time
        self.mealText.setText(self.sixth_meal)
    elif self.meal_logger_presses > 6:
        self.meal_logger_presses = 6
    self.save_data()
