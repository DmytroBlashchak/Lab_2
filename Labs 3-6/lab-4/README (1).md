import os #вводимо модуль os для роботи з операційною системою (включно з файлами)

while True: #починаємо наш код з введення вічного циклу, до поки дія не завершиться(не дійде до break)
    file_path = input("Enter the path to the file: ")#щоб дізнатися, який шлях обере користувач нам потрібно ввести константу(яка буде зберігати шлях до файлу), так як ми не знаємо, який шлях обере користувач ми записуємо його завдяки input

    if not os.path.exists(file_path): #вводимо першу умову: якщо нашого шляху(операційної системи у якій ми працюмо) немає
        print("File not found!")# то ми пишемо, що файлу не знайдено
        continue

    with open(file_path, 'r') as file: # дана команда відкриває файл(шлях якого ми написали раніше) для читання("r")
        content = file.readlines() #перевіряє вміст файлу та зберігає змінну content(використовуючи команду readlines)

    
    total_lines = len(content) #вираховує загальну кількість рядків у даному файлі 
    empty_lines = content.count('\n') #вираховує кількість порожніх рядків 
    lines_with_z = sum('z' in line for line in content)#дана програма вираховує загальну кількість z у рядку(за умовою лабораторної роботи номер 4)
    z_count = sum(line.count('z') for line in content)#даний елемент сумує загальну кількість z у файлі(використовуючи значення 15 рядка, де ми вираховували загальну кількість букв у рядку) (за умовою лабораторної роботи номер 4)
    lines_with_and = sum('and' in line for line in content) #даний елемент сумує загальну кількість and у файлі, та сумує їх, також цей код буде брати частку "and", зі слів(згадуючи методичку до лабораторної роботи номер 4 ми можемо побачити, що слово "andromeda", він зарахує, бо на початку цього слова є префікс "and") (за умовою лабораторної роботи номер 4)

    print(f"\nFile: {file_path}")# виводимо текст, який описує наш шлях до даного файлу з яким ми працювали
    print(f"total lines: {total_lines}")# виводимо інформацію(текстом), про загальну кількість рядків(беручи до уваги лайн 14(total_lines = len(content)))
    print(f"empty lines: {empty_lines}")# виводимо інформацію(текстом), про загальну кількість порожніх рядків(беручи до уваги лайн 15(empty_lines = content.count('\n'))
    print(f"lines with \"z\": {lines_with_z}")# виводимо інформацію(текстом), про загальну кількість літер "z" у рядку, у нашому коді(беручи до уваги лайн 16 який отримує та сумує кількість наших букв "z" у коді)
    print(f"\"z\" and: {z_count}") # виводимо інформацію(текстом), про загальну кількість літер "z"
    print(f"lines with \"and\": {lines_with_and}") # виводимо інформацію(текстом), про загальну кількість словосполучення "and" у рядку, у нашому коді(беручи до уваги лайн 18 який знаходить, та обраховує загальну кількість "and" у нашому файлі)

    answer = input("Do you want to analyze another file? (y/n): ") # запитуємо користувача, чи буде він надалі працювати з даною програмою
    if answer.lower() != 'y': #якщо користувач не обрав відповідь 'y'(yes), то програма зупиняє даний цикл 
        break