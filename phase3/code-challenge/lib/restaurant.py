"""
 `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created
"""
class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews = []

    def get_name(self):
        return self._name

    def reviews(self):
        return self.reviews

    def customers(self):
        reviewed_customers = [review.customer for review in self.reviews]
        return list(set(reviewed_customers))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum([review.rating for review in self.reviews])
        return total_rating / len(self.reviews)

    def add_review(self, review):
        self.reviews.append(review)
