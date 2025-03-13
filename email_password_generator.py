import random
import string
names = [
    "Mohhamed", "Mohammed", "Mohamed", "Demitri", "Kim", "alexander", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Gina", "Henry", "Ivy", "Jane", "Adam", "Ahmad",
    "Sophia", "Jackson", "Olivia", "Liam", "Emma", "Aiden", "Lucas", "Mia", "Noah", "Isabella", "Ethan", "Charlotte", "James", "Amelia", "Benjamin", "Harper", "Henry", 
    "Grace", "Jack", "Elijah", "Scarlett", "Wyatt", "Anna", "Sebastian", "Zoe", "Alexander", "Matthew", "Chloe", "Mason", "Oliver", "Lily", "Levi", "Madison", "Joseph",
    "Michael", "Charlotte", "Daniel", "Sophie", "David", "Emily", "John", "Hannah", "Samuel", "Ella", "Gabriel", "Victoria", "Leo", "Camila", "Henry", "Evan", "Aurora",
    "Leo", "Avery", "Harrison", "Audrey", "Hudson", "Savannah", "Eleanor", "Maya", "Grace", "Elizabeth", "Samuel", "Amos", "Ezra", "Lucy", "Evelyn", "Riley", "Hunter", 
    "Emily", "Caleb", "Layla", "Owen", "Madeline", "Max", "Lillian", "Isaiah", "Gianna", "Zachary", "Victoria", "Lila", "Elise", "Dylan", "Carter", "Wyatt", "Leah",
    "Jasper", "Evelyn", "Adeline", "Nathaniel", "Katherine", "Bella", "Oliver", "Joshua", "Luke", "Sophia", "Grace", "Diana", "Chase", "Megan", "Liam", "Benjamin",
    "Jasmine", "Caleb", "Landon", "Gavin", "Tessa", "Isaiah", "Anna", "Mason", "Mia", "Charlotte", "Archer", "Emma", "Cooper", "Lily", "Everett", "Ryan", "Paisley", 
    "David", "Amelia", "Charlotte", "Kai", "Sienna", "Levi", "Emma", "Violet", "Maverick", "Everett", "Olivia", "Aiden", "Grace", "Trey", "Mila", "Emery", "Henry",
    "Quinn", "Avery", "Maddox", "Cora", "Addison", "Lucas", "Victoria", "Abigail", "Megan", "Gage", "Hailey", "Eliana", "Blake", "Savannah", "Jason", "Giselle", "Alice",
    "Maddie", "Theo", "Kendall", "Jude", "Nora", "Cecilia", "Abel", "Alison", "Santiago", "Brielle", "Toby", "Riley", "Evan", "Maria", "Jenna", "Elise", "Brock", "Kian",
    "Roman", "Sadie", "Zoe", "Elijah", "Vivian", "Parker", "Theodore", "Addison", "Paige", "Marley", "Adeline", "Paxton", "Stella", "Peyton", "Sawyer", "Ellie", "Jace"
]

# A list of domains to choose from
domains = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]

# Ask the user for the number of email-password combinations they want to generate
num_combinations = int(input("Enter the number of how many lines you want: "))

# Open a file in write mode to store the generated combinations
with open("generated_emails.txt", "w") as file:
    # Generate the specified number of email-password combinations
    for i in range(num_combinations):
        # Choose a random name and birth date
        name = random.choice(names)
        birth_year = str(random.randint(1900, 2021))
        birth_month = str(random.randint(1, 12)).zfill(2)  # pad with leading zeros if needed
        birth_day = str(random.randint(1, 28)).zfill(2)  # pad with leading zeros if needed
        
        # Choose a random domain
        domain = random.choice(domains)
        
        # Generate a random email address with the name and birth date
        email = f"{name.lower()}{birth_year[2:]}{birth_month}{birth_day}@{domain}"
        
        # Generate a random password with a mix of letters and numbers, maximum 12 digits
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        
        # Write the generated email-password combination to the file
        file.write(f"{email}:{password}\n")

print("The email-password combinations have been saved to 'generated_emails.txt'.")
input("Did you finish copying?")
