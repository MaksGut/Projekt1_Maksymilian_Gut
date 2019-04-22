from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QGridLayout, QColorDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        self.button = QPushButton('Rysuj', self)
        self.clrChoose=QPushButton('Wybierz Kolor AB', self)
        self.clrChoose2=QPushButton('Wybierz Kolor CD', self)
        self.button2 = QPushButton('Wyczysć', self)
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
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.Wyniklabel = QLabel(self)
        self.WspolrzednaXp = QLabel(self)
        self.WspolrzednaYp = QLabel(self)
        self.WspolrzednaX = QLabel(self)
        self.WspolrzednaY = QLabel(self)
        # ladne ustawienie i wysrodkowanie
        layout =  QGridLayout(self)
        
        self.setLayout(layout)
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
        layout.addWidget(self.button2, 4, 1, 1, -1) 
        layout.addWidget(self.toolbar, 5, 2, 1, -1)
        layout.addWidget(self.canvas, 6, 1, 1, -1)
        layout.addWidget(self.clrChoose, 7, 1, 1, 4)
        layout.addWidget(self.clrChoose2, 7, 5, 1, -1)
        
        layout.addWidget(self.Wyniklabel, 8, 6)
        layout.addWidget(self.WspolrzednaXp, 8, 2)
        layout.addWidget(self.WspolrzednaYp, 8, 4)
        layout.addWidget(self.WspolrzednaX, 8, 1)
        layout.addWidget(self.WspolrzednaY, 8, 3)


        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        self.clrChoose2.clicked.connect(self.clrChooseB)
        self.button2.clicked.connect(self.wyczysc)
    def checkValues(self, lineE):
        if lineE.text().lstrip('-').replace('.','').isdigit():
            return float(lineE.text())
        else:
            self.Wyniklabel.setText('Sprawdz wprowadzone wartosci')
            return None
        
        
    def rysuj(self, clr='g', clr2='b'):
        
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
        Xp=Xa+t1*(Xb-Xa)
        Yp=Ya+t1*(Yb-Ya)
        if t1<1 and t1>0 and t2>0 and t2<1:
            self.Wyniklabel.setText('Punkt należy do obu odcinków')
            if x1[0]==Xp and y1[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu A')
            if x1[1]==Xp and y1[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu B')
            if x2[0]==Xp and y2[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu C')
            if x2[1]==Xp and y2[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu D')
        elif 0<t1<1:
            self.Wyniklabel.setText('Punkt należy do odcinka AB, na przedłużeniu odcinka CD')
            if x1[0]==Xp and y1[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu A, przedłużenie odcinka CD')
            if x1[1]==Xp and y1[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu B, przedłużenie odcinka CD')
            if x2[0]==Xp and y2[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu C, należy do AB')
            if x2[1]==Xp and y2[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu D, należy do AB')
        elif 0<t2<1:
            self.Wyniklabel.setText('Punkt należy do odcinka CD, na przedłużeniu odcinka AB')
            if x1[0]==Xp and y1[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu A, należy do CD')
            if x1[1]==Xp and y1[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu B, należy do CD')
            if x2[0]==Xp and y2[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu C, na przedłużeniu odcinka AB')
            if x2[1]==Xp and y2[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu D, przedłużenie odcinka AB')
        elif t1<0 or t1>0:
            self.Wyniklabel.setText('Punkt leży na przedłużeniu AB i CD')
            if x1[0]==Xp and y1[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu A, przedłużenie odcinka CD')
            if x1[1]==Xp and y1[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu B, przedłużenie odcinka CD')
            if x2[0]==Xp and y2[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu C, przedłużenie odcinka AB')
            if x2[1]==Xp and y2[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu D, przedłużenie odcinka AB')
        elif t2<0 or t2>0:
            self.Wyniklabel.setText('Puknt leży na przedłużeniu AB i CD')
            if x1[0]==Xp and y1[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu A, przedłużenie odcinka CD')
            if x1[1]==Xp and y1[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu B, przedłużenie odcinka CD')
            if x2[0]==Xp and y2[0]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu C, przedłużenie odcinka AB')
            if x2[1]==Xp and y2[1]==Yp:
                self.Wyniklabel.setText('Współrzędne punktu przecięcia takie same jak punktu D, przedłużenie odcinka AB')          
        else:
            pass

        Xp=Xa+t1*(Xb-Xa)
        Yp=Ya+t1*(Yb-Ya)
        if x1 !=None and y1 != None and x2 != None and y2 != None:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x1, y1, '-', color=clr)
            ax.plot(x1, y1, 'o', color=clr)
            ax.text(Xp, Yp, 'P')
            ax.plot(x2,y2,'-',color=clr2)
            ax.plot(x2,y2,'o',color=clr2)
            ax.plot(Xp,Yp,'o', color='r')
            ax.text(x1[0],y1[0], 'A')
            ax.text(x1[1],y1[1], 'B')
            ax.text(x2[0],y2[0], 'C')
            ax.text(x2[1],y2[1], 'D')
            if t1<0 or t1>0:
                ax.plot([x1[0],Xp],[y1[0], Yp], c=clr, linestyle='dashed')
                ax.plot([x2[0],Xp],[y2[0], Yp], c=clr2,linestyle='dashed')
            if t2<0 or t2>0:
                ax.plot([x1[1],Xp],[y1[1], Yp], c=clr, linestyle='dashed')
                ax.plot([x2[1],Xp],[y2[1], Yp], c=clr2,linestyle='dashed')
            if 0<t2<1:
                ax.plot([x1[0],Xp],[y1[0], Yp], c=clr, linestyle='dashed')
            if 0<t1<1:
                ax.plot([x2[0],Xp],[y2[0], Yp], c=clr2, linestyle='dashed')
            self.canvas.draw()
        
        self.WspolrzednaX.setText('Współrzędna X: {:.2f}'.format(Xp))
        self.WspolrzednaY.setText('Współrzędna Y: {:.2f}'.format(Yp))
    def handleButton(self):
        self.rysuj()

    def clrChooseF(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.rysuj(clr=color.name())
        else:
            pass
    
    def clrChooseB(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.rysuj(clr2=color.name())
        else:
            pass

    def wyczysc(self):
        self.xAEdit.setText('')
        self.yAEdit.setText('')
        self.xBEdit.setText('')
        self.yBEdit.setText('')
        self.xCEdit.setText('')
        self.yCEdit.setText('')
        self.xDEdit.setText('')
        self.yDEdit.setText('')
        self.figure.clear()
        self.canvas.draw()
        self.Wyniklabel.setText('')
        self.WspolrzednaXp.setText('')
        self.WspolrzednaYp.setText('')
        self.WspolrzednaX.setText('')
        self.WspolrzednaY.setText('')
if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    window = Window()
    window.show()
    sys.exit(app.exec_())