def display_chat(chat_history):
    print("Текущий текст чата:")
    for message in chat_history:
        print(message)

def send_message(username, chat_history):
    message = input(f"{username}, введите ваше сообщение: ")
    chat_history.append(f"{username}: {message}")
    print("Сообщение отправлено!")

def main():
    username = input("Введите ваше имя: ")
    chat_history = []

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть текущий текст чата")
        print("2. Отправить сообщение")
        print("3. Выйти из чата")

        choice = input("Введите номер действия: ")

        if choice == '1':
            display_chat(chat_history)
        elif choice == '2':
            send_message(username, chat_history)
        elif choice == '3':
            print("Вы вышли из чата. До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
