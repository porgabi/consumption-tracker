human_bar = ("""
    QProgressBar {
        border: 1px solid transparent;
        text-align: center;
        color:rgba(0,0,0,100);
        border-radius: 5px;
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(182, 182, 182, 100), stop:1 rgba(209, 209, 209, 100));
    }
    QProgressBar::chunk {
        background-color: qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.494, y2:0, stop: 0 rgba(21, 158, 71, 255), stop: 1 rgba(32, 201, 90, 255));
    }
    """
)

water_bar_light = ("""
    QProgressBar:horizontal {
        border: 2px solid black;
        border-radius: 3px;
        background: white;
        padding: 0px;
        font: 19pt \"Segoe UI\";
        text-align: center;
        margin-right: 0ex;
    }
    QProgressBar::chunk:horizontal {
        background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));
    }
    QProgressBar {
        color: black;
        font: 15px
    }
    """
)

water_bar_dark = ("""
    QProgressBar:horizontal { 
        border: 2px solid black;
        border-radius: 3px;
        background: rgb(90, 90, 90);
        font: 75 12pt \"Segoe UI\";
        text-align: center;
        margin-right: 0ex;
    }
    QProgressBar::chunk:horizontal {
        background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgba(135, 224, 255, 255), stop: 1 rgba(64, 164, 223, 255));
    }
    QProgressBar {
        color: white;
        font: 15px
    }
    """
)

cal_bar_light = ("""
    QProgressBar:horizontal {
        border: 2px solid black;
        border-radius: 3px;
        background: white;
        padding: 0px;
        text-align: center;
        margin-right: 0ex;
    }
    QProgressBar::chunk:horizontal {
        background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));
    }
    QProgressBar {
        color: black;
        font: 15px
    }
    """
)

cal_bar_dark = ("""
    QProgressBar:horizontal {
        border: 2px solid black;
        border-radius: 3px;
        background: rgb(90, 90, 90);
        padding: 0px;
        text-align: center;
        margin-right: 0ex;
    }
    QProgressBar::chunk:horizontal {
        background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 yellow, stop: 1 rgba(255, 170, 170, 255));
    }
    QProgressBar {
        color: white;
        font: 15px
    }
    """
)

cal_color = "color: rgba(255, 130, 0, 255);"

water_color = "color: rgb(64, 164, 223);"

text_label_font1 = "font: 11pt \"Segoe UI\";"

text_label_font2 = "font: 12pt \"Segoe UI\";"

menu_bar_light = ("""
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
    """
)

menu_bar_dark = ("""
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
    QMenu {
        background-color: rgb(90, 90, 90);
        color: rgb(255,255,255);
        border: 1px solid white;           
    }
    QMenu::item::selected {
        background-color: rgb(120, 120, 120);
    }
    """
)

tool_bar_light = ("""
    QToolBar {
        background-color: white;
    }
    QToolButton {
        background-color: white;
    }
    """
)

tool_bar_dark = ("""
    QToolBar {
        background-color: rgb(90, 90, 90);
    }
    QToolButton {
        background-color: rgb(90, 90, 90);
    }
    """
)


background_light = "background: rgb(255, 255, 255); color: black"

background_dark = "background: rgb(90, 90, 90); color: white"

secondary_menu_light = ("""
    QMenu {
        background-color: rgb(255, 255, 255);
        color: black;
        border: 1px solid black;           
    }
    QMenu::item::selected {
        background-color: rgb(220, 220, 220);
    }
    """
)

secondary_menu_dark = ("""
    QMenu {
        background-color: rgb(90, 90, 90);
        color: rgb(255,255,255);
        border: 1px solid white;           
    }
    QMenu::item::selected {
        background-color: rgb(120, 120, 120);
    }
    """
)


time_edit_light = "background: rgb(255, 255, 255); font: 20pt \"Segoe UI\"""; color: black"

time_edit_dark = "background: rgb(90, 90, 90); font: 20pt \"Segoe UI\"""; color: white"

tooltip_light = ("""
    QToolTip { 
        background-color: white; 
        color: black; 
        border: 1px solid black;
    }
    QLabel {
        color: black;
    }
    """
)

tooltip_dark = ("""
    QToolTip { 
        background-color: rgb(90, 90, 90); 
        color: white; 
        border: 1px solid white
    }
    QLabel {
        color: white;
    }
    """
)


app_open_about1 = ("""
    QPushButton {
        background-color: rgb(90, 90, 90);
        color: white;
    } 
    QLabel {
        color: white
    }
    """
)

app_open_about2 = ("""
    QPushButton {
        background-color: white;
        color: black;
    }
    QLabel {
        color: white;
    }
    """
)

app_open_project1 = ("""
    QPushButton {
        background-color: rgb(90, 90, 90);
        color: white;
    } 
    QLabel {
        color: white
    }
    """
)            

app_open_project2 = ("""
    QPushButton {
        background-color: white;
        color: black;
    }
    QLabel {
        color: white;
    }
    """
)




