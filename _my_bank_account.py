import os.path

FILE_NAME_ORDERS = 'orders.txt'
FILE_NAME_BILL = 'bill.txt'


def my_bank_account():
    history = []
    if os.path.exists(FILE_NAME_ORDERS):
        with open(FILE_NAME_ORDERS, 'r') as f:
            for order in f:
                history.append(order.replace('\n', ''))

    bill_sum = 0
    if os.path.exists(FILE_NAME_BILL):
        with open(FILE_NAME_BILL, 'r') as f:
            bill_sum = int(f.read())

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню - ')
        if choice == '1':
            try:
                cost = int(input('Введите сумму - '))
            except Exception:
                print('Вы ввели не число!')
            else:
                bill_sum += cost
        elif choice == '2':
            try:
                cost =int( input('Введите сумму покупки - '))
            except Exception:
                    print('Вы ввели не число!')
            else:
                if cost > bill_sum:
                    print('Недостаточно средств')
                else:
                    bill_sum -= cost
                    name = input('Введите название покупки - ')
                    history.append((name, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open(FILE_NAME_ORDERS, 'w') as f:
                for name in history:
                    f.write(f'{name}\n')

            with open(FILE_NAME_BILL, 'w') as f:
                f.write(f'{bill_sum}')

            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    print('Проверка фукцнии', my_bank_account())
