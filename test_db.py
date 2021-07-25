from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200,40)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.vlayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("LABEL")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.vlayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 245, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vlayout.addItem(spacerItem)

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())