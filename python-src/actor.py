class Actor:
    def __init__(self, movies:list, name:str, id:str) -> None:
        self.movies = movies
        self.name = name
        self.id = id
        self.forrige = None #Getting a feeling this is wrong
    def __str__(self) -> str:
        return f"{self.name}"

    