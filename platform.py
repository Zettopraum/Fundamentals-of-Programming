class Platform:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def find_game(self, title):
        for category in self.categories:
            for game in category.games:
                if game.title == title:
                    return game
        return None
