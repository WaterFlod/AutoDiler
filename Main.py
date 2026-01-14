from AutoDiler import AutoDealer
from TestCase import *

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Основная функция программы"""
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
        print("1. Показать все автомобили (отсортированные)")
        print("2. Показать автомобили определенной марки (отсортированные)")
        print("3. Показать автомобили в ценовом диапазоне (отсортированные)")
        print("4. Показать всю базу автомобилей (без сортировки)")
        print("5. Создание тестовых данных")
        print("6. Выход")
        
        choice = input("\nВыберите действие (1-6): ").strip()
        
        clear()
        
        if choice == "1":
            # Отчет 1
            sorted_cars = dealer.report1_all_cars_sorted()
            dealer.display_cars(sorted_cars, "ОТЧЕТ 1: Все автомобили, отсортированные по году (↓) и цене (↑)")
            dealer.print_sorting_explanation(1, sorted_cars)
            
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
            
            except ValueError:
                print("Ошибка: введите корректные числовые значения!")
        
        elif choice == "4":
            # Показать всю базу без сортировки
            dealer.display_cars(dealer.cars, "ВСЯ БАЗА АВТОМОБИЛЕЙ (без сортировки)")
            print(f"Всего автомобилей в базе: {len(dealer.cars)}")
        
        elif choice == "5":
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
                print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")

            dealer.load_from_file()

        elif choice == "6":
            # Выход
            print("\nСпасибо за использование программы 'Автодилер'!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 6.")
        
        input("\nНажмите Enter для продолжения...")

        clear()

if __name__ == "__main__":
    main()