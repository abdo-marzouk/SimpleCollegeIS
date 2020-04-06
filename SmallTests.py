# from peewee import *
# db = SqliteDatabase('PeeWeeCollegeIS.db')
# class StudentDetails(Model):
#     StudentName = CharField()
#     Gender = CharField()
#     Department = CharField()
#     Year = IntegerField()
#     Phone = IntegerField()
#     Address = CharField()
#     GPA = DoubleField()
#     class Meta:
#         database = db
# class StudentGrades(Model):
#     StudentName = ForeignKeyField(StudentDetails,backref='Grades',on_delete='CASCADE')
#     MathGrade = DoubleField()
#     DSGrade = DoubleField()
#     InformationSystemsGrade = DoubleField()
#     OOPGrade = DoubleField()
#     PMGrade = DoubleField()
#     BAGrade = DoubleField()
#     TWGrade = DoubleField()
#     GPA = DoubleField()
#     class Meta:
#         database = db
# for student in StudentDetails.select():
#     print(*student)
# for studentGrade in StudentGrades.select():
#     print(studentGrade.MathGrade)

x = 'Halapena Morgana'
print(f'Omae wa mou shindaurou, {x}')