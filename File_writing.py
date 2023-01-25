from U_Interface import input_info
info = input_info()

def write_txt():
    fl = 'Phonebook.txt'
    with open (fl, 'a', encoding = 'UTF-8') as a:
        a.write(f'{info[0]}\n\n {info[1]}\n\n {info[2]}\n\n {info[3]}\n\n\n')
        

def write_csv():
    fl = 'Phonebook.csv'
    with open (fl, 'a', encoding = 'utf-8') as a:
         a.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')
         


