def send_message(text_messages,sent_messages):
    while text_messages:
        current_messages = text_messages.pop()
        print(f"Sending messages : {current_messages}")
        sent_messages.append(current_messages)
def show_messages(sent_messages):
    print(f"\nThe following messages has been sent : \n")
    for sent_message in sent_messages:
        print(sent_message)
text_messages = ['test1','test2','test3']
sent_messages = []
send_message(text_messages[:],sent_messages)
show_messages(sent_messages)
print(sent_messages)
print(text_messages[:])