
import json

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def info(self):
        print(f"Товар: {self.name}, Цена: {self.price}, Количество: {self.stock}")

def save_data():
    two_products = []
    for item in products:
        two_products.append({
            "name": item.name,
            "price": item.price,
            "stock": item.stock
        })
    with open("data.json", "w") as file:
        json.dump(two_products, file)


products = []

try:
    with open("data.json", "r") as file:
        raw_data = json.load(file)
        converted_products = []
        for p in raw_data:
            new_obj = Product(p["name"], p["price"], p["stock"])
            converted_products.append(new_obj)
        products = converted_products
except:
    print("База пуста, создаем новую")
    products = [
    Product("Молоко", 80, 10),
    Product("Хлеб", 80, 10),
    Product("сникерс", 150, 20)
]


#products.append({"name": "Кола", "price": "100", "stock": "5"})

#bad_snikers = {"name": "Сникерс", "price": "150", "stock": "20"}
#products.remove(bad_snikers)

def show_all_products():
    total_money = 0
    print(f"--- В БАЗЕ СЕЙЧАС {len(products)} товаров ---. ")
    for product in products:
        print(f"Товар: {product.name} , Цена: {product.price}, Количество: {product.stock}.")
        if int(product.stock) < 15:
            print(f"⚠️ ВНИМАНИЕ: {product.name} заканчивается! осталось всего {product.stock} штук. ")
        final_price = int(product.price)
        if int(product.stock) > 20:
            final_price = int(final_price * 0.9)
            print(f"АКЦИЯ! {product.name} сегодня по {final_price}")
        try:
            current_sum = final_price * int(product.stock)
            total_money += current_sum
        except:
            print("Ошибка: цена или количество должны быть числами!")
            continue
    print(f"--- ОБЩАЯ СУММА ТОВАРОВ: {total_money}")

def add_new_product(name, price, stock):
    new_item = Product(name, price, stock)
    products.append(new_item)
    save_data()

def delete_product(name):
    for product in products:
        if product.name == name:
            products.remove(product)
        
    save_data()

def edit_product(name):
    found = False
    for product in products:
        if product.name == name:
            found = True
            print("1 - Change the price")
            print("2 - Change the quantity") 
            choise = input()
            if choise == "1":
                try:
                    new_p = int(input("Введите новую цену: "))
                    product.price = new_p
                except ValueError:
                    print("Ошибка нужно вводить только цифры")
            elif choise == "2":
                try:
                    new_s = int(input("Введите новое количество: "))
                    product.stock = new_s
                except ValueError:
                    print("Ошибка нужно вводить только цифры")
    if not found:
        print("К сожалению товар не найден")
    save_data()
            

while True:
    print("--- MENU --- ")
    print("1 - Show all products")
    print("2 - Add new product")
    print("3 - Delete product")
    print("4 - Edit product")
    print("5 - Exit")
    user = input()
    if user == "1":
        show_all_products()
    elif user == "2":
        new_name = input("Name: ")
        new_price = int(input("price: "))
        new_stock = int(input("stock: "))
        add_new_product(new_name, new_price, new_stock)
    elif user == "3":
        del_name = input("Enter name to delete: ")
        delete_product(del_name)
    elif user == "4":
        name_to_edit = input("Какой товар редактируем?: ")
        edit_product(name_to_edit)
    elif user == "5":
        print("Goodbye!")
        break
    else:
        print("Not a valid choice")