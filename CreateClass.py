from PyQt5 import QtCore, QtGui, QtWidgets
import res
import sqlite3
import random
import string
import datetime

connection = sqlite3.connect("Users.db")
cursor = connection.cursor()
sqlCommand_class = '''CREATE TABLE if NOT EXISTS tblClass(
        ClassID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassCode TEXT,
        TeacherUsername TEXT,
        FOREIGN KEY (teacherUsername) REFERENCES tblTeacherUsers(username))'''
sqlCommand_assignment = '''CREATE TABLE if NOT EXISTS tblAssignments(
        AssignmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassID INTEGER,
        Name TEXT,
        DueDate DATE,
        FOREIGN KEY (ClassID) REFERENCES tblClass(ClassID))'''
sqlCommand_question = '''CREATE TABLE if NOT EXISTS tblQuestions(
        QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        AssignmentID INTEGER,
        Question TEXT,
        Answer TEXT,
        FOREIGN KEY (AssignmentID) REFERENCES tblAssignments(AssignmentID))'''
sqlCommand_ClassProgress = '''CREATE TABLE if NOT EXISTS tblClassProgress(
        SubmissionID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassID INTEGER,
        AssignmentID INTEGER,
        StudentUsername TEXT,
        Grade INTEGER,
        Date DATE,
        FOREIGN KEY (ClassID) REFERENCES tblClass(ClassID),
        FOREIGN KEY (StudentUsername) REFERENCES tblStudentUsers(username),
        FOREIGN KEY (AssignmentID) REFERENCES tblAssignments(AssignmentID))'''
cursor.execute(sqlCommand_class)
cursor.execute(sqlCommand_assignment)
cursor.execute(sqlCommand_question)
cursor.execute(sqlCommand_ClassProgress)
connection.commit()
connection.close()

