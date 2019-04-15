from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLineEdit, QLabel, QGridLayout
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # stworzenie przycisku z napisem test
        self.button = QPushButton('Rysuj', self)
        self.xlabel=QLabel('X',self)
        self.xEdit=QLineEdit()
        self.ylabel=QLabel('Y',self)
        self.yEdit=QLineEdit()
        
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.canvas=FigureCanvas(self.figure)
        
        # ladne ustawienie i wyrodkowanie
        grid = QGridLayout(self)
        grid.addWidget(self.button,1,1)
        grid.addWidget(self.xlabel,1,0)
        grid.addWidget(self.xEdit,2,0)
        grid.addWidget(self.ylabel,2,1)
        grid.addWidget(self.yEdit,3,1)
        grid.addWidget(self.canvas,4,2,-1,-1)

    def handleButton(self):
        x=float(self.xEdit.text())
        y=float(self.yEdit.text())
        
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        ax.plot(x,y,'ro')
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())