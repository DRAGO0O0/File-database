#объединить все файлы в основной цикл программы
import json
from menu import*
from database import*
from tables import*

def read_data(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data
def write_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    file_name = 'database.json'

    while True:
        show_menu()

    write_data(file_name, data)
    print("Программа завершена.")

if __name__ == "__main__":
    main()



