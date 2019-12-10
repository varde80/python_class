from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
import sys

class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        def initUI(self):
            cb = QCheckBox('show title',self)
            cb.move(20,20)
            cb.toggle()
            cb.stateChanged.connect(self.changeTitle)

            self.setGeometry(300,300,250,1500)
            self.show()

        def changeTitle(self, state):
            if state == Qt.checked:




    def prt_hello(self):
        print(self.btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())