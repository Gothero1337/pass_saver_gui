# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 396)
        Dialog.setMinimumSize(QSize(346, 396))
        Dialog.setMaximumSize(QSize(346, 396))
        icon = QIcon()
        icon.addFile(u"D:/Downloads/login.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: #191919;\n"
"font-family: Montserrat;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_wlcm = QLabel(Dialog)
        self.lbl_wlcm.setObjectName(u"lbl_wlcm")
        self.lbl_wlcm.setStyleSheet(u"color: #F5E8C7;\n"
"font-size: 26pt;\n"
"font-weight: 600;\n"
"margin: 10%;")
        self.lbl_wlcm.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_wlcm)

        self.lbl_login = QLabel(Dialog)
        self.lbl_login.setObjectName(u"lbl_login")
        self.lbl_login.setStyleSheet(u"color: #404258;\n"
"font-size: 18pt;\n"
"font-weight: 400;\n"
"margin-top: 20%;")
        self.lbl_login.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_login)

        self.le_login = QLineEdit(Dialog)
        self.le_login.setObjectName(u"le_login")
        self.le_login.setStyleSheet(u"color: #F5E8C7;\n"
"font-size: 12pt;\n"
"margin: 5%;\n"
"padding: 10%;\n"
"border: 1px solid #404258;\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.le_login)

        self.lbl_password = QLabel(Dialog)
        self.lbl_password.setObjectName(u"lbl_password")
        self.lbl_password.setStyleSheet(u"color: #404258;\n"
"font-size: 18pt;\n"
"font-weight: 400;\n"
"margin-top: 20%;\n"
"\n"
"")
        self.lbl_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_password)

        self.le_password = QLineEdit(Dialog)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setStyleSheet(u"color: #F5E8C7;\n"
"font-size: 12pt;\n"
"margin: 5%;\n"
"padding: 10%;\n"
"border: 1px solid #404258;\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.le_password)

        self.btn_signin = QPushButton(Dialog)
        self.btn_signin.setObjectName(u"btn_signin")
        self.btn_signin.setStyleSheet(u"QPushButton {\n"
"background-color: #404258;\n"
"color: #F5E8C7;\n"
"font-size: 18pt;\n"
"font-weight: 600;\n"
"margin: 10%;\n"
"padding: 15%;\n"
"border-radius: 28%;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #474E68;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #50577A;\n"
"}")

        self.verticalLayout.addWidget(self.btn_signin)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Credential Saver", None))
        self.lbl_wlcm.setText(QCoreApplication.translate("Dialog", u"Welcome!", None))
        self.lbl_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.le_login.setPlaceholderText(QCoreApplication.translate("Dialog", u" Enter login...", None))
        self.lbl_password.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.le_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter password...", None))
        self.btn_signin.setText(QCoreApplication.translate("Dialog", u"Sign in!", None))
    # retranslateUi

