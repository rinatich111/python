# Теория списков в python3

# Методы
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort

# Примеры использования методов
# Часть примеров взята с сайта w3schools.com

# Создание списка
mylist = ["apple", "banana", "cherry"]
mylist = ()

# Получить длину списка
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) # 3

# Списки могут иметь элементы разных типов
list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3, 4, 5]
list3 = [True, False, True]
list4 = ["abc", 34, True, 40, "male"]

# Уточнить действительно ли объект является списком (list)
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>

# Для создание списка можно использовать метод list()
thislist = list(("apple", "banana", "cherry"))
print(thislist) # ["apple", "banana", "cherry"]


