import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
window_properties={'window_height':500,'window_width':200,'window_Title':'Command Control'}
def x():
    print('button pressed')
def window():
    global window_properties
    app = QtGui.QApplication(sys.argv)
    #layout=QtGui.QGridLayout()
    w = QtGui.QWidget()
    w.setGeometry(0,0,window_properties['window_height'],window_properties['window_width'])
    w.setWindowTitle(window_properties['window_Title'])

    motor_off_on=QtGui.QPushButton('on',w)
    motor_off_on.setCheckable(True)
    motor_off_on.setFixedSize(50,25)
    motor_off_on.move(450,10)

    #layout.addWidget(motor_off_on,0,40)

    motor_clockwise=QtGui.QPushButton('clockwise',w)
    motor_clockwise.setCheckable(False)
    motor_clockwise.setFixedSize(75,25)
    motor_clockwise.move(90,20)

    #layout.addWidget(motor_clockwise,15,20)

    motor_anti_clockwise=QtGui.QPushButton('anti clockwise',w)
    motor_anti_clockwise.setCheckable(False)
    motor_anti_clockwise.setFixedSize(100,25)
    motor_anti_clockwise.move(80,100)
    #layout.addWidget(motor_anti_clockwise)

    left_turn=QtGui.QPushButton('left',w)
    left_turn.setCheckable(False)
    left_turn.setFixedSize(50,25)
    left_turn.move(35,60)
    #layout.addWidget(left_turn)

    stop=QtGui.QPushButton('stop',w)
    stop.setCheckable(False)
    stop.setFixedSize(40,25)
    stop.move(100,60)
    #layout.addWidget(stop)

    right_turn=QtGui.QPushButton('right',w)
    right_turn.setCheckable(False)
    right_turn.move(150,60)
    right_turn.setFixedSize(50,25)
    #layout.addWidget(right_turn)
    motor_magnitude=QtGui.QSlider(QtCore.Qt.Horizontal,w)
    motor_magnitude.setMinimum(0)
    motor_magnitude.setMaximum(10)
    motor_magnitude.setValue(0)
    motor_magnitude.setTickPosition(QtGui.QSlider.TicksBelow)
    motor_magnitude.setTickInterval(1)
    motor_magnitude.move(380,60)
    #layout.addWidget(motor_magnitude)
    #w.setLayout(layout)

    #c.toggle()
    #c.setText('start')
    #b.move(10,10)
    w.show()
    print(motor_off_on.clicked[bool])
    motor_off_on.clicked[bool].connect(x)
    #c.toggle()
    sys.exit(app.exec_())
    '''
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    w.setWindowTitle("Drivig")
    w.show()
    sys.exit(app.exec_())
    '''
if __name__ == '__main__':
    window()
