import sys
from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/main.ui', self)

        self.pushButton.setText('Text Changed')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
