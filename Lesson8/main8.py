def add_contact():
    # Функция для добавления новой записи в справочник
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите описание: ")

    contact = f"{surname}, {name}, {patronymic}, {phone_number}, {description}"

    # Открываем файл для добавления новой записи
    with open("phone.txt", "a") as file:
        file.write("\n"+ contact)

    print("Запись успешно добавлена!")


def search_contact():
    # Функция для поиска записи по конкретной характеристике
    keyword = input("Введите характеристику для поиска записи: ")

    # Открываем файл для чтения записей
    with open("phone.txt", "r") as file:
        contacts = file.readlines()

    found_contacts = []

    for contact in contacts:
        if keyword in contact:
            found_contacts.append(contact)

    if found_contacts:
        print("Найдены следующие записи:")
        for contact in found_contacts:
            print(contact.strip())
    else:
        print("Записей с такой характеристикой не найдено.")


def display_contacts():
    # Функция для вывода всех записей из справочника
    with open("phone.txt", "r") as file:
        contacts = file.readlines()

    if contacts:
        print("Телефонный справочник:")
        for contact in contacts:
            print(contact.strip())
    else:
        print("Справочник пуст.")


def export_contacts():
    # Функция для экспорта всех записей справочника в файл .txt
    with open("phone.txt", "r") as file:
        contacts = file.read()

    with open("exported_phone.txt", "w") as file:
        file.write(contacts)

    print("Данные успешно экспортированы в файл exported_phone.txt.")


def import_contacts():
    # Функция для импорта записей из файла .txt в справочник
    file_name = input("Введите имя файла для импорта: ")

    try:
        with open(file_name, "r") as file:
            contacts = file.readlines()

        with open("phone.txt", "a") as file:
            for contact in contacts:
                file.write(contact)
        print("Данные успешно импортированы!")
    except FileNotFoundError:
        print("Файл не найден.")


def main():
    while True:
        print("\nМеню:")
        print("1. Добавить новую запись")
        print("2. Вывести все записи")
        print("3. Поиск записи по характеристике")
        print("4. Экспортировать данные")
        print("5. Импортировать данные")
        print("6. Выйти")

        choice = input("Введите номер выбранного пункта: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            export_contacts()
        elif choice == "5":
            import_contacts()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, повторите попытку.")


if __name__ == "__main__":
    main()
