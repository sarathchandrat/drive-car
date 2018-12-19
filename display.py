import sys
from PyQt4 import QtGui
window_properties={'window_height':500,'window_width':200,'window_Title':'Command Control'}
def x():
    print('button pressed')
def window():
    global window_properties
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setGeometry(0,0,window_properties['window_height'],window_properties['window_width'])
    w.setWindowTitle(window_properties['window_Title'])
    motor_off_on=QtGui.QPushButton('on',w)
    motor_off_on.setCheckable(True)
    motor_off_on.move(400,10)
    motor_clockwise=QtGui.QPushButton('clockwise',w)
    motor_clockwise.setCheckable(True)
    motor_clockwise.move
    #c.toggle()
    #c.setText('start')
    #b.move(10,10)
    w.show()
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
