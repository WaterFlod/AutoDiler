from CarException import *

class Car:
    """Класс для представления автомобиля"""
    
    MIN_YEAR = 1900
    MIN_PRICE = 0
    MIN_MILEAGE = 0

    def __init__(self, brand: str, model: str, year: int, body_type: str, mileage: int, price: float):
        self._validate_brand(brand)
        self._validate_body_type(body_type)
        self._validate_year(year)
        self._validate_price(price)
        self._validate_mileage(mileage)
        
        self.brand = brand
        self.model = model
        self.year = year
        self.body_type = body_type
        self.mileage = mileage
        self.price = price

    def _validate_brand(self, brand: str):
        """Проверка марки автомобиля"""
        if not brand or not brand.strip():
            raise InvalidBrandError(brand, 
                                    "Марка автомобиля должна быть указана")
    
    def _validate_body_type(self, body_type):
        """Проверка тип кузова автомобиля"""
        if not body_type:
            raise InvalidBodyTypeError(body_type, 
                                       "Тип кузова автомобиля должен быть указан")
    
    def _validate_year(self, year: int):
        """Проверка года выпуска"""
        if not year:
            raise InvalidYearError(year, "Год выпуска автомобиля должен быть указан")

        from datetime import datetime
        current_year = datetime.now().year
        
        if year < self.MIN_YEAR:
            raise InvalidYearError(year, 
                f"Год выпуска {year} меньше минимального допустимого ({self.MIN_YEAR})")
        
        if year > current_year + 1:  # +1 для автомобилей следующего года
            raise InvalidYearError(year,
                f"Год выпуска {year} больше текущего года {current_year}")
    
    def _validate_price(self, price: float):
        """Проверка цены"""
        if not price:
            raise InvalidPriceError(price, 
                                    "Цена автомобиля должна быть указана")

        if price <= self.MIN_PRICE:
            raise InvalidPriceError(price,
                f"Цена автомобиля {price} должна быть положительным числом")
    
    def _validate_mileage(self, mileage: int):
        """Проверка пробега"""
        if not mileage:
            raise InvalidMileageError(mileage, 
                                      "Пробег автомобиля должен быть указан")

        if mileage < self.MIN_MILEAGE:
            raise InvalidMileageError(mileage,
                f"Пробег {mileage} не может быть отрицательным")    

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), {self.body_type}, {self.mileage} км, {self.price:,.0f} руб."
    
    def __repr__(self):
        return str(self)
    
    def to_dict(self):
        """Преобразование в словарь для сохранения в JSON"""
        return {
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'body_type': self.body_type,
            'mileage': self.mileage,
            'price': self.price
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Создание объекта из словаря"""
        return cls(
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            body_type=data['body_type'],
            mileage=data['mileage'],
            price=data['price']
        )
    