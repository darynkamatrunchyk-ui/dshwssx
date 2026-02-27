class Humanity:
    def __init__(self, name, age):
        self.name = name          # Публічний атрибут
        self.__age = age          # Приватний атрибут (інкапсуляція)

    # Getter — доступ до приватного атрибуту
    def get_age(self):
        return self.__age

    # Метод, який буде перевизначено (поліморфізм)
    def introduce(self):
        return f"Я представник людства. Мене звати {self.name}."

    def breathe(self):
        return f"{self.name} дихає повітрям."


# Наслідування
class Student(Humanity):
    def __init__(self, name, age, course, college_name):
        super().__init__(name, age)   # Виклик конструктора батьківського класу
        self.course = course
        self.college_name = college_name

    # Поліморфізм — перевизначення методу
    def introduce(self):
        return (
            f"Я студент {self.course}-го курсу коледжу {self.college_name}. "
            f"Мене звати {self.name}, мені {self.get_age()} років."
        )

    def study(self):
        return f"{self.name} пише лабораторну роботу з програмування."


# 🔹 Точка входу в програму
if name == "__main__":
    # Створюємо об'єкти
    person = Humanity("Віктор", 45)
    student = Student("Дарина", 18, 2, "ТФК Луцьк")

    # Виклик методів
    print(person.introduce())
    print(student.introduce())  # Поліморфізм
    print(student.study()) поясни мені детально кожен рядок коду 
