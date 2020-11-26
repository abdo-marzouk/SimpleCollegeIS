import sys
from PyQt5 import QtCore, uic, QtWidgets
from MainWindow import *
from AddStudent import *
from Delete import *
from Password import *
from EditStudent import *
from SearchStudent import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
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
        self.StudentDetailsTable.setColumnWidth(0,35)
        self.StudentDetailsTable.setColumnWidth(2,65)
        self.StudentDetailsTable.setColumnWidth(4,35)
        self.StudentDetailsTable.setColumnWidth(5,90)
        self.StudentGradesTable.setColumnWidth(0,35)
        self.StudentGradesTable.setColumnWidth(2,70)
        self.StudentGradesTable.setColumnWidth(3,70)
        self.StudentGradesTable.setColumnWidth(4,70)
        self.StudentGradesTable.setColumnWidth(5,70)
        self.StudentGradesTable.setColumnWidth(6,70)
        self.StudentGradesTable.setColumnWidth(7,70)
        self.StudentGradesTable.setColumnWidth(8,70)
        def LoadData():
            self.StudentDetailsTable.setRowCount(0)
            self.StudentGradesTable.setRowCount(0)
            query1 = StudentDetails.select()
            for ID, Student in enumerate(query1):
                self.StudentDetailsTable.insertRow(ID)
                self.StudentDetailsTable.setItem(ID , 0 , QTableWidgetItem(str(Student.id)))
                self.StudentDetailsTable.setItem(ID , 1 , QTableWidgetItem(str(Student.StudentName)))
                self.StudentDetailsTable.setItem(ID , 2 , QTableWidgetItem(str(Student.Gender)))
                self.StudentDetailsTable.setItem(ID , 3 , QTableWidgetItem(str(Student.Department)))
                self.StudentDetailsTable.setItem(ID , 4 , QTableWidgetItem(str(Student.Year)))
                self.StudentDetailsTable.setItem(ID , 5 , QTableWidgetItem(str(Student.Phone)))
                self.StudentDetailsTable.setItem(ID , 6 , QTableWidgetItem(str(Student.Address)))
                self.StudentDetailsTable.setItem(ID , 7 , QTableWidgetItem(str(Student.GPA)))
            query2 = StudentGrades.select()
            for ID, Student in enumerate(query2):
                self.StudentGradesTable.insertRow(ID)
                self.StudentGradesTable.setItem(ID , 0 , QTableWidgetItem(str(Student.id)))
                self.StudentGradesTable.setItem(ID , 1 , QTableWidgetItem(str(Student.StudentName)))
                self.StudentGradesTable.setItem(ID , 2 , QTableWidgetItem(str(Student.MathGrade)))
                self.StudentGradesTable.setItem(ID , 3 , QTableWidgetItem(str(Student.DSGrade)))
                self.StudentGradesTable.setItem(ID , 4 , QTableWidgetItem(str(Student.InformationSystemsGrade)))
                self.StudentGradesTable.setItem(ID , 5 , QTableWidgetItem(str(Student.OOPGrade)))
                self.StudentGradesTable.setItem(ID , 6 , QTableWidgetItem(str(Student.PMGrade)))
                self.StudentGradesTable.setItem(ID , 7 , QTableWidgetItem(str(Student.BAGrade)))
                self.StudentGradesTable.setItem(ID , 8 , QTableWidgetItem(str(Student.TWGrade)))
                self.StudentGradesTable.setItem(ID , 9 , QTableWidgetItem(str(Student.GPA)))
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
        self.AddStudentTabSwitcher.setCurrentIndex(0)
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
                    QMessageBox(), 'Successful', 'Student is added successfully to the database. Please click the refresh button')
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
        def SearchStudentForEdit():
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
        self.SearchButtonForSearch.clicked.connect(SearchStudentForEdit)
        def SwitchTab1():
            self.SearchStudentTabSwitcher.setCurrentIndex(0)
        def SwitchTab2():
            self.SearchStudentTabSwitcher.setCurrentIndex(1)      
        self.NextButton.clicked.connect(SwitchTab2)
        self.BackButton.clicked.connect(SwitchTab1)
        self.ExitButton1.clicked.connect(self.close)
        self.ExitButton1.clicked.connect(self.ClearValues)
        self.ExitButton2.clicked.connect(self.close)
        self.ExitButton2.clicked.connect(self.ClearValues)

    def ClearValues(self):
        self.SearchInputForSearch.clear()
        self.SearchStudentTabSwitcher.setCurrentIndex(0)
        self.NameOutput.setText("")
        self.GenderOutput.setText("")
        self.DepartmentOutput.setText("")
        self.YearOutput.setText("")
        self.PhoneOutput.setText("")
        self.AddressOutput.setText("")
        self.TotalGradeOutput.setText("")
        self.MathGradeOutput.setText("")
        self.DSGradeOutput.setText("")
        self.ISGradeOutput.setText("")
        self.OOPGradeOutput.setText("")
        self.PMGradeOutput.setText("")
        self.BAGradeOutput.setText("")
        self.TWGradeOutput.setText("")  
