from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys,sqlite3,time,os

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Register")
        self.setWindowTitle("Add Student")
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        self.QBtn.clicked.connect(self.addstudent)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        self.branchinput = QComboBox()
        self.branchinput.addItem("Computer Science")
        self.branchinput.addItem("Information System")
        self.branchinput.addItem("Information Technology")
        self.branchinput.addItem("Software Engineering")
        self.yearinput = QComboBox()
        self.yearinput.addItem("1")
        self.yearinput.addItem("2")
        self.yearinput.addItem("3")
        self.yearinput.addItem("4")
        self.phoneinput = QLineEdit()
        self.phoneinput.setPlaceholderText("phone No.")
        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        self.Math_Label = QLabel()
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Math_Label.setFont(font)
        self.Math_Label.setObjectName("label")
        self.Math_Grade_input = QDoubleSpinBox()
        self.Math_Grade_input.setObjectName("Math_Grade_input")
        self.Math_Label.setText("Maths Grade: ")
        self.Programming_Label = QLabel()
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Programming_Label.setFont(font)
        self.Programming_Label.setObjectName("label_2")
        self.Programming_Label.setText("Programming Grade: ")
        self.Programming_Grade_input = QDoubleSpinBox()
        self.Programming_Grade_input.setObjectName("Programming_Grade_input")
        self.Information_System_Label = QLabel()
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Information_System_Label.setFont(font)
        self.Information_System_Label.setObjectName("label_3")
        self.Information_System_Grade_input = QDoubleSpinBox()
        self.Information_System_Label.setText("Information Systems Grade: ")
        self.Information_System_Grade_input.setObjectName("Information_System_Grade_input")
        self.Discrete_Maths_Label = QLabel()
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Discrete_Maths_Label.setFont(font)
        self.Discrete_Maths_Label.setObjectName("label_4")
        self.Discrete_Maths_Label.setText("Discrete Maths Grade: ")
        self.Discrete_Maths_Grade_input = QDoubleSpinBox()
        self.Discrete_Maths_Grade_input.setObjectName("Discrete_Maths_Grade_input")
        self.Total_Grade_Label = QLabel()
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Total_Grade_Label.setFont(font)
        self.Total_Grade_Label.setObjectName("label_5")
        self.Total_Grade_Label.setText("Total Grade: ")
        self.Total_Grade_input = QDoubleSpinBox()
        self.Total_Grade_input.setReadOnly(False)
        self.Total_Grade_input.setObjectName("Total_Grade_input")
        layout.addWidget(self.nameinput)
        layout.addWidget(self.branchinput)
        layout.addWidget(self.yearinput)
        layout.addWidget(self.phoneinput)
        layout.addWidget(self.addressinput)
        layout.addWidget(self.Math_Label)
        layout.addWidget(self.Math_Grade_input)
        layout.addWidget(self.Programming_Label)
        layout.addWidget(self.Programming_Grade_input)
        layout.addWidget(self.Information_System_Label)
        layout.addWidget(self.Information_System_Grade_input)
        layout.addWidget(self.Discrete_Maths_Label)
        layout.addWidget(self.Discrete_Maths_Grade_input)
        layout.addWidget(self.Total_Grade_Label)
        layout.addWidget(self.Total_Grade_input)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
    def addstudent(self):
        name = ""
        branch = ""
        year = -1
        phone = ""
        address = ""
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        year = self.yearinput.itemText(self.yearinput.currentIndex())
        phone = self.phoneinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO students (name,branch,year,phone,address) VALUES (?,?,?,?,?)",
                           (name, branch, year, phone, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add student to the database.')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Search")
        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()
        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("id No.")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):
        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute(
                "SELECT * from students WHERE id="+str(searchrol))
            row = result.fetchone()
            serachresult = "id : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Branch : "+str(
                row[2])+'\n'+"year : "+str(row[3])+'\n'+"Address : "+str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not Find student from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")
        self.setWindowTitle("Delete Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()
        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("id No.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):
        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE id="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not Delete student from the database.')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT ,Name TEXT,Branch TEXT,Year INTEGER,Phone INTEGER,Address TEXT,Maths_Grade REAL,Programming_Grade REAL, Information_Systems_Grade REAL,Discrete_Maths_Grade, Total_Grade REAL)")
        self.c.close()

        self.setWindowTitle("College Information System")
        self.setMinimumSize(800, 600)
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(
            ("Id", "Name", "Branch", "Year", "Phone", "Address","Maths Grade","Programming Grade","Information Systems Grade","Discrete Maths Grade","Total Grade"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Add Student", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Student")
        toolbar.addAction(btn_ac_adduser)
        btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)
        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)
        btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)
        adduser_action = QAction(
            QIcon("icon/add1.jpg"), "Insert Student", self)
        adduser_action.triggered.connect(self.insert)
        searchuser_action = QAction(
            QIcon("icon/s1.png"), "Search Student", self)
        searchuser_action.triggered.connect(self.search)
        deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM students"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()
        
    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())