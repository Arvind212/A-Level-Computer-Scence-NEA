from PyQt5 import QtCore, QtGui, QtWidgets
from Differentiation_Calc import differentiate
from Integration_Calc import integrate
from Def_Integration_Calc import Def_Integration_Calc
import res

class Ui_Calculators(object):
    def setupUi(self, Calculators):
        Calculators.setObjectName("Calculators")
        Calculators.resize(1200, 800)
        Calculators.setWindowTitle("Calculators")
        Calculators.setStyleSheet("QMainWindow#Calculators{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(Calculators)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget{background-color: rgb(24, 24, 24);}")
        self.stackedWidget.setObjectName("stackedWidget")
#--------------------------------------------------------------------------------Options Page
        self.OptionsPage = QtWidgets.QWidget()
        self.OptionsPage.setObjectName("OptionsPage")
        self.diffButton = QtWidgets.QPushButton(self.OptionsPage, clicked = lambda: self.gotoDiffPage())
        self.diffButton.setGeometry(QtCore.QRect(200, 400, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.diffButton.setFont(font)
        self.diffButton.setStyleSheet("QPushButton#diffButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#diffButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#diffButton:pressed{background-color: rgb(170, 170, 170);}")
        self.diffButton.setText("Differentiation")
        self.diffButton.setObjectName("diffButton")
        self.CalculatorsLabel = QtWidgets.QLabel(self.OptionsPage)
        self.CalculatorsLabel.setGeometry(QtCore.QRect(300, 150, 600, 100))
        font.setPointSize(30)
        self.CalculatorsLabel.setFont(font)
        self.CalculatorsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.CalculatorsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CalculatorsLabel.setText("Calculators")
        self.CalculatorsLabel.setObjectName("CalculatorsLabel")
        self.intButton = QtWidgets.QPushButton(self.OptionsPage, clicked = lambda:self.gotoIntPage())
        self.intButton.setGeometry(QtCore.QRect(700, 400, 300, 100))
        font.setPointSize(22)
        self.intButton.setFont(font)
        self.intButton.setStyleSheet("QPushButton#intButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#intButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#intButton:pressed{background-color: rgb(170, 170, 170);}")
        self.intButton.setText("Integration")
        self.intButton.setObjectName("intButton")
        self.DefIntegrationButton = QtWidgets.QPushButton(self.OptionsPage, clicked = lambda: self.gotoDefIntegrationPage())
        self.DefIntegrationButton.setGeometry(QtCore.QRect(375, 550, 450, 100))
        self.DefIntegrationButton.setFont(font)
        self.DefIntegrationButton.setStyleSheet("QPushButton#DefIntegrationButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#DefIntegrationButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#DefIntegrationButton:pressed{background-color: rgb(170, 170, 170);}")
        self.DefIntegrationButton.setText("Definite Integration")
        self.DefIntegrationButton.setObjectName("DefIntegrationButton")
        self.homeButton = QtWidgets.QPushButton(self.OptionsPage, clicked = lambda:self.gotoOptionsPage())
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("QPushButton#homeButton{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton{image: url(:/images/home button.png);}")
        self.homeButton.setObjectName("homeButton")
        self.stackedWidget.addWidget(self.OptionsPage)
#-------------------------------------------------------------------------------------Differentiation Page
        self.DiffPage = QtWidgets.QWidget()
        self.DiffPage.setObjectName("DiffPage")
        self.expressionLineEdit = QtWidgets.QLineEdit(self.DiffPage)
        self.expressionLineEdit.setGeometry(QtCore.QRect(50, 150, 1100, 100))
        font.setPointSize(20)
        font.setBold(False)
        self.expressionLineEdit.setFont(font)
        self.expressionLineEdit.setStyleSheet("QLineEdit#expressionLineEdit{border-radius:10px;padding-left:10px}")
        self.expressionLineEdit.setPlaceholderText("Enter Function here")
        self.expressionLineEdit.setObjectName("expressionLineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.DiffPage)
        self.spinBox.setGeometry(QtCore.QRect(200, 450, 200, 50))
        font.setPointSize(20)
        font.setBold(False)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.CalcLabel = QtWidgets.QLabel(self.DiffPage)
        self.CalcLabel.setGeometry(QtCore.QRect(250, 40, 700, 100))
        font.setPointSize(30)
        font.setBold(True)
        self.CalcLabel.setFont(font)
        self.CalcLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.CalcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CalcLabel.setText("Differentiation Calculator")
        self.CalcLabel.setObjectName("CalcLabel")
        self.TimesLabel = QtWidgets.QLabel(self.DiffPage)
        self.TimesLabel.setGeometry(QtCore.QRect(40, 450, 150, 50))
        font.setPointSize(15)
        self.TimesLabel.setFont(font)
        self.TimesLabel.setStyleSheet("color: rgb(170,170,170);")
        self.TimesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimesLabel.setText("Derivatives:")
        self.TimesLabel.setObjectName("TimesLabel")
        self.answerLabel = QtWidgets.QLabel(self.DiffPage)
        self.answerLabel.setGeometry(QtCore.QRect(500, 550, 200, 50))
        self.answerLabel.setFont(font)
        self.answerLabel.setStyleSheet("color: rgb(170,170,170);")
        self.answerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel.setText("Answer:")
        self.answerLabel.setObjectName("answerLabel")
        self.homeButton_2 = QtWidgets.QPushButton(self.DiffPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_2.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.homeButton_2.setFont(font)
        self.homeButton_2.setStyleSheet("QPushButton#homeButton_2{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_2:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_2:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_2{image: url(:/images/home button.png);}")
        self.homeButton_2.setObjectName("homeButton_2")
        self.answerButton = QtWidgets.QPushButton(self.DiffPage, clicked = lambda: self.derivative())
        self.answerButton.setGeometry(QtCore.QRect(450, 420, 300, 100))
        font.setPointSize(22)
        self.answerButton.setFont(font)
        self.answerButton.setStyleSheet("QPushButton#answerButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#answerButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#answerButton:pressed{background-color: rgb(170, 170, 170);}")
        self.answerButton.setText("Calculate")
        self.answerButton.setObjectName("answerButton")
        self.clearButton = QtWidgets.QPushButton(self.DiffPage, clicked = lambda: self.clear())
        self.clearButton.setGeometry(QtCore.QRect(60, 300, 120, 70))
        font.setPointSize(18)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("QPushButton#clearButton{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#clearButton:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#clearButton:pressed{background-color: rgb(255, 212, 161);}")
        self.clearButton.setText("clear")
        self.clearButton.setObjectName("clearButton")
        self.answerLineEdit = QtWidgets.QLineEdit(self.DiffPage)
        self.answerLineEdit.setGeometry(QtCore.QRect(100, 600, 1000, 150))
        font.setPointSize(25)
        font.setBold(False)
        self.answerLineEdit.setFont(font)
        self.answerLineEdit.setText("")
        self.answerLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLineEdit.setReadOnly(True)
        self.answerLineEdit.setObjectName("answerLineEdit")
        self.powerButton = QtWidgets.QPushButton(self.DiffPage, clicked = lambda: self.power())
        self.powerButton.setGeometry(QtCore.QRect(230, 300, 70, 70))
        font.setPointSize(22)
        font.setBold(True)
        self.powerButton.setFont(font)
        self.powerButton.setStyleSheet("QPushButton#powerButton{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#powerButton:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#powerButton:pressed{background-color: rgb(255, 212, 161);}")
        self.powerButton.setText("^")
        self.powerButton.setObjectName("powerButton")
        self.exampleLabel = QtWidgets.QLabel(self.DiffPage)
        self.exampleLabel.setGeometry(QtCore.QRect(770, 250, 375, 350))
        font.setPointSize(15)
        font.setBold(False)
        self.exampleLabel.setFont(font)
        self.exampleLabel.setStyleSheet("color: rgb(255,255,255)")
        self.exampleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exampleLabel.setText("Format: ax^b +cx^d -ex^f\nCannot do:\nln(x),e,sin(x),cos(x),tan(x)\nExamples:\n2x^2 +4x -9\n7x^2/3 +4x +6\n2/3x^7 -8x^2\n1/2x^3/2 -6/2x^7")
        self.exampleLabel.setObjectName("exampleLabel")
        self.stackedWidget.addWidget(self.DiffPage)
#-------------------------------------------------------------------------Integration Page
        self.IntegrationPage = QtWidgets.QWidget()
        self.IntegrationPage.setObjectName("IntegrationPage")
        self.powerButton_2 = QtWidgets.QPushButton(self.IntegrationPage, clicked = lambda: self.power())
        self.powerButton_2.setGeometry(QtCore.QRect(230, 300, 70, 70))
        font.setPointSize(22)
        font.setBold(True)
        self.powerButton_2.setFont(font)
        self.powerButton_2.setStyleSheet("QPushButton#powerButton_2{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#powerButton_2:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#powerButton_2:pressed{background-color: rgb(255, 212, 161);}")
        self.powerButton_2.setText("^")
        self.powerButton_2.setObjectName("powerButton_2")
        self.answerLineEdit_2 = QtWidgets.QLineEdit(self.IntegrationPage)
        self.answerLineEdit_2.setGeometry(QtCore.QRect(100, 600, 1000, 150))
        font.setPointSize(25)
        font.setBold(False)
        self.answerLineEdit_2.setFont(font)
        self.answerLineEdit_2.setText("")
        self.answerLineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLineEdit_2.setReadOnly(True)
        self.answerLineEdit_2.setObjectName("answerLineEdit_2")
        self.CalcLabel_2 = QtWidgets.QLabel(self.IntegrationPage)
        self.CalcLabel_2.setGeometry(QtCore.QRect(250, 40, 700, 100))
        font.setPointSize(30)
        font.setBold(True)
        self.CalcLabel_2.setFont(font)
        self.CalcLabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.CalcLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CalcLabel_2.setText("Integration Calculator")
        self.CalcLabel_2.setObjectName("CalcLabel_2")
        self.expressionLineEdit_2 = QtWidgets.QLineEdit(self.IntegrationPage)
        self.expressionLineEdit_2.setGeometry(QtCore.QRect(50, 150, 1100, 100))
        font.setPointSize(20)
        font.setBold(False)
        self.expressionLineEdit_2.setFont(font)
        self.expressionLineEdit_2.setStyleSheet("QLineEdit#expressionLineEdit_2{border-radius:10px;padding-left:10px}")
        self.expressionLineEdit_2.setPlaceholderText("Enter Function here")
        self.expressionLineEdit_2.setObjectName("expressionLineEdit_2")
        self.answerButton_2 = QtWidgets.QPushButton(self.IntegrationPage, clicked=lambda: self.integrate())
        self.answerButton_2.setGeometry(QtCore.QRect(450, 420, 300, 100))
        font.setPointSize(22)
        font.setBold(True)
        self.answerButton_2.setFont(font)
        self.answerButton_2.setStyleSheet("QPushButton#answerButton_2{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#answerButton_2:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#answerButton_2:pressed{background-color: rgb(170, 170, 170);}")
        self.answerButton_2.setText("Calculate")
        self.answerButton_2.setObjectName("answerButton_2")
        self.answerLabel_2 = QtWidgets.QLabel(self.IntegrationPage)
        self.answerLabel_2.setGeometry(QtCore.QRect(500, 550, 200, 50))
        font.setPointSize(15)
        self.answerLabel_2.setFont(font)
        self.answerLabel_2.setStyleSheet("color: rgb(170,170,170);")
        self.answerLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel_2.setText("Answer:")
        self.answerLabel_2.setObjectName("answerLabel_2")
        self.clearButton_2 = QtWidgets.QPushButton(self.IntegrationPage, clicked = lambda: self.clear())
        self.clearButton_2.setGeometry(QtCore.QRect(60, 300, 120, 70))
        font.setPointSize(18)
        self.clearButton_2.setFont(font)
        self.clearButton_2.setStyleSheet("QPushButton#clearButton_2{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#clearButton_2:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#clearButton_2:pressed{background-color: rgb(255, 212, 161);}")
        self.clearButton_2.setText("clear")
        self.clearButton_2.setObjectName("clearButton_2")
        self.homeButton_3 = QtWidgets.QPushButton(self.IntegrationPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_3.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font.setPointSize(15)
        self.homeButton_3.setFont(font)
        self.homeButton_3.setStyleSheet("QPushButton#homeButton_3{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_3:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_3:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_3{image: url(:/images/home button.png);}")
        self.homeButton_3.setObjectName("homeButton_3")
        self.exampleLabel_2 = QtWidgets.QLabel(self.IntegrationPage)
        self.exampleLabel_2.setGeometry(QtCore.QRect(770, 250, 375, 350))
        font.setBold(False)
        self.exampleLabel_2.setFont(font)
        self.exampleLabel_2.setStyleSheet("color: rgb(255,255,255)")
        self.exampleLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.exampleLabel_2.setText("Format: ax^b +cx^d -ex^f\nCannot do:\nln(x),e,sin(x),cos(x),tan(x)\nExamples:\n2x^2 +4x -9\n7x^2/3 +4x +6\n2/3x^7 -8x^2\n1/2x^3/2 -6/2x^7")
        self.exampleLabel_2.setObjectName("exampleLabel_2")
        self.stackedWidget.addWidget(self.IntegrationPage)
#------------------------------------------------------------------------Definite Integration
        self.DefIntegrationPage = QtWidgets.QWidget()
        self.DefIntegrationPage.setObjectName("DefIntegrationPage")
        self.clearButton_3 = QtWidgets.QPushButton(self.DefIntegrationPage, clicked = lambda: self.clear())
        self.clearButton_3.setGeometry(QtCore.QRect(60, 300, 120, 70))
        font.setPointSize(18)
        font.setBold(True)
        self.clearButton_3.setFont(font)
        self.clearButton_3.setStyleSheet("QPushButton#clearButton_3{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#clearButton_3:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#clearButton_3:pressed{background-color: rgb(255, 212, 161);}")
        self.clearButton_3.setText("clear")
        self.clearButton_3.setObjectName("clearButton_3")
        self.answerLabel_3 = QtWidgets.QLabel(self.DefIntegrationPage)
        self.answerLabel_3.setGeometry(QtCore.QRect(500, 550, 200, 50))
        font.setPointSize(15)
        self.answerLabel_3.setFont(font)
        self.answerLabel_3.setStyleSheet("color: rgb(170,170,170);")
        self.answerLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLabel_3.setText("Answer:")
        self.answerLabel_3.setObjectName("answerLabel_3")
        self.powerButton_3 = QtWidgets.QPushButton(self.DefIntegrationPage, clicked = lambda: self.power())
        self.powerButton_3.setGeometry(QtCore.QRect(230, 300, 70, 70))
        font.setPointSize(22)
        self.powerButton_3.setFont(font)
        self.powerButton_3.setStyleSheet("QPushButton#powerButton_3{background-color: rgb(252, 138, 0);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#powerButton_3:hover{background-color: rgb(255, 175, 79);}\n"
"QPushButton#powerButton_3:pressed{background-color: rgb(255, 212, 161);}")
        self.powerButton_3.setText("^")
        self.powerButton_3.setObjectName("powerButton_3")
        self.answerLineEdit_3 = QtWidgets.QLineEdit(self.DefIntegrationPage)
        self.answerLineEdit_3.setGeometry(QtCore.QRect(100, 600, 1000, 150))
        font.setPointSize(20)
        self.answerLineEdit_3.setFont(font)
        self.answerLineEdit_3.setText("")
        self.answerLineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.answerLineEdit_3.setReadOnly(True)
        self.answerLineEdit_3.setObjectName("answerLineEdit_3")
        self.CalcLabel_3 = QtWidgets.QLabel(self.DefIntegrationPage)
        self.CalcLabel_3.setGeometry(QtCore.QRect(150, 40, 900, 100))
        font.setPointSize(30)
        self.CalcLabel_3.setFont(font)
        self.CalcLabel_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.CalcLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CalcLabel_3.setText("Definite Integration Calculator")
        self.CalcLabel_3.setObjectName("CalcLabel_3")
        self.expressionLineEdit_3 = QtWidgets.QLineEdit(self.DefIntegrationPage)
        self.expressionLineEdit_3.setGeometry(QtCore.QRect(50, 150, 1100, 100))
        font.setPointSize(20)
        font.setBold(False)
        self.expressionLineEdit_3.setFont(font)
        self.expressionLineEdit_3.setStyleSheet("QLineEdit#expressionLineEdit_3{border-radius:10px;padding-left:10px}")
        self.expressionLineEdit_3.setPlaceholderText("Enter Function here")
        self.expressionLineEdit_3.setObjectName("expressionLineEdit_3")
        self.upperLimitLineEdit = QtWidgets.QLineEdit(self.DefIntegrationPage)
        self.upperLimitLineEdit.setGeometry(QtCore.QRect(50, 420, 340, 50))
        self.upperLimitLineEdit.setFont(font)
        self.upperLimitLineEdit.setStyleSheet("QLineEdit#upperLimitLineEdit{border-radius:10px;padding-left:10px}")
        self.upperLimitLineEdit.setPlaceholderText("Upper Limit")
        self.upperLimitLineEdit.setObjectName("upperLimitLineEdit")
        self.lowerLimitLineEdit = QtWidgets.QLineEdit(self.DefIntegrationPage)
        self.lowerLimitLineEdit.setGeometry(QtCore.QRect(50, 500, 340, 50))
        self.lowerLimitLineEdit.setFont(font)
        self.lowerLimitLineEdit.setStyleSheet("QLineEdit#lowerLimitLineEdit{border-radius:10px;padding-left:10px}")
        self.lowerLimitLineEdit.setPlaceholderText("Lower Limit")
        self.lowerLimitLineEdit.setObjectName("lowerLimitLineEdit")
        self.answerButton_3 = QtWidgets.QPushButton(self.DefIntegrationPage, clicked=lambda: self.def_integrate())
        self.answerButton_3.setGeometry(QtCore.QRect(450, 420, 300, 100))
        font.setPointSize(22)
        font.setBold(True)
        self.answerButton_3.setFont(font)
        self.answerButton_3.setStyleSheet("QPushButton#answerButton_3{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#answerButton_3:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#answerButton_3:pressed{background-color: rgb(170, 170, 170);}")
        self.answerButton_3.setText("Calculate")
        self.answerButton_3.setObjectName("answerButton_3")
        self.homeButton_4 = QtWidgets.QPushButton(self.DefIntegrationPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_4.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font.setPointSize(15)
        self.homeButton_4.setFont(font)
        self.homeButton_4.setStyleSheet("QPushButton#homeButton_4{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_4:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_4:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_4{image: url(:/images/home button.png);}")
        self.homeButton_4.setObjectName("homeButton_4")
        self.exampleLabel_3 = QtWidgets.QLabel(self.DefIntegrationPage)
        self.exampleLabel_3.setGeometry(QtCore.QRect(770, 250, 375, 350))
        font.setBold(False)
        self.exampleLabel_3.setFont(font)
        self.exampleLabel_3.setStyleSheet("color: rgb(255,255,255)")
        self.exampleLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.exampleLabel_3.setText("Format: ax^b +cx^d -ex^f\nCannot do:\nln(x),e,sin(x),cos(x),tan(x)\nExamples:\n2x^2 +4x -9\n7x^2/3 +4x +6\n2/3x^7 -8x^2\n1/2x^3/2 -6/2x^7")
        self.exampleLabel_3.setObjectName("exampleLabel_3")
        self.stackedWidget.addWidget(self.DefIntegrationPage)
        Calculators.setCentralWidget(self.centralwidget)

        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Calculators)

    def gotoOptionsPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def gotoDiffPage(self):
        self.stackedWidget.setCurrentIndex(1)
    def gotoIntPage(self):
        self.stackedWidget.setCurrentIndex(2)
    def gotoDefIntegrationPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def derivative(self):
        try:
            try:
                expression = self.expressionLineEdit.text()
                number = self.spinBox.text()
                for i in range(int(number)):
                    expression = differentiate(expression)
                self.answerLineEdit.setText(expression)
            except IndexError:
                self.answerLineEdit.setText("The function cannot be differentiated!")
        except ValueError:
            self.answerLineEdit.setText("The function cannot be differentiated!")

    def integrate(self):
        try:
            try:
                expression = self.expressionLineEdit_2.text()
                answer = integrate(expression)
                self.answerLineEdit_2.setText(f"{answer} + C")
            except IndexError:
                self.answerLineEdit_2.setText("This function cannot be integrated!")
        except ValueError:
            self.answerLineEdit_2.setText("This function cannot be integrated!")

    def def_integrate(self):
        try:
            try:
                expression = self.expressionLineEdit_3.text()
                upper_limit = self.upperLimitLineEdit.text()
                lower_limit = self.lowerLimitLineEdit.text()
                if "/" in upper_limit:
                    x = upper_limit.split("/")
                    upper_limit = str(int(x[0]) / int(x[1]))
                if "/" in lower_limit:
                    x = lower_limit.split("/")
                    lower_limit = str(int(x[0]) / int(x[1]))
                answer = Def_Integration_Calc(expression,float(upper_limit),float(lower_limit)).def_integral()
                self.answerLineEdit_3.setText(answer)
            except IndexError:
                self.answerLineEdit_3.setText("Incomplete Fields.Please try again.")
        except ValueError:
            self.answerLineEdit_3.setText("Enter the correct limits and ensure format is correct")

    def clear(self):
        if self.stackedWidget.currentIndex() == 1:
            self.expressionLineEdit.setText("")
        elif self.stackedWidget.currentIndex() == 2:
            self.expressionLineEdit_2.setText("")
        elif self.stackedWidget.currentIndex() == 3:
            self.expressionLineEdit_3.setText("")

    def power(self):
        if self.stackedWidget.currentIndex() == 1:
            self.expressionLineEdit.setText(f'{self.expressionLineEdit.text()}^')
        elif self.stackedWidget.currentIndex() == 2:
            self.expressionLineEdit_2.setText(f'{self.expressionLineEdit_2.text()}^')
        elif self.stackedWidget.currentIndex() == 3:
            self.expressionLineEdit_3.setText(f'{self.expressionLineEdit_3.text()}^')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculators = QtWidgets.QMainWindow()
    ui = Ui_Calculators()
    ui.setupUi(Calculators)
    Calculators.show()
    sys.exit(app.exec_())