# ------------------------------------------------- -----
# -------------------- mplwidget.py --------------------
# -------------------------------------------------- ----
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure


class MplWidget(QWidget):

    def __init__(self,  parent=None):

        QWidget.__init__(self,  parent)

        self.canvas = FigureCanvasQTAgg(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes1 = self.canvas.figure.add_subplot(211)
        self.canvas.axes2 = self.canvas.figure.add_subplot(212)
        self.setLayout(vertical_layout)
