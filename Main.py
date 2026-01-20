from AutoDiler import AutoDealer
from TestCase import create_error_database, create_sample_database
from CarException import (InvalidBodyTypeError, InvalidMileageError, 
                          InvalidBrandError, InvalidModelError, 
                          InvalidPriceError, InvalidYearError)

import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Основная функция программы"""
    clear()
    
    print("="*60)
    print("ПРОГРАММА 'АВТОДИЛЕР'")
    print("="*60)
    
    # Создание и загрузка базы данных
    dealer = AutoDealer()
    dealer.load_from_file()
    
    while True:
        print("\n" + "="*60)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*60)
        print("1. Добавить автомобиль")
        print("2. Изменить характеристики автомобиля")
        print("3. Удалить автомобиль")
        print("4. Показать всю базу автомобилей (без сортировки)")
        print("5. Отчёты")
        print("6. Загрузить базу данных")
        print("7. Создание тестовых данных")
        print("8. Выход")
        
        choice = input("\nВыберите действие (1-8): ").strip()
        
        clear()

        if choice == "1":
            clear()

            print("Введите характеристики автомобиля")

            brand = input("\nМарка авто: ")
            model = input("\nМодель авто: ")
            body_type = input("\nТип кузова авто: ")
            year = int(input("\nГод выпуска авто: "))
            mileage = int(input("\nПробег авто (в км.): "))
            price = int(input("\nЦена авто (в руб.): "))

            try:
                dealer.add_car(brand, model, year, body_type, mileage, price)
                print(f"Автомобиль {brand} {model} успешно добавлен.")
            except InvalidBrandError as e:
                print(e.message)    
            except InvalidModelError as e:
                print(e.message)
            except InvalidBodyTypeError as e:
                print(e.message)
            except InvalidYearError as e:
                print(e.message)
            except InvalidMileageError as e:
                print(e.message)
            except InvalidPriceError as e:
                print(e.message)
            except Exception as e:
                print("Произошла непредвиденная ошибка: {e}")

        elif choice == "2":
            clear()

            print("="*60)
            print("ИЗМЕНЕНИЕ ХАРАКТЕРИСТИК")
            print("="*60)
            id = int(input("\nВведите ID автомобиля у которого желаете изменить характеристики: "))

            print()

            print("1. Бренд")
            print("2. Модель")
            print("3. Тип кузова")
            print("4. Год выпуска")
            print("5. Пробег")
            print("6. Цена")

            choice = input("\nВыберите храктеристику, которую хотели бы изменить (1-6): ")

            print() 

            brand = None
            model = None
            year = None
            body_type = None
            mileage = None
            price = None

            if choice == "1":
                brand = input("Введите новый бренд: ")
            elif choice == "2":
                model = input("Введите новую модель: ")
            elif choice == "3":
                body_type = input("Введите новый тип кузова: ")
            elif choice == "4":
                year = input("Введите новый год выпуска: ")
            elif choice == "5":
                mileage = input("Введите новый пробег: ")
            elif choice == "6":
                price = input("Введите новую цену: ")
            else:
                print("Неверный выбор. Пожалуйста, выберите характеристику от 1 до 6")
                continue
            
            flag = dealer.update_car(id,
                              brand,
                              model,
                              year,
                              body_type,
                              mileage,
                              price
            )

            if flag:
                print("Характеристики автомобиля успешно изменены")
            else:
                print("Автомобиль с таким ID не найден")
            
        elif choice == "3":
            clear() 
            print("="*60)
            print("УДАЛЕНИЕ АВТОМОБИЛЯ")
            print("="*60)
            id = int(input("\nВведите ID автомобиля, который хотите удалить: "))
            
            flag = dealer.delete_car_with_id(id)
            
            if flag:
                print("Автомобиль успешно удалён из базы данных")
            else: 
                print("Автомобиль с таким ID не найден")
        
        elif choice == "4":
            # Показать всю базу без сортировки
            dealer.display_cars(dealer.cars, "ВСЯ БАЗА АВТОМОБИЛЕЙ (без сортировки)")
            print(f"Всего автомобилей в базе: {len(dealer.cars)}")
        
        elif choice == "5":
            clear()

            print("="*60)
            print("ОТЧЁТЫ")
            print("="*60)
            print("1. Отчёт с сортировкой по году (↓) и цене (↑)")
            print("2. Отчёт по марке авто с сортировкой по типу кузова (↑), году (↓), цене (↑)")
            print("3. Отчёт по авто в ценовых рамках с сортировкой по цене (↑) и пробегу (↑)")

            flag = True

            while(flag):

                choice = input("\nВыберите действие (1-3): ").strip()

                if choice == "1":
                    # Отчет 1
                    sorted_cars = dealer.report1_all_cars_sorted()
                    dealer.display_cars(sorted_cars, "ОТЧЕТ 1: Все автомобили, отсортированные по году (↓) и цене (↑)")
                    dealer.print_sorting_explanation(1, sorted_cars)
                    flag = False

                elif choice == "2":
                    # Отчет 2
                    print("\nДоступные марки:", ", ".join(dealer.brands))
                    brand = input("Введите марку автомобиля: ").strip()
                    if brand:
                        sorted_cars = dealer.report2_cars_by_brand_sorted(brand)
                        if sorted_cars:
                            dealer.display_cars(sorted_cars, 
                                            f"ОТЧЕТ 2: Автомобили марки '{brand}', отсортированные по типу кузова (↑), году (↓), цене (↑)")
                            dealer.print_sorting_explanation(2, sorted_cars)
                        flag = False

                elif choice == "3":
                    # Отчет 3
                    try:
                        print(f"\nДиапазон цен в базе: от {min(c.price for c in dealer.cars):,.0f} до {max(c.price for c in dealer.cars):,.0f} руб.")
                        min_price = float(input("Введите минимальную цену (N1): ").strip())
                        max_price = float(input("Введите максимальную цену (N2): ").strip())

                        if min_price > max_price:
                            print("Ошибка: минимальная цена не может быть больше максимальной!")
                        else:
                            sorted_cars = dealer.report3_cars_by_price_range_sorted(min_price, max_price)
                            if sorted_cars:
                                dealer.display_cars(sorted_cars, 
                                                f"ОТЧЕТ 3: Автомобили в ценовом диапазоне {min_price:,.0f} - {max_price:,.0f} руб., "
                                                f"отсортированные по цене (↑) и пробегу (↑)")
                                dealer.print_sorting_explanation(3, sorted_cars)
                            flag = False

                    except ValueError:
                        print("Ошибка: введите корректные числовые значения!")

                else:
                    print("Неверный выбор. Пожалуйста, выберите отчёт от 1 до 3")

                choice = input("Желаете сохранить отчёты в формате JSON? (Да \ Нет) ")

                if choice.lower() == "да":
                    filename = input("Введите имя файла: ") + ".json"
                    dealer.save_to_file(filename, sorted_cars)
                elif choice.lower() == "нет":
                    continue
                else:
                    print("Ответ должен быть только да или нет")

        elif choice == "6":
            #Загрузка базы данных
            clear()
            print("="*60)
            print("ЗАГРУЗКА БАЗЫ ДАННЫХ")
            print("="*60)
            print()
            print("Примечание: База данных должна быть в формате JSON")
            print()
            filename = input("Введите название базы данных: ")

            dealer.load_from_file()

        elif choice == "7":
            # Создание тестовых данных
            clear()

            print("="*60)
            print("СОЗДАНИЕ ТЕСТОВЫХ ДАННЫХ")
            print("="*60)
            print("1. Создать тестовые данные без ошибок")
            print("2. Создать тестовые данные с ошибками")

            choice = input("\nВыберите действие (1-2): ").strip()
            
            clear()

            if choice == "1":
                create_sample_database()
            
            elif choice == "2":
                create_error_database()
            
            else:
                print("Неверный выбор. Пожалуйста, выберите действие от 1 или 2.")

            dealer.load_from_file()

        elif choice == "8":
            # Выход
            print("\nСпасибо за использование программы 'Автодилер'!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 8.")
        
        input("\nНажмите Enter для продолжения...")

        clear()

if __name__ == "__main__":
    main()