class Validation:
    @staticmethod
    def validate_price(price):
        return price >= 0

    @staticmethod
    def check_game_name_uniqueness(platform, title):
        for category in platform.categories:
            for game in category.games:
                if game.title == title:
                    return False
        return True
