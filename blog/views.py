from django.shortcuts import render, HttpResponse

USERS_COUNT = 10


menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog_catalog"},
    {"name": "О проекте", "alias": "about"},
]

posts = [
    {
        "category": "Python",
        "tags": ["основы", "синтаксис", "советы"],
        "slug": "introduction-to-python",
        "title": "Введение в Python",
        "text": ("""
Python — это высокоуровневый язык программирования общего назначения, известный своей простотой и читаемостью кода. Он широко используется в веб-разработке, научных вычислениях, обработке данных, искусственном интеллекте и многих других областях.

### Основные концепции

#### Переменные и типы данных

Python поддерживает различные типы данных, такие как числа, строки, списки и словари.

```python
# Переменные и типы данных
x = 5           # целое число
y = 3.14        # число с плавающей точкой
name = "Alice"  # строка
is_active = True  # логическое значение

# Списки и словари
numbers = [1, 2, 3, 4, 5]  # список
person = {"name": "Alice", "age": 30}  # словарь
```

#### Условные операторы

Python использует стандартные условные операторы `if`, `elif` и `else`.

```python
# Условные операторы
age = 18

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
```

#### Циклы

Python поддерживает циклы `for` и `while` для повторения кода.

```python
# Цикл for
for i in range(5):
    print(i)

# Цикл while
count = 0
while count < 5:
    print(count)
    count += 1
```

#### Функции

Функции в Python определяются с помощью ключевого слова `def`.

```python
# Определение функции
def greet(name):
    return f"Hello, {name}!"

# Вызов функции
print(greet("Alice"))
```

#### Классы и объекты

Python поддерживает объектно-ориентированное программирование (ООП).

```python
# Определение класса
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Создание объекта
my_dog = Dog("Buddy")
print(my_dog.bark())
```

### Работа с файлами

Python позволяет легко работать с файлами.

```python
# Запись в файл
with open('example.txt', 'w') as file:
    file.write("Hello, world!")

# Чтение из файла
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Пример использования библиотек

Python имеет множество библиотек для различных задач. Пример использования библиотеки `requests` для HTTP-запросов:

```python
import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print(response.json())
else:
    print("Failed to retrieve data")
```

### Заключение

Python — мощный и гибкий язык программирования, подходящий для решения разнообразных задач. Его простота и обширная экосистема библиотек делают его отличным выбором для как начинающих, так и опытных разработчиков.
"""
        ),
        "author": "Иван Петров",
        "published_date": "2024-06-25",
        "comments": [
            {
                "author": "Алексей Смирнов",
                "text": "Отличная статья для новичков!",
                "date": "2024-06-26",
            },
            {
                "author": "Мария Иванова",
                "text": "Python действительно лучший выбор для начинающих.",
                "date": "2024-06-27",
            },
        ],
    },
    {
        "category": "Django",
        "tags": ["веб-разработка", "фреймворк", "приложения"],
        "slug": "getting-started-with-django",
        "title": "Начало работы с Django",
        "text": (
            "Django — это мощный веб-фреймворк на Python, который позволяет быстро создавать сложные веб-приложения. "
            "Он включает в себя множество встроенных функций, таких как аутентификация, управление базами данных и административный интерфейс. "
            "Django следит за принципом DRY (Don't Repeat Yourself), что помогает разработчикам писать чистый и эффективный код. "
            "Этот фреймворк подходит как для небольших проектов, так и для крупных корпоративных приложений. "
            "В данной статье мы рассмотрим основные этапы создания проекта на Django и его настройки."
        ),
        "author": "Ольга Кузнецова",
        "published_date": "2024-06-24",
        "comments": [
            {
                "author": "Сергей Васильев",
                "text": "Django - отличное решение для стартапов.",
                "date": "2024-06-25",
            },
            {
                "author": "Наталья Соколова",
                "text": "Статья помогла мне разобраться с настройками.",
                "date": "2024-06-26",
            },
        ],
    },
    {
        "category": "Базы данных",
        "tags": ["SQL", "sqlite", "управление"],
        "slug": "database-management-with-sqlite",
        "title": "Управление базами данных с SQLite",
        "text": (
            "SQLite — это легковесная, но мощная система управления базами данных, которая не требует установки сервера. "
            "Она идеально подходит для встраиваемых приложений и прототипов, где необходима полноценная реляционная база данных. "
            "SQLite хранит всю базу данных в одном файле, что упрощает ее перенос и резервное копирование. "
            "Ее простота и надежность делают SQLite популярным выбором среди разработчиков мобильных и настольных приложений. "
            "В этой статье мы рассмотрим основные команды SQL и примеры их использования в SQLite."
        ),
        "author": "Анна Сергеева",
        "published_date": "2024-06-23",
        "comments": [
            {
                "author": "Дмитрий Козлов",
                "text": "Использую SQLite для небольших проектов, очень удобно!",
                "date": "2024-06-24",
            },
            {
                "author": "Елена Миронова",
                "text": "Отличное объяснение основных команд SQL.",
                "date": "2024-06-25",
            },
        ],
    },
]


def about(request):
    """
    Вьюшка для страницы "О проекте"
    """
    context = {
        "users_count": USERS_COUNT,
        "menu": menu,
        "page_alias": "about",
    }


    return render(request, "about.html", context)


def blog_catalog(request):
    """
    Вьюшка для страницы "Блог" с каталогом постов.
    Обрабатываем поисковую форму, которая обрабатывается методом GET
    И пробуем получить от туда ключи:
        search
        searchInTitle
        searchInText
        searchInTags
    """
    
    if request.method == "GET":
        search = request.GET.get("search")
        search_in_title = request.GET.get("searchInTitle")
        search_in_text = request.GET.get("searchInText")
        search_in_tags = request.GET.get("searchInTags")
        posts_filtered = []
        
        if search:
            
            for post in posts:
                if not search_in_title and not search_in_text and not search_in_tags:
                    if search.lower() in post["text"].lower():
                        posts_filtered.append(post)
                if search_in_title:
                    if search.lower() in post["title"].lower():
                        posts_filtered.append(post)
                if search_in_text:
                    if search.lower() in post["text"].lower():
                        posts_filtered.append(post)
                if search_in_tags:
                    for tag in post["tags"]:
                        if search.lower() in tag.lower():
                            posts_filtered.append(post)

                
    
        context = {
            "menu": menu,
            "posts": posts_filtered if posts_filtered else posts,
            "page_alias": "blog_catalog",
        }
        return render(request, "blog/blog_catalog.html", context)


def index(request):
    context = {
        "users_count": USERS_COUNT,
        "menu": menu,
        "posts": posts,
        "page_alias": "main",
    }
    return render(request, "index.html", context)


def post_detail(request, slug):
    post = next((p for p in posts if p["slug"] == slug), None)
    if post is None:
        return HttpResponse("Статья не найдена", status=404)

    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog_catalog",
    }
    return render(request, "blog/post_detail.html", context)
