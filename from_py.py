import sys
from PyQt5 import QtWidgets
from ui.main import Ui_MainWindow


class myMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.setText('Text Changed')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = myMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
