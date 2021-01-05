message = "It was a bright cold day in April, and the clocks were striking thirteen"

msg_dict={}
for msg in message:
    '''print(msg, message.count(msg))'''
    if msg !=" ":
        msg_dict[msg] = message.count(msg)

for letter,num in msg_dict.items():
    print(letter, num)
