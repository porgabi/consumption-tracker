import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from model.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainView
import CT_stylesheets


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Connect everything together
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    app.setStyle('Fusion')

    # should not belong here :(
    if app.model._light_on is True:
        light_palette = QtGui.QPalette()
        light_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))
        app.setPalette(light_palette)
        app.setStyleSheet(CT_stylesheets.tooltip_light)
    else:
        dark_palette = QtGui.QPalette()
        dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(90, 90, 90))
        app.setPalette(dark_palette)
        app.setStyleSheet(CT_stylesheets.tooltip_dark)


    sys.exit(app.exec_())