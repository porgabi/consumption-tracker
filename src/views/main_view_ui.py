from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 700)
        window_geometry = MainWindow.frameGeometry()
        screen_center_point = (QtWidgets.QDesktopWidget().availableGeometry()
                               .center())
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
        # self.tray.activated['QSystemTrayIcon::ActivationReason'].connect(self.tray_icon_click)
        self.tray.setToolTip('Consumption Tracker')

        # human image
        self.human_image = QtWidgets.QLabel(self.centralwidget)
        self.human_image.setGeometry(QtCore.QRect(55, 10, 167, 500))
        self.human_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.human_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.human_image.setStyleSheet("border: 0px solid transparent;")

        # progress bar behind body silhouette
        self.human_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.human_bar.setGeometry(QtCore.QRect(55, 10, 167, 500))
        # self.human_bar.setStyleSheet(CT_stylesheets.human_bar)
        # self.human_bar.setMaximum(self.max_human_value)
        # self.human_bar.setProperty("value", self.current_water + self.current_calories)
        self.human_bar.setTextVisible(False)
        self.human_bar.setOrientation(QtCore.Qt.Vertical)
        self.human_bar.setObjectName("human_bar")
        self.human_bar.raise_()
        self.human_image.raise_()        
        
        # water progress bar
        self.water_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.water_bar.setGeometry(QtCore.QRect(20, 514, 250, 36))
        # if self.light_on is True:
        #     self.water_bar.setStyleSheet(CT_stylesheets.water_bar_light)
        # else:
        #     self.water_bar.setStyleSheet(CT_stylesheets.water_bar_dark)
        # self.water_bar.setMaximum(self.max_water)
        # self.water_bar.setProperty('value', self.current_water)
        self.water_bar.setObjectName("water_bar")        

        # calories progress bar
        self.cal_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.cal_bar.setGeometry(QtCore.QRect(20, 564, 250, 36))
        # if self.light_on is True:
        #     self.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_light)
        # else:
        #     self.cal_bar.setStyleSheet(CT_stylesheets.cal_bar_dark)
        # self.cal_bar.setMaximum(self.max_calories)
        # self.cal_bar.setProperty("value", self.current_calories)        
        # self.cal_bar.setOrientation(QtCore.Qt.Horizontal)
        self.cal_bar.setObjectName("cal_bar")

        # current water LCD display
        self.water_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.water_number.setGeometry(QtCore.QRect(290, 510, 100, 42))
        # self.water_number.setStyleSheet(CT_stylesheets.water_color)
        self.water_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.water_number.setDigitCount(2)
        self.water_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        # self.water_number.setProperty("intValue", (self.current_water / 100))
        self.water_number.setObjectName("water_number")

        # water LCD per label
        self.water_LCD_per_sign = QtWidgets.QLabel(self.centralwidget)
        self.water_LCD_per_sign.setGeometry(QtCore.QRect(360, 507, 20, 42))
        self.water_LCD_per_sign.setStyleSheet("font: 30pt \"Segoe UI\";""color: rgb(64, 164, 223)")
        self.water_LCD_per_sign.setScaledContents(False)
        self.water_LCD_per_sign.setAlignment(QtCore.Qt.AlignVCenter)
        self.water_LCD_per_sign.setObjectName("water_LCD_per_sign")

        # max water LCD display
        self.max_water_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.max_water_number.setGeometry(QtCore.QRect(383, 510, 100, 42))
        # self.max_water_number.setStyleSheet(CT_stylesheets.water_color)
        self.max_water_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.max_water_number.setDigitCount(2)
        self.max_water_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        # self.max_water_number.setProperty("intValue", self.max_water / 100)
        self.max_water_number.setObjectName("max_water_number")

        # water unit label
        self.water_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.water_unit_label.setGeometry(QtCore.QRect(460, 510, 30, 42))
        self.water_unit_label.setStyleSheet("font: 20pt \"Candara\";""color: rgb(64, 164, 223)")
        self.water_unit_label.setScaledContents(False)
        self.water_unit_label.setAlignment(QtCore.Qt.AlignBottom)
        self.water_unit_label.setObjectName("water_unit_label")

        # current calories LCD display
        self.cal_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.cal_number.setGeometry(QtCore.QRect(270, 560, 100, 42))
        # self.cal_number.setStyleSheet(CT_stylesheets.cal_color)
        self.cal_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cal_number.setDigitCount(4)
        self.cal_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        # self.cal_number.setProperty("intValue", self.current_calories)
        self.cal_number.setObjectName("cal_number")

        # cal_number LCD per label
        self.calories_LCD_per_sign = QtWidgets.QLabel(self.centralwidget)
        self.calories_LCD_per_sign.setGeometry(QtCore.QRect(360, 557, 20, 42))
        self.calories_LCD_per_sign.setStyleSheet("font: 30pt \"Segoe UI\";""color: rgba(255, 130, 0, 255)")
        self.calories_LCD_per_sign.setScaledContents(False)
        self.calories_LCD_per_sign.setAlignment(QtCore.Qt.AlignVCenter)
        self.calories_LCD_per_sign.setObjectName("calories_LCD_per_sign")

        # max calories LCD display
        self.max_calories_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.max_calories_number.setGeometry(QtCore.QRect(364, 560, 100, 42))
        # self.max_calories_number.setStyleSheet(CT_stylesheets.cal_color)
        self.max_calories_number.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.max_calories_number.setDigitCount(4)
        self.max_calories_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        # self.max_calories_number.setProperty("intValue", self.max_calories)
        self.max_calories_number.setObjectName("max_calories_number")

        # calories unit label
        self.calories_unit_label = QtWidgets.QLabel(self.centralwidget)
        self.calories_unit_label.setGeometry(QtCore.QRect(460, 560, 30, 42))
        self.calories_unit_label.setStyleSheet("font: 20pt \"Candara\";""color: rgba(255, 130, 0, 255)")
        self.calories_unit_label.setScaledContents(False)
        self.calories_unit_label.setAlignment(QtCore.Qt.AlignBottom)
        self.calories_unit_label.setObjectName("calories_unit_label")

        # manage water label
        self.add_water_label = QtWidgets.QLabel(self.centralwidget)
        self.add_water_label.setGeometry(QtCore.QRect(500, 10, 100, 30))
        # self.add_water_label.setStyleSheet(CT_stylesheets.text_label_font2)
        self.add_water_label.setScaledContents(False)
        self.add_water_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter)
        self.add_water_label.setObjectName("add_water_label")

        # large bottle button
        self.large_bottle_button = QtWidgets.QPushButton(self.centralwidget)
        self.large_bottle_button.setGeometry(QtCore.QRect(500, 50, 100, 100))
        large_bottle_icon = QtGui.QIcon()
        large_bottle_icon.addPixmap(QtGui.QPixmap("CT_icons/largeBottle.png"))
        self.large_bottle_button.setIcon(large_bottle_icon)
        self.large_bottle_button.setProperty('flat', False)
        self.large_bottle_button.setIconSize(QtCore.QSize(50, 50))
        self.large_bottle_button.setObjectName("large_bottle_button")
        # self.large_bottle_button.clicked.connect(self.add_large_bottle)

        # small bottle button
        self.small_bottle_button = QtWidgets.QPushButton(self.centralwidget)
        self.small_bottle_button.setGeometry(QtCore.QRect(500, 200, 100, 100))
        small_bottle_icon = QtGui.QIcon()
        small_bottle_icon.addPixmap(QtGui.QPixmap("CT_icons/smallBottle.png"))
        self.small_bottle_button.setIcon(small_bottle_icon)
        self.small_bottle_button.setProperty('flat', False)
        self.small_bottle_button.setIconSize(QtCore.QSize(50, 50))
        self.small_bottle_button.setObjectName("small_bottle_button")
        # self.small_bottle_button.clicked.connect(self.add_small_bottle)

        # glass of water button
        self.glass_button = QtWidgets.QPushButton(self.centralwidget)
        self.glass_button.setGeometry(QtCore.QRect(500, 350, 100, 100))
        glass_icon = QtGui.QIcon()
        glass_icon.addPixmap(QtGui.QPixmap("CT_icons/waterCup.png"))
        self.glass_button.setIcon(glass_icon)
        self.glass_button.setProperty('flat', False)
        self.glass_button.setIconSize(QtCore.QSize(30, 30))
        self.glass_button.setObjectName("glass_button")
        # self.glass_button.clicked.connect(self.add_glass)

        # subtract water button
        self.sub_water_button = QtWidgets.QPushButton(self.centralwidget)
        self.sub_water_button.setGeometry(QtCore.QRect(517.5, 500, 65, 65))
        spill_icon = QtGui.QIcon()
        spill_icon.addPixmap(QtGui.QPixmap("CT_icons/spill.png"))
        self.sub_water_button.setIcon(spill_icon)
        self.sub_water_button.setProperty('flat', False)
        self.sub_water_button.setIconSize(QtCore.QSize(30, 30))
        self.sub_water_button.setObjectName("sub_water_button")
        # self.sub_water_button.clicked.connect(self.subtract_water)
        
        # large bottle label
        self.large_bottle_text = QtWidgets.QLabel(self.centralwidget)
        self.large_bottle_text.setGeometry(QtCore.QRect(500, 150, 100, 20))
        # self.large_bottle_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.large_bottle_text.setScaledContents(False)
        self.large_bottle_text.setAlignment(QtCore.Qt.AlignCenter)
        self.large_bottle_text.setObjectName("large_bottle_text")

        # small bottle label
        self.small_bottle_text = QtWidgets.QLabel(self.centralwidget)
        self.small_bottle_text.setGeometry(QtCore.QRect(500, 300, 100, 20))
        # self.small_bottle_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.small_bottle_text.setScaledContents(False)
        self.small_bottle_text.setAlignment(QtCore.Qt.AlignCenter)
        self.small_bottle_text.setObjectName("small_bottle_text")

        # glass of water label
        self.glass_text = QtWidgets.QLabel(self.centralwidget)
        self.glass_text.setGeometry(QtCore.QRect(500, 450, 100, 20))
        # self.glass_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.glass_text.setScaledContents(False)
        self.glass_text.setAlignment(QtCore.Qt.AlignCenter)
        self.glass_text.setObjectName("glass_text")

        # subtract water label
        self.sub_water_text = QtWidgets.QLabel(self.centralwidget)
        self.sub_water_text.setGeometry(QtCore.QRect(517.5, 565, 65, 20))
        # self.sub_water_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.sub_water_text.setScaledContents(False)
        self.sub_water_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_water_text.setObjectName("sub_water_text")

        # manage calories label
        self.add_calories_label = QtWidgets.QLabel(self.centralwidget)
        self.add_calories_label.setGeometry(QtCore.QRect(640, 10, 120, 30))
        # self.add_calories_label.setStyleSheet(CT_stylesheets.text_label_font2)
        self.add_calories_label.setScaledContents(False)
        self.add_calories_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter)
        self.add_calories_label.setObjectName("add_calories_label")

        # meat button
        self.meat_button = QtWidgets.QPushButton(self.centralwidget)
        self.meat_button.setGeometry(QtCore.QRect(650, 50, 100, 100))
        meat_icon = QtGui.QIcon()
        meat_icon.addPixmap(QtGui.QPixmap("CT_icons/meat.png"))
        self.meat_button.setIcon(meat_icon)
        self.meat_button.setProperty('flat', False)
        self.meat_button.setIconSize(QtCore.QSize(50, 50))
        self.meat_button.setObjectName("meat_button")
        # self.meat_button.clicked.connect(self.add_meat)

        # eggs button
        self.eggs_button = QtWidgets.QPushButton(self.centralwidget)
        self.eggs_button.setGeometry(QtCore.QRect(650, 200, 100, 100))
        eggs_icon = QtGui.QIcon()
        eggs_icon.addPixmap(QtGui.QPixmap("CT_icons/eggs.png"))
        self.eggs_button.setIcon(eggs_icon)
        self.eggs_button.setProperty('flat', False)
        self.eggs_button.setIconSize(QtCore.QSize(50, 50))
        self.eggs_button.setObjectName("eggs_button")
        # self.eggs_button.clicked.connect(self.add_eggs)

        # sandwich button
        self.sandwich_button = QtWidgets.QPushButton(self.centralwidget)
        self.sandwich_button.setGeometry(QtCore.QRect(650, 350, 100, 100))
        sandwich_icon = QtGui.QIcon()
        sandwich_icon.addPixmap(QtGui.QPixmap("CT_icons/sandwich.png"))
        self.sandwich_button.setIcon(sandwich_icon)
        self.sandwich_button.setProperty('flat', False)
        self.sandwich_button.setIconSize(QtCore.QSize(30, 30))
        self.sandwich_button.setObjectName("sandwich_button")
        # self.sandwich_button.clicked.connect(self.add_sandwich)

        # subtract calories button
        self.sub_calories_button = QtWidgets.QPushButton(self.centralwidget)
        self.sub_calories_button.setGeometry(QtCore.QRect(667.5, 500, 65, 65))
        sub_cal_icon_dark = QtGui.QIcon()
        sub_cal_icon_dark.addPixmap(QtGui.QPixmap("CT_icons/runDark.png"))
        self.sub_calories_button.setIcon(sub_cal_icon_dark)
        self.sub_calories_button.setProperty('flat', False)
        self.sub_calories_button.setIconSize(QtCore.QSize(30, 30))
        self.sub_calories_button.setObjectName("sub_calories_button")
        # self.sub_calories_button.clicked.connect(self.subtract_calories)

        # meat label
        self.meat_text = QtWidgets.QLabel(self.centralwidget)
        self.meat_text.setGeometry(QtCore.QRect(650, 150, 100, 20))
        # self.meat_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.meat_text.setScaledContents(False)
        self.meat_text.setAlignment(QtCore.Qt.AlignCenter)
        self.meat_text.setObjectName("meat_text")

        # eggs label
        self.eggs_text = QtWidgets.QLabel(self.centralwidget)
        self.eggs_text.setGeometry(QtCore.QRect(650, 300, 100, 20))
        # self.eggs_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.eggs_text.setScaledContents(False)
        self.eggs_text.setAlignment(QtCore.Qt.AlignCenter)
        self.eggs_text.setObjectName("eggs_text")

        # sandwich label
        self.sandwich_text = QtWidgets.QLabel(self.centralwidget)
        self.sandwich_text.setGeometry(QtCore.QRect(650, 450, 100, 20))
        # self.sandwich_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.sandwich_text.setScaledContents(False)
        self.sandwich_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sandwich_text.setObjectName("sandwich_text")

        # sub cal label
        self.sub_calories_text = QtWidgets.QLabel(self.centralwidget)
        self.sub_calories_text.setGeometry(QtCore.QRect(667.5, 565, 65, 20))   # 50 pixels from button
        # self.sub_calories_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.sub_calories_text.setScaledContents(False)
        self.sub_calories_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_calories_text.setObjectName("sub_calories_text")

        # meal time logger label
        self.clock_text = QtWidgets.QLabel(self.centralwidget)
        self.clock_text.setGeometry(QtCore.QRect(300, 10, 120, 30))
        # self.clock_text.setStyleSheet(CT_stylesheets.text_label_font2)
        self.clock_text.setScaledContents(False)
        self.clock_text.setAlignment(QtCore.Qt.AlignCenter)
        self.clock_text.setObjectName("clock_text")

        # meal times list label
        self.meal_text = QtWidgets.QLabel(self.centralwidget)
        self.meal_text.setGeometry(QtCore.QRect(300, 160, 120, 220))
        # self.meal_text.setStyleSheet(CT_stylesheets.text_label_font1)
        self.meal_text.setScaledContents(False)
        self.meal_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.meal_text.setObjectName("meal_text")

        # MENU BAR
        # set screenshot folder menu option
        self.select_action = QtWidgets.QAction(MainWindow)
        self.select_action.setStatusTip('Select screenshots folder')
        # self.select_action.triggered.connect(self.select_directory)

        # reset values check menu
        self.reset_values_action = QtWidgets.QAction(MainWindow, checkable=True)
        self.reset_values_action.setObjectName("actionSubmenu2")
        # self.reset_values_action.setChecked(self.reset_app_value)
        # self.reset_values_action.triggered.connect(self.reset_app_toggler)

        # selectable max water values
        # for loop?
        self.set_water_10dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_10dl_action.setStatusTip('10 dl')
        # self.set_water_10dl_action.triggered.connect(self.set_water_to_10dl)
        self.set_water_15dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_15dl_action.setStatusTip('15 dl')
        # self.set_water_15dl_action.triggered.connect(self.set_water_to_15dl)
        self.set_water_20dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_20dl_action.setStatusTip('20 dl')
        # self.set_water_20dl_action.triggered.connect(self.set_water_to_20dl)
        self.set_water_25dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_25dl_action.setStatusTip('25 dl')
        # self.set_water_25dl_action.triggered.connect(self.set_water_to_25dl)
        self.set_water_30dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_30dl_action.setStatusTip('30 dl')
        # self.set_water_30dl_action.triggered.connect(self.set_water_to_30dl)
        self.set_water_35dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_35dl_action.setStatusTip('35 dl')
        # self.set_water_35dl_action.triggered.connect(self.set_water_to_35dl)
        self.set_water_40dl_action = QtWidgets.QAction(MainWindow)
        self.set_water_40dl_action.setStatusTip('40 dl')
        # self.set_water_40dl_action.triggered.connect(self.set_water_to_40dl)

        # selectable max calories values
        self.set_calories_1000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_1000cal_action.setStatusTip('1000 cal')
        # self.set_calories_1000cal_action.triggered.connect(self.set_calories_to_1000)
        self.set_calories_1500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_1500cal_action.setStatusTip('1500 cal')
        # self.set_calories_1500cal_action.triggered.connect(self.set_calories_to_1500)
        self.set_calories_2000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_2000cal_action.setStatusTip('2000 cal')
        # self.set_calories_2000cal_action.triggered.connect(self.set_calories_to_2000)
        self.set_calories_2500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_2500cal_action.setStatusTip('2500 cal')
        # self.set_calories_2500cal_action.triggered.connect(self.set_calories_to_2500)
        self.set_calories_3000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_3000cal_action.setStatusTip('3000 cal')
        # self.set_calories_3000cal_action.triggered.connect(self.set_calories_to_3000)
        self.set_calories_3500cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_3500cal_action.setStatusTip('3500 cal')
        # self.set_calories_3500cal_action.triggered.connect(self.set_calories_to_3500)
        self.set_calories_4000cal_action = QtWidgets.QAction(MainWindow)
        self.set_calories_4000cal_action.setStatusTip('4000 cal')
        # self.set_calories_4000cal_action.triggered.connect(self.set_calories_to_4000)

        # creating menu bar itself
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 759, 21))
        self.menu_bar.setObjectName("menu_bar")
    
        # creating file menu
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")

        # creating max values/water/calories/help menus
        self.set_max_values_menu = QtWidgets.QMenu(self.menu_bar)
        self.set_max_values_menu.setObjectName("set_max_values_menu")
        self.set_water_menu = QtWidgets.QMenu(self.set_max_values_menu)
        self.set_calories_menu = QtWidgets.QMenu(self.set_max_values_menu)
        self.help_menu = QtWidgets.QMenu(self.menu_bar)
        self.help_menu.setObjectName('help_menu')

        # creating about action | general about, current build?
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName('about_action')
        # self.about_action.triggered.connect(self.open_about)

        # creating view source action
        self.project_page_action = QtWidgets.QAction(MainWindow)
        self.project_page_action.setObjectName('source_code_action')
        # self.project_page_action.triggered.connect(self.open_project_page)
       
        # setting up file menu
        self.file_menu.addAction(self.select_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.reset_values_action)
        self.menu_bar.addAction(self.file_menu.menuAction())

        # setting up set max values menu
        self.menu_bar.addAction(self.set_max_values_menu.menuAction())
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
        self.menu_bar.addAction(self.help_menu.menuAction())
        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.project_page_action)

        MainWindow.setMenuBar(self.menu_bar)
        MainWindow.setCentralWidget(self.centralwidget)

        # TOOL BAR
        self.tool_bar = QtWidgets.QToolBar(MainWindow)
        self.tool_bar.setFloatable(False)
        self.tool_bar.setMovable(False)
        self.tool_bar.setObjectName("tool_bar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)

        # swap female/male image button
        swap_body_button = QtWidgets.QAction(QtGui.QIcon("CT_icons/swapBody.png"),
                                     "Male/female", MainWindow)
        # swap_body_button.triggered.connect(self.swap_body_image)
        self.tool_bar.addAction(swap_body_button)

        # reset app button
        reset_button = QtWidgets.QAction(QtGui.QIcon("CT_icons/reset.png"),
                                     "Reset app", MainWindow)
        # reset_button.triggered.connect(self.reset_app)
        self.tool_bar.addAction(reset_button)

        # save screenshot button
        ss_button = QtWidgets.QAction(QtGui.QIcon("CT_icons/screenshooter.png"),
                                  "Save screenshot", MainWindow)
        # ss_button.triggered.connect(self.take_screenshot)
        self.tool_bar.addAction(ss_button)

        # switch appearance button
        self.appearance_button = QtWidgets.QAction(QtGui.QIcon("CT_icons/darken.png"),
                                          'Darken', MainWindow)
        # self.appearance_button.triggered.connect(self.switch_appearance)
        self.tool_bar.addAction(self.appearance_button)

        # minimize to tray button
        self.minimize_button = QtWidgets.QAction(QtGui.QIcon("CT_icons/shrink.png"),
                                          'Minimize to tray', MainWindow)
        # self.minimize_button.triggered.connect(self.minimize)
        self.tool_bar.addAction(self.minimize_button)

        # hour logger
        self.hour_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.hour_edit.setGeometry(QtCore.QRect(300, 50, 60, 50))
        self.hour_edit.setStyleSheet("font: 20pt \"Segoe UI\"""; color: black")
        self.hour_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_edit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)        
        self.hour_edit.setObjectName("hour_edit")

        # minute logger
        self.min_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.min_edit.setGeometry(QtCore.QRect(359, 50, 60, 50))
        self.min_edit.setStyleSheet("font: 20pt \"Segoe UI\"""; color: black")
        self.min_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.min_edit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.min_edit.setObjectName("min_edit")

        # meal time logging button
        self.meal_time_button = QtWidgets.QPushButton(self.centralwidget)
        self.meal_time_button.setGeometry(QtCore.QRect(300, 100, 120, 25))
        meal_time_icon = QtGui.QIcon()
        meal_time_icon.addPixmap(QtGui.QPixmap("CT_icons/clock.png"))
        self.meal_time_button.setIcon(meal_time_icon)
        self.meal_time_button.setIconSize(QtCore.QSize(20, 20))
        self.meal_time_button.setObjectName('meal_time_button')
        # self.meal_time_button.clicked.connect(self.meal_logger)

        # set time to now button
        self.get_current_time_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_current_time_button.setGeometry(QtCore.QRect(300, 125, 120, 25))  # 25
        self.get_current_time_button.setObjectName('get_current_time_button')
        self.get_current_time_button.setStyleSheet("font: 9pt \"Segoe UI\";\n;""text-align: center")
        # self.get_current_time_button.clicked.connect(self.set_time_to_present)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consumption Tracker"))
        
        # BUTTON FUNCTIONALITY labels
        self.glass_text.setText(_translate("MainWindow", "2 dl"))
        self.small_bottle_text.setText(_translate("MainWindow", "5 dl"))
        self.large_bottle_text.setText(_translate("MainWindow", "10 dl"))
        self.add_water_label.setText(_translate('MainWindow', 'Manage water'))
        self.sub_water_text.setText(_translate('MainWindow', '-1 dl'))
        self.add_calories_label.setText(_translate('MainWindow', 'Manage calories'))
        self.sub_calories_text.setText(_translate('MainWindow', '-100 cal'))
        self.sandwich_text.setText(_translate('MainWindow', '200 cal'))
        self.eggs_text.setText(_translate('MainWindow', '500 cal'))
        self.meat_text.setText(_translate('MainWindow', '1000 cal'))
        self.clock_text.setText(_translate('MainWindow', "Set meal times"))
        self.get_current_time_button.setText(_translate('MainWindow', "Set current time"))

        # CENTRALWIDGET TEXT labels
        self.calories_LCD_per_sign.setText(_translate("MainWindow", "/"))
        self.calories_unit_label.setText(_translate('MainWindow', 'cal'))
        self.water_LCD_per_sign.setText(_translate("MainWindow", "/"))
        self.water_unit_label.setText(_translate('MainWindow', 'dl'))

        self.meal_text.setText(_translate('MainWindow', 'none'))

        # TIME EDIT settings
        self.hour_edit.setDisplayFormat(_translate("MainWindow", "HH"))
        self.min_edit.setDisplayFormat(_translate("MainWindow", "mm"))
        # self.hour_edit.setTime(self.saved_hour)
        # self.min_edit.setTime(self.saved_min)

        # BUTTON tooltips
        self.sub_water_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Subtract 1 dl</p></body></html>'))
        self.glass_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 2 dl</p></body></html>'))
        self.small_bottle_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 5 dl</p></body></html>'))
        self.large_bottle_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 10 dl</p></body></html>'))
        self.sub_calories_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Subtract 100 cal</p></body></html>'))
        self.sandwich_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 200 cal</p></body></html>'))
        self.eggs_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 500 cal</p></body></html>'))
        self.meat_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Add 1000 cal</p></body></html>'))
        self.meal_time_button.setToolTip(_translate('MainWindow', '<html><head/><body><p align="center">Log time</p></body></html>'))

        # PROGRESS BAR tooltips
        self.water_bar.setToolTip((_translate('MainWindow', '<html><head/><body><p align="center">Current water</p></body></html>')))
        self.cal_bar.setToolTip((_translate('MainWindow', '<html><head/><body><p align="center">Current calories</p></body></html>')))

        # menu_bar titles
        self.file_menu.setTitle(_translate("MainWindow", "File"))
        self.set_max_values_menu.setTitle(_translate("MainWindow", "Set max values"))
        self.help_menu.setTitle(_translate("MainWindow", "Help"))

        self.reset_values_action.setText(_translate("MainWindow", "Reset app in the morning"))
        self.select_action.setText(_translate("MainWindow", "Set screenshots folder"))
        self.set_water_menu.setTitle(_translate("MainWindow", "Water"))
        self.set_calories_menu.setTitle(_translate("MainWindow", "Calories"))
        self.about_action.setText(_translate('MainWindow', 'About'))
        self.project_page_action.setText(_translate('MainWindow', 'View project page'))

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

























































































