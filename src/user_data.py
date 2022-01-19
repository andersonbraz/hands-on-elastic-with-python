from faker import Faker
from datetime import datetime
import uuid

fake = Faker("pt_BR")


def generate_user(id):

    return {
        "id": id,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "name": fake.name(),
        "address": fake.address(),
        "postcode": fake.postcode(),
        "phone_number": fake.phone_number(),
        "ssn": fake.ssn(),
    }


if __name__ == "__main__":
    print(generate_user(1))
