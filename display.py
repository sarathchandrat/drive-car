# import sys
# from PyQt4 import QtGui
# from PyQt4 import QtCore
# from main import press
# window_properties={'window_height':500,'window_width':200,'window_Title':'Command Control'}
# def x():
#     print('button pressed')
# def window():
#     global window_properties
#     app = QtGui.QApplication(sys.argv)
#     w = QtGui.QWidget()
#     w.setGeometry(0,0,window_properties['window_height'],window_properties['window_width'])
#     w.setWindowTitle(window_properties['window_Title'])
#
#     motor_off_on=QtGui.QPushButton('on',w)
#     motor_off_on.setCheckable(True)
#     motor_off_on.setFixedSize(50,25)
#     motor_off_on.move(450,10)
#
#     motor_clockwise=QtGui.QPushButton('clockwise',w)
#     motor_clockwise.setCheckable(False)
#     motor_clockwise.setFixedSize(75,25)
#     motor_clockwise.setFixedSize(75,25)
#     motor_clockwise.move(90,20)
#
#     motor_anti_clockwise=QtGui.QPushButton('anti clockwise',w)
#     motor_anti_clockwise.setCheckable(False)
#     motor_anti_clockwise.setFixedSize(100,25)
#     motor_anti_clockwise.move(80,100)
#
#     left_turn=QtGui.QPushButton('left',w)
#     left_turn.setCheckable(False)
#     left_turn.setFixedSize(50,25)
#     left_turn.move(35,60)
#
#     stop=QtGui.QPushButton('stop',w)
#     stop.setCheckable(False)
#     stop.setFixedSize(40,25)
#     stop.move(100,60)
#
#     right_turn=QtGui.QPushButton('right',w)
#     right_turn.setCheckable(False)
#     right_turn.move(150,60)
#     right_turn.setFixedSize(50,25)
#
#     motor_magnitude=QtGui.QSlider(QtCore.Qt.Horizontal,w)
#     motor_magnitude.setMinimum(0)
#     motor_magnitude.setMaximum(10)
#     motor_magnitude.setValue(0)
#     motor_magnitude.setTickPosition(QtGui.QSlider.TicksBelow)
#     motor_magnitude.setTickInterval(1)
#     motor_magnitude.move(380,60)
#     #layout.addWidget(motor_magnitude)
#     #w.setLayout(layout)
#
#     #c.toggle()
#     #c.setText('start')
#     #b.move(10,10)
#     w.show()
#     #print(motor_off_on.clicked[bool])
#     motor_off_on.clicked[bool].connect(press)
#     #c.toggle()
#     sys.exit(app.exec_())
#     '''
#     w = QtGui.QWidget()
#     b = QtGui.QLabel(w)
#     b.setText("Hello World!")
#     w.setGeometry(100,100,200,50)
#     b.move(50,20)
#     w.setWindowTitle("Drivig")
#     w.show()
#     sys.exit(app.exec_())
#     '''
# if __name__ == '__main__':
#     window()
import sys
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class sliderdemo(QWidget):
    def __init__(self, parent = None):
        super(sliderdemo, self).__init__(parent)
        self.motor_off_on=QPushButton('on',self)
        self.motor_off_on.setCheckable(True)
        self.motor_off_on.setFixedSize(50,25)
        self.motor_off_on.move(450,10)

        self.motor_clockwise=QPushButton('clockwise',self)
        self.motor_clockwise.setEnabled(False)
        self.motor_clockwise.setCheckable(True)
        self.motor_clockwise.setFixedSize(75,25)
        self.motor_clockwise.move(90,20)

        self.motor_anti_clockwise=QPushButton('anti clockwise',self)
        self.motor_anti_clockwise.setEnabled(False)
        self.motor_anti_clockwise.setCheckable(True)
        self.motor_anti_clockwise.setFixedSize(100,25)
        self.motor_anti_clockwise.move(80,100)

        self.left_turn=QPushButton('left',self)
        self.left_turn.setEnabled(False)
        self.left_turn.setCheckable(True)
        self.left_turn.setFixedSize(50,25)
        self.left_turn.move(35,60)

        self.stop=QPushButton('stop',self)
        self.stop.setEnabled(False)
        self.stop.setCheckable(False)
        self.stop.setFixedSize(40,25)
        self.stop.move(100,60)

        self.right_turn=QPushButton('right',self)
        self.right_turn.setEnabled(False)
        self.right_turn.setCheckable(True)
        self.right_turn.move(150,60)
        self.right_turn.setFixedSize(50,25)

        self.sl = QSlider(Qt.Horizontal,self)
        self.sl.setMinimum(0)
        self.sl.setMaximum(10)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(1)
        self.sl.move(380,60)
        self.sl.setEnabled(False)
        self.motor_off_on.clicked[bool].connect(self.valuechange)
        self.motor_clockwise.clicked[bool].connect(self.motor_wheeldirection)
        self.motor_anti_clockwise.clicked[bool].connect(self.motor_wheeldirection)
        self.left_turn.clicked[bool].connect(self.turn_direction)
        self.right_turn.clicked[bool].connect(self.turn_direction)
        self.stop.clicked[bool].connect(self.complete_stop)
        self.sl.valueChanged.connect(self.valuechange)
        self.setWindowTitle("Driving application")
    def valuechange(self):
        self.motor_state=self.motor_off_on.isChecked()
        if self.motor_state:
            self.motor_clockwise.setEnabled(True)
            self.motor_anti_clockwise.setEnabled(True)
            self.left_turn.setEnabled(True)
            self.right_turn.setEnabled(True)
            self.sl.setEnabled(True)
            self.stop.setEnabled(True)
        else:
            self.motor_clockwise.setChecked(False)
            self.motor_anti_clockwise.setChecked(False)
            self.left_turn.setChecked(False)
            self.right_turn.setChecked(False)
            self.sl.setValue(0)
            self.motor_clockwise.setEnabled(False)
            self.motor_clockwise.setEnabled(False)
            self.motor_anti_clockwise.setEnabled(False)
            self.left_turn.setEnabled(False)
            self.right_turn.setEnabled(False)
            self.sl.setEnabled(False)
            self.stop.setEnabled(False)
    def motor_wheeldirection(self):
        source=self.sender()
        if source.text()=='clockwise' and self.motor_anti_clockwise.isChecked():
            self.motor_anti_clockwise.toggle()
        elif source.text()=='anti clockwise' and self.motor_clockwise.isChecked():
            self.motor_clockwise.toggle()
        elif source.text()=='clockwise':
                print('the motor must move in forward direction')
    def turn_direction(self):
        source=self.sender()
        if source.text()=='left' and self.right_turn.isChecked():
            self.right_turn.toggle()
        elif source.text()=='right' and self.left_turn.isChecked():
            self.left_turn.toggle()
    def complete_stop(self,pressed):
        print(pressed)
        self.motor_clockwise.setChecked(False)
        self.motor_anti_clockwise.setChecked(False)
        self.left_turn.setChecked(False)
        self.right_turn.setChecked(False)
        self.sl.setValue(0)


def main():
   app = QApplication(sys.argv)
   ex = sliderdemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
