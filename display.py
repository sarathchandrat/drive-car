import sys
from PyQt4 import QtGui
def x():
    print('button pressed')

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   c=QtGui.QPushButton('on',w)
   c.setCheckable(False)
   c.toggle()
   #c.setText('start')
   w.setGeometry(0,0,200,200)
   #b.move(10,10) 
   c.move(10,30)
   w.setWindowTitle("Drivig")
   w.show()
   c.clicked[bool].connect(x)
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
