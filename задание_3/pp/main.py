import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.orders_but.setChecked(True)
        self.ui.bill_of_material_but.clicked.connect(self.billOfMeterialClicked)
        self.ui.customers_but.clicked.connect(self.customersClicked)
        self.ui.employees_but.clicked.connect(self.employeeButClicked)
        self.ui.materials_but.clicked.connect(self.materialButClicked)
        self.ui.orders_but.clicked.connect(self.ordersButClicked)
        self.ui.product_batches_but.clicked.connect(self.productBatchesButClicked)
        self.ui.products_but.clicked.connect(self.productsButClicked)

    def billOfMeterialClicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    
    def customersClicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def employeeButClicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def materialButClicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def ordersButClicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def productBatchesButClicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def productsButClicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
