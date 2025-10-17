class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

film1 = Movie("Qasoskorlar", "Fantastika", "1:54:32", 8.1)
film2 = Movie("Terminator", "Fantastika", "2:10:32", 8.5)

print(film1.title, film1.genre, film1.duration, film1.rating)
print(film2.title, film2.genre, film2.duration, film2.rating)