class Game:
    def __init__(self, name, description, genre, price):
        self.name = name
        self.description = description[:12]  # Обмеження на довжину опису відеогри
        self.genre = genre
        self.price = self.validate_price(price)  # Перевірка коректності введення ціни
        self.reviews = []

    def validate_price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            return price
        else:
            raise ValueError("Ціна має бути додатнім числом")

    def __str__(self):
        return f"{self.name} - {self.genre} - {self.price}"

    def __lt__(self, other):
        return self.name < other.name

    def edit_game(self, name, description, genre, price):
        self.name = name
        self.description = description[:12]
        self.genre = genre
        self.price = self.validate_price(price)

    def check_unique_name(self, game_list, name):
        for game in game_list:
            if game.name == name:
                return False
        return True

    @staticmethod
    def sort_by_name(game_list):
        return sorted(game_list, key=lambda x: x.name)

    @staticmethod
    def sort_by_price(game_list):
        return sorted(game_list, key=lambda x: x.price)

    @staticmethod
    def sort_by_genre(game_list):
        return sorted(game_list, key=lambda x: x.genre)

    @staticmethod
    def input_game_name():
        while True:
            name = input("Введіть назву гри: ")
            if name:
                return name
            else:
                print("Назва гри не може бути порожньою.")

    @staticmethod
    def input_game_description():
        while True:
            description = input("Введіть опис гри: ")
            if description:
                return description
            else:
                print("Опис гри не може бути порожнім.")

    @staticmethod
    def input_game_genre():
        while True:
            genre = input("Введіть жанр гри: ")
            if genre:
                return genre
            else:
                print("Жанр гри не може бути порожнім.")

    @staticmethod
    def input_game_price():
        while True:
            price_input = input("Введіть ціну гри: ")
            if price_input:  # Перевірка на наявність введеного значення
                try:
                    price = float(price_input)
                    if price >= 0:
                        return price
                    else:
                        print("Ціна гри має бути додатнім числом.")
                except ValueError:
                    print("Ціна гри повинна бути числом.")
            else:
                print("Ціна гри не може бути порожньою.")

    @staticmethod
    def input_game_name():
        while True:
            name = input("Введіть назву гри: ")
            if name:
                if len(name) <= 12:
                    return name
                else:
                    print("Назва гри не може перевищувати 12 символів.")
            else:
                print("Назва гри не може бути порожньою.")

    def __init__(self, name, description, genre, price):
        self.name = name
        self.description = description
        self.genre = genre
        self.price = price
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def list_reviews(self):
        if self.reviews:
            print(f"Відгуки для гри {self.name}:")
            for review in self.reviews:
                print(review)
        else:
            print("Немає відгуків для цієї гри")

    def __str__(self):
        return f"Назва: {self.name}, Опис: {self.description}, Жанр: {self.genre}, Ціна: {self.price}"
