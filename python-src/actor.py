class Actor:
    def __init__(self, movies:list, name:str, id:str) -> None:
        self.movies = movies
        self.name = name
        self.id = id

    def __str__(self) -> str:
        return f"{self.name}"

    