# Мой проект: Магазин на ООП
# О чем это?
# Это уже третья версия моего учебного проекта. Сначала я делал всё на обычных списках, потом на словарях, а теперь переписал всё на ООП (классы и объекты).



--- Что умеет программа:


1 --- Считает деньги: сама вычисляет общую стоимость всех товаров на складе.

2 --- Следит за остатками: если чего-то меньше 15 штук, она вежливо (с предупреждением) скажет, что пора закупаться.

3 --- Делает скидки: если товара больше 20 штук, включается автоматическая акция — цена падает на 10%.

4 --- Помнит всё: данные сохраняются в файл data.json. Если программу закрыть и открыть снова, ничего не пропадет.



--- Как это работает внутри:
Я создал класс Product. Теперь каждый товар — это не просто строчка, а объект, который сам знает свою цену и имя. Для сохранения я написал одну функцию save_data, которая превращает объекты обратно в формат, понятный для файла.



--- Как запустить:
1 - Скачиваешь файл.
2 - Запускаешь через консоль: python Smart-Store-Manager.py.
3 - Если файла с данными еще нет, программа сама создаст стартовый список (Молоко, Хлеб, Сникерс).




# My project: Shop on PLO
# What is it about?
# This is the third version of my training project. At first, I did everything on regular lists, then on dictionaries, and now I've rewritten everything in OOP (classes and objects).



--- What the program can do:


1 --- Counts money: calculates the total cost of all goods in the warehouse itself.

2 --- Keeps track of the leftovers: if something is less than 15 pieces, she will politely (with a warning) tell you that it's time to shop.

3 --- Makes discounts: if there are more than 20 items, an automatic promotion is activated — the price drops by 10%.

4 --- Remembers everything: data is saved to a data.json file. If you close the program and open it again, nothing will be lost.



--- How does it work inside:
I created the Product class. Now every product is not just a line, but an object that knows its own price and name. To save, I wrote one function, save_data, which turns objects back into a format that is understandable to the file.



--- How to launch:
1 - Download the file.
2 - Run through the console: python Smart-Store-Manager.py
3 - If there is no data file yet, the program itself will create a start list (Milk, Bread, Snickers).
