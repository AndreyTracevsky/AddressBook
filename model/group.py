
class Group:
    def __init__(self, name = None, header = None, footer = None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self): # функция которая определяет как должен выглядеть объект при выводе на консоль
        return "%s:%s" % (self.id, self.name) # вывод двух значений (идендификатор и имя)

    def __eq__(self, other): # функция "логического сравнения", сравниваются идендификаторы и имена в двух списках
        return self.id == other.id and self.name == other.name # выполнение сравнения объектов по смыслу (логическое сравнение)
