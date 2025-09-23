def main():
    students = {}  # словник для збереження оцінок

    while True:
        name = input("Введіть ім'я студента (або 'stop' для завершення): ").strip()
        if name.lower() == "stop":
            break
        try:
            grade = int(input(f"Введіть оцінку для {name}: "))
            if 1 <= grade <= 12:
                students[name] = grade
            else:
                print("Оцінка має бути від 1 до 12!")
        except ValueError:
            print("Помилка! Введіть число як оцінку.")

    print("\n--- Результати ---")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    if students:
        avg = sum(students.values()) / len(students)
        print(f"\nСередній бал по групі: {avg:.2f}")

        excellent = [name for name, g in students.items() if 10 <= g <= 12]
        good = [name for name, g in students.items() if 7 <= g <= 9]
        bad = [name for name, g in students.items() if 4 <= g <= 6]
        fail = [name for name, g in students.items() if 1 <= g <= 3]

        print(f"Відмінники (10-12): {len(excellent)} -> {', '.join(excellent) if excellent else 'немає'}")
        print(f"Хорошисти (7-9): {len(good)}")
        print(f"Відстаючі (4-6): {len(bad)}")
        print(f"Не здали (1-3): {len(fail)}")
    else:
        print("Жодних даних не введено.")


if __name__ == "__main__":
    main()
