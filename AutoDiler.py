from Car import Car
from CarException import CarValidationError

import json
import os
from typing import List, Tuple


class AutoDealer:
    """Класс для управления базой автомобилей"""
    
    def __init__(self, filename: str = "cars_database.json"):
        self.filename = filename
        self.cars: List[Car] = []
        self.body_types = set()
        self.brands = set()

    def add_car(self, brand: str, model: str, year: int, body_type: str, mileage: int, price: int):
        try:
            car = Car(
                brand, 
                model, 
                year, 
                body_type, 
                mileage, 
                price
                )
            Car.up_count()
            self.cars.append(car)
            return car
        except CarValidationError as e:
            raise e
        except Exception as e:
            raise e
        
    def delete_car_with_id(self, id: int):
        flag = False
        
        car = self.find_car(id)
        if car:
            self.cars.remove(car)
            Car.down_count
            flag = True
        
        return flag

    def update_car(self, id: int, 
                   brand: str = None, 
                   model: str = None,
                   year: int = None,
                   body_type: str = None,
                   mileage: int = None,
                   price: int = None
                   ):
        flag = False

        car = self.find_car(id)

        if car:
            ind = self.cars.index(car)

            if brand:
                car.brand = brand
            elif model:
                car.model = model
            elif year:
                car.year = year
            elif body_type:
                car.body_type = body_type
            elif mileage:
                car.mileage = mileage
            elif price:
                car.price = price
            else:
                return flag
            
            self.cars[ind] = car
            flag = True

        return flag

    def find_car(self, id: int):
        search_car = None

        for car in self.cars:
            if car.id == id:
                search_car = car
        
        return search_car

    def save_to_file(self, filename = None, report = None):
        """Сохранение базы и отчётов автомобилей в файл"""
        if report:
            data = [car.to_dict() for car in report]
        else:    
            data = [car.to_dict() for car in self.cars]
        if not(filename):
            filename = self.filename
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"База данных сохранена в файл: {filename}")
    
    def load_from_file(self, filename = None):
        """Загрузка базы автомобилей из файла"""
        if not(filename):
            filename = self.filename

        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                for item in data:
                    try: 
                        car = Car(
                            brand=item['brand'],
                            model=item['model'],
                            year=item['year'],
                            body_type=item['body_type'],
                            mileage=item['mileage'],
                            price=item['price']
                        )
                    
                        Car.up_count()

                        self.cars.append(car)
                    
                        self.body_types.add(item['body_type'])
                    
                        self.brands.add(item['brand'])
                    
                    except Exception as e:
                        print(f"Ошибка: {e}")

                print(f"Загружено {len(self.cars)} автомобилей из {filename}")

            except Exception as e:      
                print(f"Ошибка загрузки файла: {e}")
        
        else:
            print("Файл базы данных не найден")
    
    def binary_insertion_sort(self, arr: List[Car], key_func) -> List[Car]:
        """
        Сортировка бинарными вставками
        
        Args:
            arr: список автомобилей для сортировки
            key_func: функция, возвращающая ключ для сравнения
            
        Returns:
            Отсортированный список автомобилей
        """
        if not arr:
            return arr
        
        sorted_arr = [arr[0]]
        
        for i in range(1, len(arr)):
            current = arr[i]
            current_key = key_func(current)
            
            # Бинарный поиск позиции для вставки
            left, right = 0, len(sorted_arr)
            while left < right:
                mid = (left + right) // 2
                if key_func(sorted_arr[mid]) <= current_key:
                    left = mid + 1
                else:
                    right = mid
            
            # Вставка на найденную позицию
            sorted_arr.insert(left, current)
        
        return sorted_arr
    
    def report1_all_cars_sorted(self) -> List[Car]:
        """
        Отчет 1: Список всех автомобилей, отсортированный по:
        год выпуска (по убыванию) + цена (по возрастанию)
        """
        def sort_key(car: Car) -> Tuple[int, float]:
            # Для сортировки по году по убыванию используем отрицательное значение
            # Для сортировки по цене по возрастанию - положительное
            return (-car.year, car.price)
        
        return self.binary_insertion_sort(self.cars.copy(), sort_key)
    
    def report2_cars_by_brand_sorted(self, brand: str) -> List[Car]:
        """
        Отчет 2: Список всех автомобилей определенной марки, отсортированный по:
        тип кузова (по возрастанию) + год выпуска (по убыванию) + цена (по возрастанию)
        """
        # Фильтрация по марке
        brand_cars = [car for car in self.cars if car.brand.lower() == brand.lower()]
        
        if not brand_cars:
            print(f"Автомобили марки '{brand}' не найдены.")
            return []
        
        # Создаем порядок сортировки для типов кузова
        body_type_order = {body: i for i, body in enumerate(self.body_types)}
        
        def sort_key(car: Car) -> Tuple[int, int, float]:
            # Получаем порядковый номер типа кузова
            body_order = body_type_order.get(car.body_type, len(self.body_types))
            return (body_order, -car.year, car.price)
        
        return self.binary_insertion_sort(brand_cars, sort_key)
    
    def report3_cars_by_price_range_sorted(self, min_price: float, max_price: float) -> List[Car]:
        """
        Отчет 3: Список всех автомобилей с ценой в диапазоне от N1 до N2 рублей,
        отсортированный по: цена (по возрастанию) + пробег (по возрастанию)
        """
        # Фильтрация по диапазону цен
        filtered_cars = [car for car in self.cars if min_price <= car.price <= max_price]
        
        if not filtered_cars:
            print(f"Автомобили в ценовом диапазоне {min_price:,.0f} - {max_price:,.0f} руб. не найдены.")
            return []
        
        def sort_key(car: Car) -> Tuple[float, int]:
            return (car.price, car.mileage)
        
        return self.binary_insertion_sort(filtered_cars, sort_key)
    
    def display_cars(self, cars: List[Car], title: str = ""):
        """Отображение списка автомобилей"""
        if title:
            print(f"\n{'='*60}")
            print(f"{title}")
            print(f"{'='*60}")
        
        if not cars:
            print("Нет автомобилей для отображения.")
            return
        
        print(f"Количество автомобилей: {len(cars)}")
        print("-" * 80)
        print(f"{'ID':<3} | {'Марка':<12} | {'Модель':<12} | {'Год':<6} | {'Тип кузова':<12} | {'Пробег':<10} | {'Цена':<12}")
        print("-" * 80)
        
        for i, car in enumerate(cars, 1):
            print(f"{car.id:<3} | {car.brand:<12} | {car.model:<12} | {car.year:<6} | "
                  f"{car.body_type:<12} | {car.mileage:<10,} | {car.price:<12,.0f}")
        print("-" * 80)
    
    def print_sorting_explanation(self, report_num: int, cars: List[Car]):
        """Вывод пояснения о сортировке для каждого отчета"""
        print("\n" + "="*60)
        print("ПОЯСНЕНИЕ СОРТИРОВКИ:")
        
        if report_num == 1:
            print("1. Сортировка по ГОДУ ВЫПУСКА (по убыванию):")
            print("   - Более новые автомобили в начале списка")
            print("2. При одинаковом годе - по ЦЕНЕ (по возрастанию):")
            print("   - Более дешевые автомобили в начале")
            
            # Демонстрация
            if len(cars) >= 2:
                print(f"\nПример: {cars[0].brand} {cars[0].model} ({cars[0].year}) - {cars[0].price:,.0f} руб.")
                print(f"        {cars[1].brand} {cars[1].model} ({cars[1].year}) - {cars[1].price:,.0f} руб.")
        
        elif report_num == 2:
            print("1. Сортировка по ТИПУ КУЗОВА (по возрастанию):")
            print("   Порядок: седан → хэтчбек → кабриолет → внедорожник → купе → универсал → минивэн")
            print("2. При одинаковом типе кузова - по ГОДУ (по убыванию):")
            print("   - Более новые автомобили в начале")
            print("3. При одинаковом годе - по ЦЕНЕ (по возрастанию):")
            print("   - Более дешевые автомобили в начале")
        
        elif report_num == 3:
            print("1. Сортировка по ЦЕНЕ (по возрастанию):")
            print("   - Более дешевые автомобили в начале списка")
            print("2. При одинаковой цене - по ПРОБЕГУ (по возрастанию):")
            print("   - Автомобили с меньшим пробегом в начале")
            
            # Демонстрация
            if len(cars) >= 2:
                print(f"\nПример: {cars[0].brand} {cars[0].model} - {cars[0].price:,.0f} руб. - {cars[0].mileage:,} км")
                print(f"        {cars[1].brand} {cars[1].model} - {cars[1].price:,.0f} руб. - {cars[1].mileage:,} км")
        
        print("="*60)