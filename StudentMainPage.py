from PyQt5 import QtCore, QtGui, QtWidgets
from Calcs import Ui_Calculators
from JoinClass import Ui_ClassWindow
from Settings import Ui_Settings
from Learn import Ui_LearnWindow
import res
import sqlite3

class Ui_StudentMainWindow(object):
    def setupUi(self, StudentMainWindow):
        StudentMainWindow.setObjectName("StudentMainWindow")
        StudentMainWindow.resize(1200, 800)
        StudentMainWindow.setWindowTitle("Student Main Window")
        StudentMainWindow.setStyleSheet("QMainWindow#StudentMainWindow{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(StudentMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calcsButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openCalcs())
        self.calcsButton.setGeometry(QtCore.QRect(200, 300, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.calcsButton.setFont(font)
        self.calcsButton.setStyleSheet("QPushButton#calcsButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#calcsButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#calcsButton:pressed{background-color: rgb(170, 170, 170);}")
        self.calcsButton.setText("Calculators")
        self.calcsButton.setObjectName("calcsButton")
        self.optionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.optionsLabel.setGeometry(QtCore.QRect(350, 180, 500, 50))
        font.setPointSize(14)
        self.optionsLabel.setFont(font)
        self.optionsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.optionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.optionsLabel.setText("Please select one of the options below:")
        self.optionsLabel.setObjectName("optionsLabel")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomeLabel.setGeometry(QtCore.QRect(300, 100, 600, 100))
        font.setPointSize(30)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)

        connection = sqlite3.connect("Users.db")
        cur = connection.cursor()
        cur.execute("SELECT firstName from tblStudentUsers WHERE Logged_in = 1")
        items = cur.fetchone()
        firstName = items[0]
        connection.commit()
        connection.close()
        self.welcomeLabel.setText(f"Welcome {firstName}!")
        
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("QPushButton#homeButton{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton{image: url(:/images/home button.png);}")
        self.homeButton.setObjectName("homeButton")
        self.learnButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.openLearn())
        self.learnButton.setGeometry(QtCore.QRect(700, 300, 300, 100))
        font.setPointSize(22)
        self.learnButton.setFont(font)
        self.learnButton.setStyleSheet("QPushButton#learnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#learnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#learnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.learnButton.setText("Learn")
        self.learnButton.setObjectName("learnButton")
        self.SettingsButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openSettings())
        self.SettingsButton.setGeometry(QtCore.QRect(700, 500, 300, 100))
        font.setPointSize(22)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setStyleSheet("QPushButton#SettingsButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SettingsButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SettingsButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SettingsButton.setText("Settings")
        self.SettingsButton.setObjectName("SettingsButton")
        self.classesButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openJoinClass())
        self.classesButton.setGeometry(QtCore.QRect(200, 500, 300, 100))
        font.setPointSize(22)
        self.classesButton.setFont(font)
        self.classesButton.setStyleSheet("QPushButton#classesButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#classesButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#classesButton:pressed{background-color: rgb(170, 170, 170);}")
        self.classesButton.setText("Classes")
        self.classesButton.setObjectName("classesButton")
        StudentMainWindow.setCentralWidget(self.centralwidget)

    def openCalcs(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Calculators()
        self.ui.setupUi(self.window)
        self.window.show()

    def openJoinClass(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui = Ui_ClassWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Settings()
        self.ui.setupUi(self.window)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.window.show()
    
    def openLearn(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui = Ui_LearnWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentMainWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentMainWindow()
    ui.setupUi(StudentMainWindow)
    StudentMainWindow.show()
    sys.exit(app.exec_())