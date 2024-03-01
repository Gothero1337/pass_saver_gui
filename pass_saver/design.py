# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import resrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 704)
        icon = QIcon()
        icon.addFile(u"D:/Downloads/login.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: #191919;\n"
"font-family: Montserrat;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: #2C3333;\n"
"margin: 10%;\n"
"border: 2px solid #404258;\n"
"border-bottom-right-radius: 20%;\n"
"border-bottom-left-radius: 20%;\n"
"}\n"
"QTableView::section {\n"
"background-color: #2C3333;\n"
"font-size: 26pt;\n"
"color: #F5E8C7;\n"
"font-weight: 600;\n"
"}\n"
"QTableView::item {\n"
"border: none;\n"
"background-color: #2C3333;\n"
"font-size: 18pt;\n"
"color: #F5E8C7;\n"
"font-weight: 400;\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"background-color: #404258;\n"
"color: #F5E8C7;\n"
"font-size: 18pt;\n"
"font-weight: 600;\n"
"margin: 20%;\n"
"padding: 15%;\n"
"border-radius: 28%;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #474E68;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #50577A;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"background-color: #404258;\n"
"color: #F5E8C7;\n"
"font-size: 18pt;\n"
"font-weight: 600;\n"
"margin: 20%;\n"
"padding: 15%;\n"
"border-radius: 28%;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #474E68;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #50577A;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon2)
        self.btn_edit.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setStyleSheet(u"QPushButton {\n"
"background-color: #404258;\n"
"color: #F5E8C7;\n"
"font-size: 18pt;\n"
"font-weight: 600;\n"
"margin: 20%;\n"
"padding: 15%;\n"
"border-radius: 28%;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #474E68;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #50577A;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del.setIcon(icon3)
        self.btn_del.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_del)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421redential Saver", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add credentials", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit credentials", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"Delete credentials", None))
    # retranslateUi

