def send_email(message, recipient, sender = "university.help@gmail.com"):
    test_sender = tuple(sender)
    test1 = True
    test2_1 = True
    test2_2 = True
    test2_3 = True
    for char_i in test_sender:
        test1 = False
        if char_i == '@':
            test1 = True
            break
    if test1 == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    length_mail = len(test_sender)
    if test_sender[length_mail-1] == 'm' and test_sender[length_mail-2] == 'o' and test_sender[length_mail-3] == 'c' and test_sender[length_mail-4] == '.':
        test2_1 = True
    else:
        test2_1 = False
    if test_sender[length_mail-1] == 'u' and test_sender[length_mail-2] == 'r' and test_sender[length_mail-3] == '.':
        test2_2 = True
    else:
        test2_2 = False
    if test_sender[length_mail-1] == 't' and test_sender[length_mail-2] == 'e' and test_sender[length_mail-3] == 'n' and test_sender[length_mail-4] == '.':
        test2_3 = True
    else:
        test2_3 = False



    if test2_1 == False and test2_2 == False and test2_3 == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    if sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

