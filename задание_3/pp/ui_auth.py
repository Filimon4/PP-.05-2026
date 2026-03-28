# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_auth(object):
    def setupUi(self, auth):
        if not auth.objectName():
            auth.setObjectName(u"auth")
        auth.resize(865, 496)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(auth.sizePolicy().hasHeightForWidth())
        auth.setSizePolicy(sizePolicy)
        self.widget = QWidget(auth)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(300, 130, 251, 148))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777214, 25))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_2)

        self.login_input = QLineEdit(self.widget)
        self.login_input.setObjectName(u"login_input")

        self.verticalLayout.addWidget(self.login_input)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_2.addWidget(self.label_3)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout_2.addWidget(self.password_input)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_3.addWidget(self.login_button)


        self.retranslateUi(auth)

        QMetaObject.connectSlotsByName(auth)
    # setupUi

    def retranslateUi(self, auth):
        auth.setWindowTitle(QCoreApplication.translate("auth", u"Form", None))
        self.label.setText(QCoreApplication.translate("auth", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("auth", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("auth", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.login_button.setText(QCoreApplication.translate("auth", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

