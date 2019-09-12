# handles data, defines rules and behaviour
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore
import json, datetime, os

class Model(QObject):
    
    water_changed = pyqtSignal(int)
    
    @property
    def water(self):
        return self.current_water


    def add_water(self, value):
        # variable modified here
        self._users.append(value)
        
        self.current_water += 200
        print(self.current_water)
        print('model add user')

        self.water_changed.emit(self.current_water)

    
    
    
    
    
    
    
    
    
    
    
    def __init__(self):
        super().__init__()
        if 'saved_data.json' in os.listdir():
            with open('saved_data.json') as json_file:
                saved_data = json.load(json_file)
                self.current_calories = saved_data.get('current_calories')
                self.current_water = saved_data.get('current_water')
                self.meal_logger_presses = saved_data.get('meal_logger_presses')
                self.light_on = bool('True' == saved_data.get('light_on'))
                self.current_body = saved_data.get('current_body')
                self.ss_directory = saved_data.get('ss_directory')
                self.null_meal = ''
                self.first_meal = saved_data.get('first_meal')
                self.second_meal = saved_data.get('second_meal')
                self.third_meal = saved_data.get('third_meal')
                self.fourth_meal = saved_data.get('fourth_meal')
                self.fifth_meal = saved_data.get('fifth_meal')
                self.sixth_meal = saved_data.get('sixth_meal')
                saved_hour_raw = saved_data.get('saved_hour')
                self.saved_hour = QtCore.QTime(saved_hour_raw, 0)
                saved_min_raw = saved_data.get('saved_minute')
                self.saved_min = QtCore.QTime(0, saved_min_raw)
                self.reset_app_value = bool('True' == saved_data.get('reset_app_value'))
                self.current_time_raw = datetime.datetime.now()
                self.current_time = datetime.datetime(self.current_time_raw.year,
                                                        self.current_time_raw.month,
                                                        self.current_time_raw.day)
                self.last_time = saved_data.get('last_time')
                self.previous_time = datetime.datetime(self.last_time[2],\
                                                        self.last_time[1],\
                                                        self.last_time[0])
                self.max_water = saved_data.get('max_water')
                self.max_calories = saved_data.get('max_calories')
        else:
            # default values
            self.current_calories = 0
            self.current_water = 0
            self.meal_logger_presses = 0
            self.light_on = True
            self.current_body = 'male_light'
            self.ss_directory = ""
            self.null_meal = ''
            self.first_meal = ""
            self.second_meal = ""
            self.third_meal = ""
            self.fourth_meal = ""
            self.fifth_meal = ""
            self.sixth_meal = ""
            self.saved_hour = QtCore.QTime(8, 0)
            self.saved_min = QtCore.QTime(0, 0)
            self.reset_app_value = False
            self.current_time_raw = datetime.datetime.now()
            self.current_time = datetime.datetime(self.current_time_raw.year,
                                                  self.current_time_raw.month,
                                                  self.current_time_raw.day)
            self.previous_time = self.current_time
            self.max_water = 3000
            self.max_calories = 2500
        self.max_human_value = (self.max_water + self.max_calories)
        self.home_path = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
