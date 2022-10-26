class Movie:
    def __init__(self, id:str, name:str, rating:float,) -> None:
        self.rating = rating
        self.name = name
        self.id = id
        self.actors = []

    def __str__(self) -> str:
        return f"{self.name} ({self.rating})"