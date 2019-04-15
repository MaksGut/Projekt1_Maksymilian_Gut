from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Rysuj', self)
        self.clrChoose=QPushButton('Wybierz Kolor', self)
        self.xAlabel = QLabel("XA", self)
        self.xAEdit = QLineEdit()
        self.yAlabel = QLabel("YA", self)
        self.yAEdit = QLineEdit()
        
        self.xBlabel = QLabel("XB", self)
        self.xBEdit = QLineEdit()
        self.yBlabel = QLabel("YB", self)
        self.yBEdit = QLineEdit()
        
        self.xClabel = QLabel("XC", self)
        self.xCEdit = QLineEdit()
        self.yClabel = QLabel("YC", self)
        self.yCEdit = QLineEdit()
        
        self.xDlabel = QLabel("XD", self)
        self.xDEdit = QLineEdit()
        self.yDlabel = QLabel("YD", self)
        self.yDEdit = QLineEdit()
        
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.Wyniklabel = QLabel(self)
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        layout.addWidget(self.xAlabel, 1, 0)
        layout.addWidget(self.xAEdit, 1, 1)
        layout.addWidget(self.yAlabel, 2, 0)
        layout.addWidget(self.yAEdit, 2, 1)
		
        layout.addWidget(self.xBlabel, 1, 2)
        layout.addWidget(self.xBEdit, 1, 3)
        layout.addWidget(self.yBlabel, 2, 2)
        layout.addWidget(self.yBEdit, 2, 3)
        
        layout.addWidget(self.xClabel, 1, 4)
        layout.addWidget(self.xCEdit, 1, 5)
        layout.addWidget(self.yClabel, 2, 4)
        layout.addWidget(self.yCEdit, 2, 5)
        
        layout.addWidget(self.xDlabel, 1, 6)
        layout.addWidget(self.xDEdit, 1, 7)
        layout.addWidget(self.yDlabel, 2, 6)
        layout.addWidget(self.yDEdit, 2, 7)
        
        layout.addWidget(self.button, 3, 1, 1, -1) 
        layout.addWidget(self.canvas, 4, 1, 1, -1)
        layout.addWidget(self.clrChoose, 5, 1, 1, -1)
        
        layout.addWidget(self.Wyniklabel, 6, 5)
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        
    def checkValues(self, lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float(lineE.text())
        else:
            self.Wyniklabel.setText('Sprawdz wprowadzone wartosci')
            return None
        
        
    def rysuj(self, clr='r'):
        
        Xa = self.checkValues(self.xAEdit)
        Ya = self.checkValues(self.yAEdit)
        Xb = self.checkValues(self.xBEdit)
        Yb = self.checkValues(self.yBEdit)
        Xc = self.checkValues(self.xCEdit)
        Yc = self.checkValues(self.yCEdit)
        Xd = self.checkValues(self.xDEdit)
        Yd = self.checkValues(self.yDEdit)
        x1 = [self.checkValues(self.xAEdit), self.checkValues(self.xBEdit)]
        y1 = [self.checkValues(self.yAEdit), self.checkValues(self.yBEdit)]
        x2 = [self.checkValues(self.xCEdit), self.checkValues(self.xDEdit)]
        y2 = [self.checkValues(self.yCEdit), self.checkValues(self.yDEdit)]
        
        if Xa !=None and Ya != None and Xb != None and Yb != None and Xc != None and Yc != None and Xd != None and Yd != None:
            pass
        else:
            msg_err=QMessageBox()
            msg_err.setWindowTitle('Komunikat')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Podane współrzędne są niepoprawne')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
        try:
            t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
            t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        except ZeroDivisionError:
            self.Wyniklabel.setText('0 w mianowniku')
            msg_err=QMessageBox()
            msg_err.setWindowTitle('Komunikat')
            msg_err.setStandardButtons(QMessageBox.Ok)
            msg_err.setText('Błąd w trakcie liczenia, 0 w mianowniku')
            msg_err.exec_()
            self.figure.clear()
            self.canvas.draw()
            return None
        
        if t1<1 and t1>0 and t2>0 and t2<1:
            self.Wyniklabel.setText('Punkt należy do obu odcinków')
        elif 0<t1<1:
            self.Wyniklabel.setText('Punkt należy do odcinka AB, na przedłużeniu odcinka CD')
        elif 0<t2<1:
            self.Wyniklabel.setText('Punkt należy do odcinka CD, na przedłużeniu odcinka AB')
        elif t1<0 or t1>0:
            self.Wyniklabel.setText('Punkt leży na przedłużeniu AB i CD')
        elif t2<0 or t2>0:
            self.Wyniklabel.setText('Puknt leży na przedłużeniu AB i CD')
        else:
            pass

        Xp=Xa+t1*(Xb-Xa)
        Yp=Ya+t1*(Yb-Ya)
        if x1 !=None and y1 != None and x2 != None and y2 != None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x1, y1, '-', color=clr)
            ax.plot(x2,y2,'-',color=clr)
            ax.plot(Xp,Yp,'o', color=clr)
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