class Ui_ClassWindow(object):
    def setupUi(self, ClassWindow):
        ClassWindow.setObjectName("ClassWindow")
        ClassWindow.resize(1200, 800)
        ClassWindow.setStyleSheet("QMainWindow#ClassWindow{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(ClassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget{background-color: rgb(24, 24, 24);}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.JoinClassPage = QtWidgets.QWidget()
        self.JoinClassPage.setObjectName("JoinClassPage")
        self.CreateClassButton = QtWidgets.QPushButton(self.JoinClassPage, clicked=lambda: self.save_class())
        self.CreateClassButton.setGeometry(QtCore.QRect(450, 500, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.CreateClassButton.setFont(font)
        self.CreateClassButton.setStyleSheet("QPushButton#CreateClassButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#CreateClassButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#CreateClassButton:pressed{background-color: rgb(170, 170, 170);}")
        self.CreateClassButton.setObjectName("CreateClassButton")
        self.createClassLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.createClassLabel.setGeometry(QtCore.QRect(300, 120, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.createClassLabel.setFont(font)
        self.createClassLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.createClassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createClassLabel.setObjectName("createClassLabel")
        self.optionsLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.optionsLabel.setGeometry(QtCore.QRect(320, 250, 560, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.optionsLabel.setFont(font)
        self.optionsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.optionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.optionsLabel.setObjectName("optionsLabel")
        self.ClassCodeLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.ClassCodeLabel.setGeometry(QtCore.QRect(305, 340, 610, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.ClassCodeLabel.setFont(font)
        self.ClassCodeLabel.setStyleSheet("color: rgb(255, 85, 0);")
        self.ClassCodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        class_code = (''.join(random.choices(string.ascii_uppercase + string.digits, k=18)))
        self.ClassCodeLabel.setText(class_code)
        self.ClassCodeLabel.setObjectName("ClassCodeLabel")
        self.stackedWidget.addWidget(self.JoinClassPage)
#-------------------------------------------------------------------------------------------Options Page
        self.ClassPage = QtWidgets.QWidget()
        self.ClassPage.setObjectName("ClassPage")
        self.WelcomeLabel = QtWidgets.QLabel(self.ClassPage)
        self.WelcomeLabel.setGeometry(QtCore.QRect(100, 150, 1000, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.WelcomeLabel.setFont(font)
        self.WelcomeLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.AssignmentsButton = QtWidgets.QPushButton(self.ClassPage, clicked=lambda: self.assignment_table())
        self.AssignmentsButton.setGeometry(QtCore.QRect(200, 400, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.AssignmentsButton.setFont(font)
        self.AssignmentsButton.setStyleSheet("QPushButton#AssignmentsButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#AssignmentsButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#AssignmentsButton:pressed{background-color: rgb(170, 170, 170);}")
        self.AssignmentsButton.setObjectName("AssignmentsButton")
        self.progressButton = QtWidgets.QPushButton(self.ClassPage, clicked=lambda: self.gotoProgressPage())
        self.progressButton.setGeometry(QtCore.QRect(700, 400, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.progressButton.setFont(font)
        self.progressButton.setStyleSheet("QPushButton#progressButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#progressButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#progressButton:pressed{background-color: rgb(170, 170, 170);}")
        self.progressButton.setObjectName("progressButton")
        self.homeButton_2 = QtWidgets.QPushButton(self.ClassPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_2.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.homeButton_2.setFont(font)
        self.homeButton_2.setStyleSheet("QPushButton#homeButton_2{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_2:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_2:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_2{image: url(:/images/home button.png);}")
        self.homeButton_2.setObjectName("homeButton_2")
        self.ClassCodeLabel_2 = QtWidgets.QLabel(self.ClassPage)
        self.ClassCodeLabel_2.setGeometry(QtCore.QRect(350, 220, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ClassCodeLabel_2.setFont(font)
        self.ClassCodeLabel_2.setStyleSheet("color: rgb(255, 85, 0);")
        self.ClassCodeLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ClassCodeLabel_2.setText(class_code)
        self.ClassCodeLabel_2.setObjectName("ClassCodeLabel_2")
        self.stackedWidget.addWidget(self.ClassPage)
#-------------------------------------------------------------------------------------------Assignments Page
        self.AssignmentPage = QtWidgets.QWidget()
        self.AssignmentPage.setObjectName("AssignmentPage")
        self.AssignmentsLabel = QtWidgets.QLabel(self.AssignmentPage)
        self.AssignmentsLabel.setGeometry(QtCore.QRect(300, 50, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.AssignmentsLabel.setFont(font)
        self.AssignmentsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.AssignmentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentsLabel.setObjectName("AssignmentsLabel")
        self.homeButton_3 = QtWidgets.QPushButton(self.AssignmentPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_3.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.homeButton_3.setFont(font)
        self.homeButton_3.setStyleSheet("QPushButton#homeButton_3{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_3:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_3:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_3{image: url(:/images/home button.png);}")
        self.homeButton_3.setObjectName("homeButton_3")
        self.editAssignButton = QtWidgets.QPushButton(self.AssignmentPage, clicked=lambda: self.edit_assignment())
        self.editAssignButton.setGeometry(QtCore.QRect(100, 550, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.editAssignButton.setFont(font)
        self.editAssignButton.setStyleSheet("QPushButton#editAssignButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#editAssignButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#editAssignButton:pressed{background-color: rgb(170, 170, 170);}")
        self.editAssignButton.setObjectName("editAssignButton")
        self.AssignmentsTableWidget = QtWidgets.QTableWidget(self.AssignmentPage)
        self.AssignmentsTableWidget.setGeometry(QtCore.QRect(45, 260, 524, 260))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AssignmentsTableWidget.setFont(font)
        self.AssignmentsTableWidget.setStyleSheet("QTableWidget#tableWidget{background-color: rgb(24, 24, 24);}")
        self.AssignmentsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.AssignmentsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.AssignmentsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.AssignmentsTableWidget.setSortingEnabled(True)
        self.AssignmentsTableWidget.setObjectName("AssignmentsTableWidget")
        self.AssignmentsTableWidget.setColumnCount(2)
        self.AssignmentsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.AssignmentsTableWidget.setHorizontalHeaderLabels(["Date Due","Assignment"])
        self.AssignmentsTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.AssignmentsTableWidget.horizontalHeader().setFixedHeight(50)
        self.AssignmentsTableWidget.horizontalHeader().setFont(font)
        self.createAssignButton = QtWidgets.QPushButton(self.AssignmentPage, clicked=lambda: self.add_assignment())
        self.createAssignButton.setGeometry(QtCore.QRect(690, 650, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.createAssignButton.setFont(font)
        self.createAssignButton.setStyleSheet("QPushButton#createAssignButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#createAssignButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#createAssignButton:pressed{background-color: rgb(170, 170, 170);}")
        self.createAssignButton.setObjectName("createAssignButton")
        self.assignmentsInfoLabel = QtWidgets.QLabel(self.AssignmentPage)
        self.assignmentsInfoLabel.setGeometry(QtCore.QRect(250, 130, 700, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.assignmentsInfoLabel.setFont(font)
        self.assignmentsInfoLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.assignmentsInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.assignmentsInfoLabel.setObjectName("assignmentsInfoLabel")

        self.OngoingAssignLabel = QtWidgets.QLabel(self.AssignmentPage)
        self.OngoingAssignLabel.setGeometry(QtCore.QRect(100, 210, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.OngoingAssignLabel.setFont(font)
        self.OngoingAssignLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.OngoingAssignLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OngoingAssignLabel.setObjectName("OngoingAssignLabel")

        self.AssignmentLineEdit = QtWidgets.QLineEdit(self.AssignmentPage)
        self.AssignmentLineEdit.setGeometry(QtCore.QRect(680, 250, 420, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AssignmentLineEdit.setFont(font)
        self.AssignmentLineEdit.setStyleSheet("QLineEdit#AssignmentLineEdit{border-radius:10px;padding-left:10px}")
        self.AssignmentLineEdit.setObjectName("AssignmentLineEdit")
        self.deleteAssignButton = QtWidgets.QPushButton(self.AssignmentPage, clicked = lambda: self.delete_assignment())
        self.deleteAssignButton.setGeometry(QtCore.QRect(100, 650, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.deleteAssignButton.setFont(font)
        self.deleteAssignButton.setStyleSheet("QPushButton#deleteAssignButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#deleteAssignButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#deleteAssignButton:pressed{background-color: rgb(170, 170, 170);}")
        self.deleteAssignButton.setObjectName("deleteAssignButton")
        self.NameErrorLabel = QtWidgets.QLabel(self.AssignmentPage)
        self.NameErrorLabel.setGeometry(QtCore.QRect(720, 320, 350, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NameErrorLabel.setFont(font)
        self.NameErrorLabel.setStyleSheet("QLabel#NameErrorLabel{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.NameErrorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NameErrorLabel.setObjectName("NameErrorLabel")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.AssignmentPage)
        self.calendarWidget.setGeometry(QtCore.QRect(680, 380, 420, 250))
        self.calendarWidget.setMinimumDate(datetime.date.today())
        self.calendarWidget.setObjectName("calendarWidget")
        self.stackedWidget.addWidget(self.AssignmentPage)
#---------------------------------------------------------------------------------------------Add Questions Page
        self.AddQuestionsPage = QtWidgets.QWidget()
        self.AddQuestionsPage.setObjectName("AddQuestionsPage")
        self.questionsLabel = QtWidgets.QLabel(self.AddQuestionsPage)
        self.questionsLabel.setGeometry(QtCore.QRect(300, 20, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.questionsLabel.setFont(font)
        self.questionsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.questionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionsLabel.setObjectName("questionsLabel")
        self.AssignmentLabel = QtWidgets.QLabel(self.AddQuestionsPage)
        self.AssignmentLabel.setGeometry(QtCore.QRect(300, 100, 600, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.AssignmentLabel.setFont(font)
        self.AssignmentLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.AssignmentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentLabel.setObjectName("AssignmentLabel")
        self.questionTextBrowser = QtWidgets.QTextBrowser(self.AddQuestionsPage)
        self.questionTextBrowser.setGeometry(QtCore.QRect(230, 180, 800, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.questionTextBrowser.setFont(font)
        self.questionTextBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.questionTextBrowser.setReadOnly(False)
        self.questionTextBrowser.setTabChangesFocus(True)
        self.questionTextBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.questionTextBrowser.setObjectName("questionTextBrowser")
        self.QuestionIDLabel = QtWidgets.QLabel(self.AddQuestionsPage)
        self.QuestionIDLabel.setGeometry(QtCore.QRect(100, 180, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.QuestionIDLabel.setFont(font)
        self.QuestionIDLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QuestionIDLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.QuestionIDLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT MAX(QuestionID) FROM tblQuestions;")
            items = cursor.fetchone()
            QuestionID = int(items[0])
        except TypeError:
            QuestionID = 0
        connection.commit()
        connection.close()
        self.QuestionIDLabel.setText(f"{QuestionID + 1})")
        
        self.QuestionIDLabel.setObjectName("QuestionIDLabel")
        self.answerLineEdit = QtWidgets.QLineEdit(self.AddQuestionsPage)
        self.answerLineEdit.setGeometry(QtCore.QRect(230, 470, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.answerLineEdit.setFont(font)
        self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px}")
        self.answerLineEdit.setPlaceholderText("Enter the answer here")
        self.answerLineEdit.setObjectName("answerLineEdit")
        self.AddQnButton = QtWidgets.QPushButton(self.AddQuestionsPage, clicked=lambda: self.add_question())
        self.AddQnButton.setGeometry(QtCore.QRect(230, 640, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.AddQnButton.setFont(font)
        self.AddQnButton.setStyleSheet("QPushButton#AddQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#AddQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#AddQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.AddQnButton.setObjectName("AddQnButton")
        self.FinishButton = QtWidgets.QPushButton(self.AddQuestionsPage, clicked=lambda: self.finish_adding())
        self.FinishButton.setGeometry(QtCore.QRect(710, 640, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.FinishButton.setFont(font)
        self.FinishButton.setStyleSheet("QPushButton#FinishButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#FinishButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#FinishButton:pressed{background-color: rgb(170, 170, 170);}")
        self.FinishButton.setObjectName("FinishButton")
        self.homeButton = QtWidgets.QPushButton(self.AddQuestionsPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("QPushButton#homeButton{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton{image: url(:/images/home button.png);}")
        self.homeButton.setObjectName("homeButton")
        self.stackedWidget.addWidget(self.AddQuestionsPage)
#---------------------------------------------------------------------------------------------Edit Questions Page
        self.EditQuestionsPage = QtWidgets.QWidget()
        self.EditQuestionsPage.setObjectName("EditQuestionsPage")
        self.homeButton_4 = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.gotoOptionsPage())
        self.homeButton_4.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.homeButton_4.setFont(font)
        self.homeButton_4.setStyleSheet("QPushButton#homeButton_4{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_4:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_4:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_4{image: url(:/images/home button.png);}")
        self.homeButton_4.setObjectName("homeButton_4")
        self.NextQnButton = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.next_qn())
        self.NextQnButton.setGeometry(QtCore.QRect(850, 110, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.NextQnButton.setFont(font)
        self.NextQnButton.setStyleSheet("QPushButton#NextQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#NextQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#NextQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.NextQnButton.setObjectName("NextQnButton")
        self.QuestionIDLabel_2 = QtWidgets.QLabel(self.EditQuestionsPage)
        self.QuestionIDLabel_2.setGeometry(QtCore.QRect(100, 230, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.QuestionIDLabel_2.setFont(font)
        self.QuestionIDLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QuestionIDLabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.QuestionIDLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.QuestionIDLabel_2.setObjectName("QuestionIDLabel_2")
        self.questionTextBrowser_2 = QtWidgets.QTextBrowser(self.EditQuestionsPage)
        self.questionTextBrowser_2.setGeometry(QtCore.QRect(230, 230, 800, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.questionTextBrowser_2.setFont(font)
        self.questionTextBrowser_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.questionTextBrowser_2.setReadOnly(False)
        self.questionTextBrowser_2.setTabChangesFocus(True)
        self.questionTextBrowser_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextSelectableByMouse)
        self.questionTextBrowser_2.setObjectName("questionTextBrowser_2")
        self.AssignmentLabel_2 = QtWidgets.QLabel(self.EditQuestionsPage)
        self.AssignmentLabel_2.setGeometry(QtCore.QRect(350, 100, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.AssignmentLabel_2.setFont(font)
        self.AssignmentLabel_2.setStyleSheet("color: rgb(170, 170, 170);")
        self.AssignmentLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentLabel_2.setObjectName("AssignmentLabel_2")
        self.editQuestionsLabel = QtWidgets.QLabel(self.EditQuestionsPage)
        self.editQuestionsLabel.setGeometry(QtCore.QRect(300, 20, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.editQuestionsLabel.setFont(font)
        self.editQuestionsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.editQuestionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editQuestionsLabel.setObjectName("editQuestionsLabel")
        self.PrevQnButton = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.prev_qn())
        self.PrevQnButton.setGeometry(QtCore.QRect(50, 110, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.PrevQnButton.setFont(font)
        self.PrevQnButton.setStyleSheet("QPushButton#PrevQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#PrevQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#PrevQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.PrevQnButton.setObjectName("PrevQnButton")
        self.answerLineEdit_2 = QtWidgets.QLineEdit(self.EditQuestionsPage)
        self.answerLineEdit_2.setGeometry(QtCore.QRect(230, 480, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.answerLineEdit_2.setFont(font)
        self.answerLineEdit_2.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px}")
        self.answerLineEdit_2.setPlaceholderText("Enter the answer here")
        self.answerLineEdit_2.setObjectName("answerLineEdit_2")
        self.FinishButton2 = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.finish_editing())
        self.FinishButton2.setGeometry(QtCore.QRect(820, 640, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.FinishButton2.setFont(font)
        self.FinishButton2.setStyleSheet("QPushButton#FinishButton2{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#FinishButton2:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#FinishButton2:pressed{background-color: rgb(170, 170, 170);}")
        self.FinishButton2.setObjectName("FinishButton2")
        self.SaveQnButton = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.save_qn())
        self.SaveQnButton.setGeometry(QtCore.QRect(440, 640, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SaveQnButton.setFont(font)
        self.SaveQnButton.setStyleSheet("QPushButton#SaveQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SaveQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SaveQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SaveQnButton.setObjectName("SaveQnButton")
        self.DeleteQnButton = QtWidgets.QPushButton(self.EditQuestionsPage, clicked=lambda: self.delete_qn())
        self.DeleteQnButton.setGeometry(QtCore.QRect(60, 640, 320, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.DeleteQnButton.setFont(font)
        self.DeleteQnButton.setStyleSheet("QPushButton#DeleteQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#DeleteQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#DeleteQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.DeleteQnButton.setObjectName("DeleteQnButton")
        self.DueDateLabel = QtWidgets.QLabel(self.EditQuestionsPage)
        self.DueDateLabel.setGeometry(QtCore.QRect(380, 160, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.DueDateLabel.setFont(font)
        self.DueDateLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.DueDateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DueDateLabel.setObjectName("DueDateLabel")
        self.DateEdit = QtWidgets.QDateEdit(self.EditQuestionsPage)
        self.DateEdit.setGeometry(QtCore.QRect(540, 160, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DateEdit.setFont(font)
        self.DateEdit.setMinimumDate(datetime.date.today())
        self.DateEdit.setObjectName("DateEdit")
        self.stackedWidget.addWidget(self.EditQuestionsPage)
#-------------------------------------------------------------------------------------------Progress Page
        self.ProgressPage = QtWidgets.QWidget()
        self.ProgressPage.setObjectName("ProgressPage")
        self.ProgressTableWidget = QtWidgets.QTableWidget(self.ProgressPage)
        self.ProgressTableWidget.setGeometry(QtCore.QRect(89, 250, 1022, 500))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ProgressTableWidget.setFont(font)
        self.ProgressTableWidget.setStyleSheet("QTableWidget#ProgressTableWidget{background-color: rgb(24, 24, 24);color:rgb(255,255,255)}")
        self.ProgressTableWidget.setObjectName("ProgressTableWidget")
        self.ProgressTableWidget.setColumnCount(4)
        self.ProgressTableWidget.setRowCount(0)
        self.ProgressTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.ProgressTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.ProgressTableWidget.setHorizontalHeaderLabels(["First Name","Surname","Username","Avg Grade (%)"])
        self.ProgressTableWidget.setSortingEnabled(True)
        self.ProgressTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ProgressTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.ProgressTableWidget.horizontalHeader().setFixedHeight(50)
        self.ProgressTableWidget.horizontalHeader().setFont(font)
        self.ProgressLabel = QtWidgets.QLabel(self.ProgressPage)
        self.ProgressLabel.setGeometry(QtCore.QRect(300, 10, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.ProgressLabel.setFont(font)
        self.ProgressLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ProgressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressLabel.setObjectName("ProgressLabel")
        self.ReviewInfoLabel = QtWidgets.QLabel(self.ProgressPage)
        self.ReviewInfoLabel.setGeometry(QtCore.QRect(125, 100, 950, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.ReviewInfoLabel.setFont(font)
        self.ReviewInfoLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.ReviewInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ReviewInfoLabel.setObjectName("ReviewInfoLabel")
        self.homeButton_5 = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.gotoOptionsPage())
        self.homeButton_5.setGeometry(QtCore.QRect(0, 0, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.homeButton_5.setFont(font)
        self.homeButton_5.setStyleSheet("QPushButton#homeButton_5{background-color: rgb(24, 24, 24);border-radius:5px;}\n"
"QPushButton#homeButton_5:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#homeButton_5:pressed{background-color: rgb(170, 170, 170);}\n"
"QPushButton#homeButton_5{image: url(:/images/home button.png);}")
        self.homeButton_5.setObjectName("homeButton_5")
        self.DisplayButton = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.display_table())
        self.DisplayButton.setGeometry(QtCore.QRect(410, 160, 230, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.DisplayButton.setFont(font)
        self.DisplayButton.setStyleSheet("QPushButton#DisplayButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#DisplayButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#DisplayButton:pressed{background-color: rgb(170, 170, 170);}")
        self.DisplayButton.setObjectName("DisplayButton")
        self.DisplayButton.setText("Display")
        self.DisplayComboBox = QtWidgets.QComboBox(self.ProgressPage)
        self.DisplayComboBox.setGeometry(QtCore.QRect(90, 160, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DisplayComboBox.setFont(font)
        self.DisplayComboBox.setStyleSheet("QComboBox#DisplayComboBox{padding-left:10px}")
        self.DisplayComboBox.setObjectName("DisplayComboBox")
        self.DisplayComboBox.addItems(["Class List","Assignments"])
        self.ReviewButton = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.review_table())
        self.ReviewButton.setGeometry(QtCore.QRect(910, 160, 230, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.ReviewButton.setFont(font)
        self.ReviewButton.setStyleSheet("QPushButton#ReviewButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#ReviewButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#ReviewButton:pressed{background-color: rgb(170, 170, 170);}")
        self.ReviewButton.setObjectName("ReviewButton")
        self.EditButton = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.edit_assignment_table())
        self.EditButton.setGeometry(QtCore.QRect(660, 160, 230, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet("QPushButton#EditButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#EditButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#EditButton:pressed{background-color: rgb(170, 170, 170);}")
        self.EditButton.setObjectName("EditButton")
        self.stackedWidget.addWidget(self.ProgressPage)

        ClassWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClassWindow)
        
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username from tblTeacherUsers WHERE Logged_in = 1")
        items = cursor.fetchone()
        teacherUsername = items[0]
        cursor.execute(f"SELECT teacherUsername FROM tblClass WHERE teacherUsername='{teacherUsername}'")
        if not cursor.fetchone():
            self.stackedWidget.setCurrentIndex(0)
        else:
            cursor.execute(f"SELECT classCode FROM tblClass WHERE teacherUsername='{teacherUsername}'")
            items = cursor.fetchone()
            classCode = items[0]
            self.ClassCodeLabel_2.setText(classCode)
            self.display_table()
            self.stackedWidget.setCurrentIndex(1)
        connection.commit()
        connection.close()

        QtCore.QMetaObject.connectSlotsByName(ClassWindow)

    def gotoOptionsPage(self):
        self.stackedWidget.setCurrentIndex(1)
    def gotoAssignmentsPage(self):
        self.stackedWidget.setCurrentIndex(2)
    def gotoQuestionsPage(self):
        self.stackedWidget.setCurrentIndex(3)
    def gotoEditQuestionsPage(self):
        self.stackedWidget.setCurrentIndex(4)
    def gotoProgressPage(self):
        self.stackedWidget.setCurrentIndex(5)

    def save_class(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username from tblTeacherUsers WHERE Logged_in = 1")
        items = cursor.fetchone()
        teacherUsername = items[0]
        classCode = self.ClassCodeLabel.text()
        try:
            cursor.execute("SELECT classID FROM tblClass ORDER BY classID DESC LIMIT 0, 1")
            items = cursor.fetchone()
            classID = int(items[0]) + 1
        except TypeError:
            classID = 1
        sqlCommand = "INSERT INTO tblClass (ClassID,ClassCode,TeacherUsername) VALUES (?,?,?);"
        record = (classID, classCode, teacherUsername)
        cursor.execute(sqlCommand,record)
        connection.commit()
        connection.close()
        self.gotoOptionsPage()

    def add_question(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        Name = self.AssignmentLabel.text()
        Question = self.questionTextBrowser.toPlainText()
        Answer = self.answerLineEdit.text()
        if Question != "" and Answer != "":
            self.questionTextBrowser.setPlaceholderText("Enter the answer here")
            self.answerLineEdit.setPlaceholderText("Enter the question here")
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE Name='{Name}' AND ClassID='{self.ClassID()}'")
            item = cursor.fetchone()
            AssignmentID = item[0]
            statement = "INSERT INTO tblQuestions(AssignmentID,Question,Answer) VALUES (?,?,?);"
            record = (AssignmentID,Question,Answer)
            cursor.execute(statement,record)
            connection.commit()
            cursor.execute(f"SELECT MAX(QuestionID) FROM tblQuestions;")
            items = cursor.fetchone()
            QuestionID = items[0]
            connection.commit()
            connection.close()
            self.QuestionIDLabel.setText(f"{int(QuestionID) + 1})")
            self.questionTextBrowser.setPlainText("")
            self.answerLineEdit.setText("")
        else:
            self.questionTextBrowser.setPlaceholderText("INCOMPLETE FIELD!")
            self.answerLineEdit.setPlaceholderText("INCOMPLETE FIELD!")
        
    def store_ids(self, qn_list, current_index):
        current_id = qn_list[current_index]
        if current_index == 0:
            prev_id = current_id
        else:
            prev_id = qn_list[current_index - 1]
        if current_index == len(qn_list) - 1:
            next_id = current_id
        else:
            next_id = qn_list[current_index + 1]
        id_dict = {
            "prev_id": prev_id,
            "current_id": current_id,
            "next_id": next_id
        }
        return id_dict
    
    def qn_list(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        AssignmentName = self.AssignmentLabel_2.text()
        cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
        item = cursor.fetchone()
        AssignmentID = item[0]
        cursor.execute(f"SELECT QuestionID FROM tblQuestions WHERE AssignmentID='{AssignmentID}';")
        items = cursor.fetchall()
        QuestionIDs = []
        for i in items:
            QuestionID = i[0]
            QuestionIDs.append(QuestionID)
        connection.commit()
        connection.close()
        return QuestionIDs

    def next_qn(self):
        current_id = self.QuestionIDLabel_2.text()[:-1]
        current_index = self.qn_list().index(int(current_id))
        id_dict = self.store_ids(self.qn_list(), current_index)
        next_id = id_dict["next_id"]
        self.QuestionIDLabel_2.setText(f"{next_id})")
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{next_id}';")
        item = cursor.fetchone()
        Question = item[0]
        self.questionTextBrowser_2.setText(Question)
        cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{next_id}';")
        item = cursor.fetchone()
        Answer = item[0]
        self.answerLineEdit_2.setText(Answer)
        connection.commit()
        connection.close()

    def prev_qn(self):
        current_id = self.QuestionIDLabel_2.text()[:-1]
        current_index = self.qn_list().index(int(current_id))
        id_dict = self.store_ids(self.qn_list(), current_index)
        prev_id = id_dict["prev_id"]
        self.QuestionIDLabel_2.setText(f"{prev_id})")
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{prev_id}';")
        item = cursor.fetchone()
        Question = item[0]
        self.questionTextBrowser_2.setText(Question)
        cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{prev_id}';")
        item = cursor.fetchone()
        Answer = item[0]
        self.answerLineEdit_2.setText(Answer)
        connection.commit()
        connection.close()

    def save_qn(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        Question = self.questionTextBrowser_2.toPlainText()
        Answer = self.answerLineEdit_2.text()
        QuestionID = self.QuestionIDLabel_2.text()[:-1]
        if Question != "" and Answer != "":
            cursor.execute(f"UPDATE tblQuestions SET Question='{Question}', Answer='{Answer}' WHERE QuestionID={QuestionID};")
            connection.commit()
        else:
            self.questionTextBrowser_2.setPlaceholderText("INCOMPLETE FIELD!")
            self.answerLineEdit_2.setPlaceholderText("INCOMPLETE FIELD!")
        connection.commit()
        connection.close()

    def delete_qn(self):
        if len(self.qn_list()) >= 2:
            current_id = self.QuestionIDLabel_2.text()[:-1]
            current_index = self.qn_list().index(int(current_id))
            id_dict = self.store_ids(self.qn_list(), current_index)
            next_id = id_dict["next_id"]
            prev_id = id_dict["prev_id"]
            connection = sqlite3.connect("Users.db")
            cursor = connection.cursor()
            AssignmentName = self.AssignmentLabel_2.text()
            QuestionID = int(self.QuestionIDLabel_2.text()[:-1])
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
            item = cursor.fetchone()
            AssignmentID = item[0]
            cursor.execute(f"DELETE FROM tblQuestions WHERE AssignmentID='{AssignmentID}' AND QuestionID='{QuestionID}';")
            connection.commit()
            if prev_id == self.qn_list()[-1]:
                self.QuestionIDLabel_2.setText(f"{prev_id})")
                self.next_qn()
            else:
                self.QuestionIDLabel_2.setText(f"{next_id})")
                self.prev_qn()
        else:
            self.delete_assignment()
            self.gotoAssignmentsPage()

    def add_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        Name = self.AssignmentLineEdit.text()
        ClassID = self.ClassID()
        Date = self.calendarWidget.selectedDate().toString()
        if Name != "":
            statement = f"SELECT Name FROM tblAssignments WHERE Name='{Name}' AND ClassID='{ClassID}';"
            cursor.execute(statement)
            if not cursor.fetchone():
                statement = ("INSERT INTO tblAssignments (ClassID,Name,DueDate) VALUES (?,?,?);")
                record = (ClassID,Name,Date)
                cursor.execute(statement,record)
                connection.commit()
                self.assignment_table()
                self.AssignmentLabel.setText(Name)
                self.gotoQuestionsPage()
            else:
                self.NameErrorLabel.setFixedHeight(50)
                self.NameErrorLabel.setText("Name already exists")
        else:
            self.NameErrorLabel.setFixedHeight(50)
        connection.commit()
        connection.close()

    def finish_adding(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        Name = self.AssignmentLineEdit.text()
        cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE Name='{Name}';")
        items = cursor.fetchone()
        AssignmentID = items[0]
        statement = f"SELECT QuestionID FROM tblQuestions WHERE AssignmentID='{AssignmentID}';"
        cursor.execute(statement)
        if not cursor.fetchone():
            self.delete_assignment()
        connection.commit()
        connection.close()
        self.assignment_table()
        self.gotoAssignmentsPage()

    def finish_editing(self):
        self.save_qn()
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        Date = self.DateEdit.date().toString()
        AssignmentName = self.AssignmentLabel_2.text()
        cursor.execute(f"UPDATE tblAssignments SET DueDate='{Date}' WHERE Name='{AssignmentName}';")
        connection.commit()
        connection.close()
        self.assignment_table()
        self.gotoAssignmentsPage()

    def edit_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        try:
            current_row = self.AssignmentsTableWidget.currentRow()
            AssignmentName = self.AssignmentsTableWidget.item(current_row,1).text()
        except AttributeError:
            try:
                current_row = self.ProgressTableWidget.currentRow()
                AssignmentName = self.ProgressTableWidget.item(current_row,0).text()
            except AttributeError:
                AssignmentName = ""
        if AssignmentName != "":
            self.AssignmentLabel_2.setText(AssignmentName)
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
            item = cursor.fetchone()
            AssignmentID = item[0]
            cursor.execute(f"SELECT DueDate FROM tblAssignments WHERE AssignmentID='{AssignmentID}';")
            items = cursor.fetchone()
            DueDate = items[0]
            self.DateEdit.setDate(QtCore.QDate.fromString(DueDate))
            cursor.execute(f"SELECT QuestionID FROM tblQuestions WHERE AssignmentID='{AssignmentID}';")
            try:
                QuestionIDs = cursor.fetchall()[0]
                self.QuestionIDLabel_2.setText(f"{QuestionIDs[0]})")
                cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{QuestionIDs[0]}';")
                item = cursor.fetchone()
                Question = item[0]
                self.questionTextBrowser_2.setText(Question)
                cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{QuestionIDs[0]}';")
                item = cursor.fetchone()
                Answer = item[0]
                self.answerLineEdit_2.setText(Answer)
                self.gotoEditQuestionsPage()
            except IndexError:
                self.delete_assignment()
        connection.commit()
        connection.close()

    def delete_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        try:
            current_row = self.AssignmentsTableWidget.currentRow()
            Name = self.AssignmentsTableWidget.item(current_row,1).text()
        except AttributeError:
            Name = self.AssignmentLabel.text()
        try:
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{Name}';")
            item = cursor.fetchone()
            AssignmentID = item[0]
            cursor.execute(f"DELETE FROM tblStudentProgress WHERE AssignmentID='{AssignmentID}';")
            cursor.execute(f"DELETE FROM tblClassProgress WHERE AssignmentID='{AssignmentID}';")
            cursor.execute(f"DELETE FROM tblQuestions WHERE AssignmentID='{AssignmentID}';")
            cursor.execute(f"DELETE FROM tblAssignments WHERE Name='{Name}';")
            connection.commit()
            self.assignment_table()
            try:
                cursor.execute(f"SELECT MAX(AssignmentID) FROM tblAssignments;")
                item = cursor.fetchone()
                number = int(item[0])
                cursor.execute(f"UPDATE sqlite_sequence SET seq={number} WHERE name='tblAssignments';")
            except TypeError:
                cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='tblAssignments';")
            try:
                cursor.execute(f"SELECT MAX(ProgressID) FROM tblStudentProgress;")
                item = cursor.fetchone()
                number = int(item[0])
                cursor.execute(f"UPDATE sqlite_sequence SET seq={number} WHERE name='tblStudentProgress';")
            except TypeError:
                cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='tblStudentProgress';")
            try:
                cursor.execute(f"SELECT MAX(SubmissionID) FROM tblClassProgress;")
                item = cursor.fetchone()
                number = int(item[0])
                cursor.execute(f"UPDATE sqlite_sequence SET seq={number} WHERE name='tblClassProgress';")
            except TypeError:
                cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='tblClassProgress';")
            try:
                cursor.execute(f"SELECT MAX(QuestionID) FROM tblQuestions;")
                item = cursor.fetchone()
                number = int(item[0])
                cursor.execute(f"UPDATE sqlite_sequence SET seq={number} WHERE name='tblQuestions';")
            except TypeError:
                cursor.execute("UPDATE sqlite_sequence SET seq=0 WHERE name='tblQuestions';")
                self.QuestionIDLabel.setText("1)")
            connection.commit()
            connection.close()
        except TypeError:
            pass
        self.assignment_table()

    def ClassID(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username from tblTeacherUsers WHERE Logged_in = 1")
        teachers = cursor.fetchone()
        teacherUsername = teachers[0]
        cursor.execute(f"SELECT ClassID from tblClass WHERE TeacherUsername = '{teacherUsername}'")
        classes = cursor.fetchone()
        ClassID = classes[0]
        connection.commit()
        connection.close()
        return ClassID
    
    def assignment_table(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        self.AssignmentsTableWidget.clear()
        self.AssignmentsTableWidget.setHorizontalHeaderLabels(["Date Due","Assignment"])
        cursor.execute(f"SELECT DueDate,Name FROM tblAssignments WHERE ClassID ='{self.ClassID()}';")
        items = cursor.fetchall()
        self.AssignmentsTableWidget.setRowCount(len(items))
        tablerow=0
        for Names in items:
            duedate = datetime.datetime.strptime(str(Names[0]),"%a %b %d %Y")
            date_yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
            if duedate > (date_yesterday):
                self.AssignmentsTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(Names[0])))
                self.AssignmentsTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(Names[1])))
                tablerow +=1
        self.AssignmentsTableWidget.setRowCount(tablerow)
        connection.close()
        self.gotoAssignmentsPage()

    def review_table(self):
        self.ProgressTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.ProgressTableWidget.setColumnCount(4)
        try:
            column_3 = self.ProgressTableWidget.item(0,2).text()
            self.EditButton.setFixedHeight(0)
            if column_3 == "Ongoing" or column_3 == "Past":
                self.review_assignment()
            else:
                self.review_student()
        except:
            pass

    def review_student(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        try:
            current_row = self.ProgressTableWidget.currentRow()
            StudentUsername = self.ProgressTableWidget.item(current_row,2).text()
        except AttributeError:
            StudentUsername = ""
        self.ProgressTableWidget.clear()
        self.ProgressTableWidget.setHorizontalHeaderLabels(["Assignment","Date Submitted","Qns Correct","Grade (%)"])
        cursor.execute(f"SELECT AssignmentID,Date,Grade FROM tblClassProgress WHERE ClassID='{self.ClassID()}' AND StudentUsername='{StudentUsername}';")
        items = cursor.fetchall()
        self.ProgressTableWidget.setRowCount(len(items))
        tablerow = 0
        for row in items:
            list = []
            for item in row:
                list.append(item)
            cursor.execute(f"SELECT Name FROM tblAssignments WHERE AssignmentID='{row[0]}';")
            Names = cursor.fetchone()
            list[0] = Names[0]
            date = list[1]
            date = datetime.datetime.strptime(str(date),"%Y-%m-%d")
            full_date = date.strftime("%a %b %#d %Y")
            self.ProgressTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(list[0])))
            self.ProgressTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(full_date)))
            self.ProgressTableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(list[2])))
            cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE AssignmentID='{row[0]}' and StudentUsername='{StudentUsername}';")
            items = cursor.fetchall()
            correct = 0
            for item in items:
                if item[0] == 1:
                    correct += 1
            ratio = f"{correct}/{len(items)}"
            self.ProgressTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(ratio))
            tablerow +=1

    def review_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        try:
            current_row = self.ProgressTableWidget.currentRow()
            AssignmentName = self.ProgressTableWidget.item(current_row,0).text()
        except AttributeError:
            AssignmentName = ""
        self.ProgressTableWidget.clear()
        self.ProgressTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.ProgressTableWidget.setColumnCount(5)
        self.ProgressTableWidget.setHorizontalHeaderLabels(["First Name","Surname","Date Submitted","Qns Correct","Grade (%)"])
        cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE Name='{AssignmentName}';")
        item = cursor.fetchone()
        AssignmentID = item[0]
        cursor.execute(f"SELECT StudentUsername,Date,Grade FROM tblClassProgress WHERE ClassID='{self.ClassID()}' AND AssignmentID='{AssignmentID}';")
        items = cursor.fetchall()
        self.ProgressTableWidget.setRowCount(len(items))
        tablerow = 0
        for row in items:
            cursor.execute(f"SELECT firstName,surname FROM tblStudentUsers WHERE username='{row[0]}';")
            Names = cursor.fetchone()
            first_name = Names[0]
            surname = Names[1]
            date = row[1]
            date = datetime.datetime.strptime(str(date),"%Y-%m-%d")
            full_date = date.strftime("%a %b %#d %Y")
            self.ProgressTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(first_name)))
            self.ProgressTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(surname)))
            self.ProgressTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(full_date)))
            self.ProgressTableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[2])))
            cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE AssignmentID='{AssignmentID}' and StudentUsername='{row[0]}';")
            items = cursor.fetchall()
            correct = 0
            for item in items:
                if item[0] == 1:
                    correct += 1
            ratio = f"{correct}/{len(items)}"
            self.ProgressTableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(ratio))
            tablerow +=1

    def edit_assignment_table(self):
        try:
            current_row = self.ProgressTableWidget.currentRow()
            status = self.ProgressTableWidget.item(current_row,2).text()
            if status == "Ongoing":
                self.edit_assignment()
        except AttributeError:
            pass

    def display_table(self):
        self.ProgressTableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.ProgressTableWidget.setColumnCount(4)
        if self.DisplayComboBox.currentText() == "Class List":
            self.class_list_table()
            self.EditButton.setFixedHeight(0)
        elif self.DisplayComboBox.currentText() == "Assignments":
            self.assignments_table()
            self.EditButton.setFixedHeight(70)
        else:
            pass

    def class_list_table(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        self.ProgressTableWidget.clear()
        self.ProgressTableWidget.setHorizontalHeaderLabels(["First Name","Surname","Username","Avg Grade (%)"])
        cursor.execute(f"SELECT StudentUsername FROM tblClassList WHERE ClassID ='{self.ClassID()}';")
        items = cursor.fetchall()
        self.ProgressTableWidget.setRowCount(len(items))
        tablerow=0
        for username in items:
            cursor.execute(f"SELECT firstName,surname,username FROM tblStudentUsers WHERE username='{username[0]}';")
            student = cursor.fetchall()
            student = student[0]
            self.ProgressTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(student[0]))
            self.ProgressTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(student[1]))
            self.ProgressTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(student[2]))
            cursor.execute(f"SELECT Grade FROM tblClassProgress WHERE StudentUsername='{username[0]}';")
            items = cursor.fetchall()
            if items != []:
                total=0
                for grade in items:
                    total += int(grade[0])
                average_grade = int(total/len(items))
                self.ProgressTableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(average_grade)))
            tablerow +=1
        self.ProgressTableWidget.setRowCount(tablerow)
        connection.close()

    def assignments_table(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        self.ProgressTableWidget.clear()
        self.ProgressTableWidget.setHorizontalHeaderLabels(["Assignment","Due Date","Status","Class Avg Grade (%)"])
        cursor.execute(f"SELECT Name,DueDate,AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}';")
        items = cursor.fetchall()
        self.ProgressTableWidget.setRowCount(len(items))
        tablerow=0
        for assignment in items:
            self.ProgressTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(assignment[0]))
            self.ProgressTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(assignment[1]))
            duedate = datetime.datetime.strptime(str(assignment[1]),"%a %b %d %Y")
            date_yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
            if duedate < (date_yesterday):
                self.ProgressTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem("Past"))
            else:
                self.ProgressTableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem("Ongoing"))
            cursor.execute(f"SELECT Grade FROM tblClassProgress WHERE AssignmentID='{assignment[2]}';")
            items = cursor.fetchall()
            if items != []:
                total=0
                for grade in items:
                    total += int(grade[0])
                average_grade = int(total/len(items))
                self.ProgressTableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(average_grade)))

            tablerow +=1
        self.ProgressTableWidget.setRowCount(tablerow)
        connection.close()
    

    def retranslateUi(self, ClassWindow):
        _translate = QtCore.QCoreApplication.translate
        ClassWindow.setWindowTitle(_translate("ClassWindow", "MainWindow"))
        self.CreateClassButton.setText(_translate("ClassWindow", "Create Class"))
        self.createClassLabel.setText(_translate("ClassWindow", "Create a Class:"))
        self.optionsLabel.setText(_translate("ClassWindow", "Please show the student the Class Code below:"))
        self.WelcomeLabel.setText(_translate("ClassWindow", "Welcome to Your Class!"))
        self.AssignmentsButton.setText(_translate("ClassWindow", "Assignments"))
        self.progressButton.setText(_translate("ClassWindow", "Progress"))
        self.AssignmentsLabel.setText(_translate("ClassWindow", "Your Assignments:"))
        self.editAssignButton.setText(_translate("ClassWindow", "Edit Assignment"))
        self.createAssignButton.setText(_translate("ClassWindow", "Create Assignment"))
        self.assignmentsInfoLabel.setText(_translate("ClassWindow", "Either Edit or Create an Assignment to set for students"))
        self.OngoingAssignLabel.setText(_translate("ClassWindow", "Ongoing Assignments"))
        self.AssignmentLineEdit.setPlaceholderText(_translate("ClassWindow", "Enter the name of the assignment"))
        self.deleteAssignButton.setText(_translate("ClassWindow", "Delete Assignment"))
        self.NameErrorLabel.setText(_translate("ClassWindow", "Please enter a name"))
        self.questionsLabel.setText(_translate("ClassWindow", "Add Questions:"))
        self.AssignmentLabel.setText(_translate("ClassWindow", ""))
        self.questionTextBrowser.setHtml(_translate("ClassWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionTextBrowser.setPlaceholderText(_translate("ClassWindow", "Enter the question here"))
        self.FinishButton.setText(_translate("ClassWindow", "Finish"))
        self.AddQnButton.setText(_translate("ClassWindow", "Add Question"))
        self.NextQnButton.setText(_translate("ClassWindow", "Next Question"))
        self.QuestionIDLabel_2.setText(_translate("ClassWindow", "1)"))
        self.questionTextBrowser_2.setHtml(_translate("ClassWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.questionTextBrowser_2.setPlaceholderText(_translate("ClassWindow", "Enter the question here"))
        self.AssignmentLabel_2.setText(_translate("ClassWindow", "Assignment Name"))
        self.editQuestionsLabel.setText(_translate("ClassWindow", "Edit Questions:"))
        self.PrevQnButton.setText(_translate("ClassWindow", "Previous Question"))
        self.FinishButton2.setText(_translate("ClassWindow", "Finish"))
        self.SaveQnButton.setText(_translate("ClassWindow", "Save Question"))
        self.DeleteQnButton.setText(_translate("ClassWindow", "Delete Question"))
        self.DueDateLabel.setText(_translate("ClassWindow", "Due Date :"))
        self.ProgressLabel.setText(_translate("ClassWindow", "Class Progress:"))
        self.ReviewButton.setText(_translate("ClassWindow", "Review"))
        self.EditButton.setText(_translate("ClassWindow", "Edit"))
        self.ReviewInfoLabel.setText(_translate("ClassWindow", "To review a student you must select them and then click the 'Review' button"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassWindow = QtWidgets.QMainWindow()
    ui = Ui_ClassWindow()
    ui.setupUi(ClassWindow)
    ClassWindow.show()
    sys.exit(app.exec_())