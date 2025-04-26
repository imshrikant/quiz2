from faker import Faker
from models import Employee, db

fake = Faker()

def generate_employee_data(num_records):
    employees = []
    for _ in range(num_records):
        employee = Employee(
            name=fake.name(),
            age=fake.random_int(min=22, max=60),
            department=fake.job(),
            salary=fake.random_int(min=30000, max=120000)
        )
        employees.append(employee)
    db.session.bulk_save_objects(employees)
    db.session.commit()