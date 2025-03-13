import random
import string

first_names = [
    "Mohammed", "Demitri", "Kim", "Alexander", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Gina", "Henry", "Ivy", "Jane", "Adam", "Ahmad",
    "Sophia", "Jackson", "Olivia", "Liam", "Emma", "Aiden", "Lucas", "Mia", "Noah", "Isabella", "Ethan", "Charlotte", "James", "Amelia", "Benjamin",
    "Harper", "Grace", "Jack", "Elijah", "Scarlett", "Wyatt", "Anna", "Sebastian", "Zoe", "Matthew", "Chloe", "Mason", "Oliver", "Lily", "Levi",
    "Joseph", "Michael", "Daniel", "Sophie", "John", "Samuel", "Gabriel", "Victoria", "Leo", "Camila", "Evan", "Aurora", "Harrison", "Audrey",
    "Hudson", "Savannah", "Eleanor", "Maya", "Emily", "Caleb", "Layla", "Owen", "Madeline", "Max", "Isaiah", "Zachary", "Dylan", "Carter", "Wyatt"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson",
    "Anderson", "Thomas", "Taylor", "Moore", "White", "Clark", "Lewis", "Harris", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott",
    "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Campbell", "Gomez", "Morris", "Murphy", "Rogers", "Reed"
]

domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "icloud.com", "protonmail.com"]

common_words = ["Pass", "Love", "123", "Life", "Secret", "World", "Forever", "2024"]

def generate_password(name, birth_year, birth_month):
    patterns = [
        f"{name}{birth_year}",
        f"{name}{birth_month}{birth_year[-2:]}",
        f"{name}_{birth_year}",
        f"{name}{random.randint(10,99)}",
        f"{name}{random.choice(common_words)}"
    ]
    return random.choice(patterns)

def generate_email(first, last, birth_year):
    formats = [
        f"{first.lower()}.{last.lower()}@{random.choice(domains)}",
        f"{first.lower()}{last.lower()}{random.randint(10, 99)}@{random.choice(domains)}",
        f"{first.lower()}_{last.lower()}@{random.choice(domains)}",
        f"{first[0].lower()}{last.lower()}{birth_year}@{random.choice(domains)}"
    ]
    return random.choice(formats)

num_combinations = int(input("Enter the number of how many lines you want: "))

with open("generated_emails.txt", "w") as file:
    for i in range(num_combinations):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        birth_year = str(random.randint(1970, 2012))
        birth_month = str(random.randint(1, 12)).zfill(2)

        email = generate_email(first_name, last_name, birth_year)
        password = generate_password(first_name, birth_year, birth_month)

        file.write(f"{email}:{password}\n")

print("The email-password combinations have been saved to 'generated_emails.txt'.")
input("Did you finish copying?")
