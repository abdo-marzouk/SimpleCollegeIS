import sys
from PyQt5 import QtCore, uic, QtWidgets
from MainWindow import *
from AddStudent import *
from Delete import *
from Password import *
from EditStudent import *
from SearchStudent import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import sqlite3
from peewee import *
db = SqliteDatabase('PeeWeeCollegeIS.db', pragmas={
    'journal_mode' : 'wal',
    'ignore_check_constraints' : 0})
class StudentDetails(Model):
    StudentName = CharField(null=False)
    Gender = CharField(null=False)
    Department = CharField(null=False)
    Year = IntegerField(null=False)
    Phone = IntegerField(null=False)
    Address = CharField(null=False)
    GPA = DoubleField(null=False)
    class Meta:
        database = db
class StudentGrades(Model):
    StudentName = CharField(null=False)
    MathGrade = DoubleField(null=False)
    DSGrade = DoubleField(null=False)
    InformationSystemsGrade = DoubleField(null=False)
    OOPGrade = DoubleField(null=False)
    PMGrade = DoubleField(null=False)
    BAGrade = DoubleField(null=False)
    TWGrade = DoubleField(null=False)
    GPA = DoubleField()
    class Meta:
        database = db
db.create_tables([StudentDetails, StudentGrades])
class MainWindow(QtWidgets.QMainWindow, Ui_MainProgram):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainProgram.__init__(self)
        self.setupUi(self)
        def LoadData():
            self.connection = sqlite3.connect("PeeWeeCollegeIS.db")
            query = "SELECT * FROM StudentDetails"
            result = self.connection.execute(query)
            self.StudentDetailsTable.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.StudentDetailsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.StudentDetailsTable.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
            query2 = "SELECT * FROM StudentGrades"
            result2 = self.connection.execute(query2)
            self.StudentGradesTable.setRowCount(0)
            for row_number2, row_data2 in enumerate(result2):
                self.StudentGradesTable.insertRow(row_number2)
                for column_number2, data2 in enumerate(row_data2):
                    self.StudentGradesTable.setItem(
                        row_number2, column_number2, QTableWidgetItem(str(data2)))
            self.connection.close()
        LoadData()
        self.AddStudentAction.triggered.connect(Add.show)
        self.SearchStudentAction.triggered.connect(Search.show)
        self.DeleteStudentAction.triggered.connect(Delete.show)
        self.EditStudentAction.triggered.connect(Edit.show)
        self.LoadDataAction.triggered.connect(LoadData)
class AddWindow(QtWidgets.QWidget, Ui_AddStudentForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_AddStudentForm.__init__(self)
        self.setupUi(self)
        self.AddStudentButton.clicked.connect(self.AddStudent)
        self.NextButton.clicked.connect(self.SwitchTab2)
        self.BackButton.clicked.connect(self.SwitchTab1)
        self.CancelButton.clicked.connect(self.close)
        self.CancelButton2.clicked.connect(self.close)
    def SwitchTab1(self):
        self.AddStudentTabSwitcher.setCurrentIndex(0)
    def SwitchTab2(self):
        self.AddStudentTabSwitcher.setCurrentIndex(1)
    def ClearValues(self):
        self.NameInput.clear()
        self.GenderComboBox.setCurrentIndex(0)
        self.DepartmentComboBox.setCurrentIndex(0)
        self.YearComboBox.setCurrentIndex(0)
        self.PhoneInput.clear()
        self.AddressInput.clear()
        self.MathInput.setValue(0)
        self.DSInput.setValue(0)
        self.ISInput.setValue(0)
        self.OOPInput.setValue(0)
        self.PMInput.setValue(0)
        self.BAInput.setValue(0)
        self.TWInput.setValue(0)
    def AddStudent(self):
        StudentNameInput = self.NameInput.text()
        GenderInput = self.GenderComboBox.itemText(self.GenderComboBox.currentIndex())
        DepartmentInput = self.DepartmentComboBox.itemText(self.DepartmentComboBox.currentIndex())
        YearInput = self.YearComboBox.itemText(self.YearComboBox.currentIndex())
        PhoneInput = self.PhoneInput.text()
        AddressInput = self.AddressInput.text()
        MathGradeInput = self.MathInput.value()
        DSGradeInput = self.DSInput.value()
        ISGradeInput = self.ISInput.value()
        OOPGradeInput = self.OOPInput.value()
        PMGradeInput = self.PMInput.value()
        BAGradeInput = self.BAInput.value()
        TWGradeInput = self.TWInput.value()
        GPAInput = ((MathGradeInput+DSGradeInput+ISGradeInput+OOPGradeInput+PMGradeInput+BAGradeInput+TWGradeInput)/700)*100
        if StudentNameInput == "" or StudentNameInput.isdigit()==True or PhoneInput.isalpha()==True or MathGradeInput == 0 or DSGradeInput == 0 or ISGradeInput == 0 or OOPGradeInput ==0 or PMGradeInput == 0 or BAGradeInput == 0 or TWGradeInput ==0:
            QMessageBox.warning(QMessageBox(), 'Error',
                'Invalid Inputs.')
        else:                 
            try:
                NewStudentDetails = StudentDetails(
                    StudentName=StudentNameInput,
                    Gender=GenderInput,
                    Department=DepartmentInput,
                    Year=YearInput,
                    Phone=PhoneInput,
                    Address=AddressInput,
                    GPA=GPAInput)
                NewStudentDetails.save()
                NewStudentGrades = StudentGrades(
                    StudentName=StudentNameInput,
                    MathGrade=MathGradeInput,
                    DSGrade=DSGradeInput,
                    InformationSystemsGrade=ISGradeInput,
                    OOPGrade=OOPGradeInput,
                    PMGrade=PMGradeInput,
                    BAGrade=BAGradeInput,
                    TWGrade=TWGradeInput,
                    GPA=GPAInput)
                NewStudentGrades.save()
                QMessageBox.information(
                    QMessageBox(), 'Successful', 'Student is added successfully to the database.')
                self.close()
                self.ClearValues()
            except Exception:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    'Could not add student to the database.')
