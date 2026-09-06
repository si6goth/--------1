import datetime
from faker import Faker

# Инициализируем Faker с русской локалью
fake = Faker('ru_RU')

print(f"Текущая дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("--- Генерация одиночных случайных данных ---")
# Случайное полное имя (зависит от пола)
print(f"Имя: {fake.name()}")

# Случайный адрес
print(f"Адрес: {fake.address()}")

# Случайный email
print(f"Email: {fake.email()}")

# Случайный номер телефона
print(f"Телефон: {fake.phone_number()}")

# Случайный текст из нескольких предложений
print(f"О себе: {fake.text(max_nb_chars=100)}")


print("\n--- Генерация списка пользователей (например, для базы данных) ---")
# Создаем список из 3 фейковых профилей
for i in range(1, 4):
    print(f"\nПользователь №{i}:")
    print(f"  Логин: {fake.user_name()}")
    print(f"  Пароль: {fake.password(length=10)}")
    print(f"  Компания: {fake.company()}")
    print(f"  Дата рождения: {fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d.%m.%Y')}")
