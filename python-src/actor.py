class Actor:
    def __init__(self, movies:list, name:str, id:str) -> None:
        self.movies = movies
        self.name = name
        self.id = id
        self.forrige = None #Getting a feeling this is wrong
        self.visited = False
        self.movieWithLast = None #On deep waters now
        self.totalWeight = 10 #the total weight of an actor, this is set when we first arrive at node, which shoudl be the shortest way

    def __str__(self) -> str:
        return f"{self.name}"

    