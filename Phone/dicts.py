"""Это телефонная книга"""
"""Новая строка"""
# printing the heading of the program
print("WELCOME TO THE PHONEBOOK DIRECTORY")

# creating a .txt file to store contact details
filename = "myphonebook.txt"
myfile = open(filename, "a+")
myfile.close

# Добавить в код новые изменения


# defining main menu
def main_menu():
    print("\nГЛАВНОЕ МЕНЮ\n")
    print("1. Показать все контакты")
    print("2. Добавить новый контакт")
    print("3. Поиск существующего контакта")
    print("4. Выход")
    choice = input("Введите ваш вариант: ")
    if choice == "1":
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print("Нет контакта в телефонной книге.")
        else:
            print(filecontents)
        myfile.close
        enter = input("Нажмите Enter чтобы продолжить ...")
        main_menu()
    elif choice == "2":
        newcontact()
        enter = input("Нажмите Enter чтобы продолжить ...")
        main_menu()
    elif choice == "3":
        searchcontact()
        enter = input("Нажмите Enter чтобы продолжить ...")
        main_menu()
    elif choice == "4":
        print("Спасибо за использование Phonebook!")
    else:
        print("Пожалуйста, укажите действительные данные!\n")
        enter = input("Нажмите Enter чтобы продолжить ...")
        main_menu()


# defining search function
def searchcontact():
    searchname = input("Введите имя для поиска контактной записи: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print("Ваша необходимая контактная информация - это:", end=" ")
            print(line)
            found = True
            break
    if found == False:
        print(
            "Искомый контакт недоступен в телефонной книге",
            searchname,
        )


# first name
def input_firstname():
    first = input("Введите свое Имя: ")
    remfname = first[1:]
    firstchar = first[0]
    return firstchar.upper() + remfname


# last name
def input_lastname():
    last = input("Введите свою Фамилию: ")
    remlname = last[1:]
    firstchar = last[0]
    return firstchar.upper() + remlname


# storing the new contact details
def newcontact():
    firstname = input_firstname()
    lastname = input_lastname()
    phoneNum = input("Введите свой номер телефона: ")
    emailID = input("Введите свой E-mail: ")
    contactDetails = (
        "["
        + firstname
        + " "
        + lastname
        + ", "
        + phoneNum
        + ", "
        + emailID
        + "]\n"
    )
    myfile = open(filename, "a")
    myfile.write(contactDetails)
    print(
        "Следующие контактные данные:\n "
        + contactDetails
        + "\nКонтакт успешно сохранен!"
    )


main_menu()
