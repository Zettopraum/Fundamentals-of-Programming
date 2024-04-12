from validation import Validation

class Game:
    def __init__(self, title, description, genre, rating, price):
        self.title = title
        self.description = description[:300]
        self.genre = genre
        self.rating = rating
        self.price = price

        if not Validation.validate_price(price):
            raise ValueError("Price should be a non-negative number.")

        if not game_review.validate_rating(rating):
            raise ValueError("Rating should be between 1 and 5.")

        if not Validation.check_game_name_uniqueness(platform, title):
            raise ValueError("Game with this title already exists.")

    def __str__(self):
        return f"{self.title} - {self.genre} - {self.rating} - ${self.price}"
