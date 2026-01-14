# create_sample_database.py
import json

def create_sample_database():
    """Создание примерной базы данных"""
    cars = [
        {"brand": "Toyota", "model": "Camry", "year": 2023, "body_type": "седан", "mileage": 15000, "price": 1800000},
        {"brand": "Toyota", "model": "Corolla", "year": 2021, "body_type": "седан", "mileage": 45000, "price": 1100000},
        {"brand": "Toyota", "model": "RAV4", "year": 2022, "body_type": "внедорожник", "mileage": 30000, "price": 2200000},
        {"brand": "Toyota", "model": "Land Cruiser", "year": 2020, "body_type": "внедорожник", "mileage": 60000, "price": 4500000},
        {"brand": "Honda", "model": "Civic", "year": 2022, "body_type": "седан", "mileage": 25000, "price": 1400000},
        {"brand": "Honda", "model": "Accord", "year": 2023, "body_type": "седан", "mileage": 10000, "price": 1900000},
        {"brand": "Honda", "model": "CR-V", "year": 2021, "body_type": "внедорожник", "mileage": 40000, "price": 1700000},
        {"brand": "BMW", "model": "3 Series", "year": 2023, "body_type": "седан", "mileage": 5000, "price": 3200000},
        {"brand": "BMW", "model": "5 Series", "year": 2022, "body_type": "седан", "mileage": 20000, "price": 3800000},
        {"brand": "BMW", "model": "X5", "year": 2021, "body_type": "внедорожник", "mileage": 35000, "price": 4200000},
        {"brand": "BMW", "model": "X3", "year": 2020, "body_type": "внедорожник", "mileage": 55000, "price": 2800000},
        {"brand": "Mercedes", "model": "C-Class", "year": 2022, "body_type": "седан", "mileage": 15000, "price": 2800000},
        {"brand": "Mercedes", "model": "E-Class", "year": 2023, "body_type": "седан", "mileage": 8000, "price": 3800000},
        {"brand": "Mercedes", "model": "S-Class", "year": 2021, "body_type": "седан", "mileage": 30000, "price": 5800000},
        {"brand": "Audi", "model": "A4", "year": 2022, "body_type": "седан", "mileage": 22000, "price": 2600000},
        {"brand": "Audi", "model": "A6", "year": 2023, "body_type": "седан", "mileage": 12000, "price": 3400000},
        {"brand": "Audi", "model": "Q5", "year": 2021, "body_type": "внедорожник", "mileage": 38000, "price": 2900000},
        {"brand": "Volkswagen", "model": "Golf", "year": 2022, "body_type": "хэтчбек", "mileage": 18000, "price": 1600000},
        {"brand": "Volkswagen", "model": "Passat", "year": 2021, "body_type": "седан", "mileage": 32000, "price": 1700000},
        {"brand": "Ford", "model": "Focus", "year": 2020, "body_type": "хэтчбек", "mileage": 50000, "price": 900000},
        {"brand": "Ford", "model": "Explorer", "year": 2022, "body_type": "внедорожник", "mileage": 25000, "price": 2400000},
        {"brand": "Chevrolet", "model": "Cruze", "year": 2019, "body_type": "седан", "mileage": 65000, "price": 750000},
        {"brand": "Hyundai", "model": "Solaris", "year": 2021, "body_type": "седан", "mileage": 40000, "price": 950000},
        {"brand": "Hyundai", "model": "Tucson", "year": 2022, "body_type": "внедорожник", "mileage": 20000, "price": 1800000},
        {"brand": "Kia", "model": "Rio", "year": 2020, "body_type": "седан", "mileage": 45000, "price": 850000},
        {"brand": "Kia", "model": "Sportage", "year": 2023, "body_type": "внедорожник", "mileage": 5000, "price": 2100000},
        {"brand": "Toyota", "model": "Prius", "year": 2022, "body_type": "хэтчбек", "mileage": 15000, "price": 1900000},
    ]
    
    with open("cars_database.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)

def create_error_database():
    """Создание базы данных c ошибками"""
    cars = [
        {"brand": "Toyota", "model": "Camry", "year": 2027, "body_type": "седан", "mileage": 15000, "price": 1800000},
        {"brand": "Toyota", "model": "Corolla", "year": 2021, "body_type": "седан", "mileage": -45000, "price": -2},
        {"brand": "Toyota", "model": "RAV4", "year": 2022, "body_type": "внедорожник", "mileage": 30000, "price": 2200000},
        {"brand": "Toyota", "model": "Land Cruiser", "year": 2020, "body_type": "внедорожник", "mileage": 60000, "price": 4500000},
        {"brand": "Honda", "model": "Civic", "year": 2022, "body_type": "седан", "mileage": 25000, "price": 1400000},
        {"brand": "Honda", "model": "Accord", "year": 2023, "body_type": "седан", "mileage": 10000, "price": 1900000},
        {"brand": "Honda", "model": "CR-V", "year": 2021, "body_type": "внедорожник", "mileage": 40000, "price": 1700000},
        {"brand": "BMW", "model": "3 Series", "year": 2023, "body_type": "седан", "mileage": 5000, "price": 3200000},
        {"brand": "BMW", "model": "5 Series", "year": 2022, "body_type": "седан", "mileage": 20000, "price": 3800000},
        {"brand": "BMW", "model": "X5", "year": 2021, "body_type": "внедорожник", "mileage": 35000, "price": 4200000},
        {"brand": "BMW", "model": "X3", "year": 2020, "body_type": "внедорожник", "mileage": 55000, "price": 2800000},
        {"brand": "Mercedes", "model": "C-Class", "year": 2022, "body_type": "седан", "mileage": 15000, "price": 2800000},
        {"brand": "Mercedes", "model": "E-Class", "year": 2023, "body_type": "седан", "mileage": 8000, "price": 3800000},
        {"brand": "Mercedes", "model": "S-Class", "year": 2021, "body_type": "седан", "mileage": 30000, "price": 5800000},
        {"brand": "Audi", "model": "A4", "year": 2022, "body_type": "седан", "mileage": 22000, "price": 2600000},
        {"brand": "Audi", "model": "A6", "year": 2023, "body_type": "седан", "mileage": 12000, "price": 3400000},
        {"brand": "Audi", "model": "Q5", "year": 2021, "body_type": "внедорожник", "mileage": 38000, "price": 2900000},
        {"brand": "Volkswagen", "model": "Golf", "year": 2022, "body_type": "хэтчбек", "mileage": 18000, "price": 1600000},
        {"brand": "Volkswagen", "model": "Passat", "year": 2021, "body_type": "седан", "mileage": 32000, "price": 1700000},
        {"brand": "Ford", "model": "Focus", "year": 2020, "body_type": "хэтчбек", "mileage": 50000, "price": 900000},
        {"brand": "Ford", "model": "Explorer", "year": 2022, "body_type": "внедорожник", "mileage": 25000, "price": 2400000},
        {"brand": "Chevrolet", "model": "Cruze", "year": 2019, "body_type": "седан", "mileage": 65000, "price": 750000},
        {"brand": "Hyundai", "model": "Solaris", "year": 2021, "body_type": "седан", "mileage": 40000, "price": 950000},
        {"brand": "Hyundai", "model": "Tucson", "year": 2022, "body_type": "внедорожник", "mileage": 20000, "price": 1800000},
        {"brand": "Kia", "model": "Rio", "year": 2020, "body_type": "седан", "mileage": 45000, "price": 850000},
        {"brand": "Kia", "model": "Sportage", "year": 2023, "body_type": "внедорожник", "mileage": 5000, "price": 2100000},
        {"brand": "Toyota", "model": "Prius", "year": 2022, "body_type": "хэтчбек", "mileage": 15000, "price": 1900000},
    ]
    
    with open("cars_database.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    create_sample_database()