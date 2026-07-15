class Movie:

    def __init__(self, name, hero, rating):
        self.name = name
        self.hero = hero
        self.rating = rating

    def display(self):
        print("Movie:", self.name)
        print("Hero:", self.hero)
        print("Rating:", self.rating)


movie1 = Movie("Avengers", "Iron Man", 9.5)

movie1.display()