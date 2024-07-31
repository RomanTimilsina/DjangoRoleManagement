from .models import Employee
from faker import Faker

fake = Faker()

def seed_db(n):
    for i in range(0, n):
        Employee.objects.create(
            employee_name = fake.name(),
            employee_contact = fake.phone_number(),
            employee_address = fake.address()
        )