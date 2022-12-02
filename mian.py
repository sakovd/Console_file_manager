import sys
import os
from _my_bank_account import my_bank_account
from _victory import victory

while True:
    print('\n1. создать папку') #done
    print('2. удалить (файл/папку)') #done
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории') #done
    print('5. посмотреть только папки') #done
    print('6. посмотреть только файлы') #done
    print('7. просмотр информации об операционной системе') #done
    print('8. создатель программы') #done
    print('9. играть в викторину') #done
    print('10. мой банковский счет') #done
    print('11. смена рабочей директории') #os.chdir(path) - смена текущей директории.
    print('12. выход') #done


    choice = input('\nВыберите пункт меню - ')
    if choice == '1':
        name = input('Введите название папки: ')
        if os.path.exists(name):
            print('Такая папка уже существует!')
        else:
            # создать папку передаем путь
            os.mkdir(name)
    elif choice == '2':
        answer = ''
        while answer not in ['файл', 'папка']:
            answer = input('Что вы хотите удалить (файл/папка): ')
        if answer == 'файл':
            name = input('Введите название файла для удаления: ')
            if name in os.listdir():
                os.remove(name)
                print(f'Файл {name} успешно удален!')
            else:
                print('Нет такого файла')
        else:
            name = input('Введите название папки для удаления: ')
            if name in os.listdir():
                os.rmdir(name)
                print(f'Папка {name} успешно удалена!')
            else:
                print('Нет такой папки')

        #name = input('Введите название файла/папки для удаления: ')

    elif choice == '3':
        pass
    elif choice == '4':
        print(os.listdir())
        with open('listdir.txt', 'w') as f:
            spisok_files = []
            spisok_folders = []
            for file in os.listdir():
                if os.path.isfile(file):
                    spisok_files.append(file)
                elif os.path.isdir(file):
                    spisok_folders.append(file)
            f.write(f'files: {spisok_files}')
            f.write(f'\nfolders: {spisok_folders}')

    elif choice == '5':
        spisok = []
        for file in os.listdir():
            if os.path.isdir(file):
                spisok.append(file)
        print(spisok)
    elif choice == '6':
        spisok = []
        for file in os.listdir():
            if os.path.isfile(file):
                spisok.append(file)
        print(spisok)
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Создатель программы - Дмитрий')
    elif choice == '9':
        victory()
    elif choice == '10':
        my_bank_account()
    elif choice == '11':
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')