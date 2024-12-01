def process_commands(message):
    while True:
        command = input().strip()

        if command == "Finalize":
            break

        elif command == "Encrypt":
            message = message[::-1]
            print(message)

        elif command == "Decrypt":
            message = message.swapcase()
            print(message)

        elif command.startswith("Substitute"):
            parts = command.split()
            old_char, new_char = parts[1], parts[2]

            if old_char in message:
                message = message.replace(old_char, new_char)
                print(message)
            else:
                print("Character not found.")

        elif command.startswith("Scramble"):
            parts = command.split()
            index = int(parts[1])
            new_char = parts[2]

            if 0 <= index < len(message):
                message = message[:index] + new_char + message[index + 1:]
                print(message)
            else:
                print("Index out of bounds.")

        elif command.startswith("Remove"):
            parts = command.split()
            substring = parts[1]
            message = message.replace(substring, "")
            print(message)

        else:
            print("Invalid command detected!")


initial_message = input().strip()
process_commands(initial_message)