class SearchResultsWindow(QtWidgets.QWidget, Ui_SearchStudentResults):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_SearchStudentResults.__init__(self)
        self.setupUi(self)
        def SearchStudent():
            try:
                SearchInputValue = self.SearchInputForSearch.text()
                SearchResultDetails = StudentDetails.select().where(StudentDetails.id == SearchInputValue).get()
                SearchResultGrades = StudentGrades.select().where(StudentGrades.id == SearchInputValue).get()
                self.NameOutput.setText(SearchResultDetails.StudentName)
                self.GenderOutput.setText(SearchResultDetails.Gender)
                self.DepartmentOutput.setText(SearchResultDetails.Department)
                self.YearOutput.setText(f'{SearchResultDetails.Year}')
                self.PhoneOutput.setText(f'{SearchResultDetails.Phone}')
                self.AddressOutput.setText(SearchResultDetails.Address)
                self.TotalGradeOutput.setText(f'{SearchResultDetails.GPA}')
                self.MathGradeOutput.setText(f'{SearchResultGrades.MathGrade}')
                self.DSGradeOutput.setText(f'{SearchResultGrades.DSGrade}')
                self.ISGradeOutput.setText(f'{SearchResultGrades.InformationSystemsGrade}')
                self.OOPGradeOutput.setText(f'{SearchResultGrades.OOPGrade}')
                self.PMGradeOutput.setText(f'{SearchResultGrades.PMGrade}')
                self.BAGradeOutput.setText(f'{SearchResultGrades.BAGrade}')
                self.TWGradeOutput.setText(f'{SearchResultGrades.TWGrade}')
            except Exception:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    'Could not find student.')
        self.SearchButtonForSearch.clicked.connect(SearchStudent)
        def SwitchTab1():
            self.SearchStudentTabSwitcher.setCurrentIndex(0)
        def SwitchTab2():
            self.SearchStudentTabSwitcher.setCurrentIndex(1)        
        self.NextButton.clicked.connect(SwitchTab2)
        self.BackButton.clicked.connect(SwitchTab1)
        self.ExitButton1.clicked.connect(self.close)
        self.ExitButton2.clicked.connect(self.close)
class DeleteWindow(QtWidgets.QWidget, Ui_DeleteForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_DeleteForm.__init__(self)
        self.setupUi(self)
class EditStudentWindow(QtWidgets.QWidget, Ui_EditStudentForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_EditStudentForm.__init__(self)
        self.setupUi(self)
class LoginWindow(QtWidgets.QWidget, Ui_PasswordForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_PasswordForm.__init__(self)
        self.setupUi(self)
        self.EnterPasswordButton.clicked.connect(self.CheckPassword)
    def CheckPassword(self):
        Password = self.PasswordInputField.text()
        msg = QMessageBox()
        msg.setWindowTitle("Login")
        msg.setText("Wrong Password")
        if Password == "Admin":
            self.MainWindow = MainWindow()
            self.MainWindow.show()
            self.hide()
        else:
            msg.exec_()
            self.PasswordInputField.clear()
app = QtWidgets.QApplication(sys.argv)
Login = LoginWindow()
Search = SearchResultsWindow()
Edit = EditStudentWindow()
Add = AddWindow()
Delete = DeleteWindow()
if __name__ == "__main__":
    Login.show()
    sys.exit(app.exec_())