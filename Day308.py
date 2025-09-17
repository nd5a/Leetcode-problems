# Design a Food Rating System

from collections import defaultdict
from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.cuisines_food = defaultdict(SortedSet)
        self.cuisines = {}
        self.ratings = {}

        for i in range(len(foods)):
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.cuisines[food]
        r = self.ratings[food]

        self.cuisines_food[c].remove((-r, food))
        self.cuisines_food[c].add((-newRating, food))

        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_food[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine