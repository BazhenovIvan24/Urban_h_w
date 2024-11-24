def send_email(message, recipient = "university.help@gmail.com"):
    test_recipient = tuple(recipient)
    test1 = True
    test2 = True
    for char_i in test_recipient:
        test1 = False
        if char_i == '@':
            test1 = True
            break
    if test1 == False:
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')

    length_mail = len(test_recipient)
    if test_recipient[length_mail-1] == 'm' or test_recipient[length_mail-1] == 'u' or test_recipient[length_mail-1] == 't':
        test2 = True
    else:
        test2 = False

    if test2 == False:
        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')


    return 0

send_email(1, '@1u' )