def main():
    guests = {}
    unliked_count = 0

    while True:
        command = input().strip()

        if command == "Stop":
            break

        if command.startswith("Like-"):
            _, guest, meal = command.split('-')

            if guest not in guests:
                guests[guest] = []

            if meal not in guests[guest]:
                guests[guest].append(meal)

        elif command.startswith("Dislike-"):
            _, guest, meal = command.split('-')

            if guest not in guests:
                print(f"{guest} is not at the party.")
            else:
                if meal not in guests[guest]:
                    print(f"{guest} doesn't have the {meal} in his/her collection.")
                else:
                    guests[guest].remove(meal)
                    print(f"{guest} doesn't like the {meal}.")
                    unliked_count += 1

    for guest, meals in guests.items():
        print(f"{guest}: {', '.join(meals)}")

    print(f"Unliked meals: {unliked_count}")


if __name__ == "__main__":
    main()
