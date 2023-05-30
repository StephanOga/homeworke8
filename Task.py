print('Коды телефонного справочника:', '1 - показать телефонную книгу',
      '2 - добавить контакт', '3 - найти контакт', '4 - изменить контакт', '5 - удалить контакт',
      '6 - выход', sep='\n')
num = int(input('Введите код: '))

if num == 1:
    data = open('phonebook.txt', 'r', encoding='utf-8')
    for line in data:
        print(line, end=" ")
    data.close()

if num == 2:
    data = open('phonebook.txt', 'a', encoding='utf-8')
    surname = input('Давайте добавим контакт. Фамилия: ')
    name = input('Имя: ')
    middle_name = input('Отчество: ')
    phone_number = input('Номер телефона: ')
    united_number = f'{surname} {name} {middle_name} {phone_number}'
    print(united_number)
    data.write(united_number + '\n')
    print('Контакт успешно добавлен. Спасибо за работу над справочником.')
    data.close()

if num == 3:
    you_seek = input('Кого или что вы ищете? Напишите или фамилию, или имя, или отчество, или номер телефона: ')
    data = open('phonebook.txt', 'r', encoding='utf-8')
    print(
        'Справочник осуществляет поиск. Ниже будет результат. Если ничего не будет найдено, ничего не будет выведено.')
    for line in data:
        if you_seek in line.split():
            print(line)
    data.close()

if num == 4:
    to_change = input(
        'Какой контакт вы хотите изменить? Напишите или фамилию, или имя, или отчество, или номер телефона: ')
    print('Справочник пытается найти данные. Если их не будет, система просто поблагодарит вас.')
    data = open('phonebook.txt', 'r', encoding='utf-8')
    temporary_file = []
    for line in data:
        if to_change in line.split():
            print(line)
            opportunity_to_exit = int(
                input('Если это тот самый контакт, напишите 0. Если нет, напишите любое другое число: '))
            if opportunity_to_exit == 0:
                old_thing = int(input(
                    'Что здесь конкретно необходимо исправить? Впишите цифру. Фамилию(0), имя(1), отчество(2) или номер телефона?(3) '))
                new_thing = input('Как надо эту запись исправить? Впишите новый вариант: ')

                line_to_dictionary = {0: line.split()[0], 1: line.split()[1], 2: line.split()[2], 3: line.split()[3]}
                for key, value in line_to_dictionary.items():
                    if key == old_thing:
                        line_to_dictionary.update({key: new_thing})
                print(line_to_dictionary)
                line_to_file = []
                for key, value in line_to_dictionary.items():
                    line_to_file.append(value)
                line = ' '.join(line_to_file)
                print('Хорошо, данные обновились. Теперь это', line,
                      'Система может закончить или предложить еще контакт для изменения!')
        temporary_file.append(line.strip())
    print('Спасибо за работу над улучшением справочника.')
    data.close()
    data = open('phonebook.txt', 'w', encoding='utf-8')
    for item in temporary_file:
        data.write(item + '\n')
    data.close()

if num == 5:
    to_delete = input('Какой контакт нужно удалить? Напишите или фамилию, или имя, или отчество, или номер телефона:  ')
    print('Справочник пытается найти данные. Если их не будет, система просто поблагодарит вас.')
    data = open('phonebook.txt', 'r', encoding='utf-8')
    temporary_file = []
    for line in data:
        if to_delete in line.split():
            print(line)
            opportunity_to_exit = int(
                input('Если это тот самый контакт, напишите 0. Если нет, напишите любое другое число: '))
            if opportunity_to_exit == 0:
                line = ''
                print(
                    'Хорошо, данные обновились. Теперь этого контакта нет. Система может закончить или предложить еще контакт для удаления!')
        temporary_file.append(line.strip())
    print('Спасибо за работу над улучшением справочника.')
    data.close()
    data = open('phonebook.txt', 'w', encoding='utf-8')
    for item in temporary_file:
        data.write(item + '\n')
    data.close()

if num == 6:
    print('До свидания!')
    exit()