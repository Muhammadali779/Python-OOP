class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")

        return None
 


film1 = Movie("Qasoskorlar", "Fantastika", "1:54:32", 8.1)

print(Movie.show_summary(film1))