import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
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
    
# region: Material

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
        
        if role == Qt.UserRole:
            return material
        
        return None

class MaterialAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_material_add()
        self.ui.setupUi(self) 
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.WindowCloseButtonHint)
    
    def getData(self):
        return {
            'name': self.ui.materialName.text().strip(),
            'unit': self.ui.materialUnits.currentText(),
            'cost': self.ui.materialCost.text().strip()
        }
    
    def validate(self):
        data = self.getData()

        if not data['name']:
            return False, "Введите название материала"
        
        if self.ui.materialUnits.currentIndex() == -1 or not data['unit']:
            return False, "Выберите единицы измерения"
        
        if not data['cost']:
            return False, "Введите цену материала"

        if not data['cost']:
            return False, "Введите стоимость материала"
        
        try:
            cost = int(data['cost'])
            if cost <= 0:
                return False, "Стоимость должна быть положительным числом"
            data['cost'] = cost
        except ValueError:
            return False, "Стоимость должна быть целым числом"
        
        return True, ""
    
    def setUnits(self, units_list):
        """Set available units in the combo box"""
        self.ui.materialUnits.clear()
        self.ui.materialUnits.addItems(units_list)

    def accept(self):
        is_valid, error_msg = self.validate()
        
        if not is_valid:
            QMessageBox.warning(self, "Ошибка", error_msg)
            return
        
        super().accept()

class MaterialChangeDialog(MaterialAddDialog):
    def __init__(self, parent=None, material=object):
        super().__init__(parent)
        self.material = material

    def setDefault(self):
        self.ui.materialName.setText(self.material['name'])
        self.ui.materialCost.setText(str(round(self.material['cost'])))

        index = self.ui.materialUnits.findText(self.material['unit_code'])
        if index >= 0:
            self.ui.materialUnits.setCurrentIndex(index)

# endregion 

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


    # region menu
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
    # endregion

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

    # region material

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
        dialog.setUnits(list(map(lambda u: u['code'], list(units))))
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.getData()
            cur = conn.cursor()
            try:
                cur.execute("""
                    SELECT
                        m.id
                    FROM units_of_measures m
                    WHERE m.code = %(code)s
                """, {"code": data['unit']})
                
                unitData = cur.fetchone()
                if unitData is None:
                    raise Exception(f"Unit of measure with code '{data['unit']}' not found")
                cur.execute("""
                    INSERT INTO materials (name, cost, unit_of_measure_id)
                    VALUES (%(name)s, %(cost)s, %(unit_id)s)
                """, {
                    "name": data['name'], 
                    "cost": data['cost'], 
                    "unit_id": unitData[0]
                })
                conn.commit()
                print("Material added successfully")
            except Exception as e:
                conn.rollback()
                print(f"Error occurred: {e}")
            finally:
                cur.close()
                self.materialLoad()

    def materialChange(self):
        if not self.ui.material_list.selectionModel(): 
            QMessageBox.warning(self, "Ошибка", "Выберете элемент")
            return
        
        selected = self.ui.material_list.selectionModel().selectedIndexes()
        
        if not selected: 
            QMessageBox.warning(self, "Ошибка", "Выберете элемент")
            return
        
        selected_index = selected[0]
        item = self.ui.material_list.model().data(selected_index, Qt.UserRole)

        dialog = MaterialChangeDialog(None, item)
        units = self.getUnitOfMeasure()
        dialog.setUnits(list(map(lambda u: u['code'], list(units))))
        dialog.setDefault()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.getData()
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT
                        m.id
                    FROM units_of_measures m
                    WHERE m.code = %(code)s
                """, {"code": data['unit']})
                unitData = cur.fetchone()
                if unitData is None:
                    raise Exception(f"Unit of measure with code '{data['unit']}' not found")
                cur.execute("""
                    update materials
                    set name = %(name)s, cost = %(cost)s, unit_of_measure_id = %(unit_id)s
                    where id = %(id)s
                    returning id
                """, {'id': item['id'], 'name': data['name'], 'unit_id': unitData['id'], 'cost': data['cost']})
                cur.fetchone()
                conn.commit()
            self.materialLoad()

    def materialDelete(self):
        if not self.ui.material_list.selectionModel():
            QMessageBox.warning(self, "Ошибка", "Выберете элемент")
            return

        selected = self.ui.material_list.selectionModel().selectedIndexes()
        
        if not selected:
            QMessageBox.warning(self, "Ошибка", "Выберете элемент")
            return
        
        selected_index = selected[0]
        item = self.ui.material_list.model().data(selected_index, Qt.UserRole)
        
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                DELETE FROM materials
                WHERE id = %s
                RETURNING *
            """, (item['id'],))
            
            cur.fetchone()
            conn.commit()
        
        self.materialLoad()

    # endregion

    # region unit_of_measure

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

    # endregion

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
