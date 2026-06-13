import random
import string


def generate_random_email() -> str:
    random_number = random.randint(10000, 99999)
    return f"sapir{random_number}@gmail.com"


def generate_random_first_name() -> str:
    names = ["Sapir", "Noa", "Dana", "Shir", "Maya", "Lior"]
    return random.choice(names)


def generate_random_last_name() -> str:
    last_names = ["Reuveni", "Cohen", "Levi", "Mizrahi", "Peretz"]
    return random.choice(last_names)


def generate_random_phone() -> str:
    return "05" + "".join(random.choices("0123456789", k=8))


def generate_random_password(length: int = 6) -> str:
    return "".join(random.choices(string.digits, k=length))