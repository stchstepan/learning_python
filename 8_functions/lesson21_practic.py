print("#1")

def show_message(messages):
  for message in messages:
    print(message)

short_messages = ['privet', 'zdorovo', 'hello', 'ya artemik']
show_message(short_messages)

print("\n#2")

def send_message(messages, sent_message):
  print("Messages is sanding")
  while messages:
    msg = messages.pop()
    sent_message.append(msg)

short_messages = ['privet', 'zdorovo', 'hello', 'ya artemik']
sent = []

print(short_messages)
print(sent)

send_message(short_messages, sent)

print(short_messages)
print(sent)

print("\n#3")

def send_message(messages, sent_message):
  print("Messages is sanding")
  while messages:
    msg = messages.pop()
    sent_message.append(msg)

short_messages = ['privet', 'zdorovo', 'hello', 'ya artemik']
sent = []

print(short_messages)
print(sent)

send_message(short_messages[:], sent)

print(short_messages)
print(sent)