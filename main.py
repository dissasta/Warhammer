import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy, QScrollArea
from PyQt5 import QtCore, QtGui, QtWidgets
from math import ceil
from lxml import etree

class Team():
    teams = []
    def __init__(self, name):
        self.name = name
        Team.teams.append(self)
        self.cards = []
        self.cards.append(Card())

class Card(QWidget):
    def __init__(self):
        super().__init__()
        intValidator = QtGui.QIntValidator(0, 999)
        self.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(100, 50, 50);")
        self.setMaximumSize(QtCore.QSize(500, 200))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(160, 10, 21, 16))
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(205, 10, 41, 16))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(271, 10, 51, 16))
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(341, 10, 51, 16))
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(415, 10, 41, 16))
        self.label_5.setStyleSheet("background-color: rgba(0,0,0,0%)");
        self.teamName = QtWidgets.QLineEdit(self)
        self.teamName.setGeometry(QtCore.QRect(0, 10, 141, 20))
        self.player1 = QtWidgets.QLineEdit(self)
        self.player1.setGeometry(QtCore.QRect(0, 40, 141, 20))
        self.player2 = QtWidgets.QLineEdit(self)
        self.player2.setGeometry(QtCore.QRect(0, 70, 141, 20))
        self.player3 = QtWidgets.QLineEdit(self)
        self.player3.setGeometry(QtCore.QRect(0, 100, 141, 20))
        self.player4 = QtWidgets.QLineEdit(self)
        self.player4.setGeometry(QtCore.QRect(0, 130, 141, 20))
        self.vp1 = QtWidgets.QLineEdit(self)
        self.vp1.setGeometry(QtCore.QRect(150, 40, 31, 20))
        self.vp2 = QtWidgets.QLineEdit(self)
        self.vp2.setGeometry(QtCore.QRect(150, 70, 31, 20))
        self.vp3 = QtWidgets.QLineEdit(self)
        self.vp3.setGeometry(QtCore.QRect(150, 100, 31, 20))
        self.vp4 = QtWidgets.QLineEdit(self)
        self.vp4.setGeometry(QtCore.QRect(150, 130, 31, 20))
        self.vp1.setValidator(intValidator)
        self.vp2.setValidator(intValidator)
        self.vp3.setValidator(intValidator)
        self.vp4.setValidator(intValidator)
        self.m1 = QtWidgets.QLineEdit(self)
        self.m1.setGeometry(QtCore.QRect(200, 40, 51, 20))
        self.m2 = QtWidgets.QLineEdit(self)
        self.m2.setGeometry(QtCore.QRect(200, 70, 51, 20))
        self.m3 = QtWidgets.QLineEdit(self)
        self.m3.setGeometry(QtCore.QRect(200, 100, 51, 20))
        self.m4 = QtWidgets.QLineEdit(self)
        self.m4.setGeometry(QtCore.QRect(200, 130, 51, 20))
        self.m1.setValidator(intValidator)
        self.m2.setValidator(intValidator)
        self.m3.setValidator(intValidator)
        self.m4.setValidator(intValidator)
        self.mvp1 = QtWidgets.QLineEdit(self)
        self.mvp1.setGeometry(QtCore.QRect(270, 40, 51, 20))
        self.mvp2 = QtWidgets.QLineEdit(self)
        self.mvp2.setGeometry(QtCore.QRect(270, 70, 51, 20))
        self.mvp3 = QtWidgets.QLineEdit(self)
        self.mvp3.setGeometry(QtCore.QRect(270, 100, 51, 20))
        self.mvp4 = QtWidgets.QLineEdit(self)
        self.mvp4.setGeometry(QtCore.QRect(270, 130, 51, 20))
        self.mvp1.setValidator(intValidator)
        self.mvp2.setValidator(intValidator)
        self.mvp3.setValidator(intValidator)
        self.mvp4.setValidator(intValidator)
        self.uc1 = QtWidgets.QLineEdit(self)
        self.uc1.setGeometry(QtCore.QRect(340, 40, 51, 20))
        self.uc2 = QtWidgets.QLineEdit(self)
        self.uc2.setGeometry(QtCore.QRect(340, 70, 51, 20))
        self.uc3 = QtWidgets.QLineEdit(self)
        self.uc3.setGeometry(QtCore.QRect(340, 100, 51, 20))
        self.uc4 = QtWidgets.QLineEdit(self)
        self.uc4.setGeometry(QtCore.QRect(340, 130, 51, 20))
        self.uc1.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.uc1.setEnabled(0)
        self.uc2.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.uc2.setEnabled(0)
        self.uc3.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.uc3.setEnabled(0)
        self.uc4.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.uc4.setEnabled(0)
        self.ca1 = QtWidgets.QLineEdit(self)
        self.ca1.setGeometry(QtCore.QRect(410, 40, 51, 20))
        self.ca2 = QtWidgets.QLineEdit(self)
        self.ca2.setGeometry(QtCore.QRect(410, 70, 51, 20))
        self.ca3 = QtWidgets.QLineEdit(self)
        self.ca3.setGeometry(QtCore.QRect(410, 100, 51, 20))
        self.ca4 = QtWidgets.QLineEdit(self)
        self.ca4.setGeometry(QtCore.QRect(410, 130, 51, 20))
        self.ca1.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.ca1.setEnabled(0)
        self.ca2.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.ca2.setEnabled(0)
        self.ca3.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.ca3.setEnabled(0)
        self.ca4.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(60, 50, 50);")
        self.ca4.setEnabled(0)
        self.res1 = QtWidgets.QLineEdit(self)
        self.res1.setEnabled(False)
        self.res1.setGeometry(QtCore.QRect(270, 170, 51, 20))
        self.res1.setReadOnly(False)
        self.res1.setStyleSheet("color: black;background-color: rgb(150,150,150)");
        self.res2 = QtWidgets.QLineEdit(self)
        self.res2.setEnabled(False)
        self.res2.setGeometry(QtCore.QRect(340, 170, 51, 20))
        self.res2.setStyleSheet("color: black;background-color: rgb(150,150,150)");
        self.res2.setReadOnly(False)
        self.res3 = QtWidgets.QLineEdit(self)
        self.res3.setEnabled(False)
        self.res3.setGeometry(QtCore.QRect(410, 170, 51, 20))
        self.res3.setStyleSheet("color: black;background-color: rgb(150,150,150)");
        self.res3.setReadOnly(False)
        self.label.setText("VP")
        self.label_2.setText("Missions")
        self.label_3.setText("Mission VP")
        self.label_4.setText("Uncapped")
        self.label_5.setText("Capped")

        self.vp1.textChanged.connect(self.recalcAll)
        self.vp2.textChanged.connect(self.recalcAll)
        self.vp3.textChanged.connect(self.recalcAll)
        self.vp4.textChanged.connect(self.recalcAll)
        self.m1.textChanged.connect(self.recalcAll)
        self.m2.textChanged.connect(self.recalcAll)
        self.m3.textChanged.connect(self.recalcAll)
        self.m4.textChanged.connect(self.recalcAll)
        self.mvp1.textChanged.connect(self.recalcAll)
        self.mvp2.textChanged.connect(self.recalcAll)
        self.mvp3.textChanged.connect(self.recalcAll)
        self.mvp4.textChanged.connect(self.recalcAll)

    def recalcAll(self):
        if self.vp1.text() and self.mvp1.text():
            uncapped = int(self.vp1.text()) + int(self.mvp1.text())
            self.uc1.setText(str(uncapped))
            if self.vp1.text() == str(0) and self.mvp1.text() == str(0):
                self.ca1.setText(str(0))
            else:
                self.ca1.setText(str(max(5, min(uncapped, 30))))
        else:
            self.uc1.clear()
            self.ca1.clear()
        if self.vp2.text() and self.mvp2.text():
            uncapped = int(self.vp2.text()) + int(self.mvp2.text())
            self.uc2.setText(str(uncapped))
            if self.vp2.text() == str(0) and self.mvp2.text() == str(0):
                self.ca2.setText(str(0))
            else:
                self.ca2.setText(str(max(5, min(uncapped, 30))))
        else:
            self.uc2.clear()
            self.ca2.clear()
        if self.vp3.text() and self.mvp3.text():
            uncapped = int(self.vp3.text()) + int(self.mvp3.text())
            self.uc3.setText(str(uncapped))
            if self.vp3.text() == str(0) and self.mvp3.text() == str(0):
                self.ca3.setText(str(0))
            else:
                self.ca3.setText(str(max(5, min(uncapped, 30))))
        else:
            self.uc3.clear()
            self.ca3.clear()
        if self.vp4.text() and self.mvp4.text():
            uncapped = int(self.vp4.text()) + int(self.mvp4.text())
            self.uc4.setText(str(uncapped))
            if self.vp4.text() == str(0) and self.mvp4.text() == str(0):
                self.ca4.setText(str(0))
            else:
                self.ca4.setText(str(max(5, min(uncapped, 30))))
        else:
            self.uc4.clear()
            self.ca4.clear()

        mvp = 0

        if self.mvp1.text():
            mvp += int(self.mvp1.text())
        if self.mvp2.text():
            mvp += int(self.mvp2.text())
        if self.mvp3.text():
            mvp += int(self.mvp3.text())
        if self.mvp4.text():
            mvp += int(self.mvp4.text())

        if mvp > 0:
            self.res1.setText(str(mvp))
        else:
            self.res1.clear()

        uc = 0

        if self.uc1.text():
            uc += int(self.uc1.text())
        if self.uc2.text():
            uc += int(self.uc2.text())
        if self.uc3.text():
            uc += int(self.uc3.text())
        if self.uc4.text():
            uc += int(self.uc4.text())

        if uc > 0:
            self.res2.setText(str(uc))
        else:
            self.res2.clear()

        ca = 0

        if self.ca1.text():
            ca += int(self.ca1.text())
        if self.ca2.text():
            ca += int(self.ca2.text())
        if self.ca3.text():
            ca += int(self.ca3.text())
        if self.ca4.text():
            ca += int(self.ca4.text())

        if ca > 0:
            self.res3.setText(str(ca))
        else:
            self.res3.clear()

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cards1 = []
        self.cards2 = []
        self.cards3 = []
        self.cards4 = []
        self.cards5 = []
        self.setStyleSheet("color: rgb(158, 158, 158);\nbackground-color: rgb(50, 50, 50);")
        self.setWindowTitle("Marc's Warhammer Ranker")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(985, 700)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 985, 682))
        self.tabWidget.setObjectName("tabWidget")
        self.round1 = QtWidgets.QWidget()
        self.round1.setEnabled(True)
        self.round1.setMinimumSize(QtCore.QSize(0, 0))
        self.round1.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.verticalLayoutWidget1 = QtWidgets.QWidget(self.round1)
        self.verticalLayoutWidget1.setGeometry(QtCore.QRect(0, 0, 985, 660))
        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget1)
        self.verticalLayout1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(self.spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget1)
        self.horizontalLayout1.addWidget(self.pushButton)
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        self.scrollArea1 = QScrollArea(self)
        self.scrollArea1.setWidgetResizable(True)
        self.scrollArea1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollWidget1 = QWidget()
        self.scrollWidget1.setFixedWidth(974)
        self.scrollArea1.setWidget(self.scrollWidget1)
        self.gridLayout1 = QtWidgets.QGridLayout(self.scrollWidget1)
        self.verticalLayout1.addWidget(self.scrollArea1)
        self.verticalLayout1.setStretch(1, 1)
        self.round2 = QtWidgets.QWidget()
        self.round2.setEnabled(True)
        self.round2.setMinimumSize(QtCore.QSize(0, 0))
        self.round2.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.verticalLayoutWidget2 = QtWidgets.QWidget(self.round2)
        self.verticalLayoutWidget2.setGeometry(QtCore.QRect(0, 0, 985, 660))
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(self.spacerItem)
        self.verticalLayout2.addLayout(self.horizontalLayout2)
        self.scrollArea2 = QScrollArea(self)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollWidget2 = QWidget()
        self.scrollWidget2.setFixedWidth(974)
        self.scrollArea2.setWidget(self.scrollWidget2)
        self.gridLayout2 = QtWidgets.QGridLayout(self.scrollWidget2)
        self.verticalLayout2.addWidget(self.scrollArea2)
        self.verticalLayout2.setStretch(1, 1)
        self.round3 = QtWidgets.QWidget()
        self.round3.setEnabled(True)
        self.round3.setMinimumSize(QtCore.QSize(0, 0))
        self.round3.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.verticalLayoutWidget3 = QtWidgets.QWidget(self.round3)
        self.verticalLayoutWidget3.setGeometry(QtCore.QRect(0, 0, 985, 660))
        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget3)
        self.verticalLayout3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(self.spacerItem)
        self.verticalLayout3.addLayout(self.horizontalLayout3)
        self.scrollArea3 = QScrollArea(self)
        self.scrollArea3.setWidgetResizable(True)
        self.scrollArea3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollWidget3 = QWidget()
        self.scrollWidget3.setFixedWidth(974)
        self.scrollArea3.setWidget(self.scrollWidget3)
        self.gridLayout3 = QtWidgets.QGridLayout(self.scrollWidget3)
        self.verticalLayout3.addWidget(self.scrollArea3)
        self.verticalLayout3.setStretch(1, 1)
        self.round4 = QtWidgets.QWidget()
        self.round4.setEnabled(True)
        self.round4.setMinimumSize(QtCore.QSize(0, 0))
        self.round4.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.verticalLayoutWidget4 = QtWidgets.QWidget(self.round4)
        self.verticalLayoutWidget4.setGeometry(QtCore.QRect(0, 0, 985, 660))
        self.verticalLayout4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget4)
        self.verticalLayout4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout4.addItem(self.spacerItem)
        self.verticalLayout4.addLayout(self.horizontalLayout4)
        self.scrollArea4 = QScrollArea(self)
        self.scrollArea4.setWidgetResizable(True)
        self.scrollArea4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollWidget4 = QWidget()
        self.scrollWidget4.setFixedWidth(974)
        self.scrollArea4.setWidget(self.scrollWidget4)
        self.gridLayout4 = QtWidgets.QGridLayout(self.scrollWidget4)
        self.verticalLayout4.addWidget(self.scrollArea4)
        self.verticalLayout4.setStretch(1, 1)
        self.round5 = QtWidgets.QWidget()
        self.round5.setEnabled(True)
        self.round5.setMinimumSize(QtCore.QSize(0, 0))
        self.round5.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.verticalLayoutWidget5 = QtWidgets.QWidget(self.round5)
        self.verticalLayoutWidget5.setGeometry(QtCore.QRect(0, 0, 985, 660))
        self.verticalLayout5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget5)
        self.verticalLayout5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout5.addItem(self.spacerItem)
        self.verticalLayout5.addLayout(self.horizontalLayout5)
        self.scrollArea5 = QScrollArea(self)
        self.scrollArea5.setWidgetResizable(True)
        self.scrollArea5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollWidget5 = QWidget()
        self.scrollWidget5.setFixedWidth(974)
        self.scrollArea5.setWidget(self.scrollWidget5)
        self.gridLayout5 = QtWidgets.QGridLayout(self.scrollWidget5)
        self.verticalLayout5.addWidget(self.scrollArea5)
        self.verticalLayout5.setStretch(1, 1)
        self.tabWidget.addTab(self.round1, "")
        self.tabWidget.addTab(self.round2, "")
        self.tabWidget.addTab(self.round3, "")
        self.tabWidget.addTab(self.round4, "")
        self.tabWidget.addTab(self.round5, "")
        self.results = QtWidgets.QTabWidget()
        self.tabWidget.addTab(self.results, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 18))
        self.setMenuBar(self.menubar)
        self.tabWidget.setCurrentIndex(0)
        self.tableWidget = QtWidgets.QTableWidget(self.results)
        self.tableWidget.setGeometry(QtCore.QRect(1, 1, 456, 656))
        self.tableWidget.setColumnCount(4)
        font = QtGui.QFont()
        font.setPointSize(8)
        item = QtWidgets.QTableWidgetItem()
        item.setText("TEAM")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("MISSION")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("UNCAPPED")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("CAPPED")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(1, 70)
        self.tableWidget.setColumnWidth(2, 70)
        self.tableWidget.setColumnWidth(3, 70)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setEnabled(False)
        for i in range(30):
            self.tableWidget.insertRow(i)
        self.tableWidget.resizeRowsToContents()
        self.loadXML()
        self.tabWidget.addTab(self.results, "")
        #self.tabWidget.currentChanged.connect(self.updateResults)
        self.show()
        self.pushButton.setText("Add Card")
        self.pushButton.clicked.connect(self.addNewTeam)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.round1), "Round 1")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.round2), "Round 2")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.round3), "Round 3")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.round4), "Round 4")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.round5), "Round 5")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results), "Results")

    def addNewTeam(self):
        teamCount = len(Team.teams)
        if teamCount < 30:
            team = Team('')
            self.cards1.append(team.cards[0])
            self.gridLayout1.addWidget(team.cards[0], int(teamCount/2), int(teamCount%2))
            self.scrollWidget1.setFixedHeight(200*ceil((teamCount+1)/2) + 10)

    def addNewTeamFromXML(self, name):
        team = Team(name)
        teamCount = len(Team.teams)-1
        self.cards1.append(team.cards[0])
        self.gridLayout1.addWidget(team.cards[0], int(teamCount/2), int(teamCount%2))
        self.scrollWidget1.setFixedHeight(200*ceil((teamCount+1)/2) + 10)
        return team.cards[0]

    def loadXML(self):
        dataFile = os.path.join(os.getcwd(), 'data.dat')
        if os.path.exists(dataFile):
            with open(dataFile, 'r') as file:
                tree = etree.parse(file)
                allCards = tree.xpath('//Cards/Round')
                for rnd in allCards:
                    team = rnd.getchildren()[0]
                    t = self.addNewTeamFromXML(team.text)
                    t.teamName.setText(team.text)
                    t.player1.setText(team.getchildren()[0].text)
                    t.player2.setText(team.getchildren()[1].text)
                    t.player3.setText(team.getchildren()[2].text)
                    t.player4.setText(team.getchildren()[3].text)
                    t.vp1.setText(team.getchildren()[0].getchildren()[0].text)
                    t.m1.setText(team.getchildren()[0].getchildren()[1].text)
                    t.mvp1.setText(team.getchildren()[0].getchildren()[2].text)
                    t.uc1.setText(team.getchildren()[0].getchildren()[3].text)
                    t.ca1.setText(team.getchildren()[0].getchildren()[4].text)
                    t.vp2.setText(team.getchildren()[1].getchildren()[0].text)
                    t.m2.setText(team.getchildren()[1].getchildren()[1].text)
                    t.mvp2.setText(team.getchildren()[1].getchildren()[2].text)
                    t.uc2.setText(team.getchildren()[1].getchildren()[3].text)
                    t.ca2.setText(team.getchildren()[1].getchildren()[4].text)
                    t.vp3.setText(team.getchildren()[2].getchildren()[0].text)
                    t.m3.setText(team.getchildren()[2].getchildren()[1].text)
                    t.mvp3.setText(team.getchildren()[2].getchildren()[2].text)
                    t.uc3.setText(team.getchildren()[2].getchildren()[3].text)
                    t.ca3.setText(team.getchildren()[2].getchildren()[4].text)
                    t.vp4.setText(team.getchildren()[3].getchildren()[0].text)
                    t.m4.setText(team.getchildren()[3].getchildren()[1].text)
                    t.mvp4.setText(team.getchildren()[3].getchildren()[2].text)
                    t.uc4.setText(team.getchildren()[3].getchildren()[3].text)
                    t.ca4.setText(team.getchildren()[3].getchildren()[4].text)
                    t.res1.setText(team.getchildren()[4].text)
                    t.res2.setText(team.getchildren()[5].text)
                    t.res3.setText(team.getchildren()[6].text)

    def writeXML(self):
        dataFile = os.path.join(os.getcwd(), 'data.dat')
        root = etree.Element('Cards')
        try:
            with open(dataFile, 'w') as file:
                for card in self.cards1:
                    roundCount = etree.Element('Round')
                    roundCount.text = str(1)

                    team = etree.SubElement(roundCount, 'TeamName')
                    team.text = card.teamName.text()

                    player1 = etree.SubElement(team, 'Player1')
                    player1.text = card.player1.text()

                    vp1 = etree.SubElement(player1, 'VP')
                    vp1.text = card.vp1.text()

                    m1 = etree.SubElement(player1, 'Mission')
                    m1.text = card.m1.text()

                    mvp1 = etree.SubElement(player1, 'MissionVP')
                    mvp1.text = card.mvp1.text()

                    unc1 = etree.SubElement(player1, 'Uncapped')
                    unc1.text = card.uc1.text()

                    cap1 = etree.SubElement(player1, 'Capped')
                    cap1.text = card.ca1.text()

                    player2 = etree.SubElement(team, 'Player2')
                    player2.text = card.player2.text()

                    vp2 = etree.SubElement(player2, 'VP')
                    vp2.text = card.vp2.text()

                    m2 = etree.SubElement(player2, 'Mission')
                    m2.text = card.m2.text()

                    mvp2 = etree.SubElement(player2, 'MissionVP')
                    mvp2.text = card.mvp2.text()

                    unc2 = etree.SubElement(player2, 'Uncapped')
                    unc2.text = card.uc2.text()

                    cap2 = etree.SubElement(player2, 'Capped')
                    cap2.text = card.ca2.text()

                    player3 = etree.SubElement(team, 'Player3')
                    player3.text = card.player3.text()

                    vp3 = etree.SubElement(player3, 'VP')
                    vp3.text = card.vp3.text()

                    m3 = etree.SubElement(player3, 'Mission')
                    m3.text = card.m3.text()

                    mvp3 = etree.SubElement(player3, 'MissionVP')
                    mvp3.text = card.mvp3.text()

                    unc3 = etree.SubElement(player3, 'Uncapped')
                    unc3.text = card.uc3.text()

                    cap3 = etree.SubElement(player3, 'Capped')
                    cap3.text = card.ca3.text()

                    player4 = etree.SubElement(team, 'Player4')
                    player4.text = card.player4.text()

                    vp4 = etree.SubElement(player4, 'VP')
                    vp4.text = card.vp4.text()

                    m4 = etree.SubElement(player4, 'Mission')
                    m4.text = card.m4.text()

                    mvp4 = etree.SubElement(player4, 'MissionVP')
                    mvp4.text = card.mvp4.text()

                    unc4 = etree.SubElement(player4, 'Uncapped')
                    unc4.text = card.uc4.text()

                    cap4 = etree.SubElement(player4, 'Capped')
                    cap4.text = card.ca4.text()

                    res1 = etree.SubElement(team, 'Res1')
                    res1.text = card.res1.text()

                    res2 = etree.SubElement(team, 'Res2')
                    res2.text = card.res2.text()

                    res3 = etree.SubElement(team, 'Res3')
                    res3.text = card.res3.text()

                    root.append(roundCount)

                s = etree.tostring(root, pretty_print=True)
                file.write(s.decode('ASCII'))
        except Exception:
            pass

    def sortResults(self):
        results = []
        for y in Card.teams:
            for x in y:
                if x:
                    if not x.res1.text():
                        res1 = 0
                    else:
                        res1 = x.res1.text()

                    if not x.res2.text():
                        res2 = 0
                    else:
                        res2 = x.res2.text()

                    if not x.res3.text():
                        res3 = 0
                    else:
                        res3 = x.res3.text()

                    results.append((x.teamName.text(), int(res1), int(res2), int(res3)))

        return results

    def updateResults(self):
        results = self.sortResults()
        sortedResults = sorted(results, key=lambda x: (-x[3], -x[2], -x[1], x[0]))
        for entry in range(len(sortedResults)):
            self.tableWidget.setItem(entry, 0, QtWidgets.QTableWidgetItem(sortedResults[entry][0]))
            if sortedResults[entry][1] != 0:
                self.tableWidget.setItem(entry, 1, QtWidgets.QTableWidgetItem(str(sortedResults[entry][1])))
            if sortedResults[entry][2] != 0:
                self.tableWidget.setItem(entry, 2, QtWidgets.QTableWidgetItem(str(sortedResults[entry][2])))
            if sortedResults[entry][3] != 0:
                self.tableWidget.setItem(entry, 3, QtWidgets.QTableWidgetItem(str(sortedResults[entry][3])))

    def closeEvent(self, e):
        self.writeXML()
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())