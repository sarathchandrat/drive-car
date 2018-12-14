import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   c=QtGui.QPushButton(w)
   c.setText('start')
   w.setGeometry(100,100,200,50)
   b.move(10,10)
   c.move(10,30)
   w.setWindowTitle("Drivig")
   w.show()
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
