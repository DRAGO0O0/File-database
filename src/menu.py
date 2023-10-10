#консоль, вызов функций из tables и database
from database import*
from tables import*
import json

def read_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data
def write_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def show_menu():
    while True:
        print("Меню:")
        print("1. Расчет среднего балла по предмету")
        print("2. Расчет среднего балла для студента")
        print("3. Вывод студентов с оценками ниже заданного значения")
        print("4. Вывод студентов-хорошистов")
        print("5. Просмотр всех записей")
        print("6. Добавить студента")
        print("7. Обновить оценку студента")
        print("8. Удалить студента")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            subject = input("Введите предмет: ")
            average_score_subject = calculate_average_score_subject(data, subject)
            print(f"Средний балл по предмету {subject}: {average_score_subject}")
        elif choice == "2":
            student_name = input("Введите имя студента: ")
            average_score_student = calculate_average_score_student(data, student_name)
            print(f"Средний балл для студента {student_name}: {average_score_student}")
        elif choice == "3":
            below = float(input("Введите пороговое значение: "))
            below_student = get_below(data, below)
            print(f"Студенты с оценками ниже {below}: {below_student}")
        elif choice == "4":
            high_students = get_high(data)
            print("Студенты-хорошисты:")
            for student in high_students:
                print(student)
        elif choice == "5":
            read_records(data)
        elif choice == "6":
            create_record(file_name,data)
            print("Запись успешно добавлена")
        elif choice == "7":
            update_record(data)
            print("Запись успешно обновлена.")
        elif choice == "8":
            delete_record(data)
            print("Студент успешно удален")
        elif choice == "9":
            print("Выход")
            break
        else:
            print("Некорректный выбор")



