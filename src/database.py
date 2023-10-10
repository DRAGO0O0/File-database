#общие функции (CRUD и доп функции)
from tables import*
import json
is_GradeID_unique = check_unique_Grade_id(data)
if is_GradeID_unique:
    print("Поле GradeID уникально для каждой записи в данных")
else:
    print("Поле GradeID имеет повторяющиеся значения в данных")

is_Student_Name_unique = check_unique_Student_Name(data)
if is_Student_Name_unique:
    print("Имена студентов уникальны для каждого класса")
else:
    print("Имеются повторяющиеся имена студентов внутри одного класса")

is_subject_valid = check_subject_values(data)
if is_subject_valid:
    print("Поле Subject имеет как минимум 3 различных значения")
else:
    print("Поле Subject не имеет достаточного количества различных значений")

is_StudentName_values = check_Student_Name_values(data)
if is_StudentName_values:
    print("Поле StudentName имеет как минимум 5 различных значений")
else:
    print("Поле StudentName не имеет достаточного количества различных значений")

is_Class_values = check_Class_values(data)
if is_Class_values:
    print("Поле Class имеет как минимум 5 различных значений")
else:
    print("Поле Class не имеет достаточного количества различных значений")
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def write_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def print_record(record):
    print("Запись:")
    print("GradeID:", record["GradeID"])
    print("StudentName:", record["StudentName"])
    print("Class:", record["Class"])
    print("Subject:", record["Subject"])
    print("Score:", record["Score"])
def read_records(file_name, data):
    for record in data:
        print_record(record)
def create_record(file_name, data):
    student_name = input("Введите имя студента: ")
    class_name = input("Введите класс студента: ")
    subject = input("Введите предмет: ")
    score = float(input("Введите оценку: "))

    new_record = {
        "GradeID": len(data) + 1,
        "StudentName": student_name,
        "Class": class_name,
        "Subject": subject,
        "Score": score
    }
    data.append(new_record)
    write_data(file_name, data)
    print_record(new_record)

def read_records(data):
    show_tables(data)

def update_record(data):
    record_id = input("Введите ID записи для обновления: ")
    for record in data:
        if str(record["GradeID"]) == record_id:
            new_score = float(input("Введите новое значение для поля Score: "))
            record["Score"] = new_score
            write_data(file_name, data)
            print("Запись успешно обновлена.")
            return

def delete_record(data):
    record_id= input(("Введите ID записи для удаления: "))
    for record in data:
        if str(record["GradeID"]) == record_id:
            data.remove(record)
            print("Запись успешно удалена.")
    print("Запись с указанным идентификатором не найдена.")

def calculate_average_score_subject(data, subject):
    scores = []
    for row in data:
        if row["Subject"] == subject:
            scores.append(row["Score"])
    if len(scores) > 0:
        average_score_subject = sum(scores) / len(scores)
        return average_score_subject
    else:
        return 0

def calculate_average_score_student(data, student_name):
    scores = []
    for row in data:
        if row["StudentName"] == student_name:
            scores.append(row["Score"])
    if len(scores) > 0:
            average_score_student = sum(scores)/len(scores)
            return average_score_student
    else:
        return 0

def get_below(data,below):
    below_student=[]
    for row in data:
        if row["Score"] < below:
            below_student.append(row["StudentName"])
    return below_student

def get_high(data):
    high_students = []
    for row in data:
        if row["Score"] in [4, 5]:
            high_students.append(row["StudentName"])
    return high_students