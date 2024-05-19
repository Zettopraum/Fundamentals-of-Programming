class GamePlatform:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, name):
        for game in self.games:
            if game.name == name:
                self.games.remove(game)
                print(f"Гра {name} успішно видалена")
                return True
        print(f"Гра {name} не знайдена в списку ігор")
        return False

    def list_games(self):
        if self.games:
            print("Список доступних відеоігор:")
            for game in self.games:
                print(game)
        else:
            print("На платформі немає доступних відеоігор")

    def search_by_price(self, max_price):
        found_games = [game for game in self.games if game.price <= max_price]
        if found_games:
            print("Результати пошуку:")
            for game in found_games:
                print(game)
        else:
            print("Жодної гри не знайдено за вказаною ціною.")

    def search_by_name(self, keyword):
        if keyword.strip():
            found_games = [game for game in self.games if keyword.lower() in game.name.lower()]
            if found_games:
                print("Результати пошуку:")
                for game in found_games:
                    print(game)
            else:
                print("Жодної гри не знайдено за вказаною назвою.")
        else:
            print("Будь ласка, введіть назву гри для пошуку.")

    def search_by_genre(self, genre):
        if genre.strip():
            found_games = [game for game in self.games if genre.lower() in game.genre.lower()]
            if found_games:
                print("Результати пошуку:")
                for game in found_games:
                    print(game)
            else:
                print("Жодної гри не знайдено за вказаним жанром.")
        else:
            print("Будь ласка, введіть жанр гри для пошуку.")

    def add_game(self, game):
        self.games.append(game)

    def find_game(self, name):
        for game in self.games:
            if game.name.lower() == name.lower():
                return game
        return None

    def add_review_to_game(self, game_name, review):
        game = self.find_game(game_name)
        if game:
            game.add_review(review)
            print(f"Відгук успішно додано до гри {game_name}")
        else:
            print(f"Гра {game_name} не знайдена")

    def list_reviews_for_game(self, game_name):
        game = self.find_game(game_name)
        if game:
            game.list_reviews()
        else:
            print(f"Гра {game_name} не знайдена")