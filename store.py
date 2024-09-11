"""
1. Создай класс `Store`:
-Атрибуты класса:
- `name`: название магазина. [a]
- `address`: адрес магазина. [b]
- `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`. [c]
- Методы класса:
- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
- метод для добавления товара в ассортимент. [1]
- метод для удаления товара из ассортимента. [2]
- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`. [3]
- метод для обновления цены товара. [4]
2. Создай несколько объектов класса `Store`:
Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
3. Протестировать методы:
Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.
"""

class Store:
    def __init__(self, name, address):
        self.name = name                # Название магазина [a]
        self.address = address          # Адрес магазина [b]
        self.items = {}                 # Словарь [c]

    def add_item(self, item_name, price):                   # Метод для добавления товара в ассортимент [1]
        if item_name in self.items:
            print("Товар уже есть в ассортименте.")
        else:
            self.items[item_name] = price
            print(f"Добавлен товар '{item_name}' по цене {price}.")

    def remove_item(self, item_name):                       # Метод для удаления товара из ассортимента [2]
        if item_name not in self.items:
            print("Такого товара нет в ассортименте.")
        else:
            del self.items[item_name]
            print(f"Удален товар '{item_name}'.")

    def get_item_price(self, item_name):                    # Метод для получения цены товара по его названию [3]
        return self.items.get(item_name)

    def update_item_price(self, old_item_name, new_price):  # Метод для обновления цены товара [4]
        if old_item_name not in self.items:
            print("Такого товара нет в ассортименте.")
        else:
            self.items[old_item_name] = new_price
            print(f"Цена товара '{old_item_name}' обновлена до {new_price}.")

store3 = Store('Всё для рабовладения', 'Башингтон, ул. Вротшилдьа, д. небескрёб')
store3.add_item('Галера', 59660000)
store3.add_item('Колония на чужом материке', 4568700000000)
store2 = Store('BumsТовары', 'Гвадалахахахара, Улеулеура, ул. Умаумауара, б. слева')
store2.add_item('бубен', 8357)
store2.add_item('флейта', 976)
store = Store('Нулёвочка', 'Москва, ул. ПушКомитского, д. 1')
store.add_item('куки', 600)
store.add_item('эрорес', 8000)
store.update_item_price('эрорес', 9000)
store.remove_item('эрорес')
print(store.get_item_price('эрорес')) # Ожидаемый вывод: 90
print(store.get_item_price('куки')) # Ожидаемый вывод: 60
print(store.get_item_price('груши')) # Ожидаемый вывод: None
print(store.get_item_price('апельсины')) # Ожидаемый вывод: None