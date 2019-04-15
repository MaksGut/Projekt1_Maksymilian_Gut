from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Rysuj', self)
        self.clrChoose=QPushButton('Wybierz Kolor', self)
        self.xlabel = QLabel("X", self)
        self.xEdit = QLineEdit()
        self.ylabel = QLabel("Y", self)
        self.yEdit = QLineEdit()
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        layout.addWidget(self.xlabel, 1, 0)
        layout.addWidget(self.xEdit, 1, 1)
        layout.addWidget(self.ylabel, 2, 0)
        layout.addWidget(self.yEdit, 2, 1)
		
        layout.addWidget(self.button, 3, 1, 1, -1) 
        layout.addWidget(self.canvas, 4, 1, 1, -1)
        layout.addWidget(self.clrChoose, 5, 1, 1, -1)
        
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        
    def checkValues(self, lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float(lineE.text())
        else:
            return None
        
        
    def rysuj(self, clr='r'):
        x = self.checkValues(self.xEdit)
        y = self.checkValues(self.yEdit)
		
        if x !=None and y != None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'o', color=clr)
            self.canvas.draw()
        
    def handleButton(self):
        self.rysuj()

    def clrChooseF(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.rysuj(color.name())
        else:
            pass
if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())