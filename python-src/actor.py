class Actor:
    def __init__(self, filmer:list, navn:str, id:str) -> None:
        self.filmer = filmer
        self.navn = navn
        self.id = id

    def __str__(self) -> str:
        return f"{self.navn} filmer: {self.filmer}"

    