def send_email(message,recipient,sender = "university.help@gmail.com"):
    suffix_list = [".com", ".ru", ".net"]
    if "@" not in recipient or not any(recipient.endswith(suffix) for suffix in  suffix_list):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif "@" not in sender or not any(sender.endswith(suffix) for suffix in suffix_list):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')