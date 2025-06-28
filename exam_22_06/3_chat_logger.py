def chat_func(new_message_: str, messages_list: list):
    messages_list.append(new_message_)
    return messages_list


def del_func(text_: str, messages_list: list):
    if text_ in messages_list:
        messages_list.remove(text_)
    return messages_list

def edited_func(text_: str, edited_text_:str, messages_list: list):
    if text_ in messages_list:
        ind = messages_list.index(text_)
        messages_list[ind] = edited_text_
    return messages_list


def pin_func(text_: str, messages_list: list):
    if text_ in messages_list:
        messages_list.remove(text_)
        messages_list.append(text_)
    return messages_list

def spam_func(command_list: list, messages_list: list):
    index_spam_messages = len(command_list) - 1
    messages_list += command_list[1:]
    return messages_list

messages = []

while True:
    command =input().split()

    if command[0] == "end":
        print("\n".join(messages))
        break

    elif command[0] == "Chat":
        new_message = command[1]
        chat_func(new_message, messages)

    elif command[0] == "Delete":
        text = command[1]
        del_func(text, messages)

    elif command[0] == "Edit":
        text = command[1]
        edited_message = command[2]
        edited_func(text, edited_message, messages)

    elif command[0] == "Pin":
        text = command[1]
        pin_func(text, messages)

    elif command[0] == "Spam":
        spam_func(command, messages)