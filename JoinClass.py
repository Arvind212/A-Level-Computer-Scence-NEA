from PyQt5 import QtCore, QtGui, QtWidgets
import res
import sqlite3
import datetime

connection = sqlite3.connect("Users.db")
cursor = connection.cursor()
sqlCommand_ClassList = '''CREATE TABLE if NOT EXISTS tblClassList(
        StudentUsername TEXT,
        ClassID INTEGER,
        FOREIGN KEY (StudentUsername) REFERENCES tblStudentUsers(username),
        FOREIGN KEY (ClassID) REFERENCES tblClass(ClassID))'''
sqlCommand_ClassProgress = '''CREATE TABLE if NOT EXISTS tblStudentProgress(
        ProgressID INTEGER PRIMARY KEY AUTOINCREMENT,
        StudentUsername TEXT,
        AssignmentID INTEGER,
        QuestionID INTEGER,
        StudentAnswer TEXT,
        Correct INTEGER,
        FOREIGN KEY (StudentUsername) REFERENCES tblStudentUsers(username),
        FOREIGN KEY (AssignmentID) REFERENCES tblAssignments(AssignmentID),
        FOREIGN KEY (QuestionID) REFERENCES tblQuestions(QuestionID))'''
cursor.execute(sqlCommand_ClassList)
cursor.execute(sqlCommand_ClassProgress)
connection.commit()
connection.close()

class Ui_ClassWindow(object):
    def setupUi(self, ClassWindow):
        ClassWindow.setObjectName("ClassWindow")
        ClassWindow.resize(1200, 798)
        ClassWindow.setStyleSheet("QMainWindow#ClassWindow{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(ClassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget{background-color: rgb(24, 24, 24);}")
        self.stackedWidget.setObjectName("stackedWidget")
