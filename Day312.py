# Design Movie Rental System

from sortedcontainers import SortedList
import collections
class MovieRentingSystem:

    def __init__(self, n, entries):
        self.unrented_by_movies = collections.defaultdict(SortedList)
        self.rented = SortedList()
        self.movies = {}

        for shop, movie, price in entries:
            self.movies[(shop, movie)] = (price, False)
            self.unrented_by_movies[movie].add((price, shop))

    def search(self, movie):
        r = []
        for _, shop in self.unrented_by_movies[movie][:5]:
            r.append(shop)
        return r

    def rent(self, shop: int, movie: int) -> None:
        price, _ = self.movies[(shop, movie)]
        self.movies[(shop, movie)] = (price, True)
        self.unrented_by_movies[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price, _ = self.movies[(shop, movie)]
        self.movies[(shop, movie)] = (price, False)
        self.unrented_by_movies[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self):
        r = []
        for _, shop, movie in self.rented[:5]:
            r.append((shop, movie))
        return r


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()