class CarValidationError(Exception):
    """Базовое исключение для ошибок валидации автомобилей"""
    pass

class InvalidYearError(CarValidationError):
    def __init__(self, year, message):
        self.year = year
        self.message = message 
        super().__init__(self.message)

class InvalidPriceError(CarValidationError):
    def __init__(self, price, message):
        self.price = price
        self.message = message
        super().__init__(self.message)

class InvalidMileageError(CarValidationError):
    def __init__(self, mileage, message):    
        self.mileage = mileage
        self.message = message 
        super().__init__(self.message)

class InvalidBodyTypeError(CarValidationError):
    def __init__(self, body_type, message):
        self.body_type = body_type
        self.message = message
        super().__init__(self.message)

class InvalidBrandError(CarValidationError):
    def __init__(self, brand, message):
        self.brand = brand
        self.message = message
        super().__init__(self.message)
