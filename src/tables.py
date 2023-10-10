#Функции для работы с каждой таблицей, структура таблицы и проверка уникальности. Сделать их аккуратный вывод (в виде таблиц) в консоль
import json

grade_id = "GradeID"
class_name = "Class"
student_name = "StudentName"
subject = "Subject"
score = "Score"

data = [
{
    "GradeID": 1,
    "StudentName": "Анна",
    "Class": "10A",
    "Subject": "Математика",
    "Score": 5
  },
  {
    "GradeID": 2,
    "StudentName": "Иван",
    "Class": "10B",
    "Subject": "Физика",
    "Score": 4
  },
  {
    "GradeID": 3,
    "StudentName": "Мария",
    "Class": "11A",
    "Subject": "Английский",
    "Score": 5
  },
  {
    "GradeID": 4,
    "StudentName": "Петр",
    "Class": "11B",
    "Subject": "Математика",
    "Score": 3
  },
  {
    "GradeID": 5,
    "StudentName": "Екатерина",
    "Class": "9A",
    "Subject": "История",
    "Score": 5
  },
  {
    "GradeID": 6,
    "StudentName": "Алексей",
    "Class": "9B",
    "Subject": "Физика",
    "Score": 4
  },
  {
    "GradeID": 7,
    "StudentName": "Анна",
    "Class": "10A",
    "Subject": "Литература",
    "Score": 4
  },
  {
    "GradeID": 8,
    "StudentName": "Михаил",
    "Class": "11A",
    "Subject": "Математика",
    "Score": 4
  },
  {
    "GradeID": 9,
    "StudentName": "Ольга",
    "Class": "11B",
    "Subject": "Биология",
    "Score": 5
  },
  {
    "GradeID": 10,
    "StudentName": "Дмитрий",
    "Class": "9A",
    "Subject": "Химия",
    "Score": 4
  },
  {
    "GradeID": 11,
    "StudentName": "Екатерина",
    "Class": "9B",
    "Subject": "География",
    "Score": 5
  },
  {
    "GradeID": 12,
    "StudentName": "Алексей",
    "Class": "10A",
    "Subject": "Алгебра",
    "Score": 5
  },
  {
    "GradeID": 13,
    "StudentName": "Ирина",
    "Class": "10B",
    "Subject": "Физика",
    "Score": 3
  },
  {
    "GradeID": 14,
    "StudentName": "Павел",
    "Class": "11A",
    "Subject": "История",
    "Score": 4
  },
  {
    "GradeID": 15,
    "StudentName": "Наталья",
    "Class": "11B",
    "Subject": "Английский",
    "Score": 5
  },
  {
    "GradeID": 16,
    "StudentName": "Андрей",
    "Class": "9A",
    "Subject": "Физкультура",
    "Score": 5
  },
  {
    "GradeID": 17,
    "StudentName": "Светлана",
    "Class": "9B",
    "Subject": "Информатика",
    "Score": 4
  },
  {
    "GradeID": 18,
    "StudentName": "Евгений",
    "Class": "10A",
    "Subject": "Музыка",
    "Score": 4
  },
  {
    "GradeID": 19,
    "StudentName": "Татьяна",
    "Class": "10B",
    "Subject": "Литература",
    "Score": 5
  },
  {
    "GradeID": 20,
    "StudentName": "Антон",
    "Class": "11A",
    "Subject": "Математика",
    "Score": 5
  }
]


def check_unique_Grade_id(data):
  unique_GradeID = set(row["GradeID"] for row in data)
  return len(unique_GradeID) == len(data)

def check_unique_Student_Name(data):
  unique_Student_Name = set((row["StudentName"], row["Class"]) for row in data)
  return len(unique_Student_Name) == len(data)

def check_subject_values(data):
  unique_subjects = set(row["Subject"] for row in data)
  return len(unique_subjects) >= 3

def check_Student_Name_values(data):
  StudentName_values = set(row["StudentName"] for row in data)
  return len(StudentName_values) >= 5

def check_Class_values(data):
  Class_values = set(row["Class"] for row in data)
  return len(Class_values) >= 5


file_name = "database.json"
with open(file_name, "w") as file:
    json.dump(data, file, indent=4)


def show_tables(data):
  print("+---------+--------------+--------+-------------+-------+")
  print("| GradeID | Student Name | Class  |  Subject    | Score |")
  print("+---------+--------------+--------+-------------+-------+")

  for row in data:
    print("| {:^7} | {:^12} | {:^6} | {:^11} | {:^5} |".format(
      row["GradeID"], row["StudentName"], row["Class"], row["Subject"], row["Score"]))

  print("+---------+--------------+--------+-------------+-------+")



