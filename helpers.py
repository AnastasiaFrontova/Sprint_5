import random
import string

class DataHelper:  # 4 usages
    @staticmethod  # 1 usage
    def generate_name() -> str:
        """Генератор имени пользователя (произвольная комбинация символов)"""
        name_length = random.randint(3, 6)
        name = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(name_length)
        )
        return name

    @staticmethod  # 1 usage
    def generate_login() -> str:
        """Генератор Email(логина) пользователя"""
        login_length = random.randint(3, 10)
        login = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(login_length)
        )
        domains = ["ya.ru", "gmail.com", "mail.ru", "yandex.ru"]
        domain = random.choice(domains)
        return f"{login}@{domain}".lower()

    @staticmethod  # 1 usage
    def generate_password(min_length=6, max_length=12) -> str:
        """Генератор пароля пользователя"""
        length = random.randint(min_length, max_length)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    @staticmethod
    def generate_invalid_password() -> str:
        """Генератор некорректного пароля"""
        # Некорректный пароль: слишком короткий (1-5 символов) и содержит только буквы
        length = random.randint(1, 5)
        characters = string.ascii_letters
        password = ''.join(random.choice(characters) for _ in range(length))
        return password