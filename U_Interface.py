def input_info():
    info = []
    surname = input ('Введите фамилию  ')
    info.append(surname)
    name = input('Введите имя ')
    info.append(name)
    correct = False
    while not correct:
        phone_number = input ('Введите номер телефона  ')
        if len(phone_number) != 11:
            print('Номер должен состоять из 11 цифр')
        else:
            phone_number = int(phone_number)
            correct = True
    info.append(phone_number)
    description = input('Введите описание ') 
    info.append(description)
    print(info)
    return(info)

   
    
