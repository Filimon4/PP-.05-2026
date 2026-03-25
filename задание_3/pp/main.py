import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from ui_mainwindow import Ui_MainWindow
from ui_material_add import Ui_material_add
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="postgres"
)

class OrdersListModel(QAbstractListModel):
    def __init__(self, orders=None):
        super().__init__()
        self.orders = orders or []

    def rowCount(self, parent=QModelIndex()):
        return len(self.orders)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.orders):
            return None

        product = self.orders[index.row()]

        if role == Qt.DisplayRole:
            return f"{product['id']} | {product['customername']} | Покупатель: {product['isbuyer']} | Оптовик: {product['issalesman']} | Телефон менеджера: {product['employeephone']} | Почта менеджера {product['employeeemail']}"

        return None
    
class MaterialsListModel(QAbstractListModel):
    def __init__(self, materials=[]):
        super().__init__()
        self.materials = materials

    def rowCount(self, parent=QModelIndex()):
        return len(self.materials)
    
    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.materials):
            return None
        
        material = self.materials[index.row()]

        if role == Qt.DisplayRole:
            return f"{material['id']} | {material['name']} | Цена: {material['cost']} | Ед. изм: {material['unit_code']}"
        
        return None
    

class MaterialAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_material_add()
        self.ui.setupUi(self) 
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowCloseButtonHint)
    
    def get_material_data(self):
        return {
            'name': self.ui.materialName.text(),
            'unit': self.ui.materialUnits.currentText()  # Or currentData() if you set data
        }
    
    def set_units(self, units_list):
        """Set available units in the combo box"""
        self.ui.materialUnits.clear()
        self.ui.materialUnits.addItems(units_list)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.orders_but.setChecked(True)
        self.ui.bill_of_material_but.clicked.connect(self.billOfMaterialClicked)

        # menu
        self.ui.customers_but.clicked.connect(self.customersClicked)
        self.ui.employees_but.clicked.connect(self.employeeButClicked)
        self.ui.materials_but.clicked.connect(self.materialButClicked)
        self.ui.orders_but.clicked.connect(self.ordersButClicked)
        self.ui.product_batches_but.clicked.connect(self.productBatchesButClicked)
        self.ui.products_but.clicked.connect(self.productsButClicked)

        # order
        self.ui.orders_add_new.clicked.connect(self.ordersAddNew)
        self.ui.orders_get_all.clicked.connect(self.ordersLoad)

        # material
        self.ui.material_load.clicked.connect(self.materialLoad)
        self.ui.material_add.clicked.connect(self.materialAdd)
        self.ui.material_change.clicked.connect(self.materialChange)
        self.ui.material_delete.clicked.connect(self.materialDelete)


    # menu clicked

    def billOfMaterialClicked(self):
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

    # orders

    def ordersLoad(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                select
                    o."date",
                    o.id,
                    os.code as statuesCode,
                    c."name" as customerName,
                    c.buyer as isBuyer,
                    c.salesman as isSalesman,
                    c.email as customerEmail,
                    e.email as employeeEmail,
                    e.phone as employeePhone
                from orders o
                left join order_statuses os on os.id = o.status_id
                left join customers c on o.customer_id = c.id
                left join employees e on o.manager_id = e.id
            """)
            orders = cur.fetchall() 

        model = OrdersListModel(orders)
        self.ui.ordersList.setModel(model)

    def ordersAddNew(self):
        pass

    # material

    def materialLoad(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                select
                    m.id,
                    m."cost",
                    m."name",
                    uom.code as unit_code
                from materials m
                left join units_of_measures uom on m.unit_of_measure_id = uom.id
            """)
            materials = cur.fetchall()

        model = MaterialsListModel(materials)
        self.ui.material_list.setModel(model)

    def materialAdd(self):
        dialog = MaterialAddDialog()
        units = self.getUnitOfMeasure()
        dialog.set_units(list(map(lambda u: u['code'], list(units))))
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # Dialog was accepted (OK button clicked)
            data = dialog.get_material_data()
            print(f"Added material: {data['name']} ({data['unit']})")
        

    def materialChange(self):
        selected = self.ui.material_list.selectionModel().selectedIndexes()
        
        if not selected: return

    def materialDelete(self):
        selected = self.ui.material_list.selectionModel().selectedIndexes()
        
        if not selected: return

    # unit_of_measure

    def getUnitOfMeasure(self):
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                select
                    uom.id,
                    uom.code
                from units_of_measures uom 
            """)
            unitsOfMeasure = cur.fetchall()

        return unitsOfMeasure

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
