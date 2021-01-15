# ------------------------------------------------- -----
# ---------------------- main.py ------------------- ----
# --------------------------------------------- ---------
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import pandas as pd
import random


class MatplotlibWidget(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        loadUi("test.ui", self)

        self.setWindowTitle("PyQt5 & Matplotlib Example GUI")

        self.pushButton1.clicked.connect(self.update_graph)
        self.pushButton2.clicked.connect(self.Quit)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def update_graph(self):
        df = pd.read_csv('data.csv', delimiter=',')
        waktu = df['hari_ke']
        kasus = df['kasus_baru']
        sembuh = df['sembuh_baru']

        self.MplWidget.canvas.axes1.clear()
        self.MplWidget.canvas.axes1.plot(waktu, kasus, 'r-')
        self.MplWidget.canvas.axes1.set_title(' Data Kasus Baru Covid-19')
        self.MplWidget.canvas.axes1.grid(True)

        self.MplWidget.canvas.axes2.clear()
        self.MplWidget.canvas.axes2.plot(waktu, sembuh, 'g-')
        self.MplWidget.canvas.axes2.set_title(' Data Sembuh Baru Covid-19')
        self.MplWidget.canvas.axes2.grid(True)
        self.MplWidget.canvas.draw()

    def Quit(self):
        self.close()


app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
