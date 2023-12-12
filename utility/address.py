# class Address defined in separate file 
# address.py

class Address:
    def __init__(self, street="", city="", zip_code="", country=""):
        self.update_address(street, city, zip_code, country)

    def __str__(self):
        return f"Address:\nStreet: {self.street}\nCity: {self.city}\nZIP Code: {self.zip_code}\nCountry: {self.country}\n"

    def update_address(self, street, city, zip_code, country):
        # Add conditions to check the validity of the input data
        if not self.is_valid_street(street):
            raise ValueError("Invalid street name")
        if not self.is_valid_city(city):
            raise ValueError("Invalid city name")
        if not self.is_valid_zip_code(zip_code):
            raise ValueError("Invalid ZIP code")
        if not self.is_valid_country(country):
            raise ValueError("Invalid country name")

        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country

    def is_valid_street(self, street):
        return bool(street) and all(c.isalnum() or c.isspace() or c in "-.,/" for c in street)

    def is_valid_city(self, city):
        return bool(city) and all(c.isalpha() or c.isspace() for c in city)

    def is_valid_zip_code(self, zip_code):
        return bool(zip_code) and (zip_code.isdigit() or '-' in zip_code and all(c.isdigit() or c == '-' for c in zip_code)) and len(zip_code) <= 6


    def is_valid_country(self, country):
        return bool(country) and all(c.isalpha() or c.isspace() for c in country)

    def display_address(self):
        return f"{self.street}, {self.zip_code} {self.city}, {self.country}"


