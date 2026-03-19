from faker import Faker


class RegistrationDataGenerator:
    def __init__(self):
        self.fake = Faker("pl_PL")
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.address = self.fake.street_address()
        self.city = self.fake.city()
        self.zip_code = self.fake.postcode()
        self.phone = self.fake.phone_number()
        self.pesel = self.fake.ssn()
        self.username = self.fake.user_name()
        self.password = self.fake.password()