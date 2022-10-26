class Movie:
    def __init__(self, id:str, navn:str, rating:float,) -> None:
        self.rating = rating
        self.navn = navn
        self.id = id
        self.actors = []

    def __str__(self) -> str:
        return f"{self.navn} ({self.rating})"