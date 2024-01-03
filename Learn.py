from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os

class Ui_LearnWindow(object):
    def setupUi(self, LearnWindow):
        LearnWindow.setObjectName("LearnWindow")
        LearnWindow.resize(1200, 800)
        LearnWindow.setStyleSheet("QMainWindow#LearnWindow{background-color: rgb(24, 24, 24);}")
        self.centralwidget = QtWidgets.QWidget(LearnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TopicsTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.TopicsTreeWidget.setGeometry(QtCore.QRect(100, 220, 650, 450))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TopicsTreeWidget.setFont(font)
        self.TopicsTreeWidget.setObjectName("TopicsTreeWidget")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TopicsTreeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.TopicsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.TopicsTreeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.LearnTopicsLabel = QtWidgets.QLabel(self.centralwidget)
        self.LearnTopicsLabel.setGeometry(QtCore.QRect(300, 70, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.LearnTopicsLabel.setFont(font)
        self.LearnTopicsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.LearnTopicsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LearnTopicsLabel.setObjectName("LearnTopicsLabel")
        self.OpenFileButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.file())
        self.OpenFileButton.setGeometry(QtCore.QRect(800, 220, 350, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.OpenFileButton.setFont(font)
        self.OpenFileButton.setStyleSheet("QPushButton#OpenFileButton{background-color: rgb(24, 24, 24);color: rgb(255, 255, 255);border-radius:10px;}\n"
"QPushButton#OpenFileButton:hover{background-color: rgb(61, 61, 61);}\n"
"QPushButton#OpenFileButton:pressed{background-color: rgb(170, 170, 170);}")
        self.OpenFileButton.setObjectName("OpenFileButton")
        LearnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LearnWindow)
        QtCore.QMetaObject.connectSlotsByName(LearnWindow)

    def open_file(self,file_path):
        folder_name = "Topics"
        pdf_file_name = f"{file_path}.pdf"
        pdf_file_path = os.path.join(folder_name, pdf_file_name)
        cmd = ['start', '', pdf_file_path]
        subprocess.run(cmd, shell=True)

    def file(self):
        current_item = self.TopicsTreeWidget.currentItem().text(0)
        if current_item != "Differentiation" and current_item != "Integration":
            seperated_item = current_item.partition(":")
            file_path = seperated_item[0]
            self.open_file(file_path)

    def retranslateUi(self, LearnWindow):
        _translate = QtCore.QCoreApplication.translate
        LearnWindow.setWindowTitle(_translate("LearnWindow", "LearnWindow"))
        self.TopicsTreeWidget.headerItem().setText(0, _translate("LearnWindow", "Topics"))
        self.TopicsTreeWidget.topLevelItem(0).setText(0, _translate("LearnWindow", "Differentiation"))
        self.TopicsTreeWidget.topLevelItem(0).child(0).setText(0, _translate("LearnWindow", "Differentiation 1: Introduction to differentiation"))
        self.TopicsTreeWidget.topLevelItem(0).child(1).setText(0, _translate("LearnWindow", "Differentiation 2: Maximum and minimum points"))
        self.TopicsTreeWidget.topLevelItem(0).child(2).setText(0, _translate("LearnWindow", "Differentiation 3: Extending the rule"))
        self.TopicsTreeWidget.topLevelItem(0).child(3).setText(0, _translate("LearnWindow", "Differentiation 4: More differentiation"))
        self.TopicsTreeWidget.topLevelItem(1).setText(0, _translate("LearnWindow", "Integration"))
        self.TopicsTreeWidget.topLevelItem(1).child(0).setText(0, _translate("LearnWindow", "Integration 1: Introduction to integration"))
        self.TopicsTreeWidget.topLevelItem(1).child(1).setText(0, _translate("LearnWindow", "Integration 2: Finding the area under a curve"))
        self.TopicsTreeWidget.topLevelItem(1).child(2).setText(0, _translate("LearnWindow", "Integration 3: Further integration"))
        self.LearnTopicsLabel.setText(_translate("LearnWindow", "Learn Topics"))
        self.OpenFileButton.setText(_translate("LearnWindow", "Open File"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LearnWindow = QtWidgets.QMainWindow()
    ui = Ui_LearnWindow()
    ui.setupUi(LearnWindow)
    LearnWindow.show()
    sys.exit(app.exec_())
