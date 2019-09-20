from PyQt5.QtCore import QObject, pyqtSignal, QTime
import datetime


class Model(QObject):

    # amount_changed = pyqtSignal(int)
    # even_odd_changed = pyqtSignal(str)
    # enable_reset_changed = pyqtSignal(bool)
    # users_changed = pyqtSignal(list)
    water_changed = pyqtSignal(int)
    max_water_changed = pyqtSignal(int)
    calories_changed = pyqtSignal(int)
    max_calories_changed = pyqtSignal(int)
    human_bar_changed = pyqtSignal(int)
    light_changed = pyqtSignal(bool)
    reset_app_value_changed = pyqtSignal(bool)
    app_reset = pyqtSignal()
    current_time_set = pyqtSignal()
    meal_logged = pyqtSignal()

    # @property
    # def water(self):
    #     return self._current_water

    # @property
    # def users(self):
    #     return self._users

    def add_water(self, value):
        print('MODEL add water')
        # variable modified here
        # self._users.append(value)
        self._current_water += value
        if self._current_water >= self._max_water:
            self._current_water = self._max_water
        print('MODEL current water', self._current_water)
        self.water_changed.emit(self._current_water)

    def change_max_water(self, value):
        print('MODEL change max water')
        self._max_water = value
        self.max_water_changed.emit(self._max_water)

    def sub_water(self, value):
        print('MODEL sub water')
        self._current_water -= value
        if self._current_water <= 0:
            self._current_water = 0
        print('MODEL current water', self._current_water)
        self.water_changed.emit(self._current_water)


    def add_calories(self, value):
        print('MODEL add calories')
        self._current_calories += value
        if self._current_calories >= self._max_calories:
            self._current_calories = self._max_calories
        print('MODEL current calories', self._current_calories)
        self.calories_changed.emit(self._current_calories)

    def change_max_calories(self, value):
        print('MODEL change max calories')
        self._max_calories = value
        self.max_calories_changed.emit(self._max_calories)

    def sub_calories(self, value):
        print('MODEL sub calories')
        self._current_calories -= value
        if self._current_calories <= 0:
            self._current_calories = 0

        print('MODEL current calories', self._current_calories)
        self.calories_changed.emit(self._current_calories)

    def change_human_bar(self, value):
        print('MODEL change human bar')
        self.human_bar_changed.emit(self._current_water + self._current_calories)

    def change_light(self, value):
        print('\nMODEL change light')
        print('value', value)
        # if value is True:
        #     value = False
        #     self.light_changed.emit(value)

        # else:
        #     value = True
        #     self.light_changed.emit(value)
        self.light_changed.emit(value)

        print('emitted value', value)

    def reset_app(self):
        self.app_reset.emit()

    def set_to_current_time(self):
        self.current_time_set.emit()

    def log_meal(self):
        self.meal_logged.emit()

    def change_reset_app_value(self, value):
        self.reset_app_value_changed.emit(value)


    # def change_water_bar(self, value):
    #     print('MODEL change water bar')

    # def delete_user(self, value):
    #     del self._users[value]
    #     self.users_changed.emit(self._users)

    @property
    def water_bar_change(self):
        return self._current_water

    @water_bar_change.setter
    def water_bar_change(self, value):
        self._current_water = value
        self.water_changed.emit(value)

    @property
    def max_water_change(self):
        return self._max_water

    @max_water_change.setter
    def max_water_change(self, value):
        self._max_water = value
        self.max_water_changed.emit(value)

    @property
    def cal_bar_change(self):
        return self._current_calories

    @cal_bar_change.setter
    def cal_bar_change(self, value):
        self._current_calories = value
        self.calories_changed.emit(value)

    @property
    def max_calories_change(self):
        return self._max_calories

    @max_calories_change.setter
    def max_calories_change(self, value):
        self._max_calories = value
        self.max_calories_changed.emit(value)

    @property
    def human_bar_change(self):
        return self._current_human_value

    @human_bar_change.setter
    def human_bar_change(self, value):
        self._current_human_value = value
        self.human_bar_changed.emit(value)

    @property
    def light_change(self):
        return self._light_on

    @light_change.setter
    def light_change(self, value):
        self._light_on = value
        self.light_changed.emit(value)

    @property
    def reset_app_value_change(self):
        return self._reset_app_value
    
    @reset_app_value_change.setter
    def reset_app_value_change(self, value):
        self._reset_app_value = value
        self.reset_app_value_changed.emit(value)



    def __init__(self):
        super().__init__()

        # variables defined here
        self._current_water = 1000
        self._max_water = 2000
        self._current_calories = 2500
        self._max_calories = 3000
        self._max_human_value = self._max_water + self._max_calories
        self._current_human_value = self._current_water + self._current_calories
        self._light_on = True
        self._meal_logger_presses = 4
        self._current_body = 'male_light'
        self._ss_directory = ""
        self._null_meal = ''
        self._first_meal = '1. Meal at 08:00.'
        self._second_meal = '1. Meal at 08:00. \n2. Meal at 12:00.'
        self._third_meal = '1. Meal at 08:00. \n2. Meal at 12:00. \n3. Meal at 16:00.'
        self._fourth_meal = '1. Meal at 08:00. \n2. Meal at 12:00. \n3. Meal at 16:00. \n4. Meal at 20:00.'
        self._fifth_meal = "5"
        self._sixth_meal = "6"
        self._saved_hour = QTime(8, 0)
        self._saved_min = QTime(0, 0)
        self._reset_app_value = True
        self._current_time_raw = datetime.datetime.now()
        self._current_time = datetime.datetime(
            self._current_time_raw.year,
            self._current_time_raw.month,
            self._current_time_raw.day
        )
        self._previous_time = self._current_time




    # @property
    # def amount(self):
    #     return self._amount

    # @amount.setter
    # def amount(self, value):
    #     self._amount = value
    #     self.amount_changed.emit(value)







    # @property
    # def even_odd(self):
    #     return self._even_odd

    # @even_odd.setter
    # def even_odd(self, value):
    #     self._even_odd = value
    #     self.even_odd_changed.emit(value)

    # @property
    # def enable_reset(self):
    #     return self._enable_reset

    # @enable_reset.setter
    # def enable_reset(self, value):
    #     self._enable_reset = value
    #     self.enable_reset_changed.emit(value)

    # starter values?

        # self._users = ["hans"]