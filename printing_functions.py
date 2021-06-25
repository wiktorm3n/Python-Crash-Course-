def printing_models(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with he following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def send_message(text_messages, sent_messages):
    while text_messages:
        current_messages = text_messages.pop()
        print(f"Sending messages : {current_messages}")
        sent_messages.append(current_messages)


def show_messages(sent_messages):
    print(f"\nThe following messages has been sent : \n")
    for sent_message in sent_messages:
        print(sent_message)


def show_messages(text_messages):
    for message in text_messages:
        print(message)
