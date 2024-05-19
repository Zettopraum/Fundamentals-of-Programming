class GameReview:
    def __init__(self, user_name, rating, comment):
        self.user_name = user_name
        self.rating = self.validate_rating(rating)
        self.comment = comment[:50]

    def validate_rating(self, rating):
        if 1 <= rating <= 5:
            return rating
        else:
            raise ValueError("Оцінка повинна бути в діапазоні від 1 до 5")

    def __str__(self):
        return f"Користувач: {self.user_name}, Оцінка: {self.rating}, Коментар: {self.comment}"
