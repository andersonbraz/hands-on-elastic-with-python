from faker import Faker
from datetime import datetime
import uuid

fake = Faker("pt_BR")


def get_user():

    return {
        "id": str(uuid.uuid4()),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "name": fake.name(),
        "address": fake.address(),
        "postcode": fake.postcode(),
        "phone_number": fake.phone_number(),
        "ssn": fake.ssn(),
    }


if __name__ == "__main__":
    print(get_user())
