class Student:
    def __init__(self, stu_id, stu_name):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.subjects_list = []
        
    def enroll_subject(self, subject):
        self.subjects_list.append(subject)

class Subject:
    def __init__(self, sub_id, sub_name, section, credit, teacher):
        self.sub_id = sub_id
        self.sub_name = sub_name
        self.section = section
        self.credit = credit
        self.teacher = teacher
        self.students_list = []
        
    def enroll_student(self, student):
        self.students_list.append(student)

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.subjects_taught_list = []

stu1 = Student('001', 'John')
stu2 = Student('002', 'Peter')
stu3 = Student('003', 'Katy[SP]')
stu4 = Student('004', 'Linda')
stu5 = Student('005', 'Alice')

tch1 = Teacher('101', 'Wilson')
tch2 = Teacher('102', 'Cherry')

oop_sec1 = Subject('011', 'OOP 1', 'Section 1', 3, tch1)
oop_sec2 = Subject('012', 'OOP 2', 'Section 2', 3, tch2)

tch1.subjects_taught_list.append(oop_sec1)
tch2.subjects_taught_list.append(oop_sec2)

# Enroll students in subjects
oop_sec1.enroll_student(stu1)
oop_sec1.enroll_student(stu2)
oop_sec1.enroll_student(stu3)
oop_sec2.enroll_student(stu3)
oop_sec2.enroll_student(stu4)
oop_sec2.enroll_student(stu5)

# Enroll subjects for students
stu1.enroll_subject(oop_sec1)
stu2.enroll_subject(oop_sec1)
stu3.enroll_subject(oop_sec1)
stu3.enroll_subject(oop_sec2)
stu4.enroll_subject(oop_sec2)
stu5.enroll_subject(oop_sec2)

def find_students_by_teacher(teacher_id):
    new_students_list = []
    for teacher in [tch1, tch2]:
        if teacher.teacher_id == teacher_id:
            for subject_taught in teacher.subjects_taught_list:
                for student in subject_taught.students_list:
                    new_students_list.append(student.stu_name)
    return new_students_list

def find_subjects_by_student(student_id):
    new_subjects_list = []
    for student in [stu1, stu2, stu3, stu4, stu5]:
        if student.stu_id == student_id:
            for subject_enrolled in student.subjects_list:
                new_subjects_list.append(subject_enrolled.sub_name)
    return new_subjects_list

teacher_id = input("Input teacher ID (101, 102) : ")
teacher_students = find_students_by_teacher(teacher_id)
print(f"Teacher teaches the following students: {teacher_students}")

student_id = input("Input student ID (001, 002, 003, 004, 005) : ")
student_subjects = find_subjects_by_student(student_id)
print(f"Student is enrolled in the following subjects: {student_subjects}")