class DeleteWindow(QtWidgets.QWidget, Ui_DeleteForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_DeleteForm.__init__(self)
        self.setupUi(self)
        def DeleteStudent():
            try:
                StudentDetailsToDelete=StudentDetails[int(self.DeleteInput.text())]
                StudentGradesToDelete=StudentGrades[int(self.DeleteInput.text())]
                StudentDetailsToDelete.delete_by_id(int(self.DeleteInput.text()))
                StudentGradesToDelete.delete_by_id(int(self.DeleteInput.text()))
                QMessageBox.information(
                    QMessageBox(), 'Successful', 'Student is successfuly deleted from the database. Please click the refresh button')
                self.DeleteInput.clear()
                self.close()
            except Exception:
                QMessageBox.warning(QMessageBox(), 'Error',
                                        'Could not find student.')
        self.DeleteButton.clicked.connect(DeleteStudent)

class EditStudentWindow(QtWidgets.QWidget, Ui_EditStudentForm):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_EditStudentForm.__init__(self)
        self.setupUi(self)
        def SearchStudentForEdit():
            try:
                SearchInputValueForEdit = self.SearchInputForEdit.text()
                SearchResultDetailsForEdit = StudentDetails.get(StudentDetails.id == SearchInputValueForEdit)
                SearchResultGradesForEdit = StudentGrades.get(StudentGrades.id == SearchInputValueForEdit)
                self.NameInput.setText(SearchResultDetailsForEdit.StudentName)
                self.GenderComboBox.setCurrentText(SearchResultDetailsForEdit.Gender)
                self.DepartmentComboBox.setCurrentText(SearchResultDetailsForEdit.Department)
                self.YearComboBox.setCurrentText(f'{SearchResultDetailsForEdit.Year}')
                self.PhoneInput.setText(f'{SearchResultDetailsForEdit.Phone}')
                self.AddressInput.setText(SearchResultDetailsForEdit.Address)
                self.MathInput.setValue(SearchResultGradesForEdit.MathGrade)
                self.DSInput.setValue(SearchResultGradesForEdit.DSGrade)
                self.ISInput.setValue(SearchResultGradesForEdit.InformationSystemsGrade)
                self.OOPInput.setValue(SearchResultGradesForEdit.OOPGrade)
                self.PMInput.setValue(SearchResultGradesForEdit.PMGrade)
                self.BAInput.setValue(SearchResultGradesForEdit.BAGrade)
                self.TWInput.setValue(SearchResultGradesForEdit.TWGrade)
            except Exception:
                QMessageBox.warning(QMessageBox(), 'Error',
                                    'Could not find student or wrong input.')
        def EditStudent():
            StudentNameEdit = self.NameInput.text()
            GenderEdit = self.GenderComboBox.itemText(self.GenderComboBox.currentIndex())
            DepartmentEdit = self.DepartmentComboBox.itemText(self.DepartmentComboBox.currentIndex())
            YearEdit = self.YearComboBox.itemText(self.YearComboBox.currentIndex())
            PhoneEdit = self.PhoneInput.text()
            AddressEdit = self.AddressInput.text()
            MathGradeEdit = self.MathInput.value()
            DSGradeEdit = self.DSInput.value()
            ISGradeEdit = self.ISInput.value()
            OOPGradeEdit = self.OOPInput.value()
            PMGradeEdit = self.PMInput.value()
            BAGradeEdit = self.BAInput.value()
            TWGradeEdit = self.TWInput.value()
            GPAEdit = ((MathGradeEdit+DSGradeEdit+ISGradeEdit+OOPGradeEdit+PMGradeEdit+BAGradeEdit+TWGradeEdit)/700)*100
            if StudentNameEdit == "" or StudentNameEdit.isdigit()==True or PhoneEdit.isalpha()==True or MathGradeEdit == 0 or DSGradeEdit == 0 or ISGradeEdit == 0 or OOPGradeEdit ==0 or PMGradeEdit == 0 or BAGradeEdit == 0 or TWGradeEdit ==0:
                QMessageBox.warning(QMessageBox(), 'Error',
                    'Invalid Inputs.')
            else:                 
                try:
                    student_Details=StudentDetails[int(self.SearchInputForEdit.text())]
                    student_Details.StudentName=StudentNameEdit
                    student_Details.Gender=GenderEdit
                    student_Details.Department=DepartmentEdit
                    student_Details.Year=YearEdit
                    student_Details.Phone=PhoneEdit
                    student_Details.Address=AddressEdit
                    student_Details.GPA=GPAEdit
                    student_Details.save()
                    student_Grades=StudentGrades[int(self.SearchInputForEdit.text())]
                    student_Grades.StudentName=StudentNameEdit
                    student_Grades.MathGrade=MathGradeEdit
                    student_Grades.DSGrade=DSGradeEdit
                    student_Grades.InformationSystemsGrade=ISGradeEdit
                    student_Grades.OOPGrade=OOPGradeEdit
                    student_Grades.PMGrade=PMGradeEdit
                    student_Grades.BAGrade=BAGradeEdit
                    student_Grades.TWGrade=TWGradeEdit
                    student_Grades.GPA=GPAEdit
                    student_Grades.save()
                    QMessageBox.information(
                        QMessageBox(), 'Successful', 'Student details have been updated. Please click the refresh button')
                    self.close()
                    self.ClearValues()
                except Exception:
                    QMessageBox.warning(QMessageBox(), 'Error',
                                        'Could not Edit student details.')
        self.AddStudentButton.clicked.connect(EditStudent)
        self.SearchButtonForEdit.clicked.connect(SearchStudentForEdit)
        def SwitchTab1():
            self.EditStudentTabSwitcher.setCurrentIndex(0)
        def SwitchTab2():
            self.EditStudentTabSwitcher.setCurrentIndex(1)        
        self.NextButton.clicked.connect(SwitchTab2)
        self.BackButton.clicked.connect(SwitchTab1)
        self.CancelButton2.clicked.connect(self.close)
        self.CancelButton.clicked.connect(self.close)
    def ClearValues(self):
        self.EditStudentTabSwitcher.setCurrentIndex(0)
        self.SearchInputForEdit.clear()
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