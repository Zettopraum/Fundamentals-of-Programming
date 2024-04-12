class GameReview:
    def __init__(self, user_name, rating, comment):
        self.user_name = user_name
        self.rating = rating
        self.comment = comment[:200]

    def validate_rating(self):
        return 1 <= self.rating <= 5

    @staticmethod
    def validate_review(user_name, rating, comment):
        if not (1 <= rating <= 5):
            return False
        if not user_name:
            return False
        if not comment:
            return False
        return True