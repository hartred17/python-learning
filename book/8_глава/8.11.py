def show_messages(messages):
    """Выводит текст каждого сообщения в списке."""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Выводит каждое сообщение и перемезает его в список sent_messages."""
    while messages:
        current_message = messages.pop()
        print(f"Отправленное сообщение: {current_message}")
        sent_messages.append(current_message)


messages = ["privet", "kak", "dela"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