#-----------------------------------------------------------------------------------Join Class Page
        self.JoinClassPage = QtWidgets.QWidget()
        self.JoinClassPage.setObjectName("JoinClassPage")
        self.JoinClassButton = QtWidgets.QPushButton(self.JoinClassPage, clicked=lambda: self.save_class())
        self.JoinClassButton.setGeometry(QtCore.QRect(450, 500, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.JoinClassButton.setFont(font)
        self.JoinClassButton.setStyleSheet("QPushButton#JoinClassButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#JoinClassButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#JoinClassButton:pressed{background-color: rgb(170, 170, 170);}")
        self.JoinClassButton.setObjectName("JoinClassButton")
        self.joinClassLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.joinClassLabel.setGeometry(QtCore.QRect(300, 120, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.joinClassLabel.setFont(font)
        self.joinClassLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.joinClassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.joinClassLabel.setObjectName("joinClassLabel")
        self.optionsLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.optionsLabel.setGeometry(QtCore.QRect(350, 250, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.optionsLabel.setFont(font)
        self.optionsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.optionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.optionsLabel.setObjectName("optionsLabel")
        self.ClassCodeLineEdit = QtWidgets.QLineEdit(self.JoinClassPage)
        self.ClassCodeLineEdit.setGeometry(QtCore.QRect(375, 320, 450, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ClassCodeLineEdit.setFont(font)
        self.ClassCodeLineEdit.setStyleSheet("QLineEdit#ClassCodeLineEdit{border-radius:10px;padding-left:10px}")
        self.ClassCodeLineEdit.setObjectName("ClassCodeLineEdit")
        self.JoinClassErrorLabel = QtWidgets.QLabel(self.JoinClassPage)
        self.JoinClassErrorLabel.setGeometry(QtCore.QRect(430, 400, 350, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.JoinClassErrorLabel.setFont(font)
        self.JoinClassErrorLabel.setStyleSheet("QLabel#JoinClassErrorLabel{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.JoinClassErrorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.JoinClassErrorLabel.setObjectName("JoinClassErrorLabel")
        self.stackedWidget.addWidget(self.JoinClassPage)
#------------------------------------------------------------------------------------Class Page
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
        self.AssignmentsButton = QtWidgets.QPushButton(self.ClassPage, clicked= lambda: self.gotoAssignmentsPage())
        self.AssignmentsButton.setGeometry(QtCore.QRect(200, 400, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.AssignmentsButton.setFont(font)
        self.AssignmentsButton.setStyleSheet("QPushButton#AssignmentsButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#AssignmentsButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#AssignmentsButton:pressed{background-color: rgb(170, 170, 170);}")
        self.AssignmentsButton.setObjectName("AssignmentsButton")
        self.progressButton = QtWidgets.QPushButton(self.ClassPage, clicked= lambda: self.progress())
        self.progressButton.setGeometry(QtCore.QRect(700, 400, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.progressButton.setFont(font)
        self.progressButton.setStyleSheet("QPushButton#progressButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#progressButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#progressButton:pressed{background-color: rgb(170, 170, 170);}")
        self.progressButton.setObjectName("progressButton")
        self.LeaveClassButton = QtWidgets.QPushButton(self.ClassPage, clicked= lambda: self.leave_class())
        self.LeaveClassButton.setGeometry(QtCore.QRect(400, 600, 400, 75))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.LeaveClassButton.setFont(font)
        self.LeaveClassButton.setStyleSheet("QPushButton#LeaveClassButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#LeaveClassButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#LeaveClassButton:pressed{background-color: rgb(170, 170, 170);}")
        self.LeaveClassButton.setText("Leave Class")
        self.LeaveClassButton.setObjectName("LeaveClassButton")
        self.homeButton_2 = QtWidgets.QPushButton(self.ClassPage, clicked= lambda: self.gotoOptionsPage())
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
        self.stackedWidget.addWidget(self.ClassPage)
#---------------------------------------------------------------------------------Assignments Page
        self.AssignmentsPage = QtWidgets.QWidget()
        self.AssignmentsPage.setObjectName("AssignmentsPage")
        self.homeButton_3 = QtWidgets.QPushButton(self.AssignmentsPage, clicked= lambda: self.gotoOptionsPage())
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
        self.AssignmentsLabel = QtWidgets.QLabel(self.AssignmentsPage)
        self.AssignmentsLabel.setGeometry(QtCore.QRect(300, 40, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.AssignmentsLabel.setFont(font)
        self.AssignmentsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.AssignmentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentsLabel.setObjectName("AssignmentsLabel")
        self.SetAssignmentsLabel = QtWidgets.QLabel(self.AssignmentsPage)
        self.SetAssignmentsLabel.setGeometry(QtCore.QRect(70, 280, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.SetAssignmentsLabel.setFont(font)
        self.SetAssignmentsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.SetAssignmentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SetAssignmentsLabel.setObjectName("SetAssignmentsLabel")
        self.AssignmentErrorLabel = QtWidgets.QLabel(self.AssignmentsPage)
        self.AssignmentErrorLabel.setGeometry(QtCore.QRect(70, 230, 500, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AssignmentErrorLabel.setFont(font)
        self.AssignmentErrorLabel.setStyleSheet("QLabel#AssignmentErrorLabel{background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.AssignmentErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentErrorLabel.setObjectName("AssignmentErrorLabel")
      
        self.AssignmentButton = QtWidgets.QPushButton(self.AssignmentsPage, clicked=lambda: self.start_assignment())
        self.AssignmentButton.setGeometry(QtCore.QRect(120, 650, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.AssignmentButton.setFont(font)
        self.AssignmentButton.setStyleSheet("QPushButton#AssignmentButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#AssignmentButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#AssignmentButton:pressed{background-color: rgb(170, 170, 170);}")
        self.AssignmentButton.setObjectName("AssignmentButton")
        self.ReviewAssignButton = QtWidgets.QPushButton(self.AssignmentsPage, clicked=lambda: self.review_assignment())
        self.ReviewAssignButton.setGeometry(QtCore.QRect(680, 650, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ReviewAssignButton.setFont(font)
        self.ReviewAssignButton.setStyleSheet("QPushButton#ReviewAssignButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#ReviewAssignButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#ReviewAssignButton:pressed{background-color: rgb(170, 170, 170);}")
        self.ReviewAssignButton.setObjectName("ReviewAssignButton")
        
        self.CompletedErrorLabel = QtWidgets.QLabel(self.AssignmentsPage)
        self.CompletedErrorLabel.setGeometry(QtCore.QRect(630, 230, 500, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CompletedErrorLabel.setFont(font)
        self.CompletedErrorLabel.setStyleSheet("QLabel#CompletedErrorLabel{background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.CompletedErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CompletedErrorLabel.setObjectName("CompletedErrorLabel")
        self.CompletedAssignLabel = QtWidgets.QLabel(self.AssignmentsPage)
        self.CompletedAssignLabel.setGeometry(QtCore.QRect(630, 280, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.CompletedAssignLabel.setFont(font)
        self.CompletedAssignLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.CompletedAssignLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CompletedAssignLabel.setObjectName("CompletedAssignLabel")

        self.AssignmentsTableWidget = QtWidgets.QTableWidget(self.AssignmentsPage)
        self.AssignmentsTableWidget.setGeometry(QtCore.QRect(58, 340, 524, 260))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AssignmentsTableWidget.setFont(font)
        self.AssignmentsTableWidget.setStyleSheet("QTableWidget#tableWidget{background-color: rgb(24, 24, 24);}")
        self.AssignmentsTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.AssignmentsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.AssignmentsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
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

        self.AssignmentsListWidget = QtWidgets.QListWidget(self.AssignmentsPage)
        self.AssignmentsListWidget.setGeometry(QtCore.QRect(110, 340, 420, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AssignmentsListWidget.setFont(font)
        self.AssignmentsListWidget.setTabKeyNavigation(True)
        self.AssignmentsListWidget.setObjectName("AssignmentsListWidget")

        self.CompletedListWidget = QtWidgets.QListWidget(self.AssignmentsPage)
        self.CompletedListWidget.setGeometry(QtCore.QRect(670, 340, 420, 260))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CompletedListWidget.setFont(font)
        self.CompletedListWidget.setObjectName("CompletedListWidget")
        self.SortButton = QtWidgets.QPushButton(self.AssignmentsPage, clicked=lambda: self.sort_assignments())
        self.SortButton.setGeometry(QtCore.QRect(610, 160, 250, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SortButton.setFont(font)
        self.SortButton.setStyleSheet("QPushButton#SortButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SortButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SortButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SortButton.setObjectName("SortButton")
        self.SortButton.setText("Sort")
        self.SortComboBox = QtWidgets.QComboBox(self.AssignmentsPage)
        self.SortComboBox.setGeometry(QtCore.QRect(190, 160, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SortComboBox.setFont(font)
        self.SortComboBox.setStyleSheet("QComboBox#SortComboBox{padding-left:10px}")
        self.SortComboBox.setObjectName("SortComboBox")
        self.SortComboBox.addItem("Sort Alphabetically")
        self.SortComboBox.addItem("Sort by Due Date")
        self.stackedWidget.addWidget(self.AssignmentsPage)
#---------------------------------------------------------------------------------Questions Page
        self.QuestionsPage = QtWidgets.QWidget()
        self.QuestionsPage.setObjectName("QuestionsPage")
        self.QuestionLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.QuestionLabel.setGeometry(QtCore.QRect(320, 180, 561, 201))
        self.QuestionLabel.setText("")
        self.QuestionLabel.setObjectName("QuestionLabel")
        self.questionTextBrowser = QtWidgets.QTextBrowser(self.QuestionsPage)
        self.questionTextBrowser.setGeometry(QtCore.QRect(230, 210, 800, 221))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.questionTextBrowser.setFont(font)
        self.questionTextBrowser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.questionTextBrowser.setReadOnly(True)
        self.questionTextBrowser.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.questionTextBrowser.setObjectName("questionTextBrowser")
        self.QuestionIDLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.QuestionIDLabel.setGeometry(QtCore.QRect(100, 210, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.QuestionIDLabel.setFont(font)
        self.QuestionIDLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QuestionIDLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.QuestionIDLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.QuestionIDLabel.setObjectName("QuestionIDLabel")
        self.answerLineEdit = QtWidgets.QLineEdit(self.QuestionsPage)
        self.answerLineEdit.setGeometry(QtCore.QRect(230, 500, 800, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.answerLineEdit.setFont(font)
        self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        self.answerLineEdit.setPlaceholderText("Enter the answer here")
        self.answerLineEdit.setObjectName("answerLineEdit")
        self.homeButton = QtWidgets.QPushButton(self.QuestionsPage, clicked= lambda: self.gotoOptionsPage())
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
        self.AnswerErrorLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.AnswerErrorLabel.setGeometry(QtCore.QRect(230, 440, 801, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AnswerErrorLabel.setFont(font)
        self.AnswerErrorLabel.setStyleSheet("QLabel#AnswerErrorLabel{padding-left: 10px;background-color: rgb(247,221,220);color: rgb(113, 43, 41)}")
        self.AnswerErrorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.AnswerErrorLabel.setObjectName("AnswerErrorLabel")
        self.SubmitButton = QtWidgets.QPushButton(self.QuestionsPage, clicked =lambda: self.submit_answer())
        self.SubmitButton.setGeometry(QtCore.QRect(400, 650, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setStyleSheet("QPushButton#SubmitButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SubmitButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SubmitButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SubmitButton.setObjectName("SubmitButton")
        self.CompleteButton = QtWidgets.QPushButton(self.QuestionsPage, clicked =lambda: self.complete_assignment())
        self.CompleteButton.setGeometry(QtCore.QRect(850, 650, 300, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.CompleteButton.setFont(font)
        self.CompleteButton.setStyleSheet("QPushButton#CompleteButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#CompleteButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#CompleteButton:pressed{background-color: rgb(170, 170, 170);}")
        self.CompleteButton.setText("Complete")
        self.CompleteButton.setObjectName("CompleteButton")
        self.ReturnButton = QtWidgets.QPushButton(self.QuestionsPage, clicked =lambda: self.gotoAssignmentsPage())
        self.ReturnButton.setGeometry(QtCore.QRect(50, 650, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setStyleSheet("QPushButton#ReturnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#ReturnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#ReturnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.ReturnButton.setText("Return")
        self.ReturnButton.setObjectName("ReturnButton")
        self.QuestionsLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.QuestionsLabel.setGeometry(QtCore.QRect(300, 0, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.QuestionsLabel.setFont(font)
        self.QuestionsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.QuestionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QuestionsLabel.setObjectName("QuestionsLabel")
        self.NextQnButton = QtWidgets.QPushButton(self.QuestionsPage, clicked=lambda: self.next_qn())
        self.NextQnButton.setGeometry(QtCore.QRect(850, 90, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.NextQnButton.setFont(font)
        self.NextQnButton.setStyleSheet("QPushButton#NextQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#NextQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#NextQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.NextQnButton.setObjectName("NextQnButton")
        self.PrevQnButton = QtWidgets.QPushButton(self.QuestionsPage, clicked=lambda: self.prev_qn())
        self.PrevQnButton.setGeometry(QtCore.QRect(50, 90, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.PrevQnButton.setFont(font)
        self.PrevQnButton.setStyleSheet("QPushButton#PrevQnButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#PrevQnButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#PrevQnButton:pressed{background-color: rgb(170, 170, 170);}")
        self.PrevQnButton.setObjectName("PrevQnButton")
        self.AssignmentNameLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.AssignmentNameLabel.setGeometry(QtCore.QRect(350, 80, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.AssignmentNameLabel.setFont(font)
        self.AssignmentNameLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.AssignmentNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssignmentNameLabel.setObjectName("AssignmentNameLabel")
        self.progressBar = QtWidgets.QProgressBar(self.QuestionsPage)
        self.progressBar.setGeometry(QtCore.QRect(390, 150, 420, 30))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.StudentAnsLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.StudentAnsLabel.setGeometry(QtCore.QRect(40, 460, 540, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.StudentAnsLabel.setFont(font)
        self.StudentAnsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.StudentAnsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StudentAnsLabel.setObjectName("StudentAnsLabel")
        self.CorrectAnsLabel = QtWidgets.QLabel(self.QuestionsPage)
        self.CorrectAnsLabel.setGeometry(QtCore.QRect(620, 460, 540, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.CorrectAnsLabel.setFont(font)
        self.CorrectAnsLabel.setStyleSheet("color: rgb(170, 170, 170);")
        self.CorrectAnsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CorrectAnsLabel.setObjectName("CorrectAnsLabel")
        self.CorrectAnsLineEdit = QtWidgets.QLineEdit(self.QuestionsPage)
        self.CorrectAnsLineEdit.setGeometry(QtCore.QRect(620, 500, 540, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CorrectAnsLineEdit.setFont(font)
        self.CorrectAnsLineEdit.setStyleSheet("QLineEdit#CorrectAnsLineEdit{border-radius:10px;padding-left:10px}")
        self.CorrectAnsLineEdit.setReadOnly(True)
        self.CorrectAnsLineEdit.setObjectName("CorrectAnsLineEdit")
        self.stackedWidget.addWidget(self.QuestionsPage)
#---------------------------------------------------------------------------------Progress Page
        self.ProgressPage = QtWidgets.QWidget()
        self.ProgressPage.setObjectName("ProgressPage")
        self.tableWidget = QtWidgets.QTableWidget(self.ProgressPage)
        self.tableWidget.setGeometry(QtCore.QRect(89, 250, 1022, 500))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget#tableWidget{background-color: rgb(24, 24, 24);color:rgb(255,255,255)}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderLabels(["Assignment","Date Submitted","Grade","Qns Correct"])
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setFixedHeight(50)
        self.tableWidget.horizontalHeader().setFont(font)
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
        self.filterLineEdit = QtWidgets.QLineEdit(self.ProgressPage)
        self.filterLineEdit.setGeometry(QtCore.QRect(100, 160, 500, 70))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.filterLineEdit.setFont(font)
        self.filterLineEdit.setStyleSheet("QLineEdit#filterLineEdit{border-radius:10px;padding-left:10px}")
        self.filterLineEdit.setPlaceholderText("Filter assignments by name")
        self.filterLineEdit.setObjectName("filterLineEdit")
        self.SearchButton = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.progress_table())
        self.SearchButton.setGeometry(QtCore.QRect(620, 160, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("QPushButton#SearchButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#SearchButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#SearchButton:pressed{background-color: rgb(170, 170, 170);}")
        self.SearchButton.setObjectName("SearchButton")
        self.ReviewButton = QtWidgets.QPushButton(self.ProgressPage, clicked= lambda: self.review_row())
        self.ReviewButton.setGeometry(QtCore.QRect(890, 160, 250, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.ReviewButton.setFont(font)
        self.ReviewButton.setStyleSheet("QPushButton#ReviewButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#ReviewButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#ReviewButton:pressed{background-color: rgb(170, 170, 170);}")
        self.ReviewButton.setObjectName("ReviewButton")
        self.stackedWidget.addWidget(self.ProgressPage)

        ClassWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClassWindow)

        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT StudentUsername FROM tblClassList WHERE StudentUsername='{self.studentUsername()}'")
        if not cursor.fetchone():
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.display_assignments()
            self.WelcomeLabel.setText(self.teacher_name())
            self.stackedWidget.setCurrentIndex(1)
        connection.commit()
        connection.close()

        QtCore.QMetaObject.connectSlotsByName(ClassWindow)

    def teacher_name(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT teacherUsername FROM tblClass WHERE classID='{self.ClassID()}'")
        items = cursor.fetchone()
        teacherUsername = items[0]
        cursor.execute(f"SELECT title,surname from tblTeacherUsers WHERE Username='{teacherUsername}'")
        items = cursor.fetchone()
        title = items[0]
        surname = items[1]
        connection.commit()
        connection.close()
        return f"Welcome to {title} {surname}'s Class!"

    def gotoJoinClassPage(self):
        self.stackedWidget.setCurrentIndex(0)
    def gotoOptionsPage(self):
        self.stackedWidget.setCurrentIndex(1)
    def gotoAssignmentsPage(self):
        self.stackedWidget.setCurrentIndex(2)
    def gotoQuestionsPage(self):
        self.stackedWidget.setCurrentIndex(3)
    def gotoProgressPage(self):
        self.stackedWidget.setCurrentIndex(4)    

    def save_class(self):
        classCode = self.ClassCodeLineEdit.text()
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        # Finds the current student logged in
        statement = f"SELECT ClassID FROM tblClass WHERE ClassCode='{classCode}'"
        cursor.execute(statement)
        if not cursor.fetchone():
            self.JoinClassErrorLabel.setFixedHeight(50)
        else:
            # Finds the ClassID from the Class Code entered
            cursor.execute(statement)
            items = cursor.fetchone()
            classID = items[0]
            # Saves the student username and the ClassID to the db
            studentClassStatement = "INSERT INTO tblClassList (StudentUsername,ClassID) VALUES (?,?);"
            record = (self.studentUsername(),classID)
            cursor.execute(studentClassStatement,record)
            connection.commit()
            self.WelcomeLabel.setText(self.teacher_name())
            # Adds the Assignment Names into the list
            self.display_assignments()
            self.AssignmentErrorLabel.setFixedHeight(0)
            self.CompletedErrorLabel.setFixedHeight(0)
            self.gotoOptionsPage()

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
        AssignmentName = self.AssignmentNameLabel.text()
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
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        self.save_answer()
        current_id = self.QuestionIDLabel.text()[:-1]
        current_index = self.qn_list().index(int(current_id))
        id_dict = self.store_ids(self.qn_list(), current_index)
        next_id = id_dict["next_id"]
        self.QuestionIDLabel.setText(f"{next_id})")
        cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{next_id}';")
        item = cursor.fetchone()
        Question = item[0]
        self.questionTextBrowser.setText(Question)
        try:
            cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{next_id}' AND StudentUsername='{self.studentUsername()}';")
            item = cursor.fetchone()
            self.answerLineEdit.setText(item[0])
        except TypeError:
            self.answerLineEdit.setText("")
        try:
            cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE QuestionID='{next_id}' AND StudentUsername='{self.studentUsername()}';")
            item = cursor.fetchone()
            if item[0] == 1:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(144,238,144)}")
                self.CorrectAnsLineEdit.setText("")            
            elif item[0] == 0:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(247,221,220)}")
                if self.SubmitButton.text() == "Finish Review":
                    cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{next_id}'")
                    items = cursor.fetchone()
                    Answer = items[0]
                    self.CorrectAnsLineEdit.setText(Answer)
            else:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        except TypeError:
            self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        connection.commit()
        connection.close()
        self.progressBar.setValue(self.progress_value())
        if self.progress_value() == 100 and self.SubmitButton.text() != "Finish Review":
            self.CompleteButton.setFixedHeight(70)
        else:
            self.CompleteButton.setFixedHeight(0)

    def prev_qn(self):
        self.save_answer()
        current_id = self.QuestionIDLabel.text()[:-1]
        current_index = self.qn_list().index(int(current_id))
        id_dict = self.store_ids(self.qn_list(), current_index)
        prev_id = id_dict["prev_id"]
        self.QuestionIDLabel.setText(f"{prev_id})")
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{prev_id}';")
        item = cursor.fetchone()
        Question = item[0]
        self.questionTextBrowser.setText(Question)
        try:
            cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{prev_id}' AND StudentUsername='{self.studentUsername()}';")
            item = cursor.fetchone()
            self.answerLineEdit.setText(item[0])
        except TypeError:
            self.answerLineEdit.setText("")
        try:
            cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE QuestionID='{prev_id}' AND StudentUsername='{self.studentUsername()}';")
            item = cursor.fetchone()
            if item[0] == 1:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(144,238,144)}")
                self.CorrectAnsLineEdit.setText("")           
            elif item[0] == 0:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(247,221,220)}")
                if self.SubmitButton.text() == "Finish Review":
                    cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{prev_id}'")
                    items = cursor.fetchone()
                    Answer = items[0]
                    self.CorrectAnsLineEdit.setText(Answer)
            else:
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        except TypeError:
            self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        connection.commit()
        connection.close()
        self.progressBar.setValue(self.progress_value())
        if self.progress_value() == 100 and self.SubmitButton.text() != "Finish Review":
            self.CompleteButton.setFixedHeight(70)
        else:
            self.CompleteButton.setFixedHeight(0)

    def save_answer(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        AssignmentName = self.AssignmentNameLabel.text()
        cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
        item = cursor.fetchone()
        AssignmentID = item[0]
        QuestionID = self.QuestionIDLabel.text()[:-1]
        studentAnswer = self.answerLineEdit.text()
        cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE StudentUsername='{self.studentUsername()}' AND QuestionID='{QuestionID}';")
        data = cursor.fetchone()
        if data is None:
            statement = (f"INSERT INTO tblStudentProgress (StudentUsername,AssignmentID,QuestionID,StudentAnswer) VALUES (?,?,?,?)")
            record = (self.studentUsername(),AssignmentID,QuestionID,studentAnswer)
            cursor.execute(statement,record)
            connection.commit()
        else:
            cursor.execute(f"UPDATE tblStudentProgress SET StudentAnswer='{studentAnswer}' WHERE StudentUsername='{self.studentUsername()}' AND QuestionID='{QuestionID}';")
            connection.commit()
        connection.commit()
        connection.close()

    def submit_answer(self):
        if self.SubmitButton.text() == "Submit Answer":
            self.save_answer()
            connection = sqlite3.connect("Users.db")
            cursor = connection.cursor()
            QuestionID = self.QuestionIDLabel.text()[:-1]
            cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{QuestionID}'")
            items = cursor.fetchone()
            Answer = items[0]
            try:
                cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{QuestionID}' AND StudentUsername='{self.studentUsername()}';")
                item = cursor.fetchone()
                studentAnswer = item[0]
            except TypeError:
                studentAnswer = ""
            if studentAnswer == Answer:
                cursor.execute(f"UPDATE tblStudentProgress SET Correct=1 WHERE QuestionID='{QuestionID}' AND StudentUsername='{self.studentUsername()}';")
                connection.commit()
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(144,238,144)}")
                self.next_qn()
            else:
                cursor.execute(f"UPDATE tblStudentProgress SET Correct=0 WHERE QuestionID='{QuestionID}' AND StudentUsername='{self.studentUsername()}';")
                connection.commit()
                self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(247,221,220)}")
            connection.commit()
            connection.close()
        elif self.SubmitButton.text() == "Finish Review":
            self.gotoAssignmentsPage()

    def start_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        current_row = self.AssignmentsTableWidget.currentRow()
        AssignmentName = self.AssignmentsTableWidget.item(current_row,1).text()
        self.AnswerErrorLabel.setFixedHeight(0)
        self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
        if AssignmentName != "":
            self.AssignmentNameLabel.setText(AssignmentName)
            self.ReturnButton.setFixedHeight(70)
            self.QuestionLabel.setText("Your Questions")
            self.CompleteButton.setFixedHeight(70)
            self.SubmitButton.setText("Submit Answer")
            self.answerLineEdit.setPlaceholderText("Enter the answer here")
            self.answerLineEdit.setGeometry(230,500,800,100)
            self.answerLineEdit.setReadOnly(False)
            self.CorrectAnsLineEdit.setFixedHeight(0)
            self.StudentAnsLabel.setFixedHeight(0)
            self.CorrectAnsLabel.setFixedHeight(0)
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
            item = cursor.fetchone()
            AssignmentID = item[0]
            cursor.execute(f"SELECT QuestionID FROM tblQuestions WHERE AssignmentID='{AssignmentID}';")
            try:
                QuestionIDs = cursor.fetchall()[0]
                self.QuestionIDLabel.setText(f"{QuestionIDs[0]})")
                cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{QuestionIDs[0]}';")
                item = cursor.fetchone()
                Question = item[0]
                self.questionTextBrowser.setText(Question)
                try:
                    cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{QuestionIDs[0]}' AND StudentUsername='{self.studentUsername()}';")
                    item = cursor.fetchone()
                    self.answerLineEdit.setText(item[0])
                except TypeError:
                    self.answerLineEdit.setText("")
                try:
                    cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE QuestionID='{QuestionIDs[0]}' AND StudentUsername='{self.studentUsername()}';")
                    item = cursor.fetchone()
                    if item[0] == 1:
                        self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(144,238,144)}")
                    elif item[0] == 0:
                        self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(247,221,220)}")
                except TypeError:
                    self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(255, 255, 255)}")
                self.gotoQuestionsPage()
                self.progressBar.setValue(self.progress_value())
                if self.progress_value() == 100 and self.SubmitButton.text() != "Finish Review":
                    self.CompleteButton.setFixedHeight(70)
                    self.save_answer()
                else:
                    self.CompleteButton.setFixedHeight(0)
            except IndexError:
                pass
        else:
            self.AssignmentErrorLabel.setFixedHeight(75)
        connection.commit()
        connection.close()

    def complete_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        AssignmentName = self.AssignmentNameLabel.text()
        cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
        item = cursor.fetchone()
        AssignmentID = item[0]
        cursor.execute(f"SELECT QuestionID FROM tblStudentProgress WHERE StudentUsername='{self.studentUsername()}' AND AssignmentID='{AssignmentID}' AND Correct IS NULL;")
        items = cursor.fetchone()
        if items is not None:
            self.AnswerErrorLabel.setFixedHeight(50)
            QuestionID = items[0]
            self.QuestionIDLabel.setText(f"{QuestionID})")
            cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{QuestionID}';")
            item = cursor.fetchone()
            Question = item[0]
            self.questionTextBrowser.setText(Question)
            try:
                cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{QuestionID}' AND StudentUsername='{self.studentUsername()}';")
                item = cursor.fetchone()
                self.answerLineEdit.setText(item[0])
            except TypeError:
                self.answerLineEdit.setText("")
        else:
            self.AnswerErrorLabel.setFixedHeight(0)
            cursor.execute(f"SELECT COUNT(Correct) FROM tblStudentProgress WHERE StudentUsername='{self.studentUsername()}'AND AssignmentID='{AssignmentID}'AND Correct='1';")
            items = cursor.fetchone()
            Grade = int((items[0] / (len(self.qn_list()))) * 100)
            Date = datetime.date.today()
            statement = (f"INSERT INTO tblClassProgress (ClassID,AssignmentID,StudentUsername,Grade,Date) VALUES (?,?,?,?,?)")
            record = (self.ClassID(),AssignmentID,self.studentUsername(),Grade,Date)
            cursor.execute(statement,record)
            connection.commit()
            self.display_assignments()
            self.gotoAssignmentsPage()
        connection.commit()
        connection.close()

    def review_assignment(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        AssignmentName = self.CompletedListWidget.currentItem().text()
        if AssignmentName != "":
            self.AssignmentNameLabel.setText(AssignmentName)
            self.AnswerErrorLabel.setFixedHeight(0)
            self.ReturnButton.setFixedHeight(0)
            self.QuestionLabel.setText("Completed Questions")
            self.CompleteButton.setFixedHeight(0)
            self.SubmitButton.setText("Finish Review")
            self.answerLineEdit.setPlaceholderText("")
            self.answerLineEdit.setGeometry(40,500,540,100)
            self.answerLineEdit.setReadOnly(True)
            self.CorrectAnsLineEdit.setFixedHeight(100)
            self.StudentAnsLabel.setFixedHeight(50)
            self.CorrectAnsLabel.setFixedHeight(50)
            cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE ClassID='{self.ClassID()}' AND Name='{AssignmentName}';")
            item = cursor.fetchone()
            AssignmentID = item[0]
            cursor.execute(f"SELECT QuestionID FROM tblQuestions WHERE AssignmentID='{AssignmentID}';")
            try:
                QuestionIDs = cursor.fetchall()[0]
                self.QuestionIDLabel.setText(f"{QuestionIDs[0]})")
                cursor.execute(f"SELECT Question FROM tblQuestions WHERE QuestionID='{QuestionIDs[0]}';")
                item = cursor.fetchone()
                Question = item[0]
                self.questionTextBrowser.setText(Question)
                try:
                    cursor.execute(f"SELECT StudentAnswer FROM tblStudentProgress WHERE QuestionID='{QuestionIDs[0]}' AND StudentUsername='{self.studentUsername()}';")
                    item = cursor.fetchone()
                    self.answerLineEdit.setText(item[0])
                except TypeError:
                    self.answerLineEdit.setText("")
                cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE QuestionID='{QuestionIDs[0]}' AND StudentUsername='{self.studentUsername()}';")
                item = cursor.fetchone()
                if item[0] == 1:
                    self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(144,238,144)}")
                    self.CorrectAnsLineEdit.setText("")
                elif item[0] == 0:
                    self.answerLineEdit.setStyleSheet("QLineEdit#answerLineEdit{border-radius:10px;padding-left:10px;background-color: rgb(247,221,220)}")
                    cursor.execute(f"SELECT Answer FROM tblQuestions WHERE QuestionID='{QuestionIDs[0]}'")
                    items = cursor.fetchone()
                    Answer = items[0]
                    self.CorrectAnsLineEdit.setText(Answer)
                self.gotoQuestionsPage()
                self.progressBar.setValue(self.progress_value())
            except IndexError:
                pass
        else:
            self.CompletedErrorLabel.setFixedHeight(75)
        connection.commit()
        connection.close()

    def leave_class(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM tblClassList WHERE StudentUsername='{self.studentUsername()}';")
        connection.commit()
        connection.close()
        self.gotoJoinClassPage()

    def progress_value(self):
        total = int(len(self.qn_list()))
        current_id = self.QuestionIDLabel.text()[:-1]
        current_index = (self.qn_list().index(int(current_id))) + 1
        progress_value = int((current_index / total) * 100)
        return progress_value

    def studentUsername(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute("SELECT username from tblStudentUsers WHERE Logged_in = 1")
        items = cursor.fetchone()
        studentUsername = items[0]
        connection.commit()
        connection.close()
        return studentUsername

    def ClassID(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT ClassID from tblClassList WHERE StudentUsername = '{self.studentUsername()}'")
        classes = cursor.fetchone()
        ClassID = classes[0]
        connection.commit()
        connection.close()
        return ClassID
    
    def display_assignments(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        self.CompletedListWidget.clear()
        list = []
        tablerow = 0
        cursor.execute(f"SELECT AssignmentID FROM tblClassProgress WHERE ClassID='{self.ClassID()}' AND StudentUsername='{self.studentUsername()}';")
        items = cursor.fetchall()
        for AssignmentID in items:
            cursor.execute(f"SELECT Name FROM tblAssignments WHERE AssignmentID='{AssignmentID[0]}'")
            items = cursor.fetchone()
            for Name in items:
                self.CompletedListWidget.addItem(Name)
                list.append(Name)
        self.AssignmentsTableWidget.clear()
        self.AssignmentsTableWidget.setHorizontalHeaderLabels(["Date Due","Assignment"])
        cursor.execute(f"SELECT DueDate,Name FROM tblAssignments WHERE ClassID ='{self.ClassID()}';")
        items = cursor.fetchall()
        self.AssignmentsTableWidget.setRowCount(len(items))
        for Names in items:
            if Names[1] not in list:
                duedate = datetime.datetime.strptime(str(Names[0]),"%a %b %d %Y")
                date_yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
                if duedate > (date_yesterday):
                    self.AssignmentsTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(Names[0])))
                    self.AssignmentsTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(Names[1])))
                    tablerow +=1
        self.AssignmentsTableWidget.setRowCount(tablerow)
        connection.close()

    def progress_table(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        query = self.filterLineEdit.text()
        cursor.execute(f"SELECT AssignmentID,Date,Grade FROM tblClassProgress WHERE ClassID='{self.ClassID()}' AND StudentUsername='{self.studentUsername()}';")
        items = cursor.fetchall()
        self.tableWidget.setRowCount(len(items))
        tablerow = 0
        assignments=[]
        if query != "":
            self.tableWidget.clear()
            self.tableWidget.setHorizontalHeaderLabels(["Assignment","Date Submitted","Grade","Qns Correct"])
            for row in items:
                list = []
                for item in row:
                    list.append(item)
                cursor.execute(f"SELECT Name FROM tblAssignments WHERE AssignmentID='{row[0]}';")
                Names = cursor.fetchone()
                Name = str(Names[0])
                if query.lower() in Name.lower():
                    list[0] = Name
                    assignments.append(Name)
                    self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(list[0])))
                    self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(list[1])))
                    self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(list[2])))
                    cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE AssignmentID='{row[0]}' and StudentUsername='{self.studentUsername()}';")
                    items = cursor.fetchall()
                    correct = 0
                    for item in items:
                        if item[0] == 1:
                            correct += 1
                    ratio = f"{correct}/{len(items)}"
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(ratio))
                    tablerow +=1
            self.tableWidget.setRowCount(len(assignments))
        else:
            self.progress()
        connection.commit()
        connection.close()

    def progress(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT AssignmentID,Date,Grade FROM tblClassProgress WHERE ClassID='{self.ClassID()}' AND StudentUsername='{self.studentUsername()}';")
        items = cursor.fetchall()
        self.tableWidget.setRowCount(len(items))
        tablerow = 0
        for row in items:
            list = []
            for item in row:
                list.append(item)
            cursor.execute(f"SELECT Name FROM tblAssignments WHERE AssignmentID='{row[0]}';")
            Names = cursor.fetchone()
            list[0] = Names[0]
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(list[0])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(list[1])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(list[2])))
            cursor.execute(f"SELECT Correct FROM tblStudentProgress WHERE AssignmentID='{row[0]}' and StudentUsername='{self.studentUsername()}';")
            items = cursor.fetchall()
            correct = 0
            for item in items:
                if item[0] == 1:
                    correct += 1
            ratio = f"{correct}/{len(items)}"
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(ratio))
            tablerow +=1
        self.gotoProgressPage()

    def review_row(self):
        try:
            current_row = self.tableWidget.currentRow()
            selected_assignment = self.tableWidget.item(current_row,0).text()
            for x in range(self.CompletedListWidget.count()):
                if selected_assignment == self.CompletedListWidget.item(x).text():
                    item = self.CompletedListWidget.item(x)
            self.CompletedListWidget.setCurrentItem(item)
            self.review_assignment()
        except AttributeError:
            pass

    def merge_sort(self,array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]
            self.merge_sort(left_half)
            self.merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def merge_sort_dates(self,array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]
            self.merge_sort_dates(left_half)
            self.merge_sort_dates(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if datetime.datetime.strptime(left_half[i], "%Y-%m-%d") < datetime.datetime.strptime(right_half[j], "%Y-%m-%d"):
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def sort_assignments(self):
        connection = sqlite3.connect("Users.db")
        cursor = connection.cursor()
        if self.SortComboBox.currentText() == "Sort Alphabetically":
            assignments = []
            completed_assignments = []
            for x in range(self.AssignmentsTableWidget.rowCount()):
                assignments.append(self.AssignmentsTableWidget.item(x,1).text())
            for x in range(self.CompletedListWidget.count()):
                completed_assignments.append(self.CompletedListWidget.item(x).text())
            self.merge_sort(assignments)
            self.AssignmentsTableWidget.clear()
            self.AssignmentsTableWidget.setHorizontalHeaderLabels(["Date Due","Assignment"])
            cursor.execute(f"SELECT Name FROM tblAssignments WHERE ClassID='{self.ClassID()}'")
            items = cursor.fetchall()
            self.AssignmentsTableWidget.setRowCount(len(items))
            tablerow=0
            for item in assignments:
                cursor.execute(f"SELECT DueDate,Name FROM tblAssignments WHERE Name='{item}' and ClassID='{self.ClassID()}';")
                row = cursor.fetchall()            
                row = row[0]
                self.AssignmentsTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.AssignmentsTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                tablerow+=1
            self.AssignmentsTableWidget.setRowCount(tablerow)
            self.merge_sort(completed_assignments)
            self.CompletedListWidget.clear()
            for item in completed_assignments:
                self.CompletedListWidget.addItem(item)
        elif self.SortComboBox.currentText() == "Sort by Due Date":
            dates = []
            sorted_dates = []
            date_dict = {}
            AssignmentID_list = []
            for x in range(self.AssignmentsTableWidget.rowCount()):
                date = self.AssignmentsTableWidget.item(x,0).text()
                name = self.AssignmentsTableWidget.item(x,1).text()
                cursor.execute(f"SELECT AssignmentID FROM tblAssignments WHERE Name='{name}'and ClassID='{self.ClassID()}'")
                item = cursor.fetchone()
                AssignmentID = item[0]
                date_dict[AssignmentID] = date
                date = datetime.datetime.strptime(str(date),"%a %b %d %Y")
                dates.append(date.strftime("%Y-%m-%d"))
            self.merge_sort_dates(dates)
            for date in dates:
                full_date = datetime.datetime.strptime(str(date),"%Y-%m-%d")
                sorted_dates.append(full_date.strftime("%a %b %#d %Y"))
            self.AssignmentsTableWidget.clear()
            self.AssignmentsTableWidget.setHorizontalHeaderLabels(["Date Due","Assignment"])
            tablerow=0
            for date in sorted_dates:
                for x,y in date_dict.items():
                    if y == date and x not in AssignmentID_list:
                        AssignmentID_list.append(x)
            self.AssignmentsTableWidget.setRowCount(len(AssignmentID_list))
            for x in AssignmentID_list:
                cursor.execute(f"SELECT DueDate,Name FROM tblAssignments WHERE AssignmentID='{x}';")
                row = cursor.fetchall()
                row = row[0]
                self.AssignmentsTableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.AssignmentsTableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                tablerow+=1
        connection.close()

    def retranslateUi(self, ClassWindow):
        _translate = QtCore.QCoreApplication.translate
        ClassWindow.setWindowTitle(_translate("ClassWindow", "MainWindow"))
        self.JoinClassButton.setText(_translate("ClassWindow", "Join Class"))
        self.joinClassLabel.setText(_translate("ClassWindow", "Join a Class:"))
        self.optionsLabel.setText(_translate("ClassWindow", "Please enter the Class Code below:"))
        self.ClassCodeLineEdit.setPlaceholderText(_translate("ClassWindow", "Class Code"))
        self.JoinClassErrorLabel.setText(_translate("ClassWindow", "Please enter a Class Code"))
        self.WelcomeLabel.setText(_translate("ClassWindow", "Welcome to Mr Heer\'s Class!"))
        self.AssignmentsButton.setText(_translate("ClassWindow", "Assignments"))
        self.progressButton.setText(_translate("ClassWindow", "Progress"))
        self.AssignmentsLabel.setText(_translate("ClassWindow", "Your Assignments:"))
        self.SetAssignmentsLabel.setText(_translate("ClassWindow", "Set Assignments will show up here:"))
        self.AssignmentErrorLabel.setText(_translate("ClassWindow", "You currently have no set assignments"))
        self.AssignmentButton.setText(_translate("ClassWindow", "Start Assignment"))
        self.ReviewAssignButton.setText(_translate("ClassWindow", "Review Assignment"))
        self.CompletedErrorLabel.setText(_translate("ClassWindow", "You have not completed any assignments"))
        self.CompletedAssignLabel.setText(_translate("ClassWindow", "Completed Assignments will show up here:"))
        self.questionTextBrowser.setHtml(_translate("ClassWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Differentiate 6x^2 to the second derivative.</p></body></html>"))
        self.QuestionIDLabel.setText(_translate("ClassWindow", "1)"))
        self.AnswerErrorLabel.setText(_translate("ClassWindow", "You have an unfinished question. Please enter an answer in the box and click submit."))
        self.SubmitButton.setText(_translate("ClassWindow", "Submit Answer"))
        self.QuestionsLabel.setText(_translate("ClassWindow", "Your Questions:"))
        self.NextQnButton.setText(_translate("ClassWindow", "Next Question"))
        self.PrevQnButton.setText(_translate("ClassWindow", "Previous Question"))
        self.AssignmentNameLabel.setText(_translate("ClassWindow", "Assignment Name"))
        self.StudentAnsLabel.setText(_translate("ClassWindow", "Your Answer:"))
        self.CorrectAnsLabel.setText(_translate("ClassWindow", "Correct Answer:"))
        self.ProgressLabel.setText(_translate("ClassWindow", "Your Progress:"))
        self.SearchButton.setText(_translate("ClassWindow", "Search"))
        self.ReviewButton.setText(_translate("ClassWindow", "Review"))
        self.ReviewInfoLabel.setText(_translate("ClassWindow", "To review an assignment you must select it and then click the 'Review' button"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassWindow = QtWidgets.QMainWindow()
    ui = Ui_ClassWindow()
    ui.setupUi(ClassWindow)
    ClassWindow.show()
    sys.exit(app.exec_())