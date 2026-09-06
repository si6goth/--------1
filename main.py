"""
Генератор случайных данных с помощью библиотеки Faker.
Задание 2: добавлено описание модуля.
"""
import datetime
from faker import Faker

# TODO: Добавить проверку на пустой ввод

# Инициализируем Faker с русской локалью
random_data = Faker('ru_RU')

print(f"Текущая дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("--- Генерация одиночных случайных данных ---")
# Случайное полное имя (зависит от пола)
print(f"Имя: {random_data.name()}")

# Случайный адрес
print(f"Адрес: {random_data.address()}")

# Случайный email
print(f"Email: {random_data.email()}")

# Случайный номер телефона
print(f"Телефон: {random_data.phone_number()}")

# Случайный текст из нескольких предложений
print(f"О себе: {random_data.text(max_nb_chars=100)}")


print("\n--- Генерация списка пользователей (например, для базы данных) ---")
# Создаем список из 3 фейковых профилей
for user_number in range(1, 4):
    print(f"\nПользователь №{user_number}:")
    print(f"  Логин: {random_data.user_name()}")
    print(f"  Пароль: {random_data.password(length=10)}")
    print(f"  Компания: {random_data.company()}")
    print(
        f"  Дата рождения: {random_data.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d.%m.%Y')}")
