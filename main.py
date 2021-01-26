# used for tracking paid bills
import datetime


def payee():
    payee_name = input('payee name: ')
    payee_amount = float(input('payee amount: $'))
    date_paid = datetime.datetime.today().replace(microsecond=0)
    payee_list = (date_paid, payee_name, payee_amount)
    f = open("report.txt", "a")
    f.write("\n" + str(payee_list))
    f.close()


def categories():
    category = ["power", "phone", "internet", "grocery", "insurance"]
    category_select = input("Please select a category: \n 0 power \n 1 phone \n 2 internet \n 3 grocery \n 4 insurance \n your selection: ")

    if category_select == '0':
        a = category[0]
        return a
    elif category_select == '1' or category_select == 'phone' or category_select == 'Phone':
        a = category[1]
        return a
    elif category_select == '2' or category_select == 'internet' or category_select == 'Internet':
        a = category[2]
        return a
    elif category_select == '3' or category_select == 'grocery' or category_select == 'Grocery':
        a = category[3]
        return a
    elif category_select == '4' or category_select == 'insurance' or category_select == 'Insurance':
        a = category[4]
        return a
    else: print('error sorry')

    f = open("report.txt", "a")
    f.write(category_select)
    f.close()


def report():
    payee()
    categories()
    f = open("report.txt", "r")
    print(f.read())
    f.close()

report()
