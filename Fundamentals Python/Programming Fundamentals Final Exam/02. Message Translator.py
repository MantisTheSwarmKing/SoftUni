import re

def translate_message(n):
    pattern = r"!([A-Z][a-z]{3,})!:\[([A-Za-z]{8,})\]"
    regex = re.compile(pattern)

    for _ in range(n):
        message = input().strip()
        valid_message = regex.match(message)

        if valid_message:
            command = valid_message.group(1)
            information = valid_message.group(2)
            print(command + ":", end=" ")
            print(" ".join(str(ord(ch)) for ch in information))
        else:
            print("The message is invalid")

n = int(input())
translate_message(n)
