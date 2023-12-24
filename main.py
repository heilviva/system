import sqlite3

# Класс, представляющий студента
class Student:
    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email

    def enroll_course(self, course):
        # логика регистрации студента на курс
        pass

    def drop_course(self, course):
        # логика отмены регистрации студента на курс
        pass

# Класс, представляющий преподавателя
class Teacher:
    def __init__(self, teacher_id, name, email):
        self._teacher_id = teacher_id
        self._name = name
        self._email = email

    def create_course(self, course_name):
        # логика создания нового курса
        pass

    def delete_course(self, course):
        # логика удаления курса
        pass

# Класс, представляющий курс
class Course:
    def __init__(self, course_id, name):
        self._course_id = course_id
        self._name = name

    def assign_teacher(self, teacher):
        # логика назначения преподавателя на курс
        pass

    def get_students(self):
        # логика получения списка студентов на курсе
        pass

# Класс, представляющий группу
class Group:
    def __init__(self, group_id, name):
        self._group_id = group_id
        self._name = name

    def add_student(self, student):
        # логика добавления студента в группу
        pass

    def remove_student(self, student):
        # логика удаления студента из группы
        pass

# Функция для подключения к базе данных
def connect_to_database():
    connection = sqlite3.connect("university.db")
    return connection

# Функция для создания таблиц в базе данных
def create_tables():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS groups (id INTEGER PRIMARY KEY, name TEXT)")

    connection.commit()
    connection.close()

# Функция для добавления студента в базу данных
def add_student(student):
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (student._name, student._email))

    connection.commit()
    connection.close()

# Функция для получения списка студентов из базы данных
def get_students():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    students = []
    for row in rows:
        student = Student(row[0], row[1], row[2])
        students.append(student)

    connection.close()

    return students

# Вызов функций и использование классов
create_tables()

student_1 = Student(1, "John Doe", "john.doe@example.com")
add_student(student_1)

students = get_students()
for student in students:
    print(student._name)
