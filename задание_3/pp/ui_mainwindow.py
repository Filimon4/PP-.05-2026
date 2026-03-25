# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 581)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttons = QVBoxLayout()
        self.buttons.setSpacing(0)
        self.buttons.setObjectName(u"buttons")
        self.orders_but = QPushButton(self.centralwidget)
        self.orders_but.setObjectName(u"orders_but")
        self.orders_but.setCheckable(True)
        self.orders_but.setAutoExclusive(True)

        self.buttons.addWidget(self.orders_but)

        self.employees_but = QPushButton(self.centralwidget)
        self.employees_but.setObjectName(u"employees_but")
        self.employees_but.setCheckable(True)
        self.employees_but.setAutoExclusive(True)

        self.buttons.addWidget(self.employees_but)

        self.products_but = QPushButton(self.centralwidget)
        self.products_but.setObjectName(u"products_but")
        self.products_but.setCheckable(True)
        self.products_but.setAutoExclusive(True)

        self.buttons.addWidget(self.products_but)

        self.product_batches_but = QPushButton(self.centralwidget)
        self.product_batches_but.setObjectName(u"product_batches_but")
        self.product_batches_but.setCheckable(True)
        self.product_batches_but.setAutoExclusive(True)

        self.buttons.addWidget(self.product_batches_but)

        self.customers_but = QPushButton(self.centralwidget)
        self.customers_but.setObjectName(u"customers_but")
        self.customers_but.setCheckable(True)
        self.customers_but.setAutoExclusive(True)

        self.buttons.addWidget(self.customers_but)

        self.materials_but = QPushButton(self.centralwidget)
        self.materials_but.setObjectName(u"materials_but")
        self.materials_but.setCheckable(True)
        self.materials_but.setAutoExclusive(True)

        self.buttons.addWidget(self.materials_but)

        self.bill_of_material_but = QPushButton(self.centralwidget)
        self.bill_of_material_but.setObjectName(u"bill_of_material_but")
        self.bill_of_material_but.setCheckable(True)
        self.bill_of_material_but.setAutoExclusive(True)

        self.buttons.addWidget(self.bill_of_material_but)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.buttons.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.buttons.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.buttons)

        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.orders = QWidget()
        self.orders.setObjectName(u"orders")
        sizePolicy.setHeightForWidth(self.orders.sizePolicy().hasHeightForWidth())
        self.orders.setSizePolicy(sizePolicy)
        self.ordersList = QListView(self.orders)
        self.ordersList.setObjectName(u"ordersList")
        self.ordersList.setGeometry(QRect(60, 60, 731, 421))
        self.orders_get_all = QPushButton(self.orders)
        self.orders_get_all.setObjectName(u"orders_get_all")
        self.orders_get_all.setGeometry(QRect(710, 10, 80, 24))
        self.orders_add_new = QPushButton(self.orders)
        self.orders_add_new.setObjectName(u"orders_add_new")
        self.orders_add_new.setGeometry(QRect(620, 10, 80, 24))
        self.stackedWidget.addWidget(self.orders)
        self.product_batches = QWidget()
        self.product_batches.setObjectName(u"product_batches")
        self.label_4 = QLabel(self.product_batches)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 230, 141, 41))
        self.stackedWidget.addWidget(self.product_batches)
        self.customers = QWidget()
        self.customers.setObjectName(u"customers")
        self.label_6 = QLabel(self.customers)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 260, 121, 31))
        self.stackedWidget.addWidget(self.customers)
        self.materials = QWidget()
        self.materials.setObjectName(u"materials")
        self.widget = QWidget(self.materials)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 841, 511))
        self.materials_layout = QVBoxLayout(self.widget)
        self.materials_layout.setObjectName(u"materials_layout")
        self.materials_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.materials_layout.setContentsMargins(0, 0, 0, 0)
        self.material_buttons = QHBoxLayout()
        self.material_buttons.setObjectName(u"material_buttons")
        self.material_add = QPushButton(self.widget)
        self.material_add.setObjectName(u"material_add")

        self.material_buttons.addWidget(self.material_add)

        self.material_delete = QPushButton(self.widget)
        self.material_delete.setObjectName(u"material_delete")

        self.material_buttons.addWidget(self.material_delete)

        self.material_change = QPushButton(self.widget)
        self.material_change.setObjectName(u"material_change")

        self.material_buttons.addWidget(self.material_change)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.material_buttons.addItem(self.horizontal_spacer)

        self.material_load = QPushButton(self.widget)
        self.material_load.setObjectName(u"material_load")

        self.material_buttons.addWidget(self.material_load)


        self.materials_layout.addLayout(self.material_buttons)

        self.material_list = QListView(self.widget)
        self.material_list.setObjectName(u"material_list")

        self.materials_layout.addWidget(self.material_list)

        self.stackedWidget.addWidget(self.materials)
        self.bill_of_material = QWidget()
        self.bill_of_material.setObjectName(u"bill_of_material")
        self.label_7 = QLabel(self.bill_of_material)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 230, 151, 41))
        self.stackedWidget.addWidget(self.bill_of_material)
        self.employee = QWidget()
        self.employee.setObjectName(u"employee")
        self.label_2 = QLabel(self.employee)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 240, 111, 16))
        self.stackedWidget.addWidget(self.employee)
        self.products = QWidget()
        self.products.setObjectName(u"products")
        self.label_5 = QLabel(self.products)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 270, 81, 31))
        self.stackedWidget.addWidget(self.products)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.menu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.orders_but.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.employees_but.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.products_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.product_batches_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.customers_but.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0438", None))
        self.materials_but.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b", None))
        self.bill_of_material_but.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.orders_get_all.setText(QCoreApplication.translate("MainWindow", u"get all", None))
        self.orders_add_new.setText(QCoreApplication.translate("MainWindow", u"add new", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"product_batchers", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"customers", None))
        self.material_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.material_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.material_change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.material_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"bill_of_material", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"employee", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"products", None))
    # retranslateUi

