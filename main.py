import db

db.init_tables()

while True:
    # print options
    print("\n1. Додати продукт\n2. Додати клієнта\n3. Створити замовлення\n4. Сумарний обсяг продажів\n5. Кількість замовлень на клієнта\n6. Середня ціна замовлення\n7. Найбільш популярна категорія\n8. Загальна кількість товарів в категоріях\n9. Оновити ціни в категорії\n10. Зберегти зміни в базу даних\n11. Закрити програму\n")

    action = input("Оберіть дію(1-11):  ")

    if action == "11":
        break

    elif action == "10":
        db.save()

    elif action == "1":
        name = input("\nІм'я: ")
        category = input("Категорія: ")
        price = input("Ціна: ")
        db.add_product(name, category, price)

        print("Продукт додано")

    elif action == "2":
        first_name = input("\nІм'я: ")
        last_name = input("Прізвище: ")
        email = input("Пошта: ")
        db.add_customer(first_name, last_name, email)

        print("Користувача додано")

    elif action == "3":
        customer_id = input("\nID користувача: ")
        product_id = input("ID продукта: ")
        quantity = input("Кількість: ")

        db.add_order(customer_id, product_id, quantity)

        print("Замовлення додано")

    elif action == "4":
        print(f"\nСумарний обсяг продажів: {db.get_total_income()}")

    elif action == "5":
        print(f"\nКількість замовлення на кліента: {db.get_orders_count()}")

    elif action == "6":
        print(f"\nСередня ціна замовлення: {db.get_avarage_order_price()}")

    elif action == "7":
        print(f"\nНайпопулярніша категорія: {db.get_most_popular_category()}")

    elif action == "8":
        print(f"\nЗагальна кількість товарів в категоріях: {db.get_product_amount_in_categories()}")

    elif action == "9":
        category = input("\nКатегорія: ")
        procentage = input("Процент: ")

        db.update_price_in_category(category, procentage)

        print("Ціни оновлено")

db.close()