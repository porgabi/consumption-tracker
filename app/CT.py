import tkinter as tk
from tkinter import filedialog
import sys, pyautogui, os, datetime, json, webbrowser
# import fix_qt_import_error    # uncomment when making an exe with pyinstaller
from PyQt5 import QtCore, QtGui, QtWidgets


class ConsumptionTracker():

    def setupUi(self, MainWindow):
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
    
        if 'data.json' in os.listdir():
            with open('data.json') as json_file:
                data = json.load(json_file)
                for i in data['saved_variables']:
                    if "current_calories" in i:
                        self.current_calories = i['current_calories']
                    if 'current_water' in i:
                        self.current_water = i['current_water']
                    if 'meal_logger_presses' in i:
                        self.meal_logger_presses = i['meal_logger_presses']
                    if 'light_on' in i:
                        self.light_on = bool('True' == i['light_on'])
                    if 'current_body' in i:
                        self.current_body = i['current_body']
                    if 'ss_directory' in i:
                        self.ss_directory = i['ss_directory']
                    if 'first_meal' in i:
                        self.first_meal = i['first_meal']
                    if 'second_meal' in i:
                        self.second_meal = i['second_meal']
                    if 'third_meal' in i:
                        self.third_meal = i['third_meal']
                    if 'fourth_meal' in i:
                        self.fourth_meal = i['fourth_meal']
                    if 'fifth_meal' in i:
                        self.fifth_meal = i['fifth_meal']
                    if 'sixth_meal' in i:
                        self.sixth_meal = i['sixth_meal']
                    if 'saved_hour' in i:
                        saved_hour_raw = i['saved_hour']
                    if 'saved_minute' in i:                    
                        saved_min_raw = i['saved_minute']
                    if 'reset_app_value' in i:
                        self.reset_app_value = bool('True' == i['reset_app_value'])
                    if 'last_time' in i:
                        self.last_time = i['last_time']
                        self.previous_time = datetime.datetime(self.last_time[2],\
                                                               self.last_time[1],\
                                                               self.last_time[0])
                    if 'max_water' in i:
                        self.max_water = i['max_water']
                    if 'max_calories' in i:
                        self.max_calories = i['max_calories']
                    self.saved_hour = QtCore.QTime(saved_hour_raw, 0)
                    self.saved_min = QtCore.QTime(0, saved_min_raw)
        
        self.max_human_value = (self.max_water + self.max_calories)
        self.home_path = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 700)
        window_geometry = MainWindow.frameGeometry()
        screen_center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(screen_center_point)
        MainWindow.move(window_geometry.topLeft())
        main_icon = QtGui.QIcon()
        main_icon.addPixmap(QtGui.QPixmap("CT_icons\\main.png"), 
                            QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(main_icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # tray icon
        self.tray = QtWidgets.QSystemTrayIcon(main_icon, app)
        self.tray.activated['QSystemTrayIcon::ActivationReason'].connect(self.tray_icon_click)
        self.tray.setToolTip('Consumption Tracker')
        
        # human image
        self.human_image = QtWidgets.QLabel(self.centralwidget)
        self.human_image.setGeometry(QtCore.QRect(55, 10, 167, 500))
        self.human_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.human_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.human_image.setText("")
        self.human_image.setStyleSheet("border: 0px solid transparent;\n")
        
        if self.current_body == "male_light":
            self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
            self.human_image_is_malebodylight = True
            self.human_image_is_malebodydark = False
        elif self.current_body == "female_light":
            self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodylight.png"))
            self.human_image_is_malebodylight = False
            self.human_image_is_malebodydark = False
        elif self.current_body == "male_dark":
            self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))
            self.human_image_is_malebodydark = True
            self.human_image_is_malebodylight = False
        elif self.current_body == "female_dark":
            self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodydark.png"))
            self.human_image_is_malebodydark = False
            self.human_image_is_malebodylight = False
        self.human_image.setScaledContents(True)
        self.human_image.setObjectName("human_image")
        
        # progress bar behind body silhouette
        self.human_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.human_bar.setGeometry(QtCore.QRect(55, 10, 167, 500))
        self.human_bar.setStyleSheet("QProgressBar{\n"
        "border: 1px solid transparent;\n"
        "text-align: center;\n"
        "color:rgba(0,0,0,100);\n"
        "border-radius: 5px;\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(182, 182, 182, 100), stop:1 rgba(209, 209, 209, 100));}\n"
        "\n"
        "QProgressBar::chunk{\n"
        "background-color: qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.494, y2:0, stop: 0 rgba(21, 158, 71, 255), stop: 1 rgba(32, 201, 90, 255));}")
        self.human_bar.setMaximum(self.max_human_value)
        self.human_bar.setProperty("value", self.current_water + self.current_calories)
        self.human_bar.setTextVisible(False)
        self.human_bar.setOrientation(QtCore.Qt.Vertical)
        self.human_bar.setObjectName("human_bar")
        self.human_bar.raise_()
        self.human_image.raise_()        
        
        # water progress bar
        self.waterBar = QtWidgets.QProgressBar(self.centralwidget)
        self.waterBar.setGeometry(QtCore.QRect(20, 514, 250, 36))
        if self.light_on == True:
            self.waterBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: white;\n"
            "padding: 0px;\n"
            "font: 19pt \"Segoe UI\";\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));\n"
            "}\n"
            "QProgressBar {"
            "color: black;"
            "font: 15px"
            "}")
        else:
            self.waterBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: rgb(90, 90, 90);\n"
            "font: 75 12pt \"Segoe UI\";\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));\n"
            "}\n"
            "QProgressBar {"
            "color: white;"
            "font: 15px"
            "}")
        self.waterBar.setMaximum(self.max_water)
        self.waterBar.setProperty('value', self.current_water)
        self.waterBar.setObjectName("waterBar")        

        # calories progress bar
        self.calBar = QtWidgets.QProgressBar(self.centralwidget)
        self.calBar.setGeometry(QtCore.QRect(20, 564, 250, 36))
        if self.light_on == True:
            self.calBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: white;\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));\n"
            "\n"
            "}\n"
            "QProgressBar {"
            "color: black;"
            "font: 15px"
            "}")
        else:
            self.calBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: rgb(90, 90, 90);\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));\n"
            "\n"
            "}\n"
            "QProgressBar {"
            "color: white;"
            "font: 15px"
            "}")
        self.calBar.setMaximum(self.max_calories)
        self.calBar.setProperty("value", self.current_calories)        
        self.calBar.setOrientation(QtCore.Qt.Horizontal)
        self.calBar.setObjectName("calBar")
        
        # current calories LCD display
        self.calNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.calNumber.setGeometry(QtCore.QRect(270, 560, 100, 42))
        self.calNumber.setStyleSheet("color: rgba(255, 130, 0, 255);")
        self.calNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.calNumber.setDigitCount(4)
        self.calNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.calNumber.setProperty("intValue", self.current_calories)
        self.calNumber.setObjectName("calNumber")

        # calNumberLCD per label
        self.calories_LCD_per_sign = QtWidgets.QLabel(self.centralwidget)
        self.calories_LCD_per_sign.setGeometry(QtCore.QRect(360, 557, 20, 42))
        self.calories_LCD_per_sign.setStyleSheet("font: 30pt \"Segoe UI\";""color: rgba(255, 130, 0, 255)")
        self.calories_LCD_per_sign.setScaledContents(False)
        self.calories_LCD_per_sign.setAlignment(QtCore.Qt.AlignVCenter)
        self.calories_LCD_per_sign.setWordWrap(True)
        self.calories_LCD_per_sign.setIndent(-1)
        self.calories_LCD_per_sign.setObjectName("calories_LCD_per_sign")

        # max calories LCD display
        self.max_calories_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.max_calories_number.setGeometry(QtCore.QRect(364, 560, 100, 42))
        self.max_calories_number.setStyleSheet("color: rgba(255, 130, 0, 255);")
        self.max_calories_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.max_calories_number.setDigitCount(4)
        self.max_calories_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.max_calories_number.setProperty("intValue", self.max_calories)
        self.max_calories_number.setObjectName("max_calories_number")

        # calories unit label
        self.calories_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.calories_unit_label.setGeometry(QtCore.QRect(460, 560, 30, 42))
        self.calories_unit_label.setStyleSheet("font: 20pt \"Candara\";""color: rgba(255, 130, 0, 255)")
        self.calories_unit_label.setScaledContents(False)
        self.calories_unit_label.setAlignment(QtCore.Qt.AlignBottom)
        self.calories_unit_label.setWordWrap(True)
        self.calories_unit_label.setIndent(-1)
        self.calories_unit_label.setObjectName("calories_unit_label")

        # current water LCD display
        self.waterNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.waterNumber.setGeometry(QtCore.QRect(290, 510, 100, 42))
        self.waterNumber.setStyleSheet("color: rgb(64, 164, 223);")
        self.waterNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.waterNumber.setDigitCount(2)
        self.waterNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.waterNumber.setProperty("intValue", (self.current_water / 100))
        self.waterNumber.setObjectName("waterNumber")

        # waterLCD per label
        self.water_LCD_per_sign = QtWidgets.QLabel(self.centralwidget)
        self.water_LCD_per_sign.setGeometry(QtCore.QRect(360, 507, 20, 42))
        self.water_LCD_per_sign.setStyleSheet("font: 30pt \"Segoe UI\";""color: rgb(64, 164, 223)")
        self.water_LCD_per_sign.setScaledContents(False)
        self.water_LCD_per_sign.setAlignment(QtCore.Qt.AlignVCenter)
        self.water_LCD_per_sign.setWordWrap(True)
        self.water_LCD_per_sign.setIndent(-1)
        self.water_LCD_per_sign.setObjectName("water_LCD_per_sign")

        # max water LCD display
        self.max_water_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.max_water_number.setGeometry(QtCore.QRect(383, 510, 100, 42))
        self.max_water_number.setStyleSheet("color: rgb(64, 164, 223);")
        self.max_water_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.max_water_number.setDigitCount(2)
        self.max_water_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.max_water_number.setProperty("intValue", self.max_water / 100)
        self.max_water_number.setObjectName("max_water_number")
        
        # water unit label
        self.water_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.water_unit_label.setGeometry(QtCore.QRect(460, 510, 30, 42))
        self.water_unit_label.setStyleSheet("font: 20pt \"Candara\";""color: rgb(64, 164, 223)")
        self.water_unit_label.setScaledContents(False)
        self.water_unit_label.setAlignment(QtCore.Qt.AlignBottom)
        self.water_unit_label.setWordWrap(True)
        self.water_unit_label.setIndent(-1)
        self.water_unit_label.setObjectName("water_unit_label")

        # manage water label
        self.addWaterLabel = QtWidgets.QLabel(self.centralwidget)
        self.addWaterLabel.setGeometry(QtCore.QRect(500, 10, 100, 30))
        self.addWaterLabel.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.addWaterLabel.setScaledContents(False)
        self.addWaterLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter)
        self.addWaterLabel.setWordWrap(True)
        self.addWaterLabel.setIndent(-1)
        self.addWaterLabel.setObjectName("addWaterLabel")

        # largeBottle button
        self.waterButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.waterButton3.setGeometry(QtCore.QRect(500, 50, 100, 100))
        waterIcon3 = QtGui.QIcon()
        waterIcon3.addPixmap(QtGui.QPixmap("CT_icons/largeBottle.png"))
        self.waterButton3.setIcon(waterIcon3)
        self.waterButton3.setProperty('flat', False)
        self.waterButton3.setIconSize(QtCore.QSize(50, 50))
        self.waterButton3.setObjectName("waterButton3")
        self.waterButton3.clicked.connect(self.largeBottleAdder)

        # smallBottle button
        self.waterButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.waterButton2.setGeometry(QtCore.QRect(500, 200, 100, 100))
        waterIcon2 = QtGui.QIcon()
        waterIcon2.addPixmap(QtGui.QPixmap("CT_icons/smallBottle.png"))
        self.waterButton2.setIcon(waterIcon2)
        self.waterButton2.setProperty('flat', False)
        self.waterButton2.setIconSize(QtCore.QSize(50, 50))
        self.waterButton2.setObjectName("waterButton2")
        self.waterButton2.clicked.connect(self.smallBottleAdder)

        # waterCup button
        self.waterButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.waterButton1.setGeometry(QtCore.QRect(500, 350, 100, 100)) # +30x30 in size
        waterIcon1 = QtGui.QIcon()
        waterIcon1.addPixmap(QtGui.QPixmap("CT_icons/waterCup.png"))
        self.waterButton1.setIcon(waterIcon1)
        self.waterButton1.setProperty('flat', False)
        self.waterButton1.setIconSize(QtCore.QSize(30, 30))
        self.waterButton1.setObjectName("waterButton1")
        self.waterButton1.clicked.connect(self.waterCupAdder)

        # subtractWater button
        self.subWaterButton = QtWidgets.QPushButton(self.centralwidget)
        self.subWaterButton.setGeometry(QtCore.QRect(517.5, 500, 65, 65))   # +20x20 in size
        spillIcon = QtGui.QIcon()
        spillIcon.addPixmap(QtGui.QPixmap("CT_icons/spill.png"))
        self.subWaterButton.setIcon(spillIcon)
        self.subWaterButton.setProperty('flat', False)
        self.subWaterButton.setIconSize(QtCore.QSize(30, 30))
        self.subWaterButton.setObjectName("subWaterButton")
        self.subWaterButton.clicked.connect(self.waterSubtractor)
        
        # largeBottle label
        self.largeBottleText = QtWidgets.QLabel(self.centralwidget)
        self.largeBottleText.setGeometry(QtCore.QRect(500, 150, 100, 20))
        self.largeBottleText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.largeBottleText.setScaledContents(False)
        self.largeBottleText.setAlignment(QtCore.Qt.AlignCenter)
        self.largeBottleText.setWordWrap(True)
        self.largeBottleText.setIndent(-1)
        self.largeBottleText.setObjectName("largeBottleText")

        # smallBottle label
        self.smallBottleText = QtWidgets.QLabel(self.centralwidget)
        self.smallBottleText.setGeometry(QtCore.QRect(500, 300, 100, 20))
        self.smallBottleText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.smallBottleText.setScaledContents(False)
        self.smallBottleText.setAlignment(QtCore.Qt.AlignCenter)
        self.smallBottleText.setWordWrap(True)
        self.smallBottleText.setIndent(-1)
        self.smallBottleText.setObjectName("smallBottleText")

        # waterCup label
        self.waterCupText = QtWidgets.QLabel(self.centralwidget)
        self.waterCupText.setGeometry(QtCore.QRect(500, 450, 100, 20))
        self.waterCupText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.waterCupText.setScaledContents(False)
        self.waterCupText.setAlignment(QtCore.Qt.AlignCenter)
        self.waterCupText.setWordWrap(True)
        self.waterCupText.setIndent(-1)
        self.waterCupText.setObjectName("waterCupText")

        # subtractWater label
        self.subWaterText = QtWidgets.QLabel(self.centralwidget)
        self.subWaterText.setGeometry(QtCore.QRect(517.5, 565, 65, 20))
        self.subWaterText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.subWaterText.setScaledContents(False)
        self.subWaterText.setAlignment(QtCore.Qt.AlignCenter)
        self.subWaterText.setWordWrap(True)
        self.subWaterText.setIndent(-1)
        self.subWaterText.setObjectName("subWaterText")

        # manage calories label
        self.addCaloriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.addCaloriesLabel.setGeometry(QtCore.QRect(640, 10, 120, 30))
        self.addCaloriesLabel.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.addCaloriesLabel.setScaledContents(False)
        self.addCaloriesLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter)
        self.addCaloriesLabel.setWordWrap(True)
        self.addCaloriesLabel.setIndent(-1)
        self.addCaloriesLabel.setObjectName("addCaloriesLabel")

        # meatButton
        self.calButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.calButton3.setGeometry(QtCore.QRect(650, 50, 100, 100))
        calIcon3 = QtGui.QIcon()
        calIcon3.addPixmap(QtGui.QPixmap("CT_icons/meat.png"))
        self.calButton3.setIcon(calIcon3)
        self.calButton3.setProperty('flat', False)
        self.calButton3.setIconSize(QtCore.QSize(50, 50))
        self.calButton3.setObjectName("calButton3")
        self.calButton3.clicked.connect(self.meatAdder)
        
        # eggsButton
        self.calButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.calButton2.setGeometry(QtCore.QRect(650, 200, 100, 100))
        calIcon2 = QtGui.QIcon()
        calIcon2.addPixmap(QtGui.QPixmap("CT_icons/eggs.png"))
        self.calButton2.setIcon(calIcon2)
        self.calButton2.setProperty('flat', False)
        self.calButton2.setIconSize(QtCore.QSize(50, 50))
        self.calButton2.setObjectName("calButton2")
        self.calButton2.clicked.connect(self.eggsAdder)

        # sandwichButton
        self.calButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.calButton1.setGeometry(QtCore.QRect(650, 350, 100, 100))
        calIcon1 = QtGui.QIcon()
        calIcon1.addPixmap(QtGui.QPixmap("CT_icons/sandwich.png"))
        self.calButton1.setIcon(calIcon1)
        self.calButton1.setProperty('flat', False)
        self.calButton1.setIconSize(QtCore.QSize(30, 30))
        self.calButton1.setObjectName("calButton1")
        self.calButton1.clicked.connect(self.sandwichAdder)

        # subtractCalories button
        self.subCalBtn = QtWidgets.QPushButton(self.centralwidget)
        self.subCalBtn.setGeometry(QtCore.QRect(667.5, 500, 65, 65))
        run_dark_icon = QtGui.QIcon()
        run_dark_icon.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
        self.subCalBtn.setIcon(run_dark_icon)
        self.subCalBtn.setProperty('flat', False)
        self.subCalBtn.setIconSize(QtCore.QSize(30, 30))
        self.subCalBtn.setObjectName("subCalBtn")
        self.subCalBtn.clicked.connect(self.calSubtractor)

        # meat label
        self.meatText = QtWidgets.QLabel(self.centralwidget)
        self.meatText.setGeometry(QtCore.QRect(650, 150, 100, 20))
        self.meatText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.meatText.setScaledContents(False)
        self.meatText.setAlignment(QtCore.Qt.AlignCenter)
        self.meatText.setWordWrap(True)
        self.meatText.setIndent(-1)
        self.meatText.setObjectName("meatText")

        # eggs label
        self.eggsText = QtWidgets.QLabel(self.centralwidget)
        self.eggsText.setGeometry(QtCore.QRect(650, 300, 100, 20))
        self.eggsText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.eggsText.setScaledContents(False)
        self.eggsText.setAlignment(QtCore.Qt.AlignCenter)
        self.eggsText.setWordWrap(True)
        self.eggsText.setIndent(-1)
        self.eggsText.setObjectName("eggsText")

        # sandwich label
        self.sandwichText = QtWidgets.QLabel(self.centralwidget)
        self.sandwichText.setGeometry(QtCore.QRect(650, 450, 100, 20))
        self.sandwichText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.sandwichText.setScaledContents(False)
        self.sandwichText.setAlignment(QtCore.Qt.AlignCenter)
        self.sandwichText.setWordWrap(True)
        self.sandwichText.setIndent(-1)
        self.sandwichText.setObjectName("sandwichText")

        # subCal label
        self.subCalText = QtWidgets.QLabel(self.centralwidget)
        self.subCalText.setGeometry(QtCore.QRect(667.5, 565, 65, 20))   # 50 pixels from button
        self.subCalText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.subCalText.setScaledContents(False)
        self.subCalText.setAlignment(QtCore.Qt.AlignCenter)
        self.subCalText.setWordWrap(True)
        self.subCalText.setIndent(-1)
        self.subCalText.setObjectName("subCalText")

        # meal time logger label
        self.clockText = QtWidgets.QLabel(self.centralwidget)
        self.clockText.setGeometry(QtCore.QRect(300, 10, 120, 30))
        self.clockText.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.clockText.setScaledContents(False)
        self.clockText.setAlignment(QtCore.Qt.AlignCenter)
        self.clockText.setWordWrap(True)
        self.clockText.setIndent(-1)
        self.clockText.setObjectName("clockText")

        # meal times list label
        self.mealText = QtWidgets.QLabel(self.centralwidget)
        self.mealText.setGeometry(QtCore.QRect(300, 160, 120, 220))
        self.mealText.setStyleSheet("font: 11pt \"Segoe UI\";")
        self.mealText.setScaledContents(False)
        self.mealText.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mealText.setWordWrap(True)
        self.mealText.setIndent(-1)
        self.mealText.setObjectName("mealText")
        
        # MENUBAR
        # set screenshot folder menu option
        self.select_action = QtWidgets.QAction(MainWindow)
        self.select_action.setStatusTip('Select screenshots folder')
        self.select_action.triggered.connect(self.select_directory)

        # reset values check menu
        self.reset_values_action = QtWidgets.QAction(MainWindow, checkable=True)
        self.reset_values_action.setObjectName("actionSubmenu2")
        self.reset_values_action.setChecked(self.reset_app_value)
        self.reset_values_action.triggered.connect(self.reset_app_toggler)

        # selectable max water values
        self.set_water_10dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_10dl_action.setStatusTip('10 dl')
        self.set_water_10dl_action.triggered.connect(self.set_water_to_10dl)
        self.set_water_15dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_15dl_action.setStatusTip('15 dl')
        self.set_water_15dl_action.triggered.connect(self.set_water_to_15dl)
        self.set_water_20dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_20dl_action.setStatusTip('20 dl')
        self.set_water_20dl_action.triggered.connect(self.set_water_to_20dl)
        self.set_water_25dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_25dl_action.setStatusTip('25 dl')
        self.set_water_25dl_action.triggered.connect(self.set_water_to_25dl)
        self.set_water_30dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_30dl_action.setStatusTip('30 dl')
        self.set_water_30dl_action.triggered.connect(self.set_water_to_30dl)
        self.set_water_35dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_35dl_action.setStatusTip('35 dl')
        self.set_water_35dl_action.triggered.connect(self.set_water_to_35dl)
        self.set_water_40dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_40dl_action.setStatusTip('40 dl')
        self.set_water_40dl_action.triggered.connect(self.set_water_to_40dl)

        # selectable max calories values
        self.set_calories_1000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_1000cal_action.setStatusTip('1000 cal')
        self.set_calories_1000cal_action.triggered.connect(self.set_calories_to_1000)
        self.set_calories_1500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_1500cal_action.setStatusTip('1500 cal')
        self.set_calories_1500cal_action.triggered.connect(self.set_calories_to_1500)
        self.set_calories_2000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_2000cal_action.setStatusTip('2000 cal')
        self.set_calories_2000cal_action.triggered.connect(self.set_calories_to_2000)
        self.set_calories_2500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_2500cal_action.setStatusTip('2500 cal')
        self.set_calories_2500cal_action.triggered.connect(self.set_calories_to_2500)
        self.set_calories_3000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_3000cal_action.setStatusTip('3000 cal')
        self.set_calories_3000cal_action.triggered.connect(self.set_calories_to_3000)
        self.set_calories_3500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_3500cal_action.setStatusTip('3500 cal')
        self.set_calories_3500cal_action.triggered.connect(self.set_calories_to_3500)
        self.set_calories_4000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_4000cal_action.setStatusTip('4000 cal')
        self.set_calories_4000cal_action.triggered.connect(self.set_calories_to_4000)

        # creating menu bar itself
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 21))
        self.menubar.setObjectName("menubar")
    
        # creating file menu
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        
        if self.light_on == True:
            self.menubar.setStyleSheet("""
            QMenuBar {
                background-color: rgb(255, 255, 255);
                color: black;
            }
            QMenuBar::item {
                background-color: rgb(255, 255, 255);
                color: black;
            }
            QMenuBar::item::selected {
                background-color: rgb(220, 220, 220);
            }
            QMenu {
                background-color: rgb(255, 255, 255);
                color: black;
                border: 1px solid black;           
            }
            QMenu::item::selected {
                background-color: rgb(220, 220, 220);
            }
        """)
        else:
            self.menubar.setStyleSheet("""
            QMenuBar {
                background-color: rgb(90, 90, 90);
                color: rgb(255, 255, 255);
            }
            QMenuBar::item {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
            }
            QMenuBar::item::selected {
                background-color: rgb(120, 120, 120);
            }
            QMenu {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
                border: 1px solid white;           
            }
            QMenu::item::selected {
                background-color: rgb(120, 120, 120);
            }
        """)

        # creating max values menu
        self.set_max_values_menu = QtWidgets.QMenu(self.menubar)
        self.set_max_values_menu.setObjectName("set_max_values_menu")

        # creating max water menu
        self.set_water_menu = QtWidgets.QMenu(self.set_max_values_menu)

        # creating max calories menu
        self.set_calories_menu = QtWidgets.QMenu(self.set_max_values_menu)

        # creating help menu
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName('help_menu')

        # creating about action | general about, current build?
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName('about_action')
        self.about_action.triggered.connect(self.open_about)

        # creating view source action
        self.project_page_action = QtWidgets.QAction(MainWindow)
        self.project_page_action.setObjectName('source_code_action')
        self.project_page_action.triggered.connect(self.open_project_page)
       
        # setting up file menu
        self.file_menu.addAction(self.select_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.reset_values_action)
        self.menubar.addAction(self.file_menu.menuAction())
        
        # setting up set max values menu
        self.menubar.addAction(self.set_max_values_menu.menuAction())
        self.set_max_values_menu.addAction(self.set_water_menu.menuAction())
        self.set_max_values_menu.addSeparator()
        self.set_max_values_menu.addAction(self.set_calories_menu.menuAction())

        # setting up water values submenu
        self.set_water_menu.addAction(self.set_water_10dl_action)
        self.set_water_menu.addAction(self.set_water_15dl_action)
        self.set_water_menu.addAction(self.set_water_20dl_action)
        self.set_water_menu.addAction(self.set_water_25dl_action)
        self.set_water_menu.addAction(self.set_water_30dl_action)
        self.set_water_menu.addAction(self.set_water_35dl_action)
        self.set_water_menu.addAction(self.set_water_40dl_action)
        
        # setting up calories values submenu
        self.set_calories_menu.addAction(self.set_calories_1000cal_action)
        self.set_calories_menu.addAction(self.set_calories_1500cal_action)
        self.set_calories_menu.addAction(self.set_calories_2000cal_action)
        self.set_calories_menu.addAction(self.set_calories_2500cal_action)
        self.set_calories_menu.addAction(self.set_calories_3000cal_action)
        self.set_calories_menu.addAction(self.set_calories_3500cal_action)
        self.set_calories_menu.addAction(self.set_calories_4000cal_action)

        # setting up help menu
        self.menubar.addAction(self.help_menu.menuAction())
        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.project_page_action)

        MainWindow.setMenuBar(self.menubar)
        MainWindow.setCentralWidget(self.centralwidget)

        # toolbar
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setFloatable(False)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        if self.light_on == True:
            self.toolBar.setStyleSheet("""
            QToolBar {
                background-color: white;
            }
            
            QToolButton {
                background-color: white;
            }
            """)

        # swap female/male image button
        body_swapper_btn = QtWidgets.QAction(QtGui.QIcon("CT_icons/swapBody.png"),
                                     "Male/female", MainWindow)
        body_swapper_btn.triggered.connect(self.image_swapper)
        self.toolBar.addAction(body_swapper_btn)

        # reset app button
        resetBtn = QtWidgets.QAction(QtGui.QIcon("CT_icons/reset.png"),
                                     "Reset app", MainWindow)
        resetBtn.triggered.connect(self.resetApp)
        self.toolBar.addAction(resetBtn)

        # save screenshot button
        ssBtn = QtWidgets.QAction(QtGui.QIcon("CT_icons/screenshooter.png"),
                                  "Save screenshot", MainWindow)
        ssBtn.triggered.connect(self.screenshot)
        self.toolBar.addAction(ssBtn)

        # switch appearance button
        self.appearance_Btn = QtWidgets.QAction(QtGui.QIcon("CT_icons/darken.png"),
                                          'Darken', MainWindow)
        self.appearance_Btn.triggered.connect(self.switch_appearance)
        self.toolBar.addAction(self.appearance_Btn)

        # minimize to tray button
        self.minimize_Btn = QtWidgets.QAction(QtGui.QIcon("CT_icons/shrink.png"),
                                          'Minimize to tray', MainWindow)
        self.minimize_Btn.triggered.connect(self.minimize)
        self.toolBar.addAction(self.minimize_Btn)

        # hour logger
        self.hourEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.hourEdit.setGeometry(QtCore.QRect(300, 50, 60, 50))
        self.hourEdit.setStyleSheet("font: 20pt \"Segoe UI\"""; color: black")
        self.hourEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.hourEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)        
        self.hourEdit.setObjectName("hourEdit")

        # minute logger
        self.minEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.minEdit.setGeometry(QtCore.QRect(359, 50, 60, 50))
        self.minEdit.setStyleSheet("font: 20pt \"Segoe UI\"""; color: black")
        self.minEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.minEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.minEdit.setObjectName("minEdit")

        # meal time logging button
        self.mealTimeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mealTimeBtn.setGeometry(QtCore.QRect(300, 100, 120, 25))   # y: 50
        mealTimeIcon = QtGui.QIcon()
        mealTimeIcon.addPixmap(QtGui.QPixmap("CT_icons/clock.png"))
        self.mealTimeBtn.setIcon(mealTimeIcon)
        self.mealTimeBtn.setIconSize(QtCore.QSize(20, 20))
        self.mealTimeBtn.setObjectName('mealTimeBtn')
        self.mealTimeBtn.clicked.connect(self.meal_logger)

        # set time to now button
        self.get_current_time_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_current_time_btn.setGeometry(QtCore.QRect(300, 125, 120, 25))  # 25
        self.get_current_time_btn.setObjectName('get_current_time_btn')
        self.get_current_time_btn.setStyleSheet("font: 9pt \"Segoe UI\";\n;""text-align: center")
        self.get_current_time_btn.clicked.connect(self.time_to_current_moment)

        if self.reset_app_value == True:
            if self.previous_time < self.current_time:
                self.resetApp()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # data saver function
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

    def set_water_to_10dl(self):
        self.max_water = 1000
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

    def set_water_to_15dl(self):
        self.max_water = 1500
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

    def set_water_to_20dl(self):
        self.max_water = 2000
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

    def set_water_to_25dl(self):
        self.max_water = 2500
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

    def set_water_to_30dl(self):
        self.max_water = 3000
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

    def set_water_to_35dl(self):
        self.max_water = 3500
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

    def set_water_to_40dl(self):
        self.max_water = 4000
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

    def set_calories_to_1000(self):
        self.max_calories = 1000
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

    def set_calories_to_1500(self):
        self.max_calories = 1500
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

    def set_calories_to_2000(self):
        self.max_calories = 2000
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

    def set_calories_to_2500(self):
        self.max_calories = 2500
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

    def set_calories_to_3000(self):
        self.max_calories = 3000
        # could be made a function from here on lol?
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

    def set_calories_to_3500(self):
        self.max_calories = 3500
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

    def set_calories_to_4000(self):
        self.max_calories = 4000
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

    def open_about(self):
        if self.light_on == False:
            app.setStyleSheet("""QPushButton {
            background-color: rgb(90, 90, 90);
            color: white;
            } 
            QLabel {
            color: white
            }""")
            QtWidgets.QMessageBox.information(MainWindow,
                'About CT', 
                "Version: v1.0.0\nRelease date: 03/09/2019\nMade in: Python 3.6.0/PyQt5 5.13.0\nTested on: Windows 10 (x64)",
                QtWidgets.QMessageBox.Ok)
            app.setStyleSheet("""QPushButton {
            background-color: white;
            color: black;
            }
            QLabel {
            color: white;
            }""")
        else:
            QtWidgets.QMessageBox.information(MainWindow,
                'About CT', 
                "Version: v1.0.0\nRelease date: 03/09/2019\nMade in: Python 3.6.0/PyQt5 5.13.0\nTested on: Windows 10 (x64)",
                QtWidgets.QMessageBox.Ok)

    def open_project_page(self):
        if self.light_on == False:
            app.setStyleSheet("""QPushButton {
            background-color: rgb(90, 90, 90);
            color: white;
            } 
            QLabel {
            color: white
            }""")            
            choice = QtWidgets.QMessageBox.question(MainWindow, 
                'View project page', 'This will open a new browser tab.', 
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Ok:
                webbrowser.open_new_tab('https://github.com/porgabi/consumption-tracker')
            app.setStyleSheet("""QPushButton {
            background-color: white;
            color: black;
            }
            QLabel {
            color: white;
            }""")
        else:
            choice = QtWidgets.QMessageBox.question(MainWindow, 
                'View project page', 'This will open a new browser tab.', 
                QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if choice == QtWidgets.QMessageBox.Ok:
                webbrowser.open_new_tab('https://github.com/porgabi/consumption-tracker')

    # TOOLBAR functions
    def resetApp(self):
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

    def screenshot(self):
        frame_pos_raw = str(MainWindow.frameGeometry())
        frame_pos_string = frame_pos_raw.replace('PyQt5.QtCore.QRect', '')
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
            self.appearance_Btn.setIcon(light_icon)
            self.appearance_Btn.setToolTip('Lighten')
            self.dark_palette = QtGui.QPalette()
            self.dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(90, 90, 90))
            app.setPalette(self.dark_palette)
            
            self.subWaterButton.setStyleSheet('background: rgb(90, 90, 90)')
            self.waterButton1.setStyleSheet('background: rgb(90, 90, 90)')
            self.waterButton2.setStyleSheet('background: rgb(90, 90, 90)')
            self.waterButton3.setStyleSheet('background: rgb(90, 90, 90)')

            self.subCalBtn.setStyleSheet('background: rgb(90, 90, 90)')
            self.calButton1.setStyleSheet('background: rgb(90, 90, 90)')
            self.calButton2.setStyleSheet('background: rgb(90, 90, 90)')
            self.calButton3.setStyleSheet('background: rgb(90, 90, 90)')

            self.waterBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: rgb(90, 90, 90);\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "font: 16pt \"Segoe UI\";\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));\n"
            "}\n"
            "QProgressBar {"
            "color: white;"
            "font: 15px"
            "}")

            self.calBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: rgb(90, 90, 90);\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));\n"
            "}\n"
            "QProgressBar {"
            "color: white;"
            "font: 15px"
            "}")

            app.setStyleSheet("""
            QToolTip { 
            background-color: rgb(90, 90, 90); 
            color: white; 
            border: 1px solid white
            }
            QLabel {
            color: white;
            }""")

            self.menubar.setStyleSheet("""
            QMenuBar {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
            }
            QMenuBar::item {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
            }
            QMenuBar::item::selected {
                background-color: rgb(120, 120, 120);
            }
            QMenu {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
                border: 1px solid white;           
            }
            QMenu::item::selected {
                background-color: rgb(120, 120, 120);
            }
            """)
            self.set_water_menu.setStyleSheet("""
            QMenu {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
                border: 1px solid white;           
            }
            QMenu::item::selected {
                background-color: rgb(120, 120, 120);
            }
            """)
            self.set_calories_menu.setStyleSheet("""
            QMenu {
                background-color: rgb(90, 90, 90);
                color: rgb(255,255,255);
                border: 1px solid white;           
            }
            QMenu::item::selected {
                background-color: rgb(120, 120, 120);
            }
            """)

            self.toolBar.setStyleSheet("""
            QToolBar {
                background-color: rgb(90, 90, 90);
            }
            
            QToolButton {
                background-color: rgb(90, 90, 90);
            }
            """)


            self.mealTimeBtn.setStyleSheet('background: rgb(90, 90, 90)')
            self.get_current_time_btn.setStyleSheet('background: rgb(90, 90, 90); color: white')

            self.hourEdit.setStyleSheet('background: rgb(90, 90, 90); color: white')
            self.minEdit.setStyleSheet('background: rgb(90, 90, 90); color: white')
            run_light_icon = QtGui.QIcon()
            run_light_icon.addPixmap(QtGui.QPixmap("CT_icons/runLight.png"))
            self.subCalBtn.setIcon(run_light_icon)
            
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
            self.appearance_Btn.setIcon(dark_icon)
            self.appearance_Btn.setToolTip('Darken')
            self.light_palette = QtGui.QPalette()
            self.light_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))
            app.setPalette(self.light_palette)

            self.mealTimeBtn.setStyleSheet('background: rgb(255, 255, 255)')
            self.get_current_time_btn.setStyleSheet('background: rgb(255, 255, 255); color: black')
            self.subWaterButton.setStyleSheet('background: rgb(255, 255, 255)')
            self.waterButton1.setStyleSheet('background: rgb(255, 255, 255)')
            self.waterButton2.setStyleSheet('background: rgb(255, 255, 255)')
            self.waterButton3.setStyleSheet('background: rgb(255, 255, 255)')
            self.subCalBtn.setStyleSheet('background: rgb(255, 255, 255)')
            self.calButton1.setStyleSheet('background: rgb(255, 255, 255)')
            self.calButton2.setStyleSheet('background: rgb(255, 255, 255)')
            self.calButton3.setStyleSheet('background: rgb(255, 255, 255)')
            self.waterBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: white;\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));\n"
            "}\n"            
            "QProgressBar {"
            "color: black;"            
            "font: 15px"
            "}")
            self.calBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border: 2px solid black;\n"
            "border-radius: 3px;\n"
            "background: white;\n"
            "padding: 0px;\n"
            "text-align: center;\n"
            "margin-right: 0ex;\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));\n"
            "}\n"
            "QProgressBar {"
            "color: black;"            
            "font: 15px"
            "}")
            app.setStyleSheet("""
            QToolTip { 
            background-color: white; 
            color: black; 
            border: 1px solid black;
            }
            QLabel {
            color: black;
            }""")
            self.menubar.setStyleSheet("""
            QMenuBar {
                background-color: rgb(255, 255, 255);
                color: black;
            }
            QMenuBar::item {
                background-color: rgb(255, 255, 255);
                color: black;
            }
            QMenuBar::item::selected {
                background-color: rgb(220, 220, 220);
            }
            QMenu {
                background-color: rgb(255, 255, 255);
                color: black;
                border: 1px solid black;           
            }
            QMenu::item::selected {
                background-color: rgb(220, 220, 220);
            }
            """)
            self.set_water_menu.setStyleSheet("""
            QMenu {
                background-color: rgb(255, 255, 255);
                color: black;
                border: 1px solid black;           
            }
            QMenu::item::selected {
                background-color: rgb(220, 220, 220);
            }
            """)
            self.set_calories_menu.setStyleSheet("""
            QMenu {
                background-color: rgb(255, 255, 255);
                color: black;
                border: 1px solid black;           
            }
            QMenu::item::selected {
                background-color: rgb(220, 220, 220);
            }
            """)
            self.toolBar.setStyleSheet("""
            QToolBar {
                background-color: white;
            }
            
            QToolButton {
                background-color: white;
            }
            """)

            self.hourEdit.setStyleSheet('background: rgb(255, 255, 255); color: black')
            self.minEdit.setStyleSheet('background: rgb(255, 255, 255); color: black')
            run_dark_icon = QtGui.QIcon()
            run_dark_icon.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
            self.subCalBtn.setIcon(run_dark_icon)
            
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

    def minimize(self):
        MainWindow.hide()
        self.tray.show()

    def tray_icon_click(self, signal):
        MainWindow.show()
        self.tray.hide()
    
    def image_swapper(self):
        if self.light_on == True:
            if self.human_image_is_malebodylight == True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodylight.png"))
                self.human_image_is_malebodylight = False
                self.current_body = 'female_light'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodylight.png"))
                self.human_image_is_malebodylight = True
                self.current_body = 'male_light'
        else:
            if self.human_image_is_malebodydark == True:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/femalebodydark.png"))
                self.human_image_is_malebodydark = False
                self.current_body = 'female_dark'
            else:
                self.human_image.setPixmap(QtGui.QPixmap("CT_icons/malebodydark.png"))
                self.human_image_is_malebodydark = True
                self.current_body = 'male_dark'
        self.save_data()

    # WATER MANAGEMENT functions
    def waterSubtractor(self):
        self.current_water -= 100 # ml
        self.waterBar.setProperty('value', self.current_water)
        if self.current_water <= 0:
            self.waterBar.setProperty('value', 0)
            self.current_water = 0
        if self.current_water + self.current_calories <= 0:
            self.human_bar.setProperty('value', 0)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.waterNumber.setProperty('intValue', (self.current_water / 100))
        self.save_data()

    def waterCupAdder(self):
        self.current_water += 200
        self.waterBar.setProperty('value', self.current_water)
        if self.current_water >= self.max_water:
            self.waterBar.setProperty('value', self.max_water)
            self.current_water = self.max_water
        if self.current_water + self.current_calories >= self.max_human_value:  
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories) # current human value
        self.waterNumber.setProperty('intValue', (self.current_water / 100))
        self.save_data()

    def smallBottleAdder(self):
        self.current_water += 500
        self.waterBar.setProperty('value', self.current_water)
        if self.current_water >= self.max_water:
            self.waterBar.setProperty('value', self.max_water)
            self.current_water = self.max_water
        if self.current_water + self.current_calories >= self.max_human_value:   
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.waterNumber.setProperty('intValue', (self.current_water / 100))
        self.save_data()

    def largeBottleAdder(self):
        self.current_water += 1000
        self.waterBar.setProperty('value', self.current_water)
        if self.current_water >= self.max_water:
            self.waterBar.setProperty('value', self.max_water)
            self.current_water = self.max_water
        if self.current_water + self.current_calories >= self.max_human_value:    
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water  + self.current_calories)
        self.waterNumber.setProperty('intValue', (self.current_water / 100))
        self.save_data()

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

    def sandwichAdder(self):
        self.current_calories += 200
        self.calBar.setProperty('value', self.current_calories)
        if self.current_calories >= self.max_calories:
            self.calBar.setProperty('value', self.max_calories)
            self.current_calories = self.max_calories
        if self.current_water + self.current_calories >= self.max_human_value:    
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.calNumber.setProperty('intValue', self.current_calories)
        self.save_data()

    def eggsAdder(self):
        self.current_calories += 500
        self.calBar.setProperty('value', self.current_calories)
        if self.current_calories >= self.max_calories:
            self.calBar.setProperty('value', self.max_calories)
            self.current_calories = self.max_calories
        if self.current_water + self.current_calories >= 6000:    
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)    
        self.calNumber.setProperty('intValue', self.current_calories)
        self.save_data()

    def meatAdder(self):
        self.current_calories += 1000
        self.calBar.setProperty('value', self.current_calories)
        if self.current_calories >= self.max_calories:
            self.calBar.setProperty('value', self.max_calories)
            self.current_calories = self.max_calories
        if self.current_water + self.current_calories >= self.max_human_value:
            self.human_bar.setProperty('value', self.max_human_value)
        self.human_bar.setProperty('value', self.current_water + self.current_calories)
        self.calNumber.setProperty('intValue', self.current_calories)
        self.save_data()

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consumption Tracker"))
        
        # BUTTON FUNCTIONALITY labels
        self.waterCupText.setText(_translate("MainWindow", "2 dl"))
        self.smallBottleText.setText(_translate("MainWindow", "5 dl"))
        self.largeBottleText.setText(_translate("MainWindow", "10 dl"))
        self.addWaterLabel.setText(_translate('MainWindow', 'Manage water'))
        self.subWaterText.setText(_translate('MainWindow', '-1 dl'))
        self.addCaloriesLabel.setText(_translate('MainWindow', 'Manage calories'))
        self.subCalText.setText(_translate('MainWindow', '-100 cal'))
        self.sandwichText.setText(_translate('MainWindow', '200 cal'))
        self.eggsText.setText(_translate('MainWindow', '500 cal'))
        self.meatText.setText(_translate('MainWindow', '1000 cal'))
        self.clockText.setText(_translate('MainWindow', "Set meal times"))
        
        self.get_current_time_btn.setText(_translate('MainWindow', "Set current time"))

        # CENTRALWIDGET TEXT labels
        self.calories_LCD_per_sign.setText(_translate("MainWindow", "/"))
        self.calories_unit_label.setText(_translate('MainWindow', 'cal'))
        self.water_LCD_per_sign.setText(_translate("MainWindow", "/"))
        self.water_unit_label.setText(_translate('MainWindow', 'dl'))
        
        if self.meal_logger_presses < 1:
            self.mealText.setText(_translate('MainWindow', self.null_meal))
        elif self.meal_logger_presses == 1:
            self.mealText.setText(_translate('MainWindow', self.first_meal))
        elif self.meal_logger_presses == 2:
            self.mealText.setText(_translate('MainWindow', self.second_meal))
        elif self.meal_logger_presses == 3:
            self.mealText.setText(_translate('MainWindow', self.third_meal))
        elif self.meal_logger_presses == 4:
            self.mealText.setText(_translate('MainWindow', self.fourth_meal))
        elif self.meal_logger_presses == 5:
            self.mealText.setText(_translate('MainWindow', self.fifth_meal))
        elif self.meal_logger_presses == 6:
            self.mealText.setText(_translate('MainWindow', self.sixth_meal))

        # TIMEEDIT settings
        self.hourEdit.setDisplayFormat(_translate("MainWindow", "HH"))
        self.minEdit.setDisplayFormat(_translate("MainWindow", "mm"))
        self.hourEdit.setTime(self.saved_hour)
        self.minEdit.setTime(self.saved_min)

        # BUTTON tooltips
        self.subWaterButton.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Subtract 1 dl</p></body></html>'))
        self.waterButton1.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 2 dl</p></body></html>'))
        self.waterButton2.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 5 dl</p></body></html>'))
        self.waterButton3.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 10 dl</p></body></html>'))
        self.subCalBtn.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Subtract 100 cal</p></body></html>'))
        self.calButton1.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 200 cal</p></body></html>'))
        self.calButton2.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 500 cal</p></body></html>'))
        self.calButton3.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 1000 cal</p></body></html>'))
        self.mealTimeBtn.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Log time</p></body></html>'))

        # PROGRESS BAR tooltips
        self.waterBar.setToolTip((_translate('MainWindow', '<html><head/><body><p align="center">Current water</p></body></html>')))
        self.calBar.setToolTip((_translate('MainWindow', '<html><head/><body><p align="center">Current calories</p></body></html>')))

        # MENUBAR titles
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.help_menu.setTitle(_translate("MainWindow", "Help"))
        
        self.project_page_action.setText(_translate('MainWindow', 'View project page'))
        self.about_action.setText(_translate('MainWindow', 'About'))
        
        self.set_max_values_menu.setTitle(_translate("MainWindow", "Set max values"))
        self.set_water_menu.setTitle(_translate("MainWindow", "Water"))
        self.set_calories_menu.setTitle(_translate("MainWindow", "Calories"))

        self.set_water_10dl_action.setText(_translate('MainWindow', '10 dl'))
        self.set_water_15dl_action.setText(_translate('MainWindow', '15 dl'))
        self.set_water_20dl_action.setText(_translate('MainWindow', '20 dl'))
        self.set_water_25dl_action.setText(_translate('MainWindow', '25 dl'))
        self.set_water_30dl_action.setText(_translate('MainWindow', '30 dl'))
        self.set_water_35dl_action.setText(_translate('MainWindow', '35 dl'))
        self.set_water_40dl_action.setText(_translate('MainWindow', '40 dl'))

        self.set_calories_1000cal_action.setText(_translate("MainWindow", "1000 cal"))
        self.set_calories_1500cal_action.setText(_translate("MainWindow", "1500 cal"))
        self.set_calories_2000cal_action.setText(_translate("MainWindow", "2000 cal"))
        self.set_calories_2500cal_action.setText(_translate("MainWindow", "2500 cal"))
        self.set_calories_3000cal_action.setText(_translate("MainWindow", "3000 cal"))
        self.set_calories_3500cal_action.setText(_translate("MainWindow", "3500 cal"))
        self.set_calories_4000cal_action.setText(_translate("MainWindow", "4000 cal"))

        self.reset_values_action.setText(_translate("MainWindow", "Reset app in the morning"))
        self.select_action.setText(_translate("MainWindow", "Set screenshots folder"))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("""
    QToolTip { 
    background-color: white; 
    color: black; 
    border: 1px solid black
    }""")


    MainWindow = QtWidgets.QMainWindow()
    ui = ConsumptionTracker()
    ui.setupUi(MainWindow)
    
    # TODO should just call switch_appearance() regardless
    if ui.light_on == True:
        light_palette = QtGui.QPalette()
        light_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))
        app.setPalette(light_palette)
        app.setStyleSheet('QLabel {color: black;}')
    else:
        ui.light_on = True
        if ui.current_body == 'male_dark':
            ui.human_image_is_malebodylight = True
            ui.human_image_is_malebodydark = False
        elif ui.current_body == 'female_dark':
            ui.human_image_is_malebodydark = False
        ui.switch_appearance()

    MainWindow.show()
    sys.exit(app.exec_())
