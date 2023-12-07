# class Address defined in separate file 
class Address:
    def __init__(self, street="", city="", zip_code="", country=""):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}, {self.country}"

    def is_empty(self):
        return all(value == "" for value in [self.street, self.city, self.zip_code, self.country])

