# pip install faker
from faker import Faker
fake = Faker()
for _ in range(5):
    print(fake.name(), "-", fake.email())
print("Fake data generated successfully